# TURBINE BusinessOS | WEB-01-R2 Qualification Evidence

**Build:** V4-R2-REVIEW-CANDIDATE | **Date:** 16 November 2026

**Decision:** OFFLINE SOURCE / LAYOUT ACCEPTED FOR FOUNDER VISUAL REVIEW. PUBLIC RELEASE NOT ACCEPTED.

## Source integrity
- **40 HTML pages**, including a dedicated 404 page, and **10 authentic original PNG assets** retained under `assets/`.
- **2,115** `href`/`src` attributes inspected across all HTML pages; **0 unresolved internal paths or anchors**.
- **220** references to original PNG assets; their bytes match the original V4 asset set.
- **39** sitemap content-page entries, each with the currently approved Original V4 GitHub Pages prefix as a provisional address.
- CSS parsed with `tinycss2`: **0 syntax errors**. JavaScript passed `node --check`.
- Review safeguards: all pages `noindex, nofollow`; `robots.txt` disallows crawlers.

## Browser preflight
- Chromium rendered the authentic HTML/CSS/JavaScript and all 10 PNG assets through in-memory source embedding because HTTP and `file:` navigation were restricted by this environment.
- **560 cases:** 40 pages × 7 viewport widths × dark/light themes.
- Widths: 320, 375, 390, 720, 768, 1024 and 1440 CSS px.
- **0 detected viewport overflows, unqualified clipping issues, broken decoded PNG images or uncaught JavaScript exceptions** in the automated source-render tests.
- Screenshots were manually inspected at desktop, tablet and phone widths, including mid-page workflow content.

## Functional source smoke checks
- Mobile menu opens: **PASS**.
- Escape closes menu and returns focus: **PASS**.
- Theme button changes current theme: **PASS**.
- Trial enquiry form reports that no lead was sent: **PASS**.
- Contact enquiry form reports that no lead was sent: **PASS**.

## Critical limits (do not misreport as passes)
- **UNTESTED:** True desktop browser 200% zoom. The 720px viewport was a reflow proxy, not a zoom qualification.
- **UNTESTED:** Publicly hosted HTTP 200/404 behavior, actual asset/font delivery, CSP/security headers, caching and cross-browser interoperability. A real hosted browser run is still mandatory.
- **UNTESTED:** Independent manual screen-reader audit, physical iOS/Android, full WCAG contrast and keyboard journey across all pages.
- **BLOCKED:** No approved enquiry mailbox or secure lead endpoint. Contact and trial forms do not transmit data or create trial tenants.
- **BLOCKED:** Commercial/product release claims must be reconciled with governing programme acceptance evidence; final domain and legal identity must be approved.
- **NOT ACCEPTED:** Founder has not accepted this build for publication. Neither public GitHub repository was modified.

### Environment disclosure
Browser automation used the local CSS with the `@import` external Google Font line omitted (network access restricted), so screenshots show browser font fallback. The deployed version will use the original V4 font import only if the approved hosting environment can fetch it successfully. This is not an external-font delivery test.
