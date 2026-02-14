
import re

file_path = r'c:\Users\sukes\Downloads\kec docs\kec site\day1.html'

# Content for Slide 6
new_slide6_content = r'''
    <!-- SLIDE 6: What is RAM? -->
    <section class="slide" data-slide="6">
        <div class="slide-content">
            <h1>What is RAM?</h1>
            <p class="subtitle">Deep, Practical & Technical Explanation</p>

            <!-- Definition -->
            <div class="content-card">
                <h2>💾 RAM = Temporary Working Memory</h2>
                <p><strong>Random Access Memory</strong> is the active workspace of your computer.</p>
                <ul class="big-list">
                    <li>Stores running programs</li>
                    <li>Stores currently open files</li>
                    <li>Stores background processes</li>
                    <li>Stores OS tasks</li>
                </ul>
                <div class="callout warning" style="margin-top: 1rem;">
                    <strong>🔄 Clears when power is off:</strong> RAM is volatile memory. Power off → Data erased.
                </div>
            </div>

            <!-- Memory Hierarchy -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🏗 Where RAM Sits in Memory Hierarchy</h2>
                <table style="width: 100%; border-collapse: collapse; margin-top: 1rem; color: white;">
                    <tr>
                        <th style="padding: 0.5rem; border-bottom: 1px solid rgba(255,255,255,0.2);">Level</th>
                        <th style="padding: 0.5rem; border-bottom: 1px solid rgba(255,255,255,0.2);">Speed</th>
                        <th style="padding: 0.5rem; border-bottom: 1px solid rgba(255,255,255,0.2);">Size</th>
                        <th style="padding: 0.5rem; border-bottom: 1px solid rgba(255,255,255,0.2);">Example</th>
                    </tr>
                    <tr><td style="padding: 0.5rem;">Cache</td><td style="padding: 0.5rem;">Fastest</td><td style="padding: 0.5rem;">Very small</td><td style="padding: 0.5rem;">Inside CPU</td></tr>
                    <tr><td style="padding: 0.5rem;">RAM</td><td style="padding: 0.5rem;">Very fast</td><td style="padding: 0.5rem;">Medium</td><td style="padding: 0.5rem;">8–64GB</td></tr>
                    <tr><td style="padding: 0.5rem;">SSD</td><td style="padding: 0.5rem;">Slower</td><td style="padding: 0.5rem;">Large</td><td style="padding: 0.5rem;">512GB–2TB</td></tr>
                    <tr><td style="padding: 0.5rem;">HDD</td><td style="padding: 0.5rem;">Slowest</td><td style="padding: 0.5rem;">Very large</td><td style="padding: 0.5rem;">1TB+</td></tr>
                </table>
                <p class="highlight center" style="margin-top: 1rem;">CPU asks RAM for data thousands of times per second.</p>
            </div>

            <!-- Low RAM Warning -->
            <div class="callout warning" style="margin-top: 2rem;">
                <h3>🚨 Low RAM = Lag & Crashes (Why?)</h3>
                <p>When RAM is full, system uses <strong>page file (virtual memory)</strong> on SSD.</p>
                <ul class="big-list">
                    <li>SSD is much slower than RAM → System becomes slow</li>
                    <li>Apps may crash (Memory Swapping)</li>
                </ul>
            </div>

            <!-- Capacity Truth -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>📊 RAM Capacity Truth</h2>
                <div class="comparison-grid">
                    <div class="comparison-card">
                        <h3>8 GB → Basic</h3>
                        <ul class="big-list">
                            <li>Browsing, Office</li>
                            <li>Light coding, Online classes</li>
                        </ul>
                        <p class="highlight" style="font-size: 0.9rem;">⚠️ Struggles with Heavy Chrome tabs, Android Studio, VMs</p>
                    </div>
                    <div class="comparison-card" style="border: 2px solid var(--color-primary);">
                        <h3>16 GB → Sweet Spot</h3>
                        <ul class="big-list">
                            <li>Coding, Multitasking</li>
                            <li>Light video editing</li>
                            <li>Most students & developers</li>
                        </ul>
                        <p class="highlight" style="font-size: 0.9rem;">👉 Best balance today.</p>
                    </div>
                    <div class="comparison-card">
                        <h3>32 GB → Heavy Tasks</h3>
                        <ul class="big-list">
                            <li>AI models, Simulations</li>
                            <li>Rendering, Virtual machines</li>
                            <li>Large datasets</li>
                        </ul>
                    </div>
                </div>
                <div class="callout tip">
                    <strong>❌ More RAM ≠ Faster PC Always:</strong> If your system only uses 10GB, adding 64GB won’t increase speed. RAM improves stability under load.
                </div>
            </div>

            <!-- Speed vs Latency -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>⚡ RAM Speed vs Latency (Very Important)</h2>
                <div class="comparison-grid">
                    <div class="comparison-card">
                        <h3>MHz (Frequency)</h3>
                        <p>Measured in MHz (e.g., 3200 MHz)</p>
                        <p>Higher MHz = more data transferred per second</p>
                    </div>
                    <div class="comparison-card">
                        <h3>CL (CAS Latency)</h3>
                        <p>Measured as a number (e.g., CL16)</p>
                        <p>Lower = faster response</p>
                    </div>
                </div>
                <h3 style="margin-top: 1rem;">⚖ Both Matter Together</h3>
                <table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem; color: white;">
                    <tr><th style="padding: 0.5rem; text-align: left;">RAM</th><th style="padding: 0.5rem; text-align: left;">Speed</th><th style="padding: 0.5rem; text-align: left;">Latency</th></tr>
                    <tr><td style="padding: 0.5rem;">3200 CL16</td><td style="padding: 0.5rem;">Balanced</td><td style="padding: 0.5rem;">Good</td></tr>
                    <tr><td style="padding: 0.5rem;">3600 CL18</td><td style="padding: 0.5rem;">Slightly higher bandwidth</td><td style="padding: 0.5rem;">Good</td></tr>
                    <tr><td style="padding: 0.5rem;">3200 CL22</td><td style="padding: 0.5rem;">Slower response</td><td style="padding: 0.5rem;">Bad</td></tr>
                </table>
                <p class="highlight center">📌 Effective latency matters more than just MHz.</p>
            </div>

            <!-- DDR4 vs DDR5 -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🔬 DDR4 vs DDR5 (In-Depth)</h2>
                <div class="comparison-grid">
                    <div class="comparison-card">
                        <h3>DDR4</h3>
                        <ul class="big-list">
                            <li>✓ Cheaper, Mature ecosystem</li>
                            <li>✓ Works with older CPUs</li>
                            <li>Speed: 2133–3600 MHz</li>
                        </ul>
                    </div>
                    <div class="comparison-card">
                        <h3>DDR5</h3>
                        <ul class="big-list">
                            <li>✓ Higher base speed</li>
                            <li>✓ On-module power management</li>
                            <li>Speed: 4800–8000+ MHz</li>
                        </ul>
                    </div>
                </div>
                <div class="callout warning">
                    <strong>⚠️ Not interchangeable:</strong> DDR4 board → cannot use DDR5. DDR5 board → cannot use DDR4.
                </div>
            </div>

            <!-- Dual Channel -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🔄 Dual Channel Concept</h2>
                <div class="comparison-grid">
                    <div class="comparison-card">
                        <h3>Single Channel</h3>
                        <p>1 RAM stick</p>
                        <p>Lower bandwidth</p>
                    </div>
                    <div class="comparison-card">
                        <h3>Dual Channel</h3>
                        <p>2 identical RAM sticks</p>
                        <p>Doubles memory bandwidth</p>
                    </div>
                </div>
                <p class="highlight center">📌 Example: 2×8GB (Dual) is faster than 1×16GB (Single)</p>
                <h3>🧠 Why Dual Channel Matters</h3>
                <ul class="big-list">
                    <li>Better gaming performance</li>
                    <li>Faster data transfer</li>
                    <li>Better integrated GPU performance</li>
                    <li>Faster AI dataset handling (5–20% difference)</li>
                </ul>
            </div>

            <!-- XMP / EXPO -->
            <div class="content-card" style="margin-top: 2rem; border-left: 4px solid #F59E0B;">
                <h2>🧩 XMP / EXPO (Very Important)</h2>
                <p>RAM does NOT run at advertised speed automatically.</p>
                <div class="highlight">
                    You must enable <strong>XMP (Intel)</strong> or <strong>EXPO (AMD)</strong> in BIOS.
                </div>
                <p>Otherwise: 3200 MHz RAM may run at 2133 MHz.</p>
            </div>

            <!-- Other Important Concepts -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🔥 Other Important RAM Concepts</h2>
                
                <h3>1️⃣ Memory Rank</h3>
                <p><strong>Single Rank</strong> (One data block) vs <strong>Dual Rank</strong>. Dual Rank often faster in multitasking.</p>

                <h3 style="margin-top: 1rem;">2️⃣ RAM Form Factor</h3>
                <p><strong>Desktop</strong> → DIMM | <strong>Laptop</strong> → SO-DIMM (Not interchangeable)</p>

                <h3 style="margin-top: 1rem;">3️⃣ ECC RAM</h3>
                <p>Error Correcting Code. Used in Servers/Workstations. Not required for normal users.</p>

                <h3 style="margin-top: 1rem;">4️⃣ RAM & Integrated Graphics</h3>
                <p>If using Intel iGPU or AMD APU, RAM speed matters A LOT because GPU uses system RAM.</p>

                <h3 style="margin-top: 1rem;">5️⃣ RAM & AI / Data Science</h3>
                <p>Large datasets → Need higher capacity.<br>
                ML training → More RAM reduces disk swapping.<br>
                Parallel tasks → Dual channel helps.</p>
            </div>

            <!-- Real-World Example -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🧠 Real-World Example</h2>
                <div class="comparison-grid">
                    <div class="comparison-card">
                        <h3>System A</h3>
                        <p>i5 + 8GB + single channel</p>
                        <p>→ Lag with 15 Chrome tabs</p>
                    </div>
                    <div class="comparison-card">
                        <h3>System B</h3>
                        <p>Same i5 + 16GB dual channel</p>
                        <p>→ Smooth performance</p>
                    </div>
                </div>
                <p class="highlight center">CPU same. RAM changed. Performance improved.</p>
            </div>

            <!-- Smart Buying Advice -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🎯 Smart Buying Advice</h2>
                 <ul class="big-list">
                    <li><strong>Students:</strong> 16GB (2×8GB) DDR4 or DDR5</li>
                    <li><strong>Developers:</strong> 16GB minimum (32GB if using VMs)</li>
                    <li><strong>AI / Simulations:</strong> 32GB recommended</li>
                </ul>
            </div>

            <div class="content-card" style="margin-top: 2rem;">
                <h2>🏁 One-Line Summary</h2>
                <div class="highlight">
                    RAM is your system’s workspace. Capacity decides how much you can do. Speed + latency decide how fast you can do it.
                </div>
            </div>
        </div>
    </section>
'''

def main():
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find end of Slide 5 (Motherboard)
    # We look for <section class="slide" data-slide="5"> ... </section>
    
    start_sl5 = content.find('<section class="slide" data-slide="5">')
    if start_sl5 == -1:
        # Fallback regex
        match = re.search(r'<section class="slide"\s+data-slide="5">', content)
        if match:
            start_sl5 = match.start()
            
    if start_sl5 == -1:
        print("Error: Could not find Slide 5 start.")
        return

    # Find closing tag of Slide 5
    end_sl5 = content.find('</section>', start_sl5)
    if end_sl5 == -1:
        print("Error: Could not find Slide 5 end.")
        return
        
    end_sl5 += len('</section>') # Include tag

    # Insert Slide 6 after Slide 5
    print(f"Inserting Slide 6 after Slide 5 (index {end_sl5})")
    
    new_content = content[:end_sl5] + "\n\n" + new_slide6_content + content[end_sl5:]
    
    # Update total slide count to 6
    new_content = re.sub(r'<span id="totalSlides">\d+</span>', '<span id="totalSlides">6</span>', new_content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Successfully added Slide 6 (RAM) and updated slide count to 6.")

if __name__ == "__main__":
    main()
