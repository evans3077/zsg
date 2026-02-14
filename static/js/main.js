// Main JavaScript for Zamar Springs Gardens

document.addEventListener('DOMContentLoaded', function() {
    // Mobile Menu
    initMobileMenu();
    
    // Back to Top
    initBackToTop();
    
    // Dropdowns
    initDropdowns();
    
    // Lazy Loading
    initLazyLoading();
    
    // Smooth Scrolling
    initSmoothScrolling();

    // Sub-navigation auto hide
    initSubNavAutoHide();
    
    // Newsletter Form
    initNewsletterForm();

    // Booking datetime window helpers
    initBookingDatetimeWindow();

    // Reviews slider / API hook
    initGoogleReviewsSection();
});

// Mobile Menu
function initMobileMenu() {
    const mobileToggle = document.querySelector('.mobile-menu-toggle');
    const mobileClose = document.querySelector('.mobile-menu-close');
    const mobileOverlay = document.querySelector('.mobile-menu-overlay');
    const mobileMenu = document.querySelector('.mobile-menu');
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
    
    if (!mobileToggle) return;
    
    // Open mobile menu
    mobileToggle.addEventListener('click', function() {
        mobileMenu.classList.add('active');
        mobileOverlay.classList.add('active');
        document.body.style.overflow = 'hidden';
    });
    
    // Close mobile menu
    function closeMenu() {
        mobileMenu.classList.remove('active');
        mobileOverlay.classList.remove('active');
        document.body.style.overflow = '';
    }
    
    mobileClose.addEventListener('click', closeMenu);
    mobileOverlay.addEventListener('click', closeMenu);
    
    // Close menu on ESC key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && mobileMenu.classList.contains('active')) {
            closeMenu();
        }
    });
    
    // Mobile dropdowns
    dropdownToggles.forEach(toggle => {
        toggle.addEventListener('click', function(e) {
            const dropdown = this.nextElementSibling;
            if (!dropdown || !dropdown.classList.contains('mobile-dropdown')) {
                return;
            }
            e.preventDefault();
            const icon = this.querySelector('i');
            
            dropdown.classList.toggle('active');
            
            if (icon) {
                if (dropdown.classList.contains('active')) {
                    icon.classList.remove('fa-chevron-down');
                    icon.classList.add('fa-chevron-up');
                } else {
                    icon.classList.remove('fa-chevron-up');
                    icon.classList.add('fa-chevron-down');
                }
            }
        });
    });

    // Close mobile menu when selecting a normal mobile link
    mobileMenu.querySelectorAll('a.mobile-nav-link:not(.dropdown-toggle), .mobile-dropdown a').forEach(link => {
        link.addEventListener('click', closeMenu);
    });
}

// Back to Top
function initBackToTop() {
    const backToTop = document.querySelector('.back-to-top');
    
    if (!backToTop) return;
    
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTop.classList.add('visible');
        } else {
            backToTop.classList.remove('visible');
        }
    });
    
    backToTop.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// Dropdowns
function initDropdowns() {
    const dropdowns = document.querySelectorAll('.nav-dropdown');
    
    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('mouseenter', function() {
            const menu = this.querySelector('.dropdown-menu');
            if (menu) {
                menu.style.opacity = '1';
                menu.style.visibility = 'visible';
                menu.style.transform = 'translateY(0)';
            }
        });
        
        dropdown.addEventListener('mouseleave', function() {
            const menu = this.querySelector('.dropdown-menu');
            if (menu) {
                menu.style.opacity = '0';
                menu.style.visibility = 'hidden';
                menu.style.transform = 'translateY(-10px)';
            }
        });
    });
}

// Lazy Loading
function initLazyLoading() {
    if ('IntersectionObserver' in window) {
        const lazyImages = document.querySelectorAll('img[data-src]');
        
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    
                    if (img.dataset.srcset) {
                        img.srcset = img.dataset.srcset;
                    }
                    
                    img.classList.remove('lazy');
                    observer.unobserve(img);
                }
            });
        });
        
        lazyImages.forEach(img => imageObserver.observe(img));
    }
}

