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

    const startInput = document.getElementById("dining_start_datetime");
    const endInput = document.getElementById("dining_end_datetime");
    const now = new Date();
    const minValue = new Date(now.getTime() - now.getTimezoneOffset() * 60000)
        .toISOString()
        .slice(0, 16);

    if (startInput) {
        startInput.min = minValue;
    }
    if (endInput) {
        endInput.min = minValue;
    }

    if (startInput && endInput) {
        startInput.addEventListener("change", function () {
            endInput.min = this.value || minValue;
            if (endInput.value && endInput.value < endInput.min) {
                endInput.value = endInput.min;
            }
        });
    }

    initDiningSpaceSliders();
});

function initDiningSpaceSliders() {
    const sliders = document.querySelectorAll("[data-slider]");
    if (!sliders.length) return;

    sliders.forEach(function (slider) {
        const track = slider.querySelector(".space-gallery-track");
        const slides = slider.querySelectorAll(".space-gallery-slide");
        const prevBtn = slider.querySelector(".space-gallery-nav.prev");
        const nextBtn = slider.querySelector(".space-gallery-nav.next");
        if (!track || slides.length < 2) return;

        let index = 0;
        let timer = null;

        function goTo(target) {
            index = (target + slides.length) % slides.length;
            track.style.transform = "translateX(-" + (index * 100) + "%)";
        }

        function startAuto() {
            stopAuto();
            timer = setInterval(function () {
                goTo(index + 1);
            }, 3600);
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
                startAuto();
            });
        }

        if (nextBtn) {
            nextBtn.addEventListener("click", function () {
                goTo(index + 1);
                startAuto();
            });
        }

        slider.addEventListener("mouseenter", stopAuto);
        slider.addEventListener("mouseleave", startAuto);
        goTo(0);
        startAuto();
    });
}
