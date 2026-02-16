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
});
