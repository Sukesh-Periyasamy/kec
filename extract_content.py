import re
import html
from pathlib import Path

def clean_text(text):
    """Remove HTML tags and clean up text"""
    # Decode HTML entities
    text = html.unescape(text)
    # Remove script and style elements
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)
    # Clean up whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_day_content(filename):
    """Extract all slide content from a day HTML file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all slides
        slides = re.findall(r'<section[^>]*class="slide[^"]*"[^>]*>(.*?)</section>', content, re.DOTALL)
        
        print(f"\n{'='*60}")
        print(f"{filename}: Found {len(slides)} slides")
        print(f"{'='*60}\n")
        
        output = []
        for i, slide in enumerate(slides, 1):
            cleaned = clean_text(slide)
            if cleaned:
                output.append(f"## Slide {i}\n{cleaned}\n")
        
        return '\n'.join(output)
    
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return ""

# Extract content from all day files
files = ['day1.html', 'day2.html', 'day3.html', 'day4.html']

all_content = []
for filename in files:
    if Path(filename).exists():
        day_num = filename.replace('.html', '').replace('day', ' Day ')
        all_content.append(f"\n\n# ===== {day_num.upper()} COMPLETE CONTENT =====\n\n")
        all_content.append(extract_day_content(filename))

# Write to output file
with open('DAY_CONTENT_EXTRACTED.md', 'w', encoding='utf-8') as f:
    f.write(''.join(all_content))

print("\n\nExtraction complete! Saved to DAY_CONTENT_EXTRACTED.md")
