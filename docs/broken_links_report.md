# Broken Links Audit (Desktop + Mobile)

Date: 2026-02-12

## Scope and method

- Crawled the Django app with both desktop and mobile user agents using Django's test client.
- Checked all discoverable internal page links (`href`) and internal static/media assets (`src`) for HTTP 4xx/5xx responses.
- Performed a template-level scan of all HTML files for external URLs and validated URL formatting where possible.

## Broken links found

### 1) WhatsApp social link uses an invalid `wa.me` format

- **Link:** `https://wa.me/+254112394681`
- **Location:** shared footer social links in `templates/base.html`
- **Why broken:** `wa.me` links must not include a `+` character. The expected format is `https://wa.me/254112394681`.
- **Impact:** appears in both desktop and mobile experiences because the same base template renders both layouts.

## No broken internal links detected

- Internal route crawl found no pages returning HTTP 4xx/5xx.
- Internal static/media asset checks found no missing files returning HTTP 4xx/5xx.

## Notes

- External network checks to third-party domains are restricted in this environment, so non-format-based external link validity could not be fully verified.
