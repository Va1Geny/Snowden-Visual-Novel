import sys

with open(r'game\screens\screens.rpy', 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

i = 0
while i < len(lines):
    if 'style "modal_action_button"' in lines[i]:
        has_font = False
        for j in range(1, 10):
            if i + j < len(lines):
                if 'text_font' in lines[i+j]:
                    has_font = True
                    break
                if 'textbutton' in lines[i+j] or 'style ' in lines[i+j] or 'frame:' in lines[i+j]:
                    break
        
        if not has_font:
            indent = len(lines[i]) - len(lines[i].lstrip())
            lines.insert(i+1, ' ' * indent + 'text_font settings_ui_font(mono=True)')
    i += 1

with open(r'game\screens\screens.rpy', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('Done')
