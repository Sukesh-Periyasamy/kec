// ========================================
// STATE MANAGEMENT
// ========================================
let currentSlide = 1;
const totalSlides = document.querySelectorAll('.slide').length;

// ========================================
// INITIALIZATION
// ========================================
document.addEventListener('DOMContentLoaded', () => {
    initializeSlides();
    updateSlideCounter();
    updateProgressBar();
    attachEventListeners();
    loadSlideFromHash();
    generateSlideNavigator();
    updateNavigatorHighlight();
});

// ========================================
// SLIDE INITIALIZATION
// ========================================
function initializeSlides() {
    const slides = document.querySelectorAll('.slide');
    slides.forEach((slide, index) => {
        if (index === 0) {
            slide.classList.add('active');
        } else {
            slide.classList.remove('active');
        }
    });
}

// ========================================
// NAVIGATION FUNCTIONS
// ========================================
function goToSlide(slideNumber) {
    // Validate slide number
    if (slideNumber < 1 || slideNumber > totalSlides) {
        return;
    }

    // Remove active class from current slide
    const currentSlideElement = document.querySelector('.slide.active');
    if (currentSlideElement) {
        currentSlideElement.classList.remove('active');
    }

    // Update current slide number
    currentSlide = slideNumber;

    // Add active class to new slide
    const newSlideElement = document.querySelector(`.slide[data-slide="${currentSlide}"]`);
    if (newSlideElement) {
        newSlideElement.classList.add('active');
    }

    // Update UI
    updateSlideCounter();
    updateProgressBar();
    updateURL();
    updateNavigatorHighlight();

    // Trigger animation reset for speed bars (if present)
    resetAnimations();

    // Update ARIA for accessibility
    updateSlideAria();
}

function nextSlide() {
    if (currentSlide < totalSlides) {
        goToSlide(currentSlide + 1);
    }
}

function previousSlide() {
    if (currentSlide > 1) {
        goToSlide(currentSlide - 1);
    }
}

function goToFirstSlide() {
    goToSlide(1);
}

function goToLastSlide() {
    goToSlide(totalSlides);
}

// ========================================
// UI UPDATE FUNCTIONS
// ========================================
function updateSlideCounter() {
    const currentSlideElement = document.getElementById('currentSlide');
    const totalSlidesElement = document.getElementById('totalSlides');

    if (currentSlideElement) {
        currentSlideElement.textContent = currentSlide;
    }

    if (totalSlidesElement) {
        totalSlidesElement.textContent = totalSlides;
    }
}

function updateProgressBar() {
    const progressFill = document.querySelector('.progress-fill');
    const progress = (currentSlide / totalSlides) * 100;

    if (progressFill) {
        progressFill.style.width = `${progress}%`;
    }
}

// ========================================
// URL HASH MANAGEMENT
// ========================================
function updateURL() {
    history.replaceState(null, null, `#slide-${currentSlide}`);
}

