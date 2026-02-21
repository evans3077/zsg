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

    // Adaptive div boxes for non-link cards
    initAdaptiveDivBoxes();
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

    let ticking = false;
    const updateVisibility = () => {
        const shouldShow = window.pageYOffset > 300;
        if (shouldShow !== backToTop.classList.contains('visible')) {
            backToTop.classList.toggle('visible', shouldShow);
        }
        ticking = false;
    };

    window.addEventListener('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(updateVisibility);
            ticking = true;
        }
    }, { passive: true });

    updateVisibility();
    
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
        dropdown.addEventListener('focusin', function() {
            this.classList.add('is-open');
        });
        
        dropdown.addEventListener('focusout', function(e) {
            if (!this.contains(e.relatedTarget)) {
                this.classList.remove('is-open');
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
    document.addEventListener('click', function(e) {
        const anchor = e.target.closest('a[href^="#"]');
        if (!anchor) return;

        const href = anchor.getAttribute('href');
        if (!href || href === '#') return;

        let target = null;
        try {
            target = document.querySelector(href);
        } catch (_error) {
            return;
        }
        if (!target) return;

        e.preventDefault();

        // Close mobile menu if open
        const mobileMenu = document.querySelector('.mobile-menu');
        if (mobileMenu && mobileMenu.classList.contains('active')) {
            mobileMenu.classList.remove('active');
            const mobileOverlay = document.querySelector('.mobile-menu-overlay');
            if (mobileOverlay) {
                mobileOverlay.classList.remove('active');
            }
            document.body.style.overflow = '';
        }

        const header = document.querySelector('.main-header');
        const headerHeight = header ? header.offsetHeight : 0;
        const targetPosition = target.offsetTop - headerHeight;

        window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
        });
    });
}

// Sub-navigation auto hide (Gardens & Conferences)
function initSubNavAutoHide() {
    const subnavs = document.querySelectorAll('.conference-nav, .gardens-nav, .food-category-nav, .kids-nav');
    if (!subnavs.length) return;

    const header = document.querySelector('.main-header');
    const diningStickySearch = document.querySelector('.dining-sticky-search');
    const applySubnavOffsets = () => {
        const headerHeight = header ? header.offsetHeight : 80;
        const diningSearchHeight = diningStickySearch ? diningStickySearch.offsetHeight : 0;
        subnavs.forEach(nav => {
            if (nav.classList.contains('food-category-nav')) {
                nav.style.top = `${headerHeight + diningSearchHeight}px`;
            } else {
                nav.style.top = `${headerHeight}px`;
            }
        });
    };
    applySubnavOffsets();

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

    window.addEventListener('resize', applySubnavOffsets, { passive: true });

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
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // Provision for API integration when keys are provided.
    if (businessProfileId && apiKey) {
        slider.dataset.reviewsSource = 'google-business-profile';
    } else {
        slider.dataset.reviewsSource = 'fallback-static';
    }

    let activeIndex = 0;
    let autoTimer = null;
    let isHovering = false;
    let isInViewport = false;
    let isPageVisible = !document.hidden;

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

    const stopAutoPlay = () => {
        if (!autoTimer) return;
        clearInterval(autoTimer);
        autoTimer = null;
    };

    const startAutoPlay = () => {
        if (prefersReducedMotion || cards.length < 2 || isHovering || !isInViewport || !isPageVisible || autoTimer) {
            return;
        }
        autoTimer = setInterval(() => goTo(activeIndex + 1), 5200);
    };

    const restartAutoPlay = () => {
        stopAutoPlay();
        startAutoPlay();
    };

    goTo(0);

    if ('IntersectionObserver' in window) {
        const sliderObserver = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                isInViewport = entry.isIntersecting;
                if (isInViewport) {
                    startAutoPlay();
                } else {
                    stopAutoPlay();
                }
            });
        }, { threshold: 0.2 });
        sliderObserver.observe(slider);
    } else {
        isInViewport = true;
        startAutoPlay();
    }

    document.addEventListener('visibilitychange', () => {
        isPageVisible = !document.hidden;
        if (isPageVisible) {
            startAutoPlay();
        } else {
            stopAutoPlay();
        }
    });

    slider.addEventListener('mouseenter', () => {
        isHovering = true;
        stopAutoPlay();
    });
    slider.addEventListener('mouseleave', () => {
        isHovering = false;
        restartAutoPlay();
    });
}

function initAdaptiveDivBoxes() {
    if (!window.matchMedia('(max-width: 767px)').matches) return;

    const groups = [
        { container: '.highlights-grid', cards: '.highlight-card' },
        { container: '.services-grid', cards: '.service-card' },
        { container: '.rooms-grid', cards: '.room-card' },
        { container: '.packages-grid', cards: '.package-card' },
        { container: '.gardens-grid', cards: '.garden-card' },
        { container: '.event-types-grid', cards: '.event-type-card' },
        { container: '.activity-grid', cards: '.activity-card' },
        { container: '.farm-grid', cards: '.farm-card' },
    ];

    const allCardSelectors = groups.map(group => group.cards).join(', ');

    document.addEventListener('click', (event) => {
        const card = event.target.closest(allCardSelectors);
        if (!card) return;

        const group = groups.find((candidate) => card.matches(candidate.cards));
        if (!group) return;

        const container = card.closest(group.container);
        if (!container) return;

        // Keep linked cards unchanged; only non-link cards trigger horizontal mode.
        const leadsToPage = card.matches('a[href]') || !!card.querySelector('a[href]');
        if (!leadsToPage) {
            container.classList.add('mobile-swipe-row');
        }
    }, { passive: true });
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
