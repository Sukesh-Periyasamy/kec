# KEC Workshop Website - Complete Site Documentation

## Overview
This document provides comprehensive details about all pages in the KEC Workshop website, including their structure, content, purpose, and technical implementation.

---

## Main Pages

### 1. **index.html** - Homepage
**Purpose:** Landing page directing users to different sections

**Structure:**
- Simple navigation hub
- Links to main sections: Days, About, Resources, Schedule

**Content:**
- Welcome heading
- Navigation grid with icon-based buttons
- Minimal design for quick access

**Technical Details:**
- File Size: ~1.2 KB
- Links to: day1.html, day2.html, day3.html, day4.html, about.html, resources.html, schedule.html
- Uses Font Awesome icons
- Responsive grid layout

---

### 2. **about.html** - About Section
**Purpose:** Information about the workshop and instructors

**Structure:**
- Header section
- About workshop content
- Instructor information
- Embedded YouTube video

**Content:**
- Workshop objectives
- Target audience
- Instructor bio
- YouTube video embed (iframe)

**Technical Details:**
- File Size: ~4.5 KB
- Includes video embedding
- External links to social profiles

---

### 3. **resources.html** - Resources Page
**Purpose:** Additional learning materials and references

**Structure:**
- Resource categories
- Links to external materials
- Download sections

**Content:**
- External resource links
- Reference materials
- Additional learning paths

**Technical Details:**
- File Size: ~1.3 KB
- External links

---

### 4. **schedule.html** - Workshop Schedule
**Purpose:** Complete workshop timeline and schedule

**Structure:**
- Day-by-day breakdown
- Time slots for each session
- Topic coverage per day

**Content:**
- 4-day workshop schedule
- Session timings
- Topics covered each day
- Break times

**Technical Details:**
- File Size: ~18.2 KB
- Table/grid layout for schedule
- Time-based organization

---

## Day Content Pages

### 5. **day1.html** - Linux x Terminal x OS x System Intro
**Purpose:** Introduction to Linux, terminal basics, operating systems, and system fundamentals

**Structure:**
- Slide-based presentation (interactive navigation)
- Total slides: ~60+
- Side arrow navigation
- Progress bar and slide counter

**Main Sections:**
1. **Introduction**
   - Welcome slide
   - Workshop overview
   - Learning objectives

2. **Operating Systems Basics**
   - What is an OS?
   - Types of OS (Windows, macOS, Linux)
   - OS components
   - Kernel concepts

3. **Linux Introduction**
   - What is Linux?
   - Linux distributions
   - Why Linux?
   - Open source concept

4. **Terminal Basics**
   - What is a terminal?
   - Shell vs Terminal
   - Why use terminal?

5. **Essential Commands**
   - Navigation: `cd`, `ls`, `pwd`
   - File operations: `mkdir`, `touch`, `rm`, `cp`, `mv`
   - File viewing: `cat`, `less`, `head`, `tail`
   - Text editing: `nano`, `vim`
   - System info: `uname`, `whoami`, `df`, `du`

6. **File System Structure**
   - / (root)
   - /home
   - /bin, /usr/bin
   - /etc
   - /var, /tmp

7. **Permissions**
   - chmod
   - chown
   - User groups
   - Permission notation (rwx)

8. **Process Management**
   - ps
   - top, htop
   - kill
   - Background/foreground processes

9. **Package Management**
   - apt (Debian/Ubuntu)
   - yum/dnf (RHEL/Fedora)
   - Installing/removing software

**Technical Details:**
- File Size: ~83.9 KB
- Uses: slides.css, day1.js
- Interactive JavaScript navigation
- Keyboard shortcuts (arrows, space, home, end)
- Touch/swipe support
- URL hash navigation

---

### 6. **day2.html** - Frontend Fundamentals (HTML, CSS, JavaScript)
**Purpose:** Web development basics covering HTML, CSS, and JavaScript

**Structure:**
- Slide-based presentation
- Total slides: ~30-40
- Interactive code examples

