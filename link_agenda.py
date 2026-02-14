
import re

file_path = r'c:\Users\sukes\Downloads\kec docs\kec site\day1.html'

def main():
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define replacements
    # We will replace the div content with onclick and pointer style
    
    replacements = [
        ('🧠 CPU', '3'),
        ('⚡ Motherboard', '5'),
        ('💾 RAM', '6'),
        ('🎮 GPU', '7'),
        ('🔌 Power Supply Unit (PSU)', '8'),
        ('💿 Storage', '9'),
        ('❄️ Cooling & Thermals', '9'),
        ('🖥️ Monitor & Display', '10'),
        ('🔗 Ports & Cables', '10'),
        ('💻 Operating System (OS)', '11'),
    ]

    new_content = content
    
    for text, slide_num in replacements:
        # We look for the div opening, some style, and then the text
        # The lines might look like: <div class="agenda-item" style="...">TEXT\n</div>
        
        # We need to match <div class="agenda-item" ...> ... TEXT ... </div>
        # But we only want to match ones that haven't been done yet (so they don't have onclick)
        
        # Regex:
        # <div class="agenda-item" (make sure no onclick here) style="...">\s*TEXT\s*</div>
        
        # To be safe, let's just look for the specific pattern we saw in the file for PSU/OS
        # They have style="text-align: left; padding: 0.8rem;">TEXT
        
        pattern_text = re.escape(text)
        
        # Allow for optional whitespace/newlines around the text inside the div
        # Capture the style content
        regex = r'(<div class="agenda-item"\s+style=")([^"]*)(">\s*)' + pattern_text + r'(\s*</div>)'
        
        # Replacement: add onclick and cursor pointer
        # \1 is start of tag + style="
        # \2 is style content
        # \3 is "> + whitespace
        # \4 is whitespace + </div>
        
        replacement = f'<div class="agenda-item" onclick="goToSlide({slide_num})" style="\\2 cursor: pointer;">{text}</div>'
        
        # Note: formatting the replacement to be on one line for cleanliness
        
        new_content = re.sub(regex, replacement, new_content)

    if new_content == content:
        print("Warning: No changes made. Check patterns.")
    else:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully linked agenda items.")

if __name__ == "__main__":
    main()
