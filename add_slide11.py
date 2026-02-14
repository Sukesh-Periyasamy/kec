
import re

file_path = r'c:\Users\sukes\Downloads\kec docs\kec site\day1.html'

slide11_content = r'''
    <!-- SLIDE 11: What is an OS? -->
    <section class="slide" data-slide="11">
        <div class="slide-content">
            <h1>What is an OS?</h1>
            <p class="subtitle">Operating System — Deep & Practical Explanation</p>

            <!-- Definition -->
            <div class="content-card">
                <h2>⚙️ OS = Operating System</h2>
                <p>The core software layer that makes a computer usable.</p>
                <div class="comparison-grid">
                    <div class="comparison-card">
                        <h3>Controls Hardware</h3>
                        <p>CPU, RAM, GPU, Storage</p>
                    </div>
                    <div class="comparison-card">
                        <h3>Runs Apps</h3>
                        <p>Manages memory & CPU time</p>
                    </div>
                    <div class="comparison-card">
                        <h3>Interface</h3>
                        <p>GUI (Windows) / CLI (Terminal)</p>
                    </div>
                </div>
                <p class="highlight center" style="margin-top: 1rem;">Without an OS, hardware is just powered metal.</p>
            </div>

            <!-- Boot Flow -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🔄 OS Installation & Boot Flow</h2>
                <div class="steps-container" style="display: flex; justify-content: space-between; text-align: center; margin-top: 1rem; flex-wrap: wrap; gap: 0.5rem;">
                    <div style="flex: 1; min-width: 100px; border: 1px solid #555; padding: 0.5rem; border-radius: 8px;">Power ON</div>
                    <div style="align-self: center;">→</div>
                    <div style="flex: 1; min-width: 120px; border: 1px solid #10B981; padding: 0.5rem; border-radius: 8px;">BIOS / UEFI<br><span style="font-size: 0.8rem; color: #aaa;">Wake Hardware</span></div>
                    <div style="align-self: center;">→</div>
                    <div style="flex: 1; min-width: 120px; border: 1px solid #3B82F6; padding: 0.5rem; border-radius: 8px;">Bootloader<br><span style="font-size: 0.8rem; color: #aaa;">Load Kernel</span></div>
                    <div style="align-self: center;">→</div>
                    <div style="flex: 1; min-width: 120px; border: 1px solid #F59E0B; padding: 0.5rem; border-radius: 8px;">OS Kernel<br><span style="font-size: 0.8rem; color: #aaa;">Take Control</span></div>
                    <div style="align-self: center;">→</div>
                    <div style="flex: 1; min-width: 100px; border: 1px solid #fff; padding: 0.5rem; border-radius: 8px;">Usable System</div>
                </div>
            </div>

            <!-- Drivers & BIOS -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>⚙️ BIOS & Drivers (Performance Unlockers)</h2>
                
                <div class="comparison-grid">
                    <div class="comparison-card">
                        <h3>1️⃣ BIOS / UEFI</h3>
                        <ul class="big-list">
                            <li>Initializes Hardware (POST)</li>
                            <li>Controls Fan Curves, Power Limits</li>
                            <li><strong>XMP / EXPO:</strong> MUST enable for full RAM speed!</li>
                        </ul>
                    </div>
                    <div class="comparison-card" style="border: 2px solid var(--color-primary);">
                        <h3>2️⃣ Drivers</h3>
                        <p>Translators between OS and Hardware.</p>
                        <ul class="big-list">
                            <li><strong>GPU Driver:</strong> Essential for gaming/AI</li>
                            <li><strong>Chipset Driver:</strong> CPU efficiency</li>
                            <li><strong>Wi-Fi/LAN:</strong> Stability</li>
                        </ul>
                    </div>
                </div>
                <div class="callout warning">
                    <strong>⚠️ Without Drivers:</strong> Hardware runs in "Basic Mode" (Low res, no boost, slow SSD).
                </div>
            </div>

            <!-- Real World Performance -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🧠 OS + Drivers = Real Performance</h2>
                <table style="width: 100%; border-collapse: collapse; margin-top: 1rem; color: white;">
                    <tr><th style="padding: 0.5rem; text-align: left;">Component</th><th style="padding: 0.5rem; text-align: left;">Without Driver</th><th style="padding: 0.5rem; text-align: left;">With Driver</th></tr>
                    <tr><td style="padding: 0.5rem;">GPU</td><td style="padding: 0.5rem;">Low resolution / Basic</td><td style="padding: 0.5rem;">Full Power / High FPS</td></tr>
                    <tr><td style="padding: 0.5rem;">CPU</td><td style="padding: 0.5rem;">No Boost / Generic</td><td style="padding: 0.5rem;">Turbo Enabled / Efficient</td></tr>
                    <tr><td style="padding: 0.5rem;">RAM</td><td style="padding: 0.5rem;">2133 MHz (Slow)</td><td style="padding: 0.5rem;">3200+ MHz (XMP On)</td></tr>
                </table>
            </div>

            <!-- Optimization Checklist -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🎯 Best Practice OS Setup (Checklist)</h2>
                <ul class="big-list">
                    <li>✅ <strong>Update BIOS</strong> (if stable)</li>
                    <li>✅ <strong>Install OS</strong> on NVMe SSD (Not HDD!)</li>
                    <li>✅ <strong>Install Chipset Drivers</strong> first</li>
                    <li>✅ <strong>Install GPU Drivers</strong> (from NVIDIA/AMD site)</li>
                    <li>✅ <strong>Enable XMP / EXPO</strong> in BIOS</li>
                    <li>✅ <strong>Run OS Updates</strong></li>
                </ul>
            </div>

            <div class="content-card" style="margin-top: 2rem;">
                <h2>🏁 One-Line Summary</h2>
                <div class="highlight center">
                    Hardware gives potential.<br>
                    OS + BIOS + Drivers decide how much of it you actually use.
                </div>
            </div>
        </div>
    </section>
'''

def main():
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find end of Slide 10
    start_sl10 = content.find('<section class="slide" data-slide="10">')
    if start_sl10 == -1:
         match = re.search(r'<section class="slide"\s+data-slide="10">', content)
         if match:
             start_sl10 = match.start()

    if start_sl10 == -1:
        print("Error: Could not find Slide 10 start.")
        return

    end_sl10 = content.find('</section>', start_sl10)
    if end_sl10 == -1:
        print("Error: Could not find Slide 10 end.")
        return
        
    end_sl10 += len('</section>') # Include tag

    # Insert Slide 11 after Slide 10
    print(f"Inserting Slide 11 after Slide 10 (index {end_sl10})")
    
    new_content = content[:end_sl10] + "\n\n" + slide11_content + content[end_sl10:]
    
    # Update total slide count to 11
    new_content = re.sub(r'<span id="totalSlides">\d+</span>', '<span id="totalSlides">11</span>', new_content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Successfully added Slide 11 and updated total count to 11.")

if __name__ == "__main__":
    main()
