# Golden Crest Commercial Janitorial and Facility Care

**Status:** Pre-formation business project
**Working name:** Golden Crest
**Founders:** Miesha and Kimberly
**Location:** Mount Holly, North Carolina
**Initial service lane:** Commercial janitorial and facility care
**Primary NAICS alignment:** `561720`
**Primary PSC alignment:** `S201`

## Project boundary

Golden Crest is a separate potential business for Miesha and Kimberly. It is not part of LeadCurate's property-data business. The repository is the shared source for the business plan, landing page, capability profile, visual assets, and future government-contracting setup.

## Files

- `AGENTS.md`: mandatory project boundaries and verification rules for Claude, Codex, and Hermes.
- `CERTIFICATION_ROADMAP.md`: plain-language registration, WOSB, EDWOSB, NCSBE, SBE, WBENC, NMSDC, operating-agreement, and secure photo-intake roadmap.
- `index.html`: procurement-first landing page. Written for public, institutional, and prime-contractor buyers rather than consumer cleaning search traffic.
- `capability-statement.html`: printable pre-registration capability profile.
- `Golden-Crest-Capability-Profile-DRAFT.pdf`: verified one-page draft PDF generated from the printable profile.
- `master_business_and_contracting_plan.md`: corrected launch and procurement plan with official sources.
- `capability_statement_and_website_copy.md`: controlled capability and copy source.
- `assets/golden-crest-facilities-hero.png`: original representative hero artwork generated for the project.

## Website structure (do not revert without discussion)

Two pages, one shared stylesheet and script.

**`index.html` - the customer-facing site.** Hero, services, facilities served, how we work, a slim band linking to the government page, and a quote request form with photo upload. Business-plan content does not belong here: no procurement strategy, no contracting thresholds, no certification roadmap, no founder biographies, no competitive positioning.

**`government.html` - the capability and vendor page.** Vendor data table (legal name, NAICS 561720 / 561790, PSC S201, UEI, CAGE, SAM status, EIN, place of performance), core capabilities and exclusions, documents we provide, buyer forms we complete and return, and registration/certification status. This is the page an APEX counselor, contracting officer, or prime's supplier-diversity manager is sent to.

Identifiers not yet issued are shown as `XXXXXXXXXXXX` placeholders so the layout reads as a finished vendor page. They are marked as placeholders in the page footer. Replace them with real values only after issuance; never substitute a plausible-looking fake identifier.

**Shared assets.** `assets/site.css` and `assets/site.js` are loaded by both pages with a `?v=N` cache-busting query. Bump `N` in both HTML files whenever either asset changes, or deployed browsers will serve stale copies.

**Contact configuration.** The `CONTACT` object at the top of the inline script in `index.html` is the only place contact details live. While `CONTACT_EMAIL` and `INQUIRY_ENDPOINT` are both empty, the quote form stays visible but its submit button is disabled and a short notice explains that nothing is transmitted. Fill in the endpoint and the form goes live, uploads included.

**Photo upload.** Native multi-file input with drag-and-drop, per-file removal, 8-file and 25 MB limits, sent as multipart when an endpoint exists. It never asks for door codes, alarm codes, keycard details, or floor plans. This implements the workflow in `CERTIFICATION_ROADMAP.md` section 7.

**Discoverability.** `robots.txt`, `sitemap.xml`, `llms.txt`, canonical URLs, Open Graph tags, and `ProfessionalService` JSON-LD on both pages. Update the absolute URLs in all of these together if the domain changes.

## Note on PREMIUM_REDESIGN_AUDIT.md

That document predates this build and conflicts with `CERTIFICATION_ROADMAP.md` in one place. The audit says to remove the photo-assisted intake entirely; roadmap section 7 says to build it properly as a real workflow. The roadmap is correct. The genuine defect in the original page was that it solicited alarm codes, keycard details, and lockbox information, and that the control was non-functional - not the photo upload itself. Read the audit as historical findings, not as a current specification.

## Current truth

The company is not yet formed, insured, bonded, registered in SAM, assigned a UEI or CAGE, or certified as WOSB, EDWOSB, WBE, MBE, MWBE, HUB, or SBE. The website and capability statement intentionally label these items pending.

## Recommended launch order

1. Founders approve the name, ownership, duties, capital, and deadlock plan.
2. Review current-employer conflict and outside-business rules.
3. Validate one narrow janitorial service lane and price a real facility.
4. Form the company, open banking, and bind appropriate insurance.
5. Start the no-cost APEX or NC SBTDC Government Contracting Assistance Program intake.
6. Build a named-account pipeline of agencies, institutions, prime contractors, and facility buyers.
7. Register in local and state vendor systems.
8. Complete SAM, UEI, CAGE, and SBA certification work only with matching legal records.
9. Pursue small RFQs, sources-sought notices, subcontracting, and suitable public opportunities.

## Preview

Open `index.html` locally. The page is suitable for design and strategy review, but public launch should wait until the final legal name, business contact information, formation, insurance, and approved credentials are added.