**Main Sections:**
1. **HTML Fundamentals**
   - HTML structure
   - Essential tags (html, head, body)
   - Headings (h1-h6)
   - Paragraphs and text
   - Lists (ul, ol)
   - Links (a tag)
   - Images (img tag)
   - Forms (form, input, button)
   - Tables
   - Semantic HTML5 (header, nav, main, footer, article, section)

2. **CSS Fundamentals**
   - What is CSS?
   - Selectors (element, class, ID)
   - Colors and backgrounds
   - Typography
   - Box model (margin, border, padding, content)
   - Display properties
   - Positioning
   - Flexbox basics
   - Grid basics
   - Responsive design
   - Media queries

3. **JavaScript Basics**
   - Variables (let, const, var)
   - Data types
   - Operators
   - Conditionals (if/else)
   - Loops (for, while)
   - Functions
   - DOM manipulation
   - Events
   - Console.log

4. **Practical Examples**
   - Building a simple webpage
   - Styling with CSS
   - Adding interactivity with JS

**Technical Details:**
- File Size: ~41.5 KB
- Uses: slides.css, day2.js
- Code syntax highlighting
- Interactive examples

---

### 7. **day3.html** - Git, Portfolio Website & Live Deployment
**Purpose:** Version control, portfolio development, and deployment

**Structure:**
- Navigation hub (Slide 1) with 5 buttons
- Slides 2-26: Main presentation content
- Total: 26 slides

**Slide 1 - Navigation Hub:**
Three buttons in first row:
1. **Interactive Slides** (Purple gradient) → Goes to Slide 2
2. **Git Installation** (Pink gradient) → Opens git-installation.html
3. **GitHub Account** (Dark blue gradient) → Opens github-account.html

Two buttons in second row:
4. **Domain Basics** (Cyan gradient) → Opens domain-basics.html
5. **Portfolio Guide** (Pastel gradient) → Opens portfolio-guide.html

**Main Presentation Sections (Slides 2-26):**

1. **Git Basics (Slides 2-8)**
   - What is Git?
   - What is version control?
   - Why use Git?
   - Git vs GitHub
   - Basic workflow
   - Essential commands:
     - `git init`
     - `git add`
     - `git commit`
     - `git status`
     - `git log`
   - Branching concepts

2. **GitHub (Slides 9-15)**
   - What is GitHub?
   - Creating repositories
   - Push/pull
   - Remote repositories
   - Cloning
   - GitHub workflow
   - Collaboration features

3. **HTML/CSS Portfolio (Slides 16-20)**
   - Portfolio importance
   - Structure planning
   - HTML skeleton
   - CSS styling
   - Responsive design
   - Best practices

4. **GitHub Pages Deployment (Slides 21-24)**
   - What is GitHub Pages?
   - Repository setup
   - Enabling Pages
   - Custom domain (optional)
   - Live deployment steps
   - Troubleshooting

5. **Final Project (Slides 25-26)**
   - Complete workflow
   - Deploying portfolio
   - Next steps

**Technical Details:**
- File Size: ~35.9 KB
- Uses: slides.css, day3.js
- Agenda slide map in JavaScript:
  - Slide 4: Git Basics
  - Slide 5: GitHub
  - Slide 17: HTML/CSS
  - Slide 22: Deployment
- Updated slide counter JavaScript for 26 total slides

---

### 8. **day4.html** - Hardware + IoT (Single-Page Format)
**Purpose:** IoT development with ESP32, sensors, and cloud integration

**Structure:**
- **Single-page scrollable layout** (NOT slides)
- White/light theme background
- 16 major sections with subsections
- Smooth scrolling navigation

**Content Sections:**

**Hero Section:**
- Title: "DAY 4 – Hardware + IoT"
- Subtitle: "ESP32, Arduino, Sensors & Live Web Data"
- Agenda cards (4): Microcontrollers, Sensors, Communication, Web Integration
- Goal statement

**Section 1: Embedded Systems**
- Definition: Small computer for specific tasks
- Examples:
  - Washing machine controller
  - Smartwatch
  - ECG monitor
  - Smart irrigation system
- Core components:
  - Microcontroller/Microprocessor
  - Sensors
  - Power supply
  - Communication interface