function loadSlideFromHash() {
    const hash = window.location.hash;
    if (hash) {
        const slideMatch = hash.match(/#slide-(\d+)/);
        if (slideMatch) {
            const slideNumber = parseInt(slideMatch[1], 10);
            if (slideNumber >= 1 && slideNumber <= totalSlides) {
                goToSlide(slideNumber);
            }
        }
    }
}

// ========================================
// ANIMATION RESET
// ========================================
function resetAnimations() {
    // Reset speed bar animations when navigating to slide 32
    if (currentSlide === 32) {
        setTimeout(() => {
            const speedBars = document.querySelectorAll('.speed-bar');
            speedBars.forEach(bar => {
                // Force reflow to restart animation
                bar.style.animation = 'none';
                void bar.offsetWidth; // Trigger reflow
                bar.style.animation = null;
            });
        }, 100);
    }
}

// ========================================
// EVENT LISTENERS
// ========================================
function attachEventListeners() {
    // Button Navigation
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');

    if (prevBtn) {
        prevBtn.addEventListener('click', previousSlide);
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', nextSlide);
    }

    // Home Button
    const homeBtn = document.getElementById('homeBtn');
    if (homeBtn) {
        homeBtn.addEventListener('click', goToFirstSlide);
    }

    // Navigator Button
    const navMenuBtn = document.getElementById('navMenuBtn');
    if (navMenuBtn) {
        navMenuBtn.addEventListener('click', toggleNavigator);
    }

    // Navigator Close Button
    const navCloseBtn = document.getElementById('navCloseBtn');
    if (navCloseBtn) {
        navCloseBtn.addEventListener('click', closeNavigator);
    }

    // Help Button
    const helpBtn = document.getElementById('helpBtn');
    if (helpBtn) {
        helpBtn.addEventListener('click', toggleHelp);
    }

    // Help Close Button
    const helpCloseBtn = document.getElementById('helpCloseBtn');
    if (helpCloseBtn) {
        helpCloseBtn.addEventListener('click', closeHelp);
    }

    // Close overlays when clicking outside
    const navOverlay = document.getElementById('navOverlay');
    if (navOverlay) {
        navOverlay.addEventListener('click', (e) => {
            if (e.target === navOverlay) {
                closeNavigator();
            }
        });
    }

    const helpOverlay = document.getElementById('helpOverlay');
    if (helpOverlay) {
        helpOverlay.addEventListener('click', (e) => {
            if (e.target === helpOverlay) {
                closeHelp();
            }
        });
    }

    // Quiz Reveal Buttons
    document.querySelectorAll('.reveal-btn').forEach(button => {
        button.addEventListener('click', () => {
            const revealBox = button.nextElementSibling;
            if (revealBox && revealBox.classList.contains('quiz-reveal')) {
                revealBox.classList.remove('hidden');
                button.disabled = true;
                button.textContent = "Answer Revealed";
            }
        });
    });

    // Keyboard Navigation
    document.addEventListener('keydown', handleKeyPress);

    // Touch Navigation (for mobile)
    let touchStartX = 0;
    let touchEndX = 0;

    document.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    document.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
    }, { passive: true });

    function handleSwipe() {
        const swipeThreshold = 50; // Minimum distance for swipe

        if (touchEndX < touchStartX - swipeThreshold) {
            // Swipe left - next slide
            nextSlide();
        }

        if (touchEndX > touchStartX + swipeThreshold) {
            // Swipe right - previous slide
            previousSlide();
        }
    }

    // Hash change listener
    window.addEventListener('hashchange', loadSlideFromHash);
}

// ========================================
// KEYBOARD CONTROLS
// ========================================
let isNavThrottled = false;

function handleKeyPress(e) {
    if (isNavThrottled) return;

    isNavThrottled = true;
    setTimeout(() => {
        isNavThrottled = false;
    }, 400); // 400ms throttle for keyboard navigation

    switch (e.key) {
        case 'ArrowRight':
        case ' ': // Spacebar
        case 'PageDown':
            e.preventDefault();
            nextSlide();
            break;

        case 'ArrowLeft':
        case 'PageUp':
            e.preventDefault();
            previousSlide();
            break;

        case 'Home':
            e.preventDefault();
            goToFirstSlide();
            break;

        case 'End':
            e.preventDefault();
            goToLastSlide();
            break;

        case 'ArrowDown':
            e.preventDefault();
            nextSlide();
            break;

        case 'ArrowUp':
            e.preventDefault();
            previousSlide();
            break;

        // Number keys for quick navigation
        case '1':
        case '2':
        case '3':
        case '4':
        case '5':
        case '6':
        case '7':
        case '8':
        case '9':
            if (!e.ctrlKey && !e.metaKey && !e.altKey) {
                const slideNum = parseInt(e.key, 10);
                if (slideNum <= totalSlides) {
                    goToSlide(slideNum);
                }
            }
            break;

        case 'Escape':
            // Close overlays first, then return to first slide
            if (isNavigatorOpen() || isHelpOpen()) {
                closeNavigator();
                closeHelp();
            } else {
                goToFirstSlide();
            }
            break;

        case 'n':
        case 'N':
            if (!e.ctrlKey && !e.metaKey && !e.altKey) {
                e.preventDefault();
                toggleNavigator();
            }
            break;

        case '?':
            if (!e.ctrlKey && !e.metaKey && !e.altKey) {
                e.preventDefault();
                toggleHelp();
            }
            break;
    }
}

