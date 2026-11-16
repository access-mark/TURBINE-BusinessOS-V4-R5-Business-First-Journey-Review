# TURBINE BusinessOS | WEB-01 V4-R5

**Classification:** business-first narrative and guided visitor experience.  
**Status:** CONTROLLED REVIEW ONLY. NOT PRODUCTION RELEASE ACCEPTED.  
**Baseline:** Original V4 visual identity; V4-R4 source, responsive CSS, occupation search and technical SEO retained.

## What is new

- A revised homepage, with **Start with my business** leading directly to five neutral operating situations.
- New `my-business.html` guided working-day page: starting out, working alone, small team, growing company and enterprise. None implies a specific occupation.
- Visitors can choose customers, work, money or people as their main priority and move to a relevant capability.
- All website guide panels now use business situations first; occupation search remains an optional next step.
- Plain-English narrative improvements on why, capabilities, business types, getting started and occupations pages.
- Context-sensitive page endings with a clear next step, instead of a repeated generic conclusion.
- Original 780-role directory, 29 curated role stories, 16 industries, 12 capabilities, QSE explanation, authentic product screenshots, DataPort, TURBINE Command and dark/light themes retained.
- New non-identifying in-memory events `business_stage_select` and `business_focus_select`. **No analytics data is transmitted externally.**

## Use

Deploy the **contents** of this ZIP to an isolated test repository or a local web server. Leave this build as a review preview; it has `noindex, follow` across every HTML page. The metadata preview base path is `https://access-mark.github.io/TURBINE-BusinessOS-V4-R5-Business-First-Journey-Review/`; if the actual preview uses a different address, regenerate the metadata first.

A deterministic metadata/sitemap preparer remains in `tools/prepare_release.py`. It does not publish or provision anything. For a different preview URL, run:

```bash
python tools/prepare_release.py --source . --output ../turbine-preview-output --base-url https://YOUR-PREVIEW-URL/ --mode preview
```

**Do not run release mode without founder acceptance and closure of release gates.** This remains a static marketing and education website; the enquiry form has no approved lead delivery destination. No automatic trial provisioning, payment collection or production subscription is operational here.

## Verification

See `WEB01_R5_QA_AND_RELEASE_GATES.md`. Local Chromium rendering tested 72 HTML pages at 7 viewport widths and both themes; 20 interaction checks passed. This is not native 200% browser zoom, public hosted inspection, screen-reader qualification or production acceptance.

## Source and governance

- Original accepted V4 source: Git `876ec9962b290dc8745ef8c044beadb9e0d6995a`.
- R4 review website source supplied in `TURBINE-BusinessOS-V4-R4-Navigation-SEO-Review.zip`.
- No original V4, R3 or R4 GitHub repository has been modified.
- CP12 technical delivery, TURBINE Command, entitlement, financial and legal decisions remain outside WEB-01 authority.