// Smooth Scrolling
function initSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            if (href === '#') return;
            
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                
                // Close mobile menu if open
                const mobileMenu = document.querySelector('.mobile-menu');
                if (mobileMenu && mobileMenu.classList.contains('active')) {
                    mobileMenu.classList.remove('active');
                    document.querySelector('.mobile-menu-overlay').classList.remove('active');
                    document.body.style.overflow = '';
                }
                
                const headerHeight = document.querySelector('.main-header').offsetHeight;
                const targetPosition = target.offsetTop - headerHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Sub-navigation auto hide (Gardens & Conferences)
function initSubNavAutoHide() {
    const subnavs = document.querySelectorAll('.conference-nav, .gardens-nav, .food-category-nav, .kids-nav');
    if (!subnavs.length) return;

    const header = document.querySelector('.main-header');
    const headerHeight = header ? header.offsetHeight : 80;
    subnavs.forEach(nav => {
        nav.style.top = `${headerHeight}px`;
    });

    let lastScrollY = Math.max(window.scrollY, 0);
    let ticking = false;
    let hideTimer = null;
    const scrollDeltaThreshold = 8;
    const idleHideDelay = 1400;

    const scheduleHide = () => {
        if (hideTimer) clearTimeout(hideTimer);
        hideTimer = setTimeout(() => {
            if (window.scrollY > 140) {
                subnavs.forEach(nav => nav.classList.add('subnav-hidden'));
            }
        }, idleHideDelay);
    };

    const onScroll = () => {
        const currentY = Math.max(window.scrollY, 0);
        const delta = currentY - lastScrollY;
        const scrollingDown = delta > scrollDeltaThreshold;
        const scrollingUp = delta < -scrollDeltaThreshold;

        subnavs.forEach(nav => {
            if (currentY < 120) {
                nav.classList.remove('subnav-hidden');
                return;
            }

            if (scrollingDown) {
                nav.classList.add('subnav-hidden');
            } else if (scrollingUp) {
                nav.classList.remove('subnav-hidden');
                scheduleHide();
            }
        });

        lastScrollY = currentY;
        ticking = false;
    };

    window.addEventListener('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(onScroll);
            ticking = true;
        }
    }, { passive: true });

    subnavs.forEach(nav => {
        nav.addEventListener('mouseenter', () => {
            if (hideTimer) clearTimeout(hideTimer);
            nav.classList.remove('subnav-hidden');
        });
        nav.addEventListener('mouseleave', scheduleHide);
    });
}

// Newsletter Form
function initNewsletterForm() {
    const newsletterForm = document.querySelector('.newsletter-form');
    
    if (!newsletterForm) return;
    
    newsletterForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const emailInput = this.querySelector('input[type="email"]');
        const email = emailInput.value.trim();
        
        if (!email) {
            showNotification('Please enter your email address', 'error');
            return;
        }
        
        if (!validateEmail(email)) {
            showNotification('Please enter a valid email address', 'error');
            return;
        }
        
        // Simulate submission
        const submitBtn = this.querySelector('button[type="submit"]');
        const originalText = submitBtn.innerHTML;
        
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
        submitBtn.disabled = true;
        
        setTimeout(() => {
            showNotification('Thank you for subscribing!', 'success');
            emailInput.value = '';
            submitBtn.innerHTML = originalText;
            submitBtn.disabled = false;
        }, 1500);
    });
}

function initBookingDatetimeWindow() {
    const startInputs = document.querySelectorAll('input.event-start-datetime');
    const endInputs = document.querySelectorAll('input.event-end-datetime');
    if (!startInputs.length || !endInputs.length) return;

    const now = new Date();
    const minValue = new Date(now.getTime() - (now.getTimezoneOffset() * 60000)).toISOString().slice(0, 16);

    startInputs.forEach((startInput, index) => {
        const endInput = endInputs[index];
        if (!endInput) return;

        startInput.min = minValue;
        endInput.min = minValue;

        startInput.addEventListener('change', function() {
            endInput.min = this.value || minValue;
            if (endInput.value && endInput.value < endInput.min) {
                endInput.value = endInput.min;
            }
        });
    });
}