**Section 2: Microcontroller**
- Definition: Small computer on single chip
- Includes: CPU, RAM, Flash memory, GPIO pins, Communication modules
- Examples: Arduino Uno, ESP32

**Section 3: ESP32**
- Definition and features:
  - Built-in WiFi
  - Built-in Bluetooth
  - Dual-core processor
  - Multiple GPIO pins
- Why ESP32:
  - No external WiFi module needed
  - Cheap and powerful
  - Ideal for IoT
  - Works with Arduino IDE
- Important pins:
  - 3.3V (Power output)
  - GND (Ground)
  - GPIO (General purpose I/O)
  - TX/RX (Serial communication)
  - VIN (Voltage input)

**Section 4: Arduino**
- Definition: Easy-to-use microcontroller platform
- Arduino Uno features:
  - ATmega328P microcontroller
  - USB programming
  - 14 Digital Pins
  - 6 Analog Pins
  - 5V logic
- When to use:
  - Basic projects
  - Learning electronics
  - When WiFi not required

**Section 5: Raspberry Pi**
- Definition: Small computer (microcomputer, not microcontroller)
- Key difference: Arduino/ESP32 = Microcontroller; Raspberry Pi = Microcomputer
- Capabilities:
  - Run Linux
  - Connect keyboard/monitor
  - Run Python
  - Host web servers
- Use cases:
  - AI projects
  - Server hosting
  - Image processing

**Comparison Table: Microcontroller vs Microcomputer**
| Feature | Arduino/ESP32 | Raspberry Pi |
|---------|---------------|--------------|
| OS | No | Yes (Linux) |
| Boot time | Instant | Takes time |
| Real-time | Yes | Not ideal |
| WiFi | Only ESP32 | Yes |
| Power usage | Very low | Higher |

**Question for students:** Why not use Raspberry Pi for simple LED blinking?

**Section 6: Sensors**
- Definition: Converts physical quantity to electrical signal
- Examples: Temperature, Light, Motion, Gas

**Types of Sensors:**
- Temperature: DHT11, LM35
- Light: LDR
- Motion: PIR
- Gas: MQ series

**DHT11 + ESP32 Wiring:**
- VCC → 3.3V
- GND → GND
- DATA → GPIO 4

**Steps:**
- Include DHT library
- Read temperature
- Print value on Serial Monitor

**Section 7: Communication Protocols**
- Definition: Rules for device communication

**I2C (Inter-Integrated Circuit):**
- 2 wires (SDA, SCL)
- Master-Slave architecture
- Address based
- Used in: OLED display, RTC modules

**SPI (Serial Peripheral Interface):**
- 4 wires (MISO, MOSI, SCK, CS)
- Faster than I2C
- Short distance
- Used in: SD card module, TFT display

**UART (Universal Asynchronous Receiver/Transmitter):**
- TX and RX pins
- Serial communication
- Used for programming
- Example: USB to Serial

**Section 8: Web Integration**
- Concept flow: Sensor → ESP32 → WiFi → Web Server → Website

**Steps:**
1. Connect ESP32 to WiFi
2. Create HTTP request
3. Send temperature data
4. Server stores/displays data

**Method 1: Local Web Server**
- ESP32 hosts webpage
- Access via: 192.168.x.x
- Live temperature updates

**Method 2: GitHub Pages**
1. Create GitHub repository
2. Add HTML file
3. Enable GitHub Pages
4. Fetch data from server
5. Show temperature on webpage

**Complete Live Demo Flow (6 steps):**
1. Connect DHT11 to ESP32
2. Read temperature
3. Connect ESP32 to WiFi
4. Send temperature to web server
5. Open website
6. Show live updating data

**Students observe:**
- Real-time IoT system
- Sensor to Cloud flow

**Section 9: Practical Activities (1.5-2 Hours)**
- Activity 1: Blink LED using ESP32
- Activity 2: Read temperature sensor
- Activity 3: Display data on webpage
- Activity 4: Modify webpage UI

**Building complete IoT system from hardware to cloud!**

