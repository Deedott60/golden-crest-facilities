# Golden Crest Agent Instructions

Shared working folder for every agent on this project — Claude, Codex, and Hermes (Danny).

**Locations**
- GitHub: `https://github.com/Deedott60/golden-crest-facilities` — source of truth
- VPS: `/root/golden-crest-facilities` — Danny's working copy
- Live site: `https://golden-crest.76-13-25-117.sslip.io/` — served from `/var/www/golden-crest-preview`

**Before starting work:** `git pull`. **After committing:** `git push`, and tell Derrick if the live site needs redeploying. Do not let the VPS copy drift — it sat six commits behind for three weeks and Danny was reading a stale plan.

## Start here

1. `README.md` — website structure and what must not go back on the public pages
2. `docs/startup-checklist.html` — the operating plan, in dependency order
3. `docs/government-contracting-track.html` — the reasoning behind that plan
4. `master_business_and_contracting_plan.md` — background (see corrections below)
5. `CERTIFICATION_ROADMAP.md` — background (see corrections below)

## Project boundary

Golden Crest is a separate business for its two founders. It is not a LeadCurate product. Do not mix customer data, branding, credentials, or infrastructure between the businesses without Derrick's explicit approval.

## Current state — nothing below is in place yet

- Not formed. "Golden Crest Facilities" is a working name.
- No monitored business email or phone. The website's quote form is deliberately disabled until one exists.
- No SAM registration, UEI, CAGE, EIN, insurance, or certification of any kind.
- No past performance under this company.
- Founder work experience is individual history, not company past performance.

## Hard rules

- Never display a credential, registration, certification, policy limit, client, contract, revenue, facility size, response guarantee, or technology feature without current evidence.
- Never invent a plausible-looking identifier. Unissued numbers appear as `XXXXXXXXXXXX` placeholders and are disclosed as placeholders.
- **Do not publish the founders' names.** They were removed from the public site, the capability statement, and the LeadCurate dashboard on 2026-08-31. `leadcurate.com/command/` is unauthenticated — anything written there is public.
- Do not claim medical-grade, infection-control, or clinical sanitation capability.
- Do not use government seals, flags, agency logos, certification marks, client logos, or employer names.
- Do not create fake forms, dead controls, phone numbers, email addresses, testimonials, case studies, or past performance.
- The hero image is representative artwork. It carries a visible caption and a footer disclosure. Replace with real photography before public launch.
- Business-plan content does not belong on the public website. Strategy, thresholds, certification roadmaps, competitive positioning, and founder biographies live in these markdown and docs files only.

## Strategy — corrected 2026-09-19

The earlier plan treated federal contracting as the starting revenue. It is not. **Government contracting is the moat; private commercial accounts are the first revenue.** The revised order is in `docs/startup-checklist.html`.

Three findings the original plan missed entirely. Verify before contradicting any of them:

1. **AbilityOne caps the federal opportunity.** Much federal custodial work is a mandatory source reserved for nonprofits employing people who are blind or severely disabled, awarded without competition. No certification overrides it.
2. **Service Contract Act sets wages on federal work** — the DOL county wage determination plus a health & welfare fringe of **$5.92/hour** as of August 2026. It flows down to subcontractors. Never price federal or prime-subcontract work at a commercial rate.
3. **Payment is 30–60 days.** With no employees yet this is not a payroll crisis, but it means working a month or two before the first check.

## Verified facts as of 2026-09-19

Re-verify anything load-bearing before relying on it; these move.

- **NAICS 561720** (Janitorial Services) is on SBA's eligible list under the **EDWOSB** designation — the restricted tier. Plain WOSB does not open cleaning set-asides; EDWOSB does.
- **WOSB / EDWOSB is one free application, not two choices.** EDWOSB is the higher tier and includes WOSB status. EDWOSB adds personal financial tests: net worth under $850,000, three-year average AGI $400,000 or less, total assets $6.5M or less.
- **The WOSB program is intact and active**, with a governmentwide goal of 5% of contracting dollars.
- **8(a) changed on 2026-09-10.** SBA eliminated the rebuttable presumption of social disadvantage based on race; applicants must now show evidence of group discrimination and personal material harm, and SBA has told staff to stop relying on written "social disadvantage narratives." **Do not cite pre-September-2026 guidance on 8(a).**
- **NC HUB was eliminated 2026-07-07.** HUB certifications are no longer recognized on state contracts. NCSBE replaced it and is race- and gender-neutral.
- Micro-purchase threshold generally **$15,000**; **$2,500** for Service Contract Labor Standards-covered services. Simplified acquisition threshold **$350,000**. Subcontracting plan threshold roughly **$750,000**.
- Federal reps and certifications are completed **inside SAM.gov**, not sent as a separate document.
- Gaston County Schools registers vendors through **Public Purchase** plus its own packet. Gaston College requires an **NC eVP** vendor number.
- SAM registration, UEI, CAGE, and all SBA certifications are **free**. Anyone charging is selling nothing.

## Known conflict in the older documents

`PREMIUM_REDESIGN_AUDIT.md` says remove the photo intake entirely. `CERTIFICATION_ROADMAP.md` §7 says build it properly as a real workflow. **The roadmap is correct.** The real defect was that the original form solicited alarm codes, keycard details, and lockbox information through a control that did nothing. Treat the audit as historical findings, not a current specification.

## Design direction

Restrained and institutional: warm white, deep ink, **teal accent** (`--teal: #11776e`), clear grid, IBM Plex typography, soft cards rather than hard bordered grids. **No gold or brass** — Derrick rejected it explicitly on 2026-08-31 despite the company name. Premium means specific and verifiable, not decorated.

Shared assets are `assets/site.css` and `assets/site.js`, loaded by both pages with a `?v=N` query. **Bump `N` in both HTML files whenever either asset changes** or deployed browsers serve stale copies.

## Verification before committing

- `git diff --check`
- Parse local links and image sources; confirm no dead anchors
- Confirm no horizontal overflow at 375px and 1280px
- Confirm the capability PDF remains one letter-size page
- Scan customer-facing copy for unsupported credentials, guarantees, and founder names
- Confirm contrast on any new button or badge — a nav button shipped dark-on-dark once

## Deploying the live site

Static files copied to the VPS:

```
scp index.html government.html capability-statement.html robots.txt sitemap.xml llms.txt \
    Golden-Crest-Capability-Profile-DRAFT.pdf leadcurate-vps:/var/www/golden-crest-preview/
scp assets/site.css assets/site.js assets/golden-crest-facilities-hero.png \
    leadcurate-vps:/var/www/golden-crest-preview/assets/
```

nginx sends `Cache-Control: no-cache, must-revalidate` on HTML so updates are never served stale. The server also sends `X-Robots-Tag: noindex` — it is a private preview. **Removing that header is a deliberate launch decision, not a cleanup task.**
