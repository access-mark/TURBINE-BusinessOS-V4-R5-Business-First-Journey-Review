# TURBINE BusinessOS | Search Growth Operating Plan

**Workstream:** WEB-01 / SEO-01  
**Revision:** V4-R4, 16 November 2026  
**Positioning:** One integrated BusinessOS for South African businesses  
**Classification:** Implementation and acquisition strategy, not an assertion of existing rankings  
**Current release status:** Review / NO-GO for public indexing until founder and production gates

## Executive objective

Make TURBINE discoverable to people who need a better business day, not just to people already searching for the phrase "business operating system". A gardener may search for quoting, scheduling or invoices. An estate agent may search for lead follow-up. A QSE owner may search for approvals, working capital and reporting. These are entry points into a connected operating story.

The goal is **qualified organic acquisition**: relevant impressions -> useful landing page -> engaged business journey -> qualified enquiry -> governed onboarding -> subscription when independently qualified. Rankings, impressions, leads and sales cannot be promised in advance.

## Source-backed search principles

The search architecture follows Google's Search Essentials, people-first content guidance, canonical and sitemap guidance, and structured-data requirements. Google states that inclusion in its AI features requires ordinary search eligibility, not special AI markup or `llms.txt`. See official guidance below. Bing IndexNow is a potential later integration, but needs domain control and verified submission facilities. No fake ratings, schema offers, generated doorway-page networks, purchased backlinks, keyword stuffing or automated mass submissions.

## R4 technical implementation

- **71 static HTML pages**, including 29 hand-curated occupation stories and 16 industry pages; 69 candidate canonical indexable pages after approval. The 404 page and JS-driven dynamic role shell remain `noindex` even in release mode.
- **780 roles** stay searchable in the occupation directory; the presence of a search listing does not by itself justify 780 separate search landing pages.
- Unique page-specific titles and descriptions; metadata is not truncated in the middle of a sentence.
- Canonical URLs, Open Graph and Twitter metadata, authentic screenshot preview image, `en-ZA` language targeting, preconnects, and explicit image dimensions.
- JSON-LD `WebPage` and `BreadcrumbList`, with `WebSite` and `Organization` on the homepage; curated `ItemList` on the occupation hub. No fabricated ratings, prices or product availability.
- Sitemap index split into `sitemap-core.xml` (24), `sitemap-industries.xml` (16), and `sitemap-occupations.xml` (29), so Google Search Console can assess sections separately.
- Accessible, real anchor links for chapter navigation, important top-level hubs and curated occupation pages.
- Zero `!important` in the current CSS, with responsive rules grouped by breakpoint and no horizontal clipping used to hide defects.
- In-memory telemetry events for page views, internal navigation, occupation search counts, role discovery, CTA intent, guide interactions and blocked enquiry attempts. **No network analytics tag is active**. The source never collects or forwards raw search queries, names, contact emails, form values or other personal details.
- Preview `noindex, follow` is intentionally retained. An isolated release generator prepares indexable pages only when given a genuine approved base URL and an explicit founder-acceptance flag.

## Site architecture and search intent clusters

| Cluster | User question | Primary destination |
|---|---|---|
| Connected BusinessOS | "How can I run the whole business from one place?" | `index.html`, `why-turbine.html`, `platform.html` |
| Business type and maturity | "What does a QSE or SME need?" | `business-types.html`, role-specific QSE pages |
| Occupation and daily work | "Does it work for people like me?" | `occupations.html`, curated `/roles/*.html` |
| Industry workflow | "How does the whole job work in my sector?" | `industries.html`, 16 `industry-XX.html` pages |
| Operations, CRM and finance | "How do quotations, work and payment connect?" | `capabilities.html`, `journeys.html` |
| Guided adoption and migration | "Can I actually move my data safely?" | `getting-started.html`, `migration.html`, `guide.html` |
| Trust, qualification, privacy | "Can I rely on the controls and is the product available?" | `security.html`, `command.html`, `faq.html`, `trial.html` |

## Content depth and authority standards

