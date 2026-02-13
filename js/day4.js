// ========================================
// DAY 4 PRESENTATION - NAVIGATION LOGIC
// ========================================

// State
let currentSlide = 1;
const totalSlides = document.querySelectorAll('.slide').length;

// ========================================
// INITIALIZATION
// ========================================
function initPresentation() {
    updateSlideCounter();
    updateProgressBar();
    updateHash();

    // Check URL hash on load
    const hash = window.location.hash;
    if (hash) {
        const slideNum = parseInt(hash.replace('#slide-', ''));
        if (slideNum >= 1 && slideNum <= totalSlides) {
            goToSlide(slideNum);
        }
    }
}

// ========================================
// NAVIGATION FUNCTIONS
// ========================================
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

function goToSlide(slideNumber) {
    if (slideNumber < 1 || slideNumber > totalSlides) return;

    // Remove active class from current slide
    const slides = document.querySelectorAll('.slide');
    slides.forEach(slide => slide.classList.remove('active'));

    // Add active class to target slide
    slides[slideNumber - 1].classList.add('active');

    // Update current slide
    currentSlide = slideNumber;

    // Update UI
    updateSlideCounter();
    updateProgressBar();
    updateHash();
}

// ========================================
// UI UPDATE FUNCTIONS
// ========================================
function updateSlideCounter() {
    const counter = document.getElementById('slideNumber');
    if (counter) {
        counter.textContent = `${currentSlide} / ${totalSlides}`;
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
function updateHash() {
    window.location.hash = `slide-${currentSlide}`;
}

// ========================================
// EVENT LISTENERS
// ========================================
document.addEventListener('DOMContentLoaded', () => {
    initPresentation();

    // Navigation Buttons (if exist)
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

    // Touch/Swipe Support
    let touchStartX = 0;
    let touchEndX = 0;

    document.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
    });

    document.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
    });

    function handleSwipe() {
        const swipeThreshold = 50;
        const diff = touchStartX - touchEndX;

        if (Math.abs(diff) > swipeThreshold) {
            if (diff > 0) {
                // Swipe left - next slide
                nextSlide();
            } else {
                // Swipe right - previous slide
                previousSlide();
            }
        }
    }

    console.log('%c🚀 Day 4: Hardware + IoT Presentation Loaded! ', 'background: #667eea; color: white; font-size: 16px; padding: 10px; border-radius: 4px;');
    console.log(`Total slides: ${totalSlides}`);
});

// ========================================
// KEYBOARD CONTROLS
// ========================================
let lastKeyPress = 0;
const keyPressDelay = 300; // Throttle to prevent rapid firing

function handleKeyPress(e) {
    const now = Date.now();
    if (now - lastKeyPress < keyPressDelay) return;
    lastKeyPress = now;

    switch (e.key) {
        case 'ArrowRight':
        case ' ':
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
            goToSlide(1);
            break;
        case 'End':
            e.preventDefault();
            goToSlide(totalSlides);
            break;
        case 'Escape':
            e.preventDefault();
            goToSlide(1);
            break;
        case 'f':
        case 'F':
            e.preventDefault();
            toggleFullscreen();
            break;
    }
}

// ========================================
// FULLSCREEN TOGGLE
// ========================================
function toggleFullscreen() {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen();
    } else {
        if (document.exitFullscreen) {
            document.exitFullscreen();
        }
    }
}

// ========================================
// EXPOSE GLOBAL API
// ========================================
window.presentation = {
    next: nextSlide,
    previous: previousSlide,
    goToSlide: goToSlide,
    toggleFullscreen: toggleFullscreen,
    getCurrentSlide: () => currentSlide,
    getTotalSlides: () => totalSlides
};
