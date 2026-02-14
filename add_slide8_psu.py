
import re

file_path = r'c:\Users\sukes\Downloads\kec docs\kec site\day1.html'

# Content for Slide 8 (PSU)
slide8_psu_content = r'''
    <!-- SLIDE 8: What is a PSU? -->
    <section class="slide" data-slide="8">
        <div class="slide-content">
            <h1>What is a PSU?</h1>
            <p class="subtitle">Power Supply Unit — Explained In-Depth</p>

            <!-- Definition -->
            <div class="content-card">
                <h2>⚡ PSU = Power Supply Unit</h2>
                <p>The PSU feeds life to your PC. It does three critical jobs:</p>
                <ul class="big-list">
                    <li><strong>🔄 Converts AC → DC:</strong> Wall socket (AC) to Component power (DC).</li>
                    <li><strong>⚡ Supplies Clean Power:</strong> Smooths fluctuations, prevents spikes.</li>
                    <li><strong>🛡️ Protects Components:</strong> OVP, OCP, SCP (Short Circuit Protection).</li>
                </ul>
                <div class="callout warning" style="margin-top: 1rem;">
                    <strong>⚠️ Most ignored, most important part:</strong> Cheap PSU = risk of killing components.
                </div>
            </div>

            <!-- Wattage Reality -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>⚡ PSU Wattage Reality (Big Myth Buster)</h2>
                <p><strong>Wattage = Maximum Output</strong> (Not forced consumption)</p>
                <div class="example-box">
                    <p><strong>Example:</strong> 750W PSU with 320W PC load 👉 Supplies only 320W.</p>
                </div>
                <p class="highlight center">❌ Higher Watt ≠ Higher Electricity Bill. 📌 Think of PSU like a water tank, not a pump.</p>
            </div>

            <!-- Review Wattage Needs -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🧮 How Much Wattage Do You Actually Need?</h2>
                <table style="width: 100%; border-collapse: collapse; margin-top: 1rem; color: white;">
                    <tr><th style="padding: 0.5rem; text-align: left;">System Type</th><th style="padding: 0.5rem; text-align: left;">Recommended PSU</th></tr>
                    <tr><td style="padding: 0.5rem;">Office PC</td><td style="padding: 0.5rem;">450–550W</td></tr>
                    <tr><td style="padding: 0.5rem;">Entry GPU</td><td style="padding: 0.5rem;">550–650W</td></tr>
                    <tr><td style="padding: 0.5rem;">Mid GPU</td><td style="padding: 0.5rem;">650–750W</td></tr>
                    <tr><td style="padding: 0.5rem;">High-end GPU</td><td style="padding: 0.5rem;">750–850W+</td></tr>
                </table>
                <p class="highlight" style="font-size: 0.9rem;">👉 Always keep 30% headroom.</p>
            </div>

            <!-- Efficiency Ratings -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🏅 PSU Quality & 80+ Ratings</h2>
                <p><strong>Efficiency = How much wall power becomes usable PC power.</strong></p>
                <div class="comparison-grid">
                    <div class="comparison-card">
                        <h3>Bronze</h3>
                        <p>~82–85%</p>
                        <p>Good</p>
                    </div>
                    <div class="comparison-card" style="border: 2px solid #F59E0B;">
                        <h3>Gold</h3>
                        <p>~87–90%</p>
                        <p>Best Value</p>
                    </div>
                    <div class="comparison-card">
                        <h3>Platinum</h3>
                        <p>~90–92%</p>
                        <p>Premium</p>
                    </div>
                </div>
                <p class="highlight center">📌 Gold is the sweet spot. Higher efficiency = Less heat, Quieter.</p>
            </div>

            <!-- Cheap vs Good -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🔥 Cheap PSU vs Good PSU</h2>
                <div class="comparison-grid">
                    <div class="comparison-card" style="border-top: 3px solid #EF4444;">
                        <h3>Cheap PSU</h3>
                        <ul class="big-list">
                            <li>Fake wattage</li>
                            <li>Poor protection</li>
                            <li>Voltage spikes</li>
                            <li><strong>Can damage PC</strong></li>
                        </ul>
                    </div>
                    <div class="comparison-card" style="border-top: 3px solid #10B981;">
                        <h3>Good PSU</h3>
                        <ul class="big-list">
                            <li>True rated</li>
                            <li>Full protection</li>
                            <li>Stable output</li>
                            <li><strong>Protects PC</strong></li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Cables Explained -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🔌 PSU Cables Explained (Know This!)</h2>
                <ul class="big-list">
                    <li><strong>24-Pin ATX:</strong> Main motherboard power.</li>
                    <li><strong>8-Pin (4+4) CPU:</strong> Powers CPU VRMs.</li>
                    <li><strong>PCIe (6+2) GPU:</strong> Powers Graphics Card.</li>
                    <li><strong>SATA Power:</strong> SSDs, HDDs, RGB.</li>
                </ul>
                <div class="callout warning">
                    <strong>⚠️ CRITICAL WARNING:</strong> Never Mix PSU Cables! Pinouts differ. Mixing can kill SSD/Motherboard.
                </div>
            </div>

            <!-- Modular vs Non-Modular -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🧩 Modular vs Non-Modular PSU</h2>
                <table style="width: 100%; border-collapse: collapse; margin-top: 1rem; color: white;">
                    <tr><th style="padding: 0.5rem; text-align: left;">Type</th><th style="padding: 0.5rem; text-align: left;">Description</th></tr>
                    <tr><td style="padding: 0.5rem;">Non-modular</td><td style="padding: 0.5rem;">All cables fixed</td></tr>
                    <tr><td style="padding: 0.5rem;">Semi-modular</td><td style="padding: 0.5rem;">Some fixed, some detachable</td></tr>
                    <tr><td style="padding: 0.5rem;">Fully modular</td><td style="padding: 0.5rem;">All cables detachable (Cleaner, Better Airflow)</td></tr>
                </table>
            </div>

            <!-- Cooling & Orientation -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>❄️ PSU Cooling & Orientation</h2>
                <p>PSU has its own fan. <strong>Mount fan towards vent</strong> (usually bottom).</p>
                <p class="highlight">Wrong orientation → overheating.</p>
            </div>

            <!-- Real World Example -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🧪 Real Example (Why it Matters)</h2>
                 <div class="comparison-grid">
                    <div class="comparison-card">
                        <h3>High-end GPU + Cheap PSU</h3>
                        <p>PC boots → Crashes under load → GPU throttles.</p>
                    </div>
                    <div class="comparison-card">
                        <h3>Same PC + Good Gold PSU</h3>
                        <p>Stable → Sustained boost → Longer life.</p>
                    </div>
                </div>
            </div>

            <div class="content-card" style="margin-top: 2rem;">
                <h2>🏁 One-Line Summary</h2>
                <div class="highlight center">
                    CPU is the brain, GPU is the muscle, PSU is the heart — weak heart, whole system fails.
                </div>
            </div>
        </div>
    </section>
'''

