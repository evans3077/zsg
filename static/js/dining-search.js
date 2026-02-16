document.addEventListener("DOMContentLoaded", function () {
    const input = document.getElementById("dining-menu-search-input");
    const resultsEl = document.getElementById("dining-search-results");
    if (!input || !resultsEl) return;

    const endpoint = "/dining/api/search/";
    let activeIndex = -1;
    let items = [];
    let debounceTimer = null;
    let controller = null;

    function closeResults() {
        resultsEl.classList.remove("is-open");
        resultsEl.innerHTML = "";
        activeIndex = -1;
        items = [];
        input.setAttribute("aria-expanded", "false");
        input.removeAttribute("aria-activedescendant");
    }

    function openResults() {
        resultsEl.classList.add("is-open");
        input.setAttribute("aria-expanded", "true");
    }

    function render(results) {
        items = results || [];
        if (!items.length) {
            resultsEl.innerHTML = '<div class="dining-search-empty">No results found.</div>';
            openResults();
            return;
        }

        const html = items
            .map((item, idx) => {
                const price = item.price ? `<span class="dining-search-price">Ksh ${item.price}</span>` : "";
                const thumb = item.thumbnail
                    ? `<img src="${item.thumbnail}" alt="${item.name}" loading="lazy" width="56" height="56">`
                    : '<div class="dining-search-thumb-fallback"><i class="fas fa-utensils"></i></div>';
                return `
                    <a href="${item.url}" class="dining-search-item" id="dining-search-option-${idx}" role="option" aria-selected="false" data-idx="${idx}">
                        <div class="dining-search-thumb">${thumb}</div>
                        <div class="dining-search-meta">
                            <div class="dining-search-title">${item.name}</div>
                            <div class="dining-search-sub">${item.category}</div>
                        </div>
                        ${price}
                    </a>
                `;
            })
            .join("");

        resultsEl.innerHTML = html;
        openResults();
    }

    async function fetchResults(query) {
        if (controller) controller.abort();
        controller = new AbortController();
        const response = await fetch(`${endpoint}?q=${encodeURIComponent(query)}`, {
            method: "GET",
            headers: { "X-Requested-With": "XMLHttpRequest" },
            signal: controller.signal,
        });
        if (!response.ok) throw new Error("Search request failed");
        return response.json();
    }

    function setActive(index) {
        const nodes = Array.from(resultsEl.querySelectorAll(".dining-search-item"));
        nodes.forEach((el) => {
            el.classList.remove("active");
            el.setAttribute("aria-selected", "false");
        });
        if (index < 0 || index >= nodes.length) return;
        nodes[index].classList.add("active");
        nodes[index].setAttribute("aria-selected", "true");
        input.setAttribute("aria-activedescendant", nodes[index].id);
        nodes[index].scrollIntoView({ block: "nearest" });
        activeIndex = index;
    }

    input.addEventListener("input", function () {
        const query = this.value.trim();
        if (debounceTimer) clearTimeout(debounceTimer);
        if (query.length < 2) {
            closeResults();
            return;
        }
        debounceTimer = setTimeout(async () => {
            try {
                const payload = await fetchResults(query);
                render(payload.results || []);
            } catch (err) {
                if (err.name !== "AbortError") {
                    resultsEl.innerHTML = '<div class="dining-search-empty">Unable to search right now.</div>';
                    openResults();
                }
            }
        }, 250);
    });

    input.addEventListener("keydown", function (e) {
        const nodes = Array.from(resultsEl.querySelectorAll(".dining-search-item"));
        if (!nodes.length) return;

        if (e.key === "ArrowDown") {
            e.preventDefault();
            setActive((activeIndex + 1) % nodes.length);
        } else if (e.key === "ArrowUp") {
            e.preventDefault();
            setActive((activeIndex - 1 + nodes.length) % nodes.length);
        } else if (e.key === "Enter") {
            if (activeIndex >= 0 && nodes[activeIndex]) {
                e.preventDefault();
                window.location.href = nodes[activeIndex].getAttribute("href");
            }
        } else if (e.key === "Escape") {
            closeResults();
        }
    });

    document.addEventListener("click", function (e) {
        if (!resultsEl.contains(e.target) && e.target !== input) {
            closeResults();
        }
    });

    input.addEventListener("focus", function () {
        if (resultsEl.innerHTML.trim()) {
            openResults();
        }
    });
});
