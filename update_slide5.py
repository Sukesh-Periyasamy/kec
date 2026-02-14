
import re

file_path = r'c:\Users\sukes\Downloads\kec docs\kec site\day1.html'

# The comprehensive content provided by the user, formatted as HTML
new_slide5_content = r'''       <!-- SLIDE 5: What Is a Motherboard? -->
    <section class="slide" data-slide="5">
        <div class="slide-content">
            <h1>What Is a Motherboard?</h1>
            <p class="subtitle">In-Depth, Practical Explanation</p>

            <!-- Main Functions -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🔌 Main Circuit Board</h2>
                <p class="definition">The motherboard is the foundation of the computer. Every major component plugs into it.</p>
            </div>

            <div class="content-card" style="margin-top: 2rem;">
                <h2>🔗 Connects All Components</h2>
                <p><strong>It physically and electrically connects:</strong></p>
                <ul class="big-list">
                    <li>CPU</li>
                    <li>RAM</li>
                    <li>GPU</li>
                    <li>Storage (SSD/HDD)</li>
                    <li>Power supply</li>
                    <li>USB, LAN, audio, display ports</li>
                </ul>
            </div>

            <div class="content-card" style="margin-top: 2rem;">
                <h2>⚡ Controls Communication & Power Delivery</h2>
                <ul class="big-list">
                    <li>Routes data signals between components</li>
                    <li>Distributes power safely and stably</li>
                    <li>Sets operating limits (RAM speed, PCIe version, CPU boost behavior)</li>
                </ul>
            </div>

            <div class="content-card" style="margin-top: 2rem;">
                <h2>🔄 Decides Upgrade Path</h2>
                <p><strong>Your motherboard decides:</strong></p>
                <ul class="big-list">
                    <li>Which CPUs you can install</li>
                    <li>Max RAM speed & capacity</li>
                    <li>PCIe generation (GPU / SSD speed)</li>
                    <li>Overclocking support</li>
                </ul>
                <div class="callout tip">
                    <strong>Think of the motherboard as the city map:</strong> even a fast car (CPU) can’t perform if the roads (power, lanes, cooling) are poor.
                </div>
            </div>

            <!-- CPU & Socket Dependency -->
            <div class="content-card" style="margin-top: 3rem; border-top: 3px solid var(--color-primary); padding-top: 2rem;">
                <h2>🧩 CPU & Socket Dependency</h2>

                <h3>🔌 Socket = physical CPU connection</h3>
                <p>The socket is the exact shape and pin layout where the CPU fits.<br>
                <strong>CPU and motherboard socket must match.</strong></p>

                <div class="comparison-grid">
                    <div class="comparison-card">
                        <h3>🔵 Intel</h3>
                        <p><strong>Uses LGA sockets</strong> (pins on motherboard)</p>
                        <ul class="big-list">
                            <li>LGA1200 → 10th/11th Gen</li>
                            <li>LGA1700 → 12th/13th/14th Gen</li>
                        </ul>
                        <p class="highlight" style="font-size: 0.9rem;">⚠️ Meaning: You can’t put a 12th Gen Intel CPU into an older LGA1200 board.</p>
                    </div>
                    <div class="comparison-card">
                        <h3>🔴 AMD</h3>
                        <p><strong>Uses AM sockets</strong> (pins on CPU)</p>
                        <ul class="big-list">
                            <li>AM4 → Ryzen 1000–5000</li>
                            <li>AM5 → Ryzen 7000+</li>
                        </ul>
                        <p class="highlight" style="font-size: 0.9rem;">✅ Meaning: AM4 had long support → better upgrade flexibility.</p>
                    </div>
                </div>
            </div>

            <!-- Chipsets Explained -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🧠 Motherboard Chipsets Explained (Very Important)</h2>
                <p class="definition">A chipset is the controller that defines features and limits of the motherboard.</p>

                <h3>🔵 Intel Chipsets</h3>
                <div class="comparison-grid">
                    <div class="comparison-card">
                        <h4>H-Series → Basic</h4>
                        <ul>
                            <li>No overclocking</li>
                            <li>Limited RAM speed</li>
                            <li>Fewer USB & PCIe lanes</li>
                        </ul>
                        <p class="highlight">Office / budget builds</p>
                    </div>
                    <div class="comparison-card">
                        <h4>B-Series → Balanced</h4>
                        <ul>
                            <li>Better RAM support</li>
                            <li>Good I/O</li>
                            <li>No CPU overclocking</li>
                        </ul>
                        <p class="highlight">Best for students & developers</p>
                    </div>
                    <div class="comparison-card">
                        <h4>Z-Series → Overclocking</h4>
                        <ul>
                            <li>CPU + RAM overclocking</li>
                            <li>Strong VRMs</li>
                            <li>More PCIe lanes</li>
                        </ul>
                        <p class="highlight">Enthusiast / gaming rigs</p>
                    </div>
                </div>

                <h3>🔴 AMD Chipsets</h3>
                <div class="comparison-grid">
                    <div class="comparison-card">
                        <h4>A-Series → Entry</h4>
                         <ul>
                            <li>Basic features</li>
                            <li>Limited expansion</li>
                        </ul>
                        <p class="highlight">Office / basic use</p>
                    </div>
                    <div class="comparison-card">
                        <h4>B-Series → Best Value</h4>
                         <ul>
                            <li>RAM & CPU tuning</li>
                            <li>Good VRMs</li>
                        </ul>
                        <p class="highlight">Excellent for coding & multitasking</p>
                    </div>
                    <div class="comparison-card">
                        <h4>X-Series → High-End</h4>
                         <ul>
                            <li>Maximum PCIe lanes</li>
                            <li>Strongest power delivery</li>
                        </ul>
                        <p class="highlight">Multi-GPU / heavy workloads</p>
                    </div>
                </div>
            </div>

            <!-- Performance Factors -->
            <div class="content-card" style="margin-top: 3rem; border-top: 3px solid var(--color-primary); padding-top: 2rem;">
                <h2>🤔 Why the SAME CPU Performs Differently on Different Motherboards</h2>
                <p>Even with the same CPU, performance can change due to:</p>

                <h3>1️⃣ 📊 RAM Speed Support</h3>
                <ul class="big-list">
                    <li>CPU may support DDR4-3200 but Cheap board may limit to DDR4-2666</li>
                </ul>
                <p><strong>Performance loss:</strong> Slower apps, Lower FPS, Slower AI/data workloads.</p>
                <div class="callout tip">📌 RAM speed is controlled by the motherboard chipset + BIOS</div>

                <h3>2️⃣ ⚡ Power Delivery (VRMs)</h3>
                <p><strong>Voltage Regulator Modules</strong> supply clean, stable power to the CPU.</p>
                <ul class="big-list">
                    <li>Weak VRMs → CPU throttles</li>
                    <li>Strong VRMs → CPU boosts higher & longer</li>
                </ul>
                <div class="example-box">
                    <p><strong>📌 Result:</strong> Same CPU on Cheap board → lower sustained speed.</p>
                </div>

                <h3>3️⃣ 🔌 PCIe Lanes</h3>
                <p>PCIe lanes decide GPU bandwidth, NVMe SSD speed, Expansion cards.</p>
                <table style="width: 100%; border-collapse: collapse; margin-top: 1rem; color: white;">
                    <tr><th style="padding: 0.5rem; text-align: left;">Board Type</th><th style="padding: 0.5rem; text-align: left;">PCIe Result</th></tr>
                    <tr><td style="padding: 0.5rem;">Entry</td><td style="padding: 0.5rem;">Limited lanes</td></tr>
                    <tr><td style="padding: 0.5rem;">Mid-range</td><td style="padding: 0.5rem;">Balanced</td></tr>
                    <tr><td style="padding: 0.5rem;">High-end</td><td style="padding: 0.5rem;">Maximum</td></tr>
                </table>
                 <div class="example-box">
                    <p><strong>📌 Example:</strong> PCIe 3.0 SSD on cheap board vs PCIe 4.0 SSD on good board → 2× speed.</p>
                </div>

                <h3>4️⃣ ❄️ Cooling Support</h3>
                <div class="comparison-grid">
                    <div class="comparison-card">
                         <h4>Poor board:</h4>
                        <ul>
                            <li>Fewer fan headers</li>
                            <li>Less thermal control</li>
                            <li>CPU throttles earlier</li>
                        </ul>
                    </div>
                    <div class="comparison-card">
                        <h4>Good board:</h4>
                        <ul>
                            <li>Multiple fans</li>
                            <li>Stable temps</li>
                            <li>Sustained performance</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Real-World Example -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🧪 Real-World Example</h2>
                <p><strong>Same CPU: Ryzen 5 5600X</strong></p>
                <table style="width: 100%; border-collapse: collapse; margin-top: 1rem; color: white;">
                    <tr><th style="padding: 0.5rem; text-align: left;">Motherboard</th><th style="padding: 0.5rem; text-align: left;">Result</th></tr>
                    <tr><td style="padding: 0.5rem;">A-Series</td><td style="padding: 0.5rem;">Lower RAM speed, throttling</td></tr>
                    <tr><td style="padding: 0.5rem;">B-Series</td><td style="padding: 0.5rem;">Full performance</td></tr>
                    <tr><td style="padding: 0.5rem;">X-Series</td><td style="padding: 0.5rem;">Best boost, cooler, faster</td></tr>
                </table>
            </div>

            <div class="content-card" style="margin-top: 2rem;">
                <h2>🧠 Simple One-Line Truth</h2>
                <p class="highlight center" style="font-size: 1.5rem;">CPU gives potential. Motherboard decides how much of that potential you actually get.</p>
            </div>
        </div>
    </section>
'''