// ========================================
// FULLSCREEN SUPPORT (Optional)
// ========================================
function toggleFullscreen() {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(err => {
            console.log(`Error attempting to enable fullscreen: ${err.message}`);
        });
    } else {
        document.exitFullscreen();
    }
}

// Optional: Press 'F' to toggle fullscreen
document.addEventListener('keydown', (e) => {
    if (e.key === 'f' || e.key === 'F') {
        if (!e.ctrlKey && !e.metaKey && !e.altKey) {
            e.preventDefault();
            toggleFullscreen();
        }
    }
});

// ========================================
// PRESENTATION MODE (Optional)
// ========================================
// Hide cursor after inactivity
let cursorTimeout;
let navTimeout;

function showCursor() {
    document.body.style.cursor = 'default';
    document.querySelectorAll('.nav-btn, .slide-counter').forEach(el => {
        el.style.opacity = '1';
    });
}

function hideCursor() {
    document.body.style.cursor = 'none';
    document.querySelectorAll('.nav-btn, .slide-counter').forEach(el => {
        el.style.opacity = '0.3';
    });
}

document.addEventListener('mousemove', () => {
    clearTimeout(cursorTimeout);
    showCursor();

    cursorTimeout = setTimeout(() => {
        hideCursor();
    }, 3000); // Hide after 3 seconds of inactivity
});

// ========================================
// AGENDA ITEM CLICK NAVIGATION (Slide 1)
// ========================================
document.addEventListener('DOMContentLoaded', () => {
    const agendaItems = document.querySelectorAll('.agenda-item');

    // Map agenda items to slide numbers
    // Map agenda items to slide numbers - Day 2 (36 Slides)
    const agendaSlideMap = {
        0: 4,   // Understand OS
        1: 7,   // OS Architecture
        2: 9,   // Virtualization Concepts
        3: 17,  // Install Windows 11 in VM (Step 2)
        4: 29   // Configure & Troubleshoot
    };

    agendaItems.forEach((item, index) => {
        item.addEventListener('click', () => {
            const targetSlide = agendaSlideMap[index];
            if (targetSlide) {
                goToSlide(targetSlide);
            }
        });

        // Add keyboard support for agenda items
        item.setAttribute('tabindex', '0');
        item.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                const targetSlide = agendaSlideMap[index];
                if (targetSlide) {
                    goToSlide(targetSlide);
                }
            }
        });
    });
});

// ========================================
// UTILITY FUNCTIONS
// ========================================
// Get current slide progress percentage
function getProgress() {
    return Math.round((currentSlide / totalSlides) * 100);
}

// Check if at start or end
function isFirstSlide() {
    return currentSlide === 1;
}

function isLastSlide() {
    return currentSlide === totalSlides;
}

// Export for console debugging (optional)
if (typeof window !== 'undefined') {
    window.presentation = {
        goToSlide,
        nextSlide,
        previousSlide,
        currentSlide: () => currentSlide,
        totalSlides: () => totalSlides,
        getProgress,
        isFirstSlide,
        isLastSlide,
        toggleFullscreen
    };
}

// ========================================
// SLIDE NAVIGATOR FUNCTIONS
// ========================================
function generateSlideNavigator() {
    const navContent = document.getElementById('navOverlayContent');
    if (!navContent) return;

    const slides = document.querySelectorAll('.slide');
    const navGrid = document.createElement('div');
    navGrid.className = 'nav-grid';

    slides.forEach((slide, index) => {
        const slideNumber = index + 1;
        const slideTitle = getSlideTitle(slide);
        const isQuiz = slide.classList.contains('quiz-slide');

        const navItem = document.createElement('button');
        navItem.className = 'nav-item';
        navItem.setAttribute('data-slide', slideNumber);
        navItem.innerHTML = `
            <div class="nav-item-number">${slideNumber}</div>
            <div class="nav-item-title">${isQuiz ? '🧠 ' : ''}${slideTitle}</div>
        `;

        navItem.addEventListener('click', () => {
            goToSlide(slideNumber);
            closeNavigator();
        });

        navGrid.appendChild(navItem);
    });

    navContent.appendChild(navGrid);
}

