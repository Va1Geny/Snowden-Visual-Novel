import re

with open("game/scripts/definitions.rpy", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
in_image_block = False
current_char = ""
image_block_indent = "    "

char_tags = [
    "edward", "supervisor", "colleague", "greenwald",
    "poitras", "journalist", "editor", "nsa_chief", "russian_official"
]

for i, line in enumerate(lines):
    match = re.match(r'^image\s+([a-z_]+)\s+[a-z_]+:\s*$', line)
    if match and match.group(1) in char_tags:
        current_char = match.group(1)
        in_image_block = True
        new_lines.append(line)
        continue

    if in_image_block:
        if line.strip() == "" or line.startswith(" ") or line.startswith("\t"):
            new_lines.append(line)
        else:
            if current_char:
                new_lines.append(f"{image_block_indent}function dim_{current_char}\n")
            in_image_block = False
            current_char = ""
            new_lines.append(line)
    else:
        new_lines.append(line)

if in_image_block and current_char:
    new_lines.append(f"{image_block_indent}function dim_{current_char}\n")

with open("game/scripts/definitions.rpy", "w", encoding="utf-8") as f:
    f.writelines(new_lines)