def main():
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find Slide 5
    start_marker = '<section class="slide" data-slide="5">'
    start_pos = content.find(start_marker)

    if start_pos == -1:
        # Fallback regex
        match = re.search(r'<section class="slide"\s+data-slide="5">', content)
        if match:
            start_pos = match.start()

    if start_pos == -1:
        print("Error: Could not find Slide 5 start.")
        return

    # Find the end of Slide 5. 
    # Current structure is Slide 5 -> End of Slide Container div -> Navigation Controls comment
    # We removed slides 6-44, so Slide 5 should be followed by:
    # 1. Closing </section>
    # 2. Closing </div> (slide container) OR another section if we messed up.
    # Actually, we want to replace the WHOLE content of Slide 5 up to its closing tag.
    # The snippet ends with </section>.
    
    # Let's find the closing </section> of Slide 5.
    # It should be the first </section> after start_pos.
    end_tag = '</section>'
    end_pos = content.find(end_tag, start_pos)
    
    if end_pos == -1:
         print("Error: Could not find Slide 5 end.")
         return
         
    end_pos += len(end_tag) # Include the tag

    print(f"Replacing Slide 5 from index {start_pos} to {end_pos}")
    
    new_content = content[:start_pos] + new_slide5_content + content[end_pos:]
    
    # Also clean up the stray comment if it exists
    stray_comment = '<!-- SLIDE 5: What Does a CPU Actually Do? -->'
    new_content = new_content.replace(stray_comment, '')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Successfully updated Slide 5 with comprehensive Motherboard content.")

if __name__ == "__main__":
    main()
