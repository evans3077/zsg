# PageSpeed Follow-up (Mobile + Desktop)

This follow-up addresses improvements that are actionable in the app code (excluding Render platform latency/cold-start effects).

## Problems addressed

1. **Broken WhatsApp social link**
   - Problem: `https://wa.me/+254112394681` used an invalid `wa.me` format.
   - Fix: Changed to `https://wa.me/254112394681`.

2. **Render-blocking main script execution**
   - Problem: Base script was loaded without `defer`, which can delay first paint and interactivity.
   - Fix: Added `defer` to the base `main.js` script tag.

3. **Conference card image loading not optimized**
   - Problem: Featured conference image on overview lacked lazy loading/decoding hints and intrinsic dimensions.
   - Fix: Added `loading="lazy"`, `decoding="async"`, and dimensions to reduce layout shifts and improve mobile bandwidth usage.

4. **Template markup issue in conference category cards**
   - Problem: Extra `>` in an image tag (`...loading="lazy">>`) may produce invalid HTML parsing behavior.
   - Fix: Removed the extra character and added decoding and dimensions.

5. **Logo image optimization hints**
   - Problem: Header/footer logo images lacked explicit dimensions/decoding hints.
   - Fix: Added width/height and decoding hints; header logo prioritized, footer logo lazy-loaded.

6. **Third-party CSS is high priority on mobile render path**
   - Problem: Google Fonts and Font Awesome were loaded with `preload` links, which can still contend for early network bandwidth on constrained mobile connections.
   - Fix: Switched both to non-blocking `media="print"` stylesheet loading with `onload` fallback to `media="all"`, while keeping `<noscript>` fallbacks.

## Additional recommendations (next pass)

- Convert Font Awesome CDN dependency to a reduced local icon subset (or inline SVGs for only used icons) to reduce third-party CSS cost.
- Consider self-hosting or reducing Google Font weights to cut font transfer size on mobile.
- Add explicit width/height across remaining large content images in gardens/dining templates where possible.
- Use responsive `srcset/sizes` for hero and gallery images.
- Evaluate preloading one likely LCP image on key landing pages.