**Section 10: ThingSpeak Cloud Integration**
**What we'll cover:**
- How to program ESP32
- How to connect ESP32 to ThingSpeak
- How to show live data using GitHub Pages
- How to make full system live

**Complete Architecture:**
DHT11 → ESP32 → WiFi → ThingSpeak Cloud → GitHub Website → Live Dashboard

This is a real cloud IoT system - data travels from physical sensor to cloud and displays globally.

**Section 11: ESP32 Setup**

**Step 1: Install Arduino IDE**
1. Download from: arduino.cc
2. Install on computer

**Add ESP32 Board Support:**
1. File → Preferences
2. Add Board URL:
```
https://dl.espressif.com/dl/package_esp32_index.json
```
3. Tools → Board → Board Manager
4. Install ESP32

**Select Board:**
- Tools → Board → ESP32 Dev Module

**Step 2: Install Libraries**

Required libraries:
- DHT sensor library (Adafruit)
- Adafruit Unified Sensor

**How to install:**
1. Sketch → Include Library → Manage Libraries
2. Search for each library
3. Click Install

**Section 12: ThingSpeak Account**

**Steps:**
1. Login to ThingSpeak
2. Click New Channel
3. Add Fields:
   - Field 1 → Temperature
   - Field 2 → Humidity
4. Save Channel

**Get API Keys:**
Go to API Keys tab and copy:
- Write API Key
- Read API Key
- Channel ID

**⚠️ Keep these safe!** You'll need them for coding.

**Section 13: Complete ESP32 Code**

**Replace these values:**
- YOUR_WIFI
- YOUR_PASSWORD
- YOUR_WRITE_API_KEY

**Full code provided:**
```cpp
#include <WiFi.h>
#include <HTTPClient.h>
#include "DHT.h"

#define DHTPIN 4
#define DHTTYPE DHT11

const char* ssid = "YOUR_WIFI";
const char* password = "YOUR_PASSWORD";

String apiKey = "YOUR_WRITE_API_KEY";

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
  
  WiFi.begin(ssid, password);
  Serial.print("Connecting");
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("\nConnected to WiFi");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    
    float temp = dht.readTemperature();
    float hum = dht.readHumidity();
    
    if (!isnan(temp) && !isnan(hum)) {
      
      HTTPClient http;
      
      String url = "http://api.thingspeak.com/update?api_key=" 
                   + apiKey + "&field1=" + String(temp) 
                   + "&field2=" + String(hum);
      
      http.begin(url);
      int httpCode = http.GET();
      http.end();
      
      Serial.println("Data sent to ThingSpeak");
    }
  }
  
  delay(15000);
}
```

**Upload to ESP32:**
1. Connect ESP32 to USB
2. Select correct COM port
3. Click Upload button
4. Wait for upload to complete
5. Open Serial Monitor

**Result:** ESP32 → ThingSpeak → Live Graph
Graph updates every 15 seconds!

**Section 14: GitHub Live Dashboard**

**Get Read API URL:**
Your public API format:
```
https://api.thingspeak.com/channels/YOUR_CHANNEL_ID/feeds/last.json?api_key=YOUR_READ_API_KEY
```
Test in browser - you should see JSON.

**Create GitHub Website:**
1. Go to GitHub
2. Create new repository
3. Name: `esp32-dashboard`
4. Add file: `index.html`
5. Paste code (below)
6. Settings → Pages → Enable
7. Select branch → main
8. Save

GitHub gives you live link!

**GitHub Dashboard Code:**

Replace: YOUR_CHANNEL_ID, YOUR_READ_API_KEY

**Complete HTML/CSS/JavaScript code provided** for:
- Dark theme dashboard
- Temperature card
- Humidity card
- Auto-refresh every 15 seconds
- Fetch API integration

**Section 15: Final Live System**

**Complete System Flow:**
```
ESP32 (Your lab)
↓
ThingSpeak Cloud
↓
GitHub Website
↓
Accessible from Anywhere
```

Students can open from mobile also!

**What Students Learn:**
- Embedded Coding
- HTTP Request
- Cloud API
- JSON Handling
- Website Hosting
- Full IoT Architecture