def main():
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to insert PSU slide (new Slide 8) BEFORE the current Slide 8 ("Storage & Cooling")
    # And then rename current Slide 8 to Slide 9.
    
    # 1. Find Start of current Slide 8
    start_sl8_current = content.find('<section class="slide" data-slide="8">')
    if start_sl8_current == -1:
         match = re.search(r'<section class="slide"\s+data-slide="8">', content)
         if match:
             start_sl8_current = match.start()
    
    if start_sl8_current == -1:
        print("Error: Could not find current Slide 8 start.")
        return

    # 2. Rename current Slide 8 to Slide 9 in the content buffer (we'll modify the file later)
    # We can just replace the definition at this location
    # BUT we need to be careful not to mess up indexing.
    
    # Let's verify we have the right slide
    # extract the first few lines to check title
    chunk = content[start_sl8_current:start_sl8_current+200]
    if "Storage" not in chunk and "Cooling" not in chunk:
         print(f"Warning: Slide 8 might not be Storage & Cooling. Chunk: {chunk}")
         # Proceeding anyway as indexes are what matters for the user request
    
    # 3. Modify the existing content string to change Slide 8 -> Slide 9
    # We only change the one at start_sl8_current.
    # We can splice the new content in right before start_sl8_current.
    
    # The new content already has data-slide="8"
    
    # So:
    # [Content before Slide 8] + [New PSU Slide 8] + [Old Slide 8 (renamed to 9)] + [Rest]
    
    prefix = content[:start_sl8_current]
    suffix = content[start_sl8_current:]
    
    # Rename data-slide="8" to data-slide="9" in the suffix (the old Slide 8)
    # We only want to replace the FIRST occurrence in suffix
    suffix = suffix.replace('data-slide="8"', 'data-slide="9"', 1)
    
    # Also we need to update total slide count to 9
    
    new_content = prefix + "\n\n" + slide8_psu_content + "\n\n" + suffix
    
    new_content = re.sub(r'<span id="totalSlides">\d+</span>', '<span id="totalSlides">9</span>', new_content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Successfully added Slide 8 (PSU), moved Storage to Slide 9, updated count to 9.")

if __name__ == "__main__":
    main()