function getSlideTitle(slide) {
    const h1 = slide.querySelector('h1');
    const h2 = slide.querySelector('h2:not(.subtitle)');
    if (h1) return h1.textContent.substring(0, 30);
    if (h2) return h2.textContent.substring(0, 30);
    return 'Slide';
}

function updateNavigatorHighlight() {
    const navItems = document.querySelectorAll('.nav-item');
    navItems.forEach(item => {
        const slideNum = parseInt(item.getAttribute('data-slide'), 10);
        if (slideNum === currentSlide) {
            item.classList.add('active');
        } else {
            item.classList.remove('active');
        }
    });
}

function toggleNavigator() {
    const navOverlay = document.getElementById('navOverlay');
    if (navOverlay) {
        navOverlay.classList.toggle('hidden');
        if (!navOverlay.classList.contains('hidden')) {
            updateNavigatorHighlight();
            // Scroll to current slide in navigator
            setTimeout(() => {
                const activeItem = document.querySelector('.nav-item.active');
                if (activeItem) {
                    activeItem.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
            }, 100);
        }
    }
}

function closeNavigator() {
    const navOverlay = document.getElementById('navOverlay');
    if (navOverlay) {
        navOverlay.classList.add('hidden');
    }
}

function isNavigatorOpen() {
    const navOverlay = document.getElementById('navOverlay');
    return navOverlay && !navOverlay.classList.contains('hidden');
}

// ========================================
// HELP OVERLAY FUNCTIONS
// ========================================
function toggleHelp() {
    const helpOverlay = document.getElementById('helpOverlay');
    if (helpOverlay) {
        helpOverlay.classList.toggle('hidden');
    }
}

function closeHelp() {
    const helpOverlay = document.getElementById('helpOverlay');
    if (helpOverlay) {
        helpOverlay.classList.add('hidden');
    }
}

function isHelpOpen() {
    const helpOverlay = document.getElementById('helpOverlay');
    return helpOverlay && !helpOverlay.classList.contains('hidden');
}

// ========================================
// ACCESSIBILITY FUNCTIONS
// ========================================
function updateSlideAria() {
    const slides = document.querySelectorAll('.slide');
    slides.forEach((slide, index) => {
        const slideNumber = index + 1;
        slide.setAttribute('role', 'region');
        slide.setAttribute('aria-label', `Slide ${slideNumber} of ${totalSlides}`);
    });
}

// ========================================
// CONSOLE WELCOME MESSAGE
// ========================================
console.log('%cDay 2: Operating Systems & Virtualization',
    'font-size: 20px; font-weight: bold; color: #667eea;');
console.log('%cKeyboard Controls:',
    'font-size: 14px; font-weight: bold; color: #f093fb;');
console.log('→ / Space / PageDown: Next slide');
console.log('← / PageUp: Previous slide');
console.log('Home: First slide');
console.log('End: Last slide');
console.log('F: Toggle fullscreen');
console.log('Esc: Close overlays / Return to first slide');
console.log('N: Open slide navigator');
console.log('?: Show keyboard shortcuts help');
console.log('\n%cYou can also use:',
    'font-size: 14px; font-weight: bold; color: #4facfe;');
console.log('• Click navigation arrows');
console.log('• Swipe on touch devices');
console.log('• Click agenda items on first slide');
console.log('• Click the menu button for slide navigator');
console.log('\n%cDebug Commands (type in console):',
    'font-size: 14px; font-weight: bold; color: #f5576c;');
console.log('presentation.goToSlide(number)');
console.log('presentation.getProgress()');
console.log('presentation.currentSlide()');

