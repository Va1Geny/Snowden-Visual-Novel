import argparse
import asyncio
import hashlib
import importlib.util
import json
import re
import site
import sys
from collections import defaultdict
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

USER_SITE_DIR = Path(r"C:\Users\Богдан\AppData\Roaming\Python\Python314\site-packages")
if USER_SITE_DIR.exists() and str(USER_SITE_DIR) not in sys.path:
    sys.path.insert(0, str(USER_SITE_DIR))


def load_edge_tts():
    try:
        import edge_tts as module
        if hasattr(module, "Communicate") and hasattr(module, "list_voices"):
            return module
    except Exception:
        pass

    vendor_init = TOOLS_DIR / "vendor_edge_tts" / "__init__.py"
    if vendor_init.exists():
        spec = importlib.util.spec_from_file_location(
            "edge_tts",
            vendor_init,
            submodule_search_locations=[str(vendor_init.parent)],
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            sys.modules["edge_tts"] = module
            spec.loader.exec_module(module)
            if hasattr(module, "Communicate") and hasattr(module, "list_voices"):
                return module

    candidate_roots = []
    try:
        candidate_roots.extend(site.getsitepackages())
    except Exception:
        pass
    try:
        candidate_roots.append(site.getusersitepackages())
    except Exception:
        pass

    for root in candidate_roots:
        init_path = Path(root) / "edge_tts" / "__init__.py"
        if not init_path.exists():
            continue

        spec = importlib.util.spec_from_file_location(
            "edge_tts",
            init_path,
            submodule_search_locations=[str(init_path.parent)],
        )
        if not spec or not spec.loader:
            continue

        module = importlib.util.module_from_spec(spec)
        sys.modules["edge_tts"] = module
        spec.loader.exec_module(module)
        if hasattr(module, "Communicate") and hasattr(module, "list_voices"):
            return module

    raise ImportError("Unable to load edge_tts with Communicate/list_voices.")


edge_tts = load_edge_tts()


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
    "im": {
        "voice": "en-US-AndrewMultilingualNeural",
        "tag": "internal_monologue",
        "rate": "-4%",
        "pitch": "-6Hz",
        "volume": "-18%",
    },
    "e": {"voice": "en-US-BrianMultilingualNeural", "tag": "edward"},
    "greenwald": {"voice": "en-US-AndrewMultilingualNeural", "tag": "greenwald", "rate": "-1%"},
    "poitras": {"voice": "en-US-EmmaMultilingualNeural", "tag": "poitras"},
    "nsa_chief": {"voice": "en-US-AndrewNeural", "tag": "nsa_chief", "pitch": "-5Hz", "rate": "-4%"},
    "supervisor": {"voice": "en-US-AndrewNeural", "tag": "supervisor", "pitch": "-3Hz", "rate": "-3%"},
    "colleague": {"voice": "en-US-RogerNeural", "tag": "colleague", "rate": "+2%", "pitch": "+2Hz"},
    "russian_official": {"voice": "ru-RU-DmitryNeural", "tag": "russian_official", "pitch": "+1Hz", "rate": "+2%"},
}

TAG_RE = re.compile(r"\{[^}]*\}")
WHITESPACE_RE = re.compile(r"\s+")

EMOTION_PRESETS = {
    "neutral": {"rate": 0, "pitch": 0, "volume": 0},
    "reflective": {"rate": -6, "pitch": -1, "volume": -5},
    "tense": {"rate": 4, "pitch": 2, "volume": 3},
    "urgent": {"rate": 7, "pitch": 4, "volume": 5},
    "warm": {"rate": 2, "pitch": 2, "volume": 2},
    "cold": {"rate": -4, "pitch": -2, "volume": -1},
    "suspicious": {"rate": -2, "pitch": -1, "volume": -2},
    "resolute": {"rate": 2, "pitch": -1, "volume": 1},
    "vulnerable": {"rate": -5, "pitch": 1, "volume": -4},
    "conspiratorial": {"rate": -4, "pitch": -1, "volume": -6},
}

CHARACTER_BASE_MODES = {
    "e": "reflective",
    "im": "conspiratorial",
    "greenwald": "suspicious",
    "poitras": "warm",
    "supervisor": "cold",
    "nsa_chief": "cold",
    "colleague": "warm",
    "russian_official": "cold",
}

TENSE_KEYWORDS = (
    "careful",
    "warning",
    "risk",
    "flagged",
    "monitored",
    "danger",
    "audit",
    "caught",
    "threat",
    "compromised",
)
WARM_KEYWORDS = (
    "thank",
    "help",
    "trust",
    "glad",
    "good",
    "safe",
    "together",
    "friend",
)
RESOLUTE_KEYWORDS = (
    "i need",
    "we need",
    "must",
    "have to",
    "i will",
    "we will",
    "focus",
    "decide",
    "truth",
)
VULNERABLE_KEYWORDS = (
    "maybe",
    "i think",
    "i know",
    "never",
    "alone",
    "afraid",
    "doubt",
    "wrong",
)
CONSPIRATORIAL_KEYWORDS = (
    "quiet",
    "listen",
    "nobody",
    "walls have ears",
    "keep this",
    "off the record",
    "they monitor",
    "don't use",
)


def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = TAG_RE.sub("", text)
    text = text.replace("[[", "[").replace("]]", "]")
    text = text.replace("\\\"", "\"")
    text = text.replace("\\n", " ")
    text = re.sub(r"\bAES-256\b", "A E S two fifty six", text)
    text = re.sub(r"\bAES\b", "A E S", text)
    text = text.replace("\n", " ")
    text = text.replace("—", ", ")
    text = text.replace("–", ", ")
    text = text.replace(";", ", ")
    text = WHITESPACE_RE.sub(" ", text).strip()
    return text