Each indexable page should have a unique **end in mind**, a recognizable real-world scene, five practical beliefs or decisions, explicit connected workflow steps, proof or substantiation appropriate to the product's qualification status, and a meaningful next action. A role page should not exist merely because its title differs from another role. New pages must pass editorial review for genuine useful differentiation.

For new occupation pages, require: 1) independently grounded search demand or first-party search impressions, 2) at least one distinct workflow and situational example, 3) meaningful internal links, 4) no product claims beyond approved capability evidence, 5) an identified next-step path. Keep the remaining 780 role names in the search experience unless individually qualified for editorial expansion.

Product screenshots are development/qualification evidence with synthetic records. Never describe them as proof of unrestricted production availability.

## South African search positioning

Write in clear South African business language: sole proprietor, one-person business, QSE, SME, quotation, bakkie, job card, supplier, working capital, debtor, collection, VAT and teams, where context supports it. Do not assume all visitors are technology buyers. Industry-specific vocabulary should serve the reader, not be repeated as keywords. QSE is a B-BBEE turnover classification under the generic codes, not a universal enterprise-size segment; sector codes may use different thresholds.

Suggested editorial demand angles, **without invented volume estimates**:

1. How a solo garden service can keep bookings, repeat clients, quotations and invoices together.
2. A property agent's week from first enquiry to viewing follow-up and offer.
3. The end-to-end working capital journey for a growing QSE.
4. The true difference between a CRM, an accounting system and a complete operating environment.
5. From customer order to purchase order, stock receipt and invoice for a small manufacturer.
6. Importing contacts, opportunities and accounting records without breaking customer history.
7. What to ask before replacing spreadsheets with an integrated BusinessOS.
8. Business process handoffs and approval limits for a multi-team enterprise.

## Organic growth distribution plan

**First 30 days after approved launch:** claim and verify the final canonical domain; submit the validated XML sitemap in Google Search Console and Bing Webmaster Tools; implement analytics with approved consent; perform URL inspection and index coverage sampling on hub, industry and role pages; publish a small set of substantial "problem to outcome" explainers grounded in genuine workflows.

**Days 31-60:** use Search Console queries and landing-page engagement to identify 10-15 real demand clusters. Improve pages visitors land on but do not engage with. Develop verified demonstrations, screenshots, technical explanations and practitioner interviews where permitted. Engage legitimate South African business communities, professional bodies and implementation partners where content genuinely helps their members.

**Days 61-90:** deepen the best-performing occupation and industry clusters; publish approved evidence-led case studies and migration guides; build accessible calculators or checklists where useful; evaluate backlinks and referrals from earned, relevant publications and partnerships; reassess coverage, engagement, conversion and qualification gates. Do not manufacture reviews, backlinks or citations.

## Performance and technical quality

- Prioritize real Core Web Vitals (LCP, CLS, INP) measured in PageSpeed Insights / CrUX and approved analytics after deployment. Automated layout tests alone do not establish real-world performance.
- Preserve authentic screenshots, specify image intrinsic sizes, lazy-load genuinely below-the-fold images and prioritize the actual visible hero.
- Keep CSS maintainable, low-specificity and testable; no blanket `min-width:0`, hidden global overflow or `!important` workaround chains.
- Make the site keyboard and screen-reader usable; review 200% browser zoom physically.
- Maintain one canonical origin and one final site address. The historical GitHub Pages repo path is a provisional preview path, **not a long-term custom domain decision**.

## Indexability, robots and canonical domain

**Important GitHub Pages detail:** `robots.txt` applies from the host root (`https://access-mark.github.io/robots.txt`), not from a project subdirectory. The file included in this ZIP is the correct template for a later dedicated domain or root-level deployment, but the project-path copy alone cannot override the host's root robots policy. On a GitHub Pages project, Google must be shown the actual sitemap URL through Search Console.

**Do not publish this preview ZIP with the expectation of indexing:** preview pages deliberately carry `noindex`. The `tools/prepare_release.py` script generates an isolated release only when provided the final canonical `--base-url`, `--mode release`, and `--founder-accepted` after approval. A new repository path or custom domain requires regenerating canonical, OG URLs and all sitemaps; copying the ZIP without that step risks wrong canonical targets.

