# TURBINE BusinessOS V4-R3 Narrative Review Candidate

**Date:** 16 November 2026  
**Classification:** read-only review ZIP; production release remains NO-GO.  
**Authority:** V4's design language, 10 logo/screenshot assets, existing product positioning and governing technical gates.

## What changed

- All 42 HTML pages carry an end-in-mind destination and five tailored beliefs; new capability copy starts with a recognisable problem instead of module jargon.
- All 12 capability chapters explain practical outcomes, show examples at four business scales, list five workflow steps, then retain source scope in expandable details.
- Each of 16 industry pages replaces repeated generic paragraphs and a literal `{esc(journey)}` source bug with a specific story and nine illustrated (text) operating steps.
- Home page introduces solo service, estate agency, QSE and enterprise routes.
- Searchable **Who it is for** directory contains **780 curated occupation names** in **17 groups**, with aliases, industry links and stage context.
- Each role has a shareable dynamic profile at `occupation.html?role=<slug>`; examples include `gardener`, `estate-agent`, `plumber` and `qse-business-owner`. The source is `occupations-data.json` / `occupations-directory.csv` and the runtime data is `occupations-data.js`.
- Business-size section covers sole proprietors, microbusinesses, SMEs, QSEs, medium businesses and large enterprises, carefully distinguishing B-BBEE QSE from Small Enterprise Act business-size categories.
- Every page includes a non-modal website **Guide me** journey assistant. This is website navigation, not an operational TURBINE Guide product agent.

## How to review

1. Extract the ZIP *with folders preserved*. Open `index.html` in a local static server, or upload its contents to an isolated non-production static host.
2. Use `occupations.html` to search for a role; aliases such as `realtor` also work. Open a role profile, then follow its industry and journey links.
3. Use `business-types.html#qse-business` for QSE-specific context; the generic B-BBEE QSE turnover thresholds are not automatically the size thresholds under the National Small Enterprise Act or every sector B-BBEE code.
4. Test both themes and mobile navigation. The published site is **not** a live enquiry or trial service.
5. Review `WEB01_R3_RELEASE_GATES.md` and the separately delivered QA document before any acceptance or deployment decision.

## Content and technical boundaries

- No live lead submission destination, provisioning endpoint, subscription checkout or price has been invented.
- The screenshots are authentic development/qualification images containing synthetic records, not evidence of production release.
- `robots.txt` disallows crawling and every HTML page is `noindex` **for this review package**. Production search visibility requires formal approval and updated canonical sitemap.
- Static HTML/CSS/JS: no build step or external runtime frameworks. One Google Fonts stylesheet is the only optional third-party visual dependency; the offline test used system fallback fonts.
- The directory is curated, broad and extensible; **780 is not literally every occupation**. Specialist suitability is subject to capability and regulatory qualification.
- Do not overwrite either original V4 or failed repair GitHub repositories without explicit instruction.
