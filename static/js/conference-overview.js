document.addEventListener("DOMContentLoaded", function () {
    const filterRoot = document.getElementById("layout-style-filter");
    const roomsGrid = document.getElementById("overview-rooms-grid");
    const emptyState = document.getElementById("layout-filter-empty");
    if (!filterRoot || !roomsGrid) return;

    const buttons = filterRoot.querySelectorAll("[data-layout-filter]");
    const roomCards = roomsGrid.querySelectorAll("[data-room-layouts]");
    if (!buttons.length || !roomCards.length) return;

    function setActiveButton(nextButton) {
        buttons.forEach((button) => {
            const isActive = button === nextButton;
            button.classList.toggle("is-active", isActive);
            button.setAttribute("aria-pressed", isActive ? "true" : "false");
        });
    }

    function applyFilter(layoutKey) {
        let visibleCount = 0;
        roomCards.forEach((card) => {
            const layoutText = (card.dataset.roomLayouts || "").trim();
            const roomLayouts = layoutText ? layoutText.split(/\s+/) : [];
            const shouldShow = layoutKey === "all" || roomLayouts.includes(layoutKey);
            card.hidden = !shouldShow;
            if (shouldShow) visibleCount += 1;
        });
        if (emptyState) {
            emptyState.hidden = visibleCount > 0;
        }
    }

    buttons.forEach((button) => {
        button.addEventListener("click", function () {
            const selectedLayout = button.dataset.layoutFilter || "all";
            setActiveButton(button);
            applyFilter(selectedLayout);
        });
    });

    applyFilter("all");
});
