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
    updateSlideAria();
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
    const slideNumberElement = document.getElementById('slideNumber');
    if (slideNumberElement) {
        slideNumberElement.textContent = `${currentSlide} / ${totalSlides}`;
    }
}

function updateProgressBar() {
    const progressFill = document.querySelector('.progress-fill');
    const progress = (currentSlide / totalSlides) * 100;

    if (progressFill) {
        progressFill.style.width = `${progress}%`;
    }

    updateArrowButtons();
}

function updateArrowButtons() {
    const leftArrow = document.getElementById('leftArrow');
    const rightArrow = document.getElementById('rightArrow');

    if (leftArrow) {
        leftArrow.disabled = currentSlide === 1;
    }

    if (rightArrow) {
        rightArrow.disabled = currentSlide === totalSlides;
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

    // Side Arrow Buttons
    const leftArrow = document.getElementById('leftArrow');
    const rightArrow = document.getElementById('rightArrow');

    if (leftArrow) {
        leftArrow.addEventListener('click', previousSlide);
    }

    if (rightArrow) {
        rightArrow.addEventListener('click', nextSlide);
    }

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
            goToFirstSlide();
            break;
    }
}

// ========================================
// FULLSCREEN SUPPORT
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
// PRESENTATION MODE
// ========================================
// Hide cursor after inactivity
let cursorTimeout;

function showCursor() {
    document.body.style.cursor = 'default';
    document.querySelectorAll('.nav-btn, .slide-nav').forEach(el => {
        el.style.opacity = '1';
    });
}

function hideCursor() {
    document.body.style.cursor = 'none';
    document.querySelectorAll('.nav-btn, .slide-nav').forEach(el => {
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

    // Map agenda items to slide numbers - Day 3
    const agendaSlideMap = {
        0: 4,   // Git Basics (was 3, now 4)
        1: 5,   // GitHub (was 4, now 5)
        2: 17,  // HTML/CSS (was 16, now 17)
        3: 22   // Deployment (was 21, now 22)
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
console.log('%cDay 3: Git, Portfolio Website & Deployment',
    'font-size: 20px; font-weight: bold; color: #667eea;');
console.log('%cKeyboard Controls:',
    'font-size: 14px; font-weight: bold; color: #f093fb;');
console.log('→ / Space / PageDown: Next slide');
console.log('← / PageUp: Previous slide');
console.log('Home: First slide');
console.log('End: Last slide');
console.log('F: Toggle fullscreen');
console.log('Esc: Return to first slide');
console.log('\n%cYou can also use:',
    'font-size: 14px; font-weight: bold; color: #4facfe;');
console.log('• Click navigation arrows');
console.log('• Swipe on touch devices');
console.log('• Click agenda items on first slide');
console.log('\n%cDebug Commands (type in console):',
    'font-size: 14px; font-weight: bold; color: #f5576c;');
console.log('presentation.goToSlide(number)');
console.log('presentation.getProgress()');
console.log('presentation.currentSlide()');
