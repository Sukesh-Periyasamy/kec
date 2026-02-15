import re
from bs4 import BeautifulSoup

try:
    with open('day2.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    slides = soup.find_all('section', class_='slide')

    output_text = ''
    for i, slide in enumerate(slides, 1):
        # check for data-slide attribute first, otherwise use counter
        slide_num = slide.get('data-slide', str(i))
        
        output_text += f'--- SLIDE {slide_num} ---\n'
        
        content = slide.find('div', class_='slide-content')
        if content:
            # Clean extraction:
            # 1. Get all text with separator
            text = content.get_text(separator='\n', strip=True)
            # 2. Add some spacing
            lines = [line.strip() for line in text.splitlines() if line.strip()]
            output_text += '\n'.join(lines)
            
        output_text += '\n\n' + '='*30 + '\n\n'

    with open('day2.txt', 'w', encoding='utf-8') as f:
        f.write(output_text)

    print("Successfully extracted slide text to day2.txt")

except Exception as e:
    print(f"Error: {e}")
