
import re

file_path = r'c:\Users\sukes\Downloads\kec docs\kec site\day1.html'

# Content for Slide 7 (GPU)
slide7_content = r'''
    <!-- SLIDE 7: What is a GPU? -->
    <section class="slide" data-slide="7">
        <div class="slide-content">
            <h1>What is a GPU?</h1>
            <p class="subtitle">Deep, Practical & Real-World Explanation</p>

            <!-- Definition -->
            <div class="content-card">
                <h2>🎨 GPU = Graphics Processing Unit</h2>
                <p>A specialized processor designed to handle:</p>
                <ul class="big-list">
                    <li>Graphics (images, video, 3D)</li>
                    <li>Massive parallel computation</li>
                    <li>Thousands of small cores working together</li>
                </ul>
            </div>

            <!-- CPU vs GPU -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>CPU vs GPU (Core Idea)</h2>
                <div class="comparison-grid">
                    <div class="comparison-card">
                        <h3>CPU (Manager)</h3>
                        <p>Few powerful cores</p>
                        <p>Handles decisions & logic</p>
                        <p>Serial processing</p>
                    </div>
                    <div class="comparison-card">
                        <h3>GPU (Factory)</h3>
                        <p>Thousands of small cores</p>
                        <p>Handles bulk work</p>
                        <p>Parallel processing</p>
                    </div>
                </div>
                <p class="highlight center">📌 <strong>Analogy:</strong> CPU = Project Manager. GPU = Assembly Line.</p>
            </div>

            <!-- When Do You Need a GPU? -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🎯 When Do You Need a GPU?</h2>
                <div class="comparison-grid">
                    <div class="comparison-card" style="border-top: 3px solid #10B981;">
                        <h3>✅ GPU is NEEDED for</h3>
                        <ul class="big-list">
                            <li><strong>Gaming:</strong> Textures, lighting, shadows</li>
                            <li><strong>AI / ML:</strong> Matrix multiplication, Neural networks</li>
                            <li><strong>Video Editing:</strong> Timeline playback, Grading</li>
                            <li><strong>3D Rendering:</strong> CAD, Blender</li>
                        </ul>
                    </div>
                    <div class="comparison-card" style="border-top: 3px solid #EF4444;">
                        <h3>❌ GPU is NOT Needed for</h3>
                        <ul class="big-list">
                            <li>Office work (Word, Excel)</li>
                            <li>Browsing</li>
                            <li>Basic Programming</li>
                            <li>Online classes</li>
                        </ul>
                        <p class="highlight" style="font-size: 0.9rem;">👉 Integrated GPU (iGPU) is enough here.</p>
                    </div>
                </div>
            </div>

            <!-- GPU Types -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🧩 GPU Types (Very Important)</h2>
                <div class="comparison-grid">
                    <div class="comparison-card">
                        <h3>1️⃣ Gaming GPUs</h3>
                        <p><em>(NVIDIA GeForce, AMD Radeon)</em></p>
                        <ul class="big-list">
                            <li>High FPS</li>
                            <li>Real-time rendering</li>
                        </ul>
                    </div>
                    <div class="comparison-card">
                        <h3>2️⃣ Workstation GPUs</h3>
                        <p><em>(NVIDIA RTX A-series, Radeon Pro)</em></p>
                        <ul class="big-list">
                            <li>Accuracy & Stability</li>
                            <li>Certified drivers</li>
                            <li>Medical / Scientific work</li>
                        </ul>
                    </div>
                    <div class="comparison-card">
                        <h3>3️⃣ Integrated GPUs</h3>
                        <p><em>(Iris Xe, Radeon APU)</em></p>
                        <ul class="big-list">
                            <li>Built into CPU</li>
                            <li>Uses system RAM</li>
                            <li>Office / Light use</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Specs That Matter -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🔍 GPU Specs That REALLY Matter</h2>
                
                <h3>1️⃣ 💾 VRAM (Video Memory)</h3>
                <p>Stores textures, models, AI tensors. More VRAM = handle larger data.</p>
                <table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem; color: white;">
                     <tr><th style="padding: 0.5rem; text-align: left;">Task</th><th style="padding: 0.5rem; text-align: left;">VRAM Needed</th></tr>
                     <tr><td style="padding: 0.5rem;">Office</td><td style="padding: 0.5rem;">0–1 GB</td></tr>
                     <tr><td style="padding: 0.5rem;">Gaming (1080p)</td><td style="padding: 0.5rem;">6–8 GB</td></tr>
                     <tr><td style="padding: 0.5rem;">3D / Video</td><td style="padding: 0.5rem;">8–16 GB</td></tr>
                     <tr><td style="padding: 0.5rem;">AI / ML</td><td style="padding: 0.5rem;">12–24+ GB</td></tr>
                </table>

                <h3 style="margin-top: 1rem;">2️⃣ ⚡ Core Count (CUDA / Stream Processors)</h3>
                <p>More cores = Better parallel performance. (Note: Count across brands isn't directly comparable).</p>

                <h3 style="margin-top: 1rem;">3️⃣ 📊 Memory Bandwidth</h3>
                <p>How fast data moves. High bandwidth = smoother high-res gaming & AI.</p>

                <h3 style="margin-top: 1rem;">4️⃣ 🔌 Power Consumption (TDP)</h3>
                <p>Mid GPU (150-250W) vs High-end (300-450W+). More power = needs better cooling.</p>
                
                <div class="callout warning">
                    <strong>❄️ Cooling & Power Reality:</strong> Weak PSU → crashes. Poor airflow → throttling.
                </div>
            </div>

            <!-- Real-World Context -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🧪 Real Example (Why GPU Choice Matters)</h2>
                <p><strong>Same CPU, Different GPUs</strong></p>
                <table style="width: 100%; border-collapse: collapse; margin-top: 1rem; color: white;">
                    <tr><th style="padding: 0.5rem; text-align: left;">GPU</th><th style="padding: 0.5rem; text-align: left;">Result</th></tr>
                    <tr><td style="padding: 0.5rem;">Integrated</td><td style="padding: 0.5rem;">Can’t run AI</td></tr>
                    <tr><td style="padding: 0.5rem;">Entry GPU</td><td style="padding: 0.5rem;">Basic ML</td></tr>
                    <tr><td style="padding: 0.5rem;">High-end GPU</td><td style="padding: 0.5rem;">Fast training</td></tr>
                </table>
                <p class="highlight center">CPU thinks. GPU works. And for AI/rendering — GPU decides speed.</p>
            </div>
        </div>
    </section>
'''