Do not index the dynamic `occupation.html?role=...` shell. Curated static `/roles/` pages are the crawlable entry points. Avoid faceted search URL indexing (`?q=`, `?group=`, `?stage=`); canonicalize them to `occupations.html`.

## Measurement architecture: tracking that leads to decisions

The funnel should be instrumented with the following **future approved integrations**:

- **Google Search Console:** impressions, clicks, CTR, average position, page index coverage, queries by canonical page and sitemap cluster.
- **Bing Webmaster Tools:** indexing and query visibility outside Google. IndexNow only when verified and supported by hosting/domain facilities.
- **GA4 / GTM or approved alternative:** search landing pages, engaged sessions, occupation discovery, industry navigation, enquiry CTA intent and qualified conversions, subject to South African privacy requirements and actual visitor consent.
- **Verified lead delivery:** only a confirmed back-end delivery event counts as `generate_lead` or a business conversion. A blocked form, mailto draft or CTA click is not a lead.
- **CRM attribution when available:** original channel, landing page, referrer, occupation/industry page, first enquiry and qualified pipeline outcome. Keep consent, retention and privacy rules explicit.
- **Edge or hosting traffic logs:** bot and crawler diagnostics require a hosting/CDN layer that exposes those records. GitHub Pages alone does not provide full raw bot-log analytics.

Use a small executive measurement view: organic clicks, qualified organic enquiries, lead-to-opportunity rate, conversion by topic cluster, organic-sourced pipeline, top technical exclusions, top growing pages and 30/90-day trends. No invented traffic forecasts or keyword volumes.

## External tags and consent gate

R4 includes `telemetry.js` for local, non-PII event validation only. Do not paste a Google tag, Meta pixel or arbitrary tracking script without an approved measurement property, lawful consent mechanism and review of data processing. Use a consent framework appropriate to the site's audiences and applicable law. If Google Consent Mode is adopted, follow the official consent v2 defaults and update semantics. The site must not transmit enquiry fields before submission and must not claim lead delivery without verified endpoints.

## Search launch gates

1. Founder accepts public product claims and final visual behavior.
2. Canonical public domain and URL plan approved, including redirects if replacing earlier sites.
3. Legal company identity and privacy notice approved.
4. Enquiry form has an approved, verified delivery path and retention policy.
5. Real 200% browser zoom, keyboard/screen-reader, color contrast and mobile acceptance completed.
6. Production qualification evidence reconciled to published capability claims.
7. Search Console / Bing properties verified, sitemaps submitted and URL Inspection shows indexability.
8. Approved consent and measurement implementation tested with consent accepted, declined and revoked.
9. Physical hosted performance, response codes, canonical and robots behavior tested.
10. Only then change review `noindex` to production `index, follow` using the release script.

## Sources (authoritative, checked 16 November 2026)

- Google Search Essentials: https://developers.google.com/search/docs/essentials
- Google SEO Starter Guide: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Google Sitemaps: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- Google Breadcrumb markup: https://developers.google.com/search/docs/appearance/structured-data/breadcrumb
- Google Organization markup: https://developers.google.com/search/docs/appearance/structured-data/organization
- Google AI Search guidance: https://developers.google.com/search/docs/appearance/ai-features
- Google Consent Mode: https://developers.google.com/tag-platform/security/guides/consent
- Bing IndexNow: https://www2.bing.com/indexnow/getstarted
- South African B-BBEE Commission QSE: https://www.bbbeecommission.co.za/frequently-asked-questions/how-is-b-bbee-classification-determined/


## V4-R5 addition: Business-first search-to-conversion journey

The primary landing experience asks how the visitor runs a business rather than assuming an occupation. The optional occupational directory remains searchable and has static curated role pages where there is differentiated editorial content. When measurement is approved, distinguish landing-page intent, business-stage selections, priority selection, guided-story completion and a confirmed qualified enquiry. Do not send a person's name, contact details, free-text search, form values or business-specific secrets to analytics. All preview pages stay noindex until the production SEO activation gate is accepted.