**Section 16: Troubleshooting**

**Common Problems & Solutions:**

**❌ Data Not Updating**
→ Wait 15 seconds (ThingSpeak limit)

**❌ CORS Error**
→ Make channel public

**❌ WiFi Not Connecting**
→ Use 2.4 GHz network

**❌ API Not Working**
→ Check Write vs Read API key

**Final Call to Action:**
"You've Completed Day 4! Students now understand the complete IoT stack from hardware to cloud!"

**Technical Details:**
- File Size: ~44.5 KB
- Format: Single-page scrollable (NOT slides)
- Theme: White/light background
- No JavaScript navigation required
- All content flows vertically
- Smooth scrolling enabled
- Responsive grid layouts
- Clean typography
- 16 major sections with nested subsections

---

## Guide Pages

### 9. **git-installation.html** - Git Installation Guide
**Purpose:** Step-by-step Git installation for Windows 11

**Structure:**
- Installation steps
- Screenshots/visuals
- Troubleshooting section

**Content:**
1. Download Git for Windows
2. Installation wizard steps
3. Configuration options
4. Verification commands
5. Common issues

**Technical Details:**
- File Size: ~12.3 KB
- Platform: Windows 11 specific
- Includes download links

---

### 10. **github-account.html** - GitHub Account Creation Guide
**Purpose:** Complete guide for creating and setting up GitHub account

**Structure:**
- Step-by-step process
- Screenshots for each step
- Best practices
- SSH key setup

**Content:**
1. Sign up process
2. Email verification
3. Profile setup
4. SSH key generation
5. SSH key addition to GitHub
6. Verification
7. First repository creation

**Technical Details:**
- File Size: ~18.5 KB
- Includes SSH setup
- Security best practices

---

### 11. **domain-basics.html** - Domain & DNS Basics Guide
**Purpose:** Complete guide to domains, DNS, and GitHub Pages custom domain setup

**Structure:**
- 7 main parts
- Step-by-step instructions
- Diagrams and examples
- Troubleshooting

**Content:**

**Part 1: Basic Concepts**
- IP addresses (e.g., 142.250.183.14)
- Domain names (e.g., google.com)
- DNS (Domain Name System)
- Real-life analogy: Contact Name = Domain, Phone Number = IP, Phonebook = DNS

**Part 2: Top Level Domains (TLDs)**
- .com (Commercial, most popular)
- .in (India-specific)
- .org (Organizations)
- .edu (Educational, restricted)
- Recommendation: .com first choice, .in second

**Part 3: Domain Pricing**
- .com: ₹800 - ₹1200/year
- .in: ₹500 - ₹900/year
- .org: ₹900 - ₹1300/year
- Note: First year cheaper, renewal may cost more

**Part 4: Where to Buy**
- GoDaddy (beginner friendly)
- Namecheap (cheaper)
- Google Domains (simple)
- Demo: Search "yournameportfolio.com"

**Part 5: After Buying Domain**
- DNS Management Panel
- Nameservers
- A Record
- CNAME Record
- MX Record

**Part 6: Connect Custom Domain to GitHub Pages**

**Step 1:** Deploy to GitHub Pages
- Push portfolio to GitHub
- Repository → Settings → Pages
- Select Branch: main
- GitHub gives link: `username.github.io/repository-name`

**Step 2:** Add Custom Domain in GitHub
- Repository → Settings → Pages
- Under Custom Domain enter: `yourdomain.com`
- Save (creates CNAME file)

**Step 3:** DNS Settings in Domain Provider
- Open DNS Management

**Step 4:** Add A Records
Add 4 A Records pointing to GitHub IPs:
- 185.199.108.153
- 185.199.109.153
- 185.199.110.153
- 185.199.111.153

Type: A, Host: @

**Step 5:** Add CNAME Record
For www version:
- Type: CNAME
- Host: www
- Points to: `username.github.io`

**Step 6:** Wait for DNS Propagation
- Time: 10 minutes – 24 hours
- After propagation: `yourdomain.com` works!

**Step 7:** Enable HTTPS
- In GitHub Pages settings
- Enable "Enforce HTTPS"
- Website is now secure