# Content for Slide 8 (Storage & Cooling)
slide8_content = r'''
    <!-- SLIDE 8: Storage & Cooling Basics -->
    <section class="slide" data-slide="8">
        <div class="slide-content">
            <h1>Storage & Cooling Basics</h1>
            <p class="subtitle">In-Depth, Practical Explanation</p>

            <!-- Storage Definition -->
            <div class="content-card">
                <h2>🧠 What Is Storage? (Long-term Memory)</h2>
                <p>Storage permanently holds OS, Apps, Files, and Datasets.</p>
                <div class="callout tip">
                    <strong>📌 Non-Volatile:</strong> Unlike RAM, storage does <strong>not</strong> clear when power is off.
                </div>
                <p class="highlight" style="margin-top: 1rem;">Fast CPU + slow storage = system still feels slow.</p>
            </div>

            <!-- Storage Types -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>🧩 Storage Types Explained</h2>
                <div class="comparison-grid">
                    <div class="comparison-card">
                        <h3>1️⃣ HDD (Hard Disk)</h3>
                        <p>Spinning platters</p>
                        <ul class="big-list">
                            <li>❌ Slow, Noisy, Fragile</li>
                            <li>✅ Huge capacity, Cheap</li>
                        </ul>
                        <p class="highlight">Best for: Backups / Archives</p>
                    </div>
                    <div class="comparison-card">
                        <h3>2️⃣ SATA SSD</h3>
                        <p>NAND Flash</p>
                        <ul class="big-list">
                            <li>✅ Fast, Silent, Durable</li>
                            <li>⚠️ Limited speed (550 MB/s)</li>
                        </ul>
                        <p class="highlight">Best for: OS / Daily Apps</p>
                    </div>
                    <div class="comparison-card" style="border: 2px solid var(--color-primary);">
                        <h3>3️⃣ NVMe SSD</h3>
                        <p>M.2 PCIe</p>
                        <ul class="big-list">
                            <li>🚀 Extremely fast (7000+ MB/s)</li>
                            <li>⚠️ Can get hot</li>
                        </ul>
                        <p class="highlight">Best for: Boot, AI, Video</p>
                    </div>
                </div>
            </div>

            <!-- Speed Comparison -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>📊 Storage Speed Comparison (Real-World Feel)</h2>
                <table style="width: 100%; border-collapse: collapse; margin-top: 1rem; color: white;">
                    <tr><th style="padding: 0.5rem; text-align: left;">Task</th><th style="padding: 0.5rem; text-align: left;">HDD</th><th style="padding: 0.5rem; text-align: left;">SATA SSD</th><th style="padding: 0.5rem; text-align: left;">NVMe SSD</th></tr>
                    <tr><td style="padding: 0.5rem;">Windows boot</td><td style="padding: 0.5rem;">60–90s</td><td style="padding: 0.5rem;">15–20s</td><td style="padding: 0.5rem;">5–10s</td></tr>
                    <tr><td style="padding: 0.5rem;">App open</td><td style="padding: 0.5rem;">Slow</td><td style="padding: 0.5rem;">Fast</td><td style="padding: 0.5rem;">Instant</td></tr>
                    <tr><td style="padding: 0.5rem;">AI dataset load</td><td style="padding: 0.5rem;">Painful</td><td style="padding: 0.5rem;">Okay</td><td style="padding: 0.5rem;">Smooth</td></tr>
                </table>
            </div>

            <!-- Important Concepts -->
            <div class="content-card" style="margin-top: 2rem;">
                <h2>⚠️ Concepts You Must Know</h2>
                <ul class="big-list">
                    <li><strong>IOPS:</strong> Small file access speed. NVMe wins huge here.</li>
                    <li><strong>Separation:</strong> Keep OS on NVMe, Data on HDD/SSD.</li>
                    <li><strong>FPS Myth:</strong> Faster storage reduces load times, but does NOT obtain higher FPS.</li>
                </ul>
            </div>

            <!-- Cooling Section -->
            <div class="content-card" style="margin-top: 3rem; border-top: 3px solid #3B82F6; padding-top: 2rem;">
                <h2>❄️ Cooling & Thermals</h2>
                <div class="callout warning">
                    <strong>Heat = Enemy of Performance.</strong> Too much heat → Thermal Throttling (Speed drops to prevent damage).
                </div>

                <h3>🧊 Cooling Types</h3>
                <div class="comparison-grid" style="margin-top: 1rem;">
                    <div class="comparison-card">
                        <h3>Air Cooling</h3>
                        <p>Heatsink + Fan</p>
                        <p>Reliable, Cheaper, Long life.</p>
                        <p class="highlight">Best for most users.</p>
                    </div>
                    <div class="comparison-card">
                        <h3>Liquid Cooling (AIO)</h3>
                        <p>Pump + Radiator</p>
                        <p>Better cooling, Cleaner look.</p>
                        <p class="highlight">Best for High-end CPUs.</p>
                    </div>
                </div>

                <div class="comparison-grid" style="margin-top: 1rem;">
                    <div class="comparison-card">
                        <h3>🌬️ Case Airflow</h3>
                        <ul class="big-list">
                            <li>Front intake, Rear exhaust</li>
                            <li>Bad airflow = throttling even with good cooler</li>
                        </ul>
                    </div>
                    <div class="comparison-card">
                        <h3>🔥 NVMe Heat</h3>
                        <ul class="big-list">
                            <li>NVMe SSDs reach 70–80°C</li>
                            <li>Always use a heatsink!</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="content-card" style="margin-top: 2rem;">
                <h2>🎯 Smart Recommendations</h2>
                <ul class="big-list">
                    <li><strong>Students:</strong> NVMe (500GB) + Air Cooling</li>
                    <li><strong>Developers:</strong> NVMe (1TB) + Good Airflow</li>
                    <li><strong>AI / Simulation:</strong> NVMe Gen4 + SSD Heatsink + Strong Cooling</li>
                </ul>
            </div>

            <div class="content-card" style="margin-top: 2rem;">
                <h2>🏁 One-Line Summary</h2>
                <div class="highlight center">
                    Storage decides how fast things load.<br>
                    Cooling decides how long performance lasts.
                </div>
            </div>
        </div>
    </section>
'''

def main():
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find end of Slide 6 (RAM)
    start_sl6 = content.find('<section class="slide" data-slide="6">')
    if start_sl6 == -1:
        match = re.search(r'<section class="slide"\s+data-slide="6">', content)
        if match:
             start_sl6 = match.start()
            
    if start_sl6 == -1:
        print("Error: Could not find Slide 6 start.")
        return

    # Find closing tag of Slide 6
    end_sl6 = content.find('</section>', start_sl6)
    if end_sl6 == -1:
        print("Error: Could not find Slide 6 end.")
        return
        
    end_sl6 += len('</section>') # Include tag

    # Insert Slide 7 and 8 after Slide 6
    print(f"Inserting Slides 7 & 8 after Slide 6 (index {end_sl6})")
    
    new_content = content[:end_sl6] + "\n\n" + slide7_content + "\n\n" + slide8_content + content[end_sl6:]
    
    # Update total slide count to 8
    new_content = re.sub(r'<span id="totalSlides">\d+</span>', '<span id="totalSlides">8</span>', new_content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Successfully added Slide 7 (GPU) and Slide 8 (Storage & Cooling), updated count to 8.")

if __name__ == "__main__":
    main()