function initGoogleReviewsSection() {
    const slider = document.getElementById('reviews-slider');
    if (!slider) return;

    const track = slider.querySelector('.reviews-track');
    const dotsContainer = slider.querySelector('.reviews-dots');
    const prevBtn = slider.querySelector('.review-prev');
    const nextBtn = slider.querySelector('.review-next');
    const cards = slider.querySelectorAll('.review-card');
    if (!cards.length) return;

    const config = window.ZAMAR_GOOGLE_REVIEWS || {};
    const businessProfileId = config.businessProfileId || slider.dataset.businessProfileId;
    const apiKey = config.apiKey || '';

    // Provision for API integration when keys are provided.
    if (businessProfileId && apiKey) {
        slider.dataset.reviewsSource = 'google-business-profile';
    } else {
        slider.dataset.reviewsSource = 'fallback-static';
    }

    let activeIndex = 0;
    let autoTimer = null;

    const goTo = (index) => {
        if (!track) return;
        activeIndex = (index + cards.length) % cards.length;
        track.style.transform = `translateX(-${activeIndex * 100}%)`;
        slider.querySelectorAll('.review-dot').forEach((dot, dotIndex) => {
            dot.classList.toggle('active', dotIndex === activeIndex);
        });
    };

    if (dotsContainer) {
        dotsContainer.innerHTML = '';
        cards.forEach((_, index) => {
            const dot = document.createElement('button');
            dot.type = 'button';
            dot.className = `review-dot${index === 0 ? ' active' : ''}`;
            dot.setAttribute('aria-label', `Show review ${index + 1}`);
            dot.addEventListener('click', () => {
                goTo(index);
                restartAutoPlay();
            });
            dotsContainer.appendChild(dot);
        });
    }

    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            goTo(activeIndex - 1);
            restartAutoPlay();
        });
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            goTo(activeIndex + 1);
            restartAutoPlay();
        });
    }

    const startAutoPlay = () => {
        autoTimer = setInterval(() => goTo(activeIndex + 1), 5200);
    };

    const restartAutoPlay = () => {
        if (autoTimer) clearInterval(autoTimer);
        startAutoPlay();
    };

    goTo(0);
    startAutoPlay();

    slider.addEventListener('mouseenter', () => {
        if (autoTimer) clearInterval(autoTimer);
    });
    slider.addEventListener('mouseleave', restartAutoPlay);
}

// Helper Functions
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function showNotification(message, type) {
    // Remove existing notifications
    const existing = document.querySelector('.notification');
    if (existing) existing.remove();
    
    // Create notification
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <span>${message}</span>
        <button class="notification-close">&times;</button>
    `;
    
    document.body.appendChild(notification);
    
    // Show notification
    setTimeout(() => {
        notification.classList.add('show');
    }, 10);
    
    // Auto remove after 5 seconds
    const autoRemove = setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 300);
    }, 5000);
    
    // Close button
    notification.querySelector('.notification-close').addEventListener('click', function() {
        clearTimeout(autoRemove);
        notification.classList.remove('show');
        setTimeout(() => {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 300);
    });
}

// Add notification styles
const style = document.createElement('style');
style.textContent = `
    .notification {
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 1.5rem;
        border-radius: 0.5rem;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transform: translateX(120%);
        transition: transform 0.3s ease;
        z-index: 10000;
        display: flex;
        align-items: center;
        justify-content: space-between;
        min-width: 300px;
        max-width: 400px;
    }
    
    .notification.show {
        transform: translateX(0);
    }
    
    .notification-success {
        background: var(--success);
    }
    
    .notification-error {
        background: var(--error);
    }
    
    .notification-close {
        background: none;
        border: none;
        color: inherit;
        font-size: 1.5rem;
        cursor: pointer;
        margin-left: 1rem;
    }
`;
document.head.appendChild(style);
