// Conference Page JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll for category navigation
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            if(this.getAttribute('href') !== '#') {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if(target) {
                    const headerHeight = document.querySelector('.main-header').offsetHeight;
                    const targetPosition = target.getBoundingClientRect().top + window.pageYOffset;
                    window.scrollTo({
                        top: targetPosition - headerHeight - 20,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
    
    // Image lazy loading
    if('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if(entry.isIntersecting) {
                    const img = entry.target;
                    if(img.dataset.src) {
                        img.src = img.dataset.src;
                    }
                    observer.unobserve(img);
                }
            });
        });
        
        document.querySelectorAll('img[loading="lazy"]').forEach(img => {
            imageObserver.observe(img);
        });
    }
    
});