**Part 7: Conceptual Understanding**
- Domain = Name
- IP = Real Address
- DNS = Translator
- A Record = Direct IP linking
- CNAME = Alias linking

**Diagram:**
```
User types: sukeshdev.com
↓
DNS checks records
↓
Points to GitHub IP
↓
GitHub server loads website
```

**Common Problems:**
- Website not opening → DNS delay, wrong IP, CNAME typo
- HTTPS not working → Wait, re-check domain
- Only www works → Check A record

**Technical Details:**
- File Size: ~20.3 KB
- Includes pricing in INR
- GitHub Pages integration
- DNS configuration details

---

### 12. **portfolio-guide.html** - Portfolio Website Development Guide
**Purpose:** Complete 5-phase guide from manual coding to AI-powered portfolio creation

**Structure:**
- 5 progressive phases
- Practical examples
- Earning potential guide
- AI integration (placeholder)

**Content:**

**Phase 1: Manual Portfolio from Scratch**

**Basic Structure:**
```
portfolio/
├── index.html
├── style.css
├── script.js
├── images/
└── projects/
```

**index.html essentials:**
- Hero section (name, title, photo)
- About section
- Skills section
- Projects section (3-5 projects with images)
- Contact section (email, phone, LinkedIn, GitHub)

**style.css basics:**
- Colors & fonts
- Layout (flexbox/grid)
- Responsive design
- Hover effects

**script.js features:**
- Smooth scrolling
- Project filtering
- Contact form validation

**Phase 2: Using Templates**

**Where to find:**
- ThemeWagon
- TemplateMonster
- HTML5 UP

**Customization steps:**
1. Download template
2. Replace text (name, bio, skills)
3. Update images (your photos)
4. Add your projects
5. Change colors (CSS variables)
6. Update fonts (Google Fonts)
7. Modify layout if needed

**Teaching tips:**
- Show before/after comparison
- Demonstrate CSS variable changes
- Explain responsive breakpoints

**Phase 3: GitHub Integration**

**Deployment:**
1. Create repository: `username.github.io`
2. Push portfolio files
3. Settings → Pages → Enable
4. Live at: `username.github.io`

**Custom domain:**
- Buy domain (Part 4)
- Configure DNS (see domain-basics.html)

**Phase 4: Freelancing with Portfolios**

**Client Approach:**
```
Subject: Portfolio Website Development

Hi [Name],

I build professional portfolio websites.

Services:
✔ Custom design
✔ Responsive (mobile-friendly)
✔ GitHub hosting (free)
✔ 2-3 days delivery

Price: ₹2000-5000
```

**Pricing Guide:**
- Basic (template): ₹2000-3000
- Custom design: ₹4000-6000
- With domain setup: ₹5000-8000

**Where to find clients:**
- LinkedIn
- Local businesses
- College students
- Freelance platforms

**Phase 5: AI-Powered Portfolio Creation**

**Using Antigravity:**
- [Placeholder button: "Click here to create with Antigravity"]
- Explain: AI can generate portfolio based on:
  - Your skills
  - Your projects
  - Design preferences
  - Target industry

**What AI can do:**
- Generate HTML/CSS/JS
- Suggest color schemes
- Write project descriptions
- Optimize for SEO
- Make responsive automatically

**Teaching approach:**
- Manual first (understanding)
- Templates second (efficiency)
- AI third (speed + customization)

**Key Takeaways:**
- Phase 1: Learn fundamentals
- Phase 2: Save time with templates
- Phase 3: Deploy for free
- Phase 4: Earn money (₹2000-8000/project)
- Phase 5: Use AI for rapid development

**Student Activities:**
1. Create manual portfolio (2-3 hours)
2. Customize a template (1 hour)
3. Deploy to GitHub (30 mins)
4. Practice client pitch
5. Experiment with AI tools

**Technical Details:**
- File Size: ~20.5 KB
- Includes earning potential
- Freelancing guidance
- AI integration section

---

### 13. **linux-installation.html** - Kali Linux Installation Guide
**Purpose:** Complete guide for installing Kali Linux

