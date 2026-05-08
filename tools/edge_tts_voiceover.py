import argparse
import asyncio
import json
import re
from collections import defaultdict
from pathlib import Path

import edge_tts


REPO_ROOT = Path(__file__).resolve().parent.parent
GAME_DIR = REPO_ROOT / "game"
VOICE_DIR = GAME_DIR / "audio" / "voice" / "en"
MANIFEST_PATH = VOICE_DIR / "manifest.json"
AUTO_MARKER = "# edge-tts-auto"
SOURCE_FILES = [
    GAME_DIR / "scripts" / "script.rpy",
    GAME_DIR / "scripts" / "endings.rpy",
]

VOICE_PROFILES = {
    "centered": {"voice": "en-US-BrianNeural", "tag": "narration"},
    "narrator_voice": {"voice": "en-US-BrianNeural", "tag": "narration"},
    "im": {"voice": "en-US-AndrewNeural", "tag": "internal_monologue", "rate": "-8%"},
    "e": {"voice": "en-US-GuyNeural", "tag": "edward"},
    "greenwald": {"voice": "en-US-ChristopherNeural", "tag": "greenwald"},
    "poitras": {"voice": "en-US-JennyNeural", "tag": "poitras"},
    "nsa_chief": {"voice": "en-US-BrianNeural", "tag": "nsa_chief", "pitch": "-4Hz"},
    "supervisor": {"voice": "en-US-AndrewNeural", "tag": "supervisor"},
    "colleague": {"voice": "en-US-EricNeural", "tag": "colleague"},
    "russian_official": {"voice": "en-US-RogerNeural", "tag": "russian_official", "pitch": "-6Hz"},
    "sys": {"voice": "en-US-SteffanNeural", "tag": "system", "rate": "-12%"},
}

TAG_RE = re.compile(r"\{[^}]*\}")
WHITESPACE_RE = re.compile(r"\s+")


def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = TAG_RE.sub("", text)
    text = text.replace("[[", "[").replace("]]", "]")
    text = text.replace("\\\"", "\"")
    text = text.replace("\n", " ")
    text = text.replace("—", " - ")
    text = text.replace("–", " - ")
    text = WHITESPACE_RE.sub(" ", text).strip()
    return text


def build_entries():
    entries = []
    say_re = re.compile(r'^\s*(?P<speaker>[A-Za-z_][A-Za-z0-9_]*)\s+"(?P<text>.*)"\s*$')

    for file_path in SOURCE_FILES:
        relative_src = file_path.relative_to(GAME_DIR).as_posix()
        raw_lines = file_path.read_text(encoding="utf-8").splitlines()
        lines = [line for line in raw_lines if AUTO_MARKER not in line]

        for line_number, line in enumerate(lines, start=1):
            match = say_re.match(line)
            if not match:
                continue

            speaker = match.group("speaker")
            if speaker not in VOICE_PROFILES:
                continue

            text = clean_text(match.group("text"))
            if not text:
                continue

            base_name = f"{file_path.stem}_{line_number:04d}_{speaker}.mp3"
            rel_path = Path("audio") / "voice" / "en" / base_name
            profile = VOICE_PROFILES[speaker]

            entries.append(
                {
                    "src": relative_src,
                    "line": line_number,
                    "speaker": speaker,
                    "text": text,
                    "voice": profile["voice"],
                    "tag": profile["tag"],
                    "rate": profile.get("rate", "+0%"),
                    "pitch": profile.get("pitch", "+0Hz"),
                    "relative_audio_path": rel_path.as_posix(),
                    "absolute_audio_path": str((GAME_DIR / rel_path).resolve()),
                }
            )

    return entries


async def synthesize_entry(entry, force=False):
    out_path = Path(entry["absolute_audio_path"])
    if out_path.exists() and not force:
        return False

    out_path.parent.mkdir(parents=True, exist_ok=True)
    communicate = edge_tts.Communicate(
        text=entry["text"],
        voice=entry["voice"],
        rate=entry["rate"],
        pitch=entry["pitch"],
    )
    await communicate.save(str(out_path))
    return True


async def generate_audio(entries, force=False, concurrency=4):
    semaphore = asyncio.Semaphore(concurrency)
    generated = 0

    async def worker(entry):
        nonlocal generated
        async with semaphore:
            created = await synthesize_entry(entry, force=force)
            if created:
                generated += 1

    await asyncio.gather(*(worker(entry) for entry in entries))
    return generated


def write_manifest(entries):
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(
        json.dumps(entries, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def cleanup_stale_audio(entries):
    expected = {Path(entry["absolute_audio_path"]).resolve() for entry in entries}
    expected.add(MANIFEST_PATH.resolve())

    for path in VOICE_DIR.glob("*.mp3"):
        if path.resolve() not in expected:
            path.unlink()


def inject_voice_calls(entries):
    grouped = defaultdict(list)
    for entry in entries:
        grouped[entry["src"]].append(entry)

    for relative_src, src_entries in grouped.items():
        file_path = GAME_DIR / relative_src
        lines = file_path.read_text(encoding="utf-8").splitlines()

        # Reset previous auto-generated calls so line numbers stay aligned.
        lines = [line for line in lines if AUTO_MARKER not in line]
        rebuilt = []
        entry_index = 0
        say_re = re.compile(r'^(?P<indent>\s*)(?P<speaker>[A-Za-z_][A-Za-z0-9_]*)\s+"(?P<text>.*)"\s*$')

        for line in lines:
            match = say_re.match(line)
            if match and entry_index < len(src_entries):
                speaker = match.group("speaker")
                source_text = clean_text(match.group("text"))
                entry = src_entries[entry_index]

                if speaker == entry["speaker"] and source_text == entry["text"]:
                    helper = f'{match.group("indent")}voice "{entry["relative_audio_path"]}"  {AUTO_MARKER}'
                    rebuilt.append(helper)
                    entry_index += 1

            rebuilt.append(line)

        if entry_index != len(src_entries):
            missing = src_entries[entry_index]
            raise RuntimeError(
                f"Could not align all voice lines for {relative_src}. "
                f"Stopped at {missing['speaker']}:{missing['text']}"
            )

        file_path.write_text("\n".join(rebuilt) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Generate and inject English Edge TTS voiceover.")
    parser.add_argument("--generate-only", action="store_true", help="Only generate audio and manifest.")
    parser.add_argument("--inject-only", action="store_true", help="Only inject runtime calls into script files.")
    parser.add_argument("--force", action="store_true", help="Regenerate audio files even if they already exist.")
    parser.add_argument("--concurrency", type=int, default=4, help="Concurrent Edge TTS requests.")
    args = parser.parse_args()

    entries = build_entries()
    write_manifest(entries)
    cleanup_stale_audio(entries)

    if not args.inject_only:
        generated = asyncio.run(generate_audio(entries, force=args.force, concurrency=max(1, args.concurrency)))
        print(f"Generated {generated} audio files.")

    if not args.generate_only:
        inject_voice_calls(entries)
        print(f"Injected voice calls into {len({entry['src'] for entry in entries})} script files.")

    print(f"Prepared {len(entries)} English voice lines.")


if __name__ == "__main__":
    main()
