document.addEventListener("DOMContentLoaded", function () {
    const lightbox = document.getElementById("gallery-lightbox");
    const imageNode = document.getElementById("gallery-lightbox-image");
    const captionNode = document.getElementById("gallery-lightbox-caption");
    const closeBtn = lightbox ? lightbox.querySelector(".gallery-lightbox-close") : null;
    const triggers = document.querySelectorAll(".gallery-lightbox-trigger");
    if (!lightbox || !imageNode || !captionNode || !triggers.length) return;

    function closeLightbox() {
        lightbox.classList.remove("is-open");
        lightbox.setAttribute("aria-hidden", "true");
        imageNode.src = "";
        imageNode.alt = "";
        captionNode.textContent = "";
    }

    function openLightbox(source, altText, caption) {
        imageNode.src = source || "";
        imageNode.alt = altText || "Gallery image";
        captionNode.textContent = caption || "";
        lightbox.classList.add("is-open");
        lightbox.setAttribute("aria-hidden", "false");
    }

    triggers.forEach(function (trigger) {
        trigger.addEventListener("click", function () {
            openLightbox(
                this.getAttribute("data-src"),
                this.getAttribute("data-alt"),
                this.getAttribute("data-caption")
            );
        });
    });

    if (closeBtn) {
        closeBtn.addEventListener("click", closeLightbox);
    }

    lightbox.addEventListener("click", function (event) {
        if (event.target === lightbox) {
            closeLightbox();
        }
    });

    document.addEventListener("keydown", function (event) {
        if (event.key === "Escape" && lightbox.classList.contains("is-open")) {
            closeLightbox();
        }
    });
});
