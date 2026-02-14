import re

file_path = 'day1.html'

def update_day1():
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Extract the Workshop Topics content
    # Look for the specific content card we added
    topics_pattern = re.compile(r'(<div class="content-card" style="padding: 1\.5rem;">\s*<h3>Workshop Topics</h3>[\s\S]*?</div>)', re.DOTALL)
    match = topics_pattern.search(content)
    
    if not match:
        print("Could not find Workshop Topics section to move.")
        return

    topics_html = match.group(1)
    
    # 2. Remove the Topics section from its current place
    content_without_topics = content.replace(topics_html, '')
    
    # 3. Create the new Slide 1 HTML
    # We need to wrap the topics HTML in a slide section
    # And ensure the title is correct
    new_slide_html = f'''
        <!-- SLIDE 1: Workshop Topics -->
        <section class="slide active" data-slide="1" role="region" aria-label="Slide 1">
            <div class="slide-content">
                <h1 class="title">Workshop Topics</h1>
                <h2 class="subtitle">What We Will Cover</h2>
                {topics_html}
            </div>
        </section>
'''

    # 4. Remove 'active' class from the *old* Slide 1
    # The old slide 1 is currently: <section class="slide active" data-slide="1"
    # We replace it with: <section class="slide" data-slide="1" (we will renumber later)
    content_modified = re.sub(r'<section class="slide active" data-slide="1"', '<section class="slide" data-slide="1"', content_without_topics)

    # 5. Insert the new slide at the beginning of slide-container
    container_start = '<div class="slide-container">'
    insert_pos = content_modified.find(container_start) + len(container_start)
    
    final_content = content_modified[:insert_pos] + new_slide_html + content_modified[insert_pos:]

    # 6. Renumber all slides
    # We need to find all data-slide="N" and replace them with correct sequential numbers
    # The new slide is hardcoded as 1. The old slide 1 (now simple slide) is still marked as 1 in text, 
    # but we need to re-index EVERYTHING from scratch to be safe.
    
    # Actually, simpler approach:
    # 1. Split content by sections
    # 2. Re-assign numbers
    
    def replace_slide_number(match):
        # We use a counter in the closure or global? 
        # Regex replacement with function doesn't easily support state across multiple calls unless we use an object
        return match.group(0) # placeholder

    # Let's iterate manually
    # Find all slide definitions
    slide_pattern = re.compile(r'<section class="slide.*?" data-slide="(\d+)"')
    
    # We will build a new content string by iterating
    # But strings are immutable.
    
    # Better: find all start positions, then iterate and replace
    matches = list(slide_pattern.finditer(final_content))
    
    # We need to replace from last to first to not mess up indices
    new_total_slides = 0
    
    # Convert string to list of chars for easier manipulation or just string slicing
    # Because we added a slide at the top (data-slide="1"), and the next is ALSO data-slide="1" (the old one)
    # And then data-slide="2", etc.
    # We basically want to renumber 1, 1, 2, 3... to 1, 2, 3, 4...
    
    # Let's verify existing slides.
    # The new slide is inserted. 
    # Current sequence in text: [New Slide 1], [Old Slide 1 (marked 1)], [Old Slide 2 (marked 2)]...
    
    # New re-numbering logic:
    current_slide_num = 1
    
    def sub_callback(m):
        nonlocal current_slide_num
        # Keep class attributes but update number
        full_tag = m.group(0)
        # Replace the number inside the tag
        new_tag = re.sub(r'data-slide="\d+"', f'data-slide="{current_slide_num}"', full_tag)
        # Also update aria-label if present
        if 'aria-label="Slide' in full_tag:
             new_tag = re.sub(r'aria-label="Slide \d+"', f'aria-label="Slide {current_slide_num}"', new_tag)
        elif 'aria-label="Slide' not in full_tag:
             # Add aria-label if missing (optional, but good practice)
             pass
             
        current_slide_num += 1
        return new_tag

    final_content = slide_pattern.sub(sub_callback, final_content)
    new_total_slides = current_slide_num - 1 # because it increments after usage

    # 7. Update total slides count in footer
    # <span id="totalSlides">43</span>
    final_content = re.sub(r'<span id="totalSlides">\d+</span>', f'<span id="totalSlides">{new_total_slides}</span>', final_content)

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"Successfully inserted new slide. Total slides: {new_total_slides}")

if __name__ == "__main__":
    update_day1()
