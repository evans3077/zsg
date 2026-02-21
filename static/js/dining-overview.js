document.addEventListener("DOMContentLoaded", function () {
    const galleryCards = document.querySelectorAll(".dining-gallery-card");
    galleryCards.forEach(function (card) {
        card.addEventListener("click", function () {
            this.classList.toggle("is-expanded");
        });
        card.addEventListener("keypress", function (event) {
            if (event.key === "Enter" || event.key === " ") {
                event.preventDefault();
                this.classList.toggle("is-expanded");
            }
        });
    });

    initDiningSpaceSliders();
});

function initDiningSpaceSliders() {
    const sliders = document.querySelectorAll("[data-slider]");
    if (!sliders.length) return;
    const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    sliders.forEach(function (slider) {
        const track = slider.querySelector(".space-gallery-track");
        const slides = slider.querySelectorAll(".space-gallery-slide");
        const prevBtn = slider.querySelector(".space-gallery-nav.prev");
        const nextBtn = slider.querySelector(".space-gallery-nav.next");
        if (!track || slides.length < 2) return;

        let index = 0;
        let timer = null;
        let isInViewport = false;
        let isHovered = false;

        function goTo(target) {
            index = (target + slides.length) % slides.length;
            track.style.transform = "translateX(-" + (index * 100) + "%)";
        }

        function startAuto() {
            if (prefersReducedMotion || slides.length < 2 || timer || !isInViewport || isHovered || document.hidden) {
                return;
            }
            timer = setInterval(function () {
                goTo(index + 1);
            }, 3600);
        }

        function updateAuto() {
            stopAuto();
            startAuto();
        }

        function stopAuto() {
            if (timer) {
                clearInterval(timer);
                timer = null;
            }
        }

        if (prevBtn) {
            prevBtn.addEventListener("click", function () {
                goTo(index - 1);
                updateAuto();
            });
        }

        if (nextBtn) {
            nextBtn.addEventListener("click", function () {
                goTo(index + 1);
                updateAuto();
            });
        }

        slider.addEventListener("mouseenter", function () {
            isHovered = true;
            stopAuto();
        });
        slider.addEventListener("mouseleave", function () {
            isHovered = false;
            startAuto();
        });

        if ("IntersectionObserver" in window) {
            const sliderObserver = new IntersectionObserver(function (entries) {
                entries.forEach(function (entry) {
                    isInViewport = entry.isIntersecting;
                    updateAuto();
                });
            }, { threshold: 0.15 });
            sliderObserver.observe(slider);
        } else {
            isInViewport = true;
            startAuto();
        }

        document.addEventListener("visibilitychange", function () {
            updateAuto();
        });

        goTo(0);
    });
}
