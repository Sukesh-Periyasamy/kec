
import re

file_path = r'c:\Users\sukes\Downloads\kec docs\kec site\day1.html'

# Content for Slide 10
slide10_content = r'''
    <!-- SLIDE 10: Monitor, Ports & Cables -->
    <section class="slide" data-slide="10">
        <div class="slide-content">
            <h1>Monitor, Ports & Cables</h1>
            <p class="subtitle">Complete Practical Guide (Beginner → Advanced)</p>

            <!-- Monitor Basics -->
            <div class="content-card">
                <h2>🖥️ Monitor Basics (What Actually Matters)</h2>
                <div class="comparison-grid">
                    <div class="comparison-card">
                        <h3>📏 Size</h3>
                        <p>Measured diagonally.</p>
                        <ul class="big-list">
                            <li><strong>24″:</strong> Best for 1080p</li>
                            <li><strong>27″:</strong> Best for 1440p</li>
                            <li><strong>32″:</strong> Best for 4K</li>
                        </ul>
                    </div>
                    <div class="comparison-card">
                        <h3>🖼️ Resolution</h3>
                        <table style="width: 100%; color: white; margin-top: 0.5rem;">
                            <tr><td>1080p</td><td>Full HD</td></tr>
                            <tr><td>1440p</td><td>2K</td></tr>
                            <tr><td>2160p</td><td>4K (Sharpest)</td></tr>
                        </table>
                    </div>
                    <div class="comparison-card">
                        <h3>🔄 Refresh Rate</h3>
                        <ul class="big-list">
                            <li><strong>60Hz:</strong> Office</li>
                            <li><strong>144Hz:</strong> Gaming</li>
                            <li><strong>240Hz:</strong> Esports</li>
                        </ul>
                    </div>
                </div>
                <p class="highlight center" style="margin-top: 1rem;">⚠️ GPU + Cable + Monitor must ALL support the refresh rate.</p>
            </div>

            <!-- Panel Types -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🎨 Panel Types</h2>
                <table style="width: 100%; border-collapse: collapse; color: white;">
                    <tr style="border-bottom: 1px solid rgba(255,255,255,0.2);"><th style="padding:0.5rem; text-align:left;">Panel</th><th style="padding:0.5rem; text-align:left;">Strength</th></tr>
                    <tr><td style="padding:0.5rem;"><strong>IPS</strong></td><td style="padding:0.5rem;">Best colors, viewing angles (Best for most)</td></tr>
                    <tr><td style="padding:0.5rem;"><strong>VA</strong></td><td style="padding:0.5rem;">Best contrast (Deep blacks)</td></tr>
                    <tr><td style="padding:0.5rem;"><strong>TN</strong></td><td style="padding:0.5rem;">Fastest, poor colors (Old esports)</td></tr>
                </table>
            </div>

            <!-- Display Cables -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🔌 Display Cables (VERY IMPORTANT)</h2>
                <div class="comparison-grid">
                    <div class="comparison-card">
                        <h3>HDMI</h3>
                        <p>TVs, Laptops, Monitors</p>
                        <ul class="big-list">
                            <li><strong>1.4:</strong> 1080p 144Hz</li>
                            <li><strong>2.0:</strong> 1440p 144Hz</li>
                            <li><strong>2.1:</strong> 4K 144Hz / 8K</li>
                        </ul>
                        <p class="highlight">Video + Audio</p>
                    </div>
                    <div class="comparison-card" style="border: 2px solid var(--color-primary);">
                        <h3>DisplayPort (DP)</h3>
                        <p>Best for PCs</p>
                        <ul class="big-list">
                            <li><strong>1.2:</strong> 1440p 144Hz</li>
                            <li><strong>1.4:</strong> 4K 144Hz</li>
                        </ul>
                        <p class="highlight">Sup. G-Sync/FreeSync</p>
                    </div>
                    <div class="comparison-card" style="opacity: 0.7;">
                        <h3>VGA / DVI (OLD)</h3>
                        <p>❌ Avoid</p>
                        <ul class="big-list">
                            <li>Analog / Old Digital</li>
                            <li>No Audio (VGA)</li>
                            <li>Obsolete</li>
                        </ul>
                    </div>
                </div>
                <div class="callout tip">
                    <strong>🧠 Rule:</strong> TV / Casual → HDMI. Gaming / High Refresh → DisplayPort.
                </div>
            </div>

            <!-- USB Ports -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🔌 USB Ports Explained</h2>
                <div class="callout warning">
                    <strong>⚠️ Confusion Alert:</strong> USB Version (Speed) ≠ USB Shape (Connector).
                </div>
                
                <h3 style="margin-top: 1rem;">⚡ USB Speeds</h3>
                <table style="width: 100%; border-collapse: collapse; color: white;">
                    <tr><td style="padding:0.2rem;">USB 2.0</td><td style="padding:0.2rem;">480 Mbps</td></tr>
                    <tr><td style="padding:0.2rem;">USB 3.2 Gen1</td><td style="padding:0.2rem;">5 Gbps</td></tr>
                    <tr><td style="padding:0.2rem;">USB 3.2 Gen2</td><td style="padding:0.2rem;">10 Gbps</td></tr>
                </table>

                <h3 style="margin-top: 1rem;">📌 USB-C Truth</h3>
                <p>USB-C is just a <strong>shape</strong>. It MAY support Charging, Data, Display (Alt Mode)... or just charging. <strong>Check specs!</strong></p>
            </div>

            <!-- Thunderbolt & Ethernet -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>⚡ Thunderbolt & Network</h2>
                <div class="comparison-grid">
                    <div class="comparison-card">
                        <h3>Thunderbolt 3/4</h3>
                        <p>Uses USB-C connector</p>
                        <ul class="big-list">
                            <li>🚀 40 Gbps</li>
                            <li>Video + Power + Data</li>
                            <li>Daisy Chaining</li>
                        </ul>
                    </div>
                    <div class="comparison-card">
                        <h3>Ethernet (LAN)</h3>
                        <p>Wired Internet (RJ45)</p>
                        <ul class="big-list">
                            <li>Cat5e: 1 Gbps</li>
                            <li>Cat6: 10 Gbps</li>
                            <li>Lower latency than Wi-Fi</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Internal Cables & Other Ports -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🔌 Internal & Audio Cables</h2>
                
                <h3>🔲 Internal PC Cables</h3>
                <ul class="big-list">
                     <li><strong>SATA Data:</strong> Motherboard ↔ SSD/HDD (Thin cable)</li>
                     <li><strong>SATA Power:</strong> PSU → Storage (Wide connector) ❌ Not interchangeable</li>
                     <li><strong>Front Panel:</strong> Power SW, Reset, HDD LED (Polarity matters!)</li>
                     <li><strong>Fan Headers:</strong> CPU_FAN (Cooler), SYS_FAN (Case), PUMP (AIO)</li>
                </ul>

                <h3 style="margin-top: 1rem;">🌈 RGB vs ARGB (Don't Burn It!)</h3>
                <p><strong>RGB (12V, 4-pin)</strong> vs <strong>ARGB (5V, 3-pin)</strong>. Mixing = 🔥 Burned LEDs.</p>

                <h3 style="margin-top: 1rem;">🔊 Audio Ports</h3>
                <p>💚 Green (Headphones) | 🩷 Pink (Mic) | 💙 Blue (Line-in)</p>
            </div>
            
            <div class="content-card" style="margin-top: 2rem;">
                 <h2>🧠 Monitor + Cable + GPU Rule</h2>
                 <p class="highlight center">All three must support Resolution, Refresh Rate, and Color Depth.<br>Weakest link limits performance.</p>
            </div>

            <div class="content-card" style="margin-top: 2rem;">
                <h2>🏁 One-Line Truths</h2>
                <ul class="big-list">
                    <li>Cable choice matters.</li>
                    <li>USB-C ≠ Thunderbolt.</li>
                    <li>HDMI ≠ DisplayPort.</li>
                    <li>ARGB ≠ RGB.</li>
                    <li>Ports define capability, not looks.</li>
                </ul>
            </div>

            <div class="content-card" style="margin-top: 2rem;">
                <h2>🧠 Ultimate Summary</h2>
                <div class="highlight center">
                    Monitor decides what you see.<br>
                    Cable decides how well you see.<br>
                    Port decides what is possible.
                </div>
            </div>
        </div>
    </section>
'''

def main():
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find end of Slide 9
    start_sl9 = content.find('<section class="slide" data-slide="9">')
    if start_sl9 == -1:
         # Try regex for flexible whitespace
         match = re.search(r'<section class="slide"\s+data-slide="9">', content)
         if match:
             start_sl9 = match.start()

    if start_sl9 == -1:
        print("Error: Could not find Slide 9 start.")
        return

    end_sl9 = content.find('</section>', start_sl9)
    if end_sl9 == -1:
        print("Error: Could not find Slide 9 end.")
        return
        
    end_sl9 += len('</section>') # Include tag

    # Insert Slide 10 after Slide 9
    print(f"Inserting Slide 10 after Slide 9 (index {end_sl9})")
    
    new_content = content[:end_sl9] + "\n\n" + slide10_content + content[end_sl9:]
    
    # Update total slide count to 10
    new_content = re.sub(r'<span id="totalSlides">\d+</span>', '<span id="totalSlides">10</span>', new_content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Successfully added Slide 10 and updated total count to 10.")

if __name__ == "__main__":
    main()
