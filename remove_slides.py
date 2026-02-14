
import re

file_path = r'c:\Users\sukes\Downloads\kec docs\kec site\day1.html'

def main():
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Find Start of Slide 6
    start_marker = '<section class="slide" data-slide="6">'
    start_pos = content.find(start_marker)
    
    # Fallback if specific formatting differs (e.g. spaces)
    if start_pos == -1:
        match = re.search(r'<section class="slide"\s+data-slide="6">', content)
        if match:
            start_pos = match.start()
    
    if start_pos == -1:
        print("Error: Could not find Start of Slide 6")
        return

    # 2. Find End of Slide Container
    # We look for "<!-- Navigation Controls -->" and go back to the matching closing div
    # simpler: Look for the div immediately preceding Navigation Controls
    nav_marker = '<!-- Navigation Controls -->'
    nav_pos = content.find(nav_marker)
    
    if nav_pos == -1:
        print("Error: Could not find Navigation Controls marker")
        return

    # Find the last </div> before nav_pos
    # We need to be careful. The file has indentation.
    # It likely looks like:
    #     </div>
    # 
    #     <!-- Navigation Controls -->
    
    end_pos = content.rfind('</div>', 0, nav_pos)
    
    if end_pos == -1:
        print("Error: Could not find closing div of slide container")
        return
    
    # We want to keep the </div> at end_pos.
    # So we remove from start_pos UP TO end_pos.
    # But we might want to trim whitespace before end_pos to make it clean.
    # Let's just slice strictly.
    
    print(f"Removing content from index {start_pos} to {end_pos}")
    
    new_content = content[:start_pos] + content[end_pos:]
    
    # 3. Update Total Slides
    # Replaces <span id="totalSlides">38</span> (or whatever number) with 5
    new_content = re.sub(r'<span id="totalSlides">\d+</span>', '<span id="totalSlides">5</span>', new_content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Successfully removed slides 6-44 and updated total count.")

if __name__ == "__main__":
    main()
