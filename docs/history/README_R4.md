# TURBINE BusinessOS V4-R4 | Narrative, navigation and SEO review

This is the V4-derived review candidate. It preserves the approved visual identity, the existing detailed content and authentic image assets. It consolidates legacy CSS and improves navigation without replacing the site design.

## Contents

- 71 HTML files, including 29 curated crawlable occupation stories.
- 16 original detailed industry pages, 780 searchable occupations.
- `styles.css` with zero `!important` and a consolidated responsive cascade.
- Cyan active underline on the top navigation, accessible responsive chapter navigation.
- `telemetry.js` safe event instrumentation, no external transmission.
- Page-specific metadata, social cards, JSON-LD, canonical URLs and 3-category sitemap index.
- `tools/prepare_release.py` to generate an isolated indexable build after founder acceptance.
- `SEO_MASTER_EXECUTION_PLAN.md`, `WEB01_R4_RELEASE_GATES.md`, `SEO_QUERY_MAP.csv` and QA evidence.

## Critical: preview indexing stays blocked

The ZIP remains **noindex**. That is deliberate because product-claim acceptance, public domain, lead delivery, legal terms and analytics consent gates remain open. The Search Console and Bing submissions have not been performed.

The preview metadata assumes the known R3 GitHub Pages address solely for reproducible source QA. For a different final URL, regenerate canonical tags and sitemaps. Never upload a preview package expecting it to be indexed.

After launch gates are independently closed and the founder has accepted publication:

```bash
python tools/prepare_release.py --source . --output ../turbine-approved-release --base-url https://YOUR-APPROVED-DOMAIN/ --mode release --founder-accepted
```

This command does not deploy anything. It produces a reviewable output folder. The accepted final domain must be an actual HTTPS origin you control, and must end with a slash. Confirm HTTPS host redirects, actual `robots.txt` at the host root, live canonical URLs and search-index eligibility before publishing.

Do not overwrite either the R3 or original V4 GitHub repository without explicit founder instruction.