def adjust_percent(value: str, delta: int) -> str:
    number = int(value.rstrip("%"))
    updated = number + delta
    return "{:+d}%".format(updated)


def adjust_hz(value: str, delta: int) -> str:
    number = int(value.rstrip("Hz"))
    updated = number + delta
    return "{:+d}Hz".format(updated)


def clamp(value: int, minimum: int, maximum: int) -> int:
    return max(minimum, min(maximum, value))


def extract_numeric_percent(value: str) -> int:
    return int(value.rstrip("%"))


def extract_numeric_hz(value: str) -> int:
    return int(value.rstrip("Hz"))


def infer_emotion_mode(text: str, speaker: str) -> str:
    lowered = text.lower()
    exclamations = text.count("!")
    questions = text.count("?")

    if exclamations >= 2 or "ALERT:" in text or "WARNING:" in text:
        return "urgent"

    if any(keyword in lowered for keyword in CONSPIRATORIAL_KEYWORDS):
        return "conspiratorial"

    if any(keyword in lowered for keyword in TENSE_KEYWORDS):
        return "tense"

    if questions and speaker in {"greenwald", "supervisor", "nsa_chief"}:
        return "suspicious"

    if any(keyword in lowered for keyword in RESOLUTE_KEYWORDS):
        return "resolute"

    if any(keyword in lowered for keyword in WARM_KEYWORDS):
        return "warm"

    if "..." in text or any(keyword in lowered for keyword in VULNERABLE_KEYWORDS):
        return "vulnerable"

    if speaker in CHARACTER_BASE_MODES:
        return CHARACTER_BASE_MODES[speaker]

    return "neutral"


def apply_emotion(profile: dict, text: str, speaker: str) -> tuple[str, str, str, str]:
    rate = profile.get("rate", "+0%")
    pitch = profile.get("pitch", "+0Hz")
    volume = profile.get("volume", "+0%")
    mode = infer_emotion_mode(text, speaker)

    if speaker in {"centered", "narrator_voice"}:
        return rate, pitch, volume, "neutral"

    exclamations = text.count("!")
    questions = text.count("?")
    trailing_ellipsis = "..." in text
    upper_ratio = 0.0

    letters = [ch for ch in text if ch.isalpha()]
    if letters:
        upper_ratio = sum(1 for ch in letters if ch.isupper()) / float(len(letters))

    if exclamations:
        rate = adjust_percent(rate, min(8, exclamations * 3))
        pitch = adjust_hz(pitch, min(8, exclamations * 2))
        volume = adjust_percent(volume, min(8, exclamations * 2))

    if questions:
        pitch = adjust_hz(pitch, min(6, questions * 2))
        rate = adjust_percent(rate, min(4, questions * 1))

    if trailing_ellipsis:
        rate = adjust_percent(rate, -4)
        volume = adjust_percent(volume, -4)

    if upper_ratio > 0.55 or "WARNING:" in text or "ALERT:" in text:
        pitch = adjust_hz(pitch, -2)
        volume = adjust_percent(volume, 6)

    if len(text.split()) <= 5 and not exclamations and not questions:
        rate = adjust_percent(rate, 2)

    preset = EMOTION_PRESETS.get(mode, EMOTION_PRESETS["neutral"])
    rate_value = clamp(extract_numeric_percent(rate) + preset["rate"], -18, 12)
    pitch_value = clamp(extract_numeric_hz(pitch) + preset["pitch"], -8, 8)
    volume_value = clamp(extract_numeric_percent(volume) + preset["volume"], -24, 10)

    if speaker == "russian_official":
        pitch_value = clamp(pitch_value, -2, 4)
        rate_value = clamp(rate_value, -6, 6)

    return (
        "{:+d}%".format(rate_value),
        "{:+d}Hz".format(pitch_value),
        "{:+d}%".format(volume_value),
        mode,
    )


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

            profile = VOICE_PROFILES[speaker]
            rate, pitch, volume, mode = apply_emotion(profile, text, speaker)
            signature = hashlib.sha1(
                "|".join(
                    [
                        speaker,
                        profile["voice"],
                        rate,
                        pitch,
                        volume,
                        text,
                    ]
                ).encode("utf-8")
            ).hexdigest()[:10]
            base_name = f"{file_path.stem}_{line_number:04d}_{speaker}_{signature}.mp3"
            rel_path = Path("audio") / "voice" / "en" / base_name

            entries.append(
                {
                    "src": relative_src,
                    "line": line_number,
                    "speaker": speaker,
                    "text": text,
                    "voice": profile["voice"],
                    "tag": profile["tag"],
                    "rate": rate,
                    "pitch": pitch,
                    "volume": volume,
                    "emotion_mode": mode,
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
    attempts = 4

    for attempt in range(1, attempts + 1):
        try:
            communicate = edge_tts.Communicate(
                text=entry["text"],
                voice=entry["voice"],
                rate=entry["rate"],
                volume=entry["volume"],
                pitch=entry["pitch"],
            )
            await communicate.save(str(out_path))
            break
        except Exception:
            if attempt == attempts:
                raise
            await asyncio.sleep(2 * attempt)

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
            try:
                path.unlink()
            except PermissionError:
                print(f"Skipping locked stale audio: {path.name}")


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
                    indent = match.group("indent")
                    rebuilt.append(f'{indent}$ localized_voice = voice_for_current_language("{entry["relative_audio_path"]}")  {AUTO_MARKER}')
                    rebuilt.append(f"{indent}if localized_voice:  {AUTO_MARKER}")
                    rebuilt.append(f"{indent}    voice localized_voice  {AUTO_MARKER}")
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
