# WEB-01 V4-R4 Release Gates

**Status: REVIEW / NOT RELEASE ACCEPTED**  
**Source:** V4-R3 published snapshot; changes restricted to navigation, CSS hygiene, crawlability, curated occupation stories, technical SEO and privacy-safe instrumentation.

| Gate | Status | Evidence / blocker |
|---|---|---|
| V4 layout and narrative retained | VERIFIED in source | No redesign of existing content sections |
| CSS `!important` | PASS | Zero declarations; prior four removed |
| CSS duplicate top-level selectors | PASS | Rules consolidated to single selector per base scope |
| Desktop and section navigation | PASS offline | Active underline and responsive chapter disclosure |
| Images and static links | PASS source | 295 image instances, 3725 internal link references, no unresolved paths |
| Offline reflow and themes | PASS offline | 539 layout checks, no detected overflow |
| Browser interactions | PASS offline | Navigation, guide, occupation search, safe form behavior |
| Technical metadata | PASS source | 71 unique titles and descriptions; valid JSON-LD |
| Canonical sitemap structure | PASS build | Core 24 + industries 16 + occupations 29 |
| Controlled release generation | PASS dry run | 69 release-indexable pages + 2 noindex exclusions |
| Native 200% browser zoom | UNTESTED | Reflow proxy is not equivalent to native zoom acceptance |
| Production lead delivery | BLOCKED | No approved destination; no form conversion claims |
| Live Search Console / Bing data | BLOCKED | Properties unverified here; no indexing measurements established |
| Consent and external analytics | BLOCKED | Event hooks only; no external tracking SDK or measurement IDs |
| Independent technical capability qualification | BLOCKED | CP12 governance controls product claims |
| Legal and public launch approval | BLOCKED | Founder acceptance and company/legal validation required |
| Public deployment | NOT DONE | No repository modified in this workstream |

**Release decision:** GO for founder review and further host verification, NO-GO for public indexable deployment until gates close.