**Structure:**
- Pre-installation requirements
- Step-by-step installation
- Post-installation setup
- Troubleshooting

**Content:**
1. Download Kali Linux ISO
2. Create bootable USB (Rufus/Etcher)
3. Boot from USB
4. Installation wizard
5. Partitioning
6. User setup
7. Installation completion
8. First boot
9. Updates and setup

**Technical Details:**
- File Size: ~14.8 KB
- Includes screenshots
- TPM/Secure Boot considerations

---

### 14. **windows-installation.html** - Windows 11 Installation Guide
**Purpose:** Complete Windows 11 installation guide with TPM bypass

**Structure:**
- System requirements
- TPM bypass methods
- Installation process
- Troubleshooting

**Content:**
1. Download Windows 11 ISO
2. Create bootable USB
3. TPM bypass (if needed)
4. Installation steps
5. Out-of-box experience (OOBE)
6. Initial setup
7. Updates
8. FAQ section

**Technical Details:**
- File Size: ~19.2 KB
- Includes TPM bypass
- Hardware requirements

---

## Support Files

### CSS Files (css/ directory)
1. **slides.css** - Main presentation styles
   - Slide layouts
   - Navigation styles
   - Progress bars
   - Responsive design
   - Animations
   - Day 3 utility classes

2. **style.css** - Global styles
3. **Other CSS files** - Component-specific styles

### JavaScript Files (js/ directory)
1. **day1.js** - Day 1 navigation logic
2. **day2.js** - Day 2 navigation logic
3. **day3.js** - Day 3 navigation logic
   - Updates for 26 slides
   - Agenda slide map
4. **day4.js** - Day 4 navigation logic (not used in single-page version)

### Assets Directory
- Images
- Icons
- Media files

---

## Documentation Files

### CONTENT_REFERENCE.md
**Purpose:** Reference for all workshop content
**Size:** 29.6 KB
**Contains:** Content outline and references

### QUICK_START.md
**Purpose:** Quick start guide for the workshop
**Size:** 7.6 KB
**Contains:** Getting started instructions

### README.md
**Purpose:** Main repository documentation
**Size:** 12.2 KB
**Contains:** Project overview, setup instructions

### VERIFICATION_REPORT.md
**Purpose:** Quality verification report
**Size:** 13.1 KB
**Contains:** Testing and verification results

---

## Summary Statistics

**Total HTML Pages:** 14
- Main pages: 4
- Day content: 4
- Guide pages: 6

**Total File Size:** ~296 KB (HTML files only)

**Technology Stack:**
- HTML5 with semantic elements
- CSS3 with modern features (Grid, Flexbox, Variables)
- Vanilla JavaScript (no frameworks)
- Font Awesome icons
- Google Fonts (Inter, Space Grotesk)

**Key Features:**
- Responsive design (mobile-first)
- Progressive enhancement
- Accessibility considerations
- SEO-friendly structure
- Fast loading times
- No external dependencies (except fonts and icons)

**Content Coverage:**
- Operating Systems & Linux
- Terminal & Command Line
- Web Development (HTML/CSS/JavaScript)
- Version Control (Git/GitHub)
- IoT & Hardware (ESP32, Arduino)
- Cloud Integration (ThingSpeak)
- Domain Management
- Portfolio Development
- Deployment & Hosting

---

## Navigation Flow

```
index.html (Homepage)
├── day1.html (Linux & Terminal)
├── day2.html (Frontend)
├── day3.html (Git & Portfolio)
│   ├── Slide 1 (Navigation Hub)
│   │   ├── Interactive Slides (Slide 2)
│   │   ├── git-installation.html
│   │   ├── github-account.html
│   │   ├── domain-basics.html
│   │   └── portfolio-guide.html
│   └── Slides 2-26 (Main Content)
├── day4.html (Hardware & IoT)
├── about.html
├── resources.html
├── schedule.html
├── linux-installation.html
└── windows-installation.html
```

---

*This documentation provides a complete reference for all pages in the KEC Workshop website. Each page is designed to be self-contained while maintaining consistent design and navigation patterns across the site.*
