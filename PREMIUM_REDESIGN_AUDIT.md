# Golden Crest Landing Page Audit & Premium Redesign Brief

## Executive direction

The current page looks polished at first glance but presents a mature, certified, technology-enabled contractor that does not yet exist operationally. For commercial facility buyers and contracting officers, that is a larger credibility problem than an unfinished visual design.

The redesign should position Golden Crest as a **founder-led commercial janitorial company built on real casino/resort hospitality operations experience**—not as a compliance-tech platform or certified government contractor. Premium should come from restraint, clear scope, real people, documented processes, and accurate procurement data.

**Launch principle:** publish only what Golden Crest can prove, perform, receive, or respond to today.

---

## 1. Critical audit findings

### A. Launch blockers: remove or hold until documented

| Current claim or feature | Problem | Launch-safe treatment |
|---|---|---|
| “WOSB / WBE,” “100% Woman-Owned Enterprise,” “WOSB eligible,” “MWBE,” “MBE,” “set-aside ready” | The business is not formed, registered, or certified. Ownership facts do not equal third-party certification. “Eligible” is also a determination Golden Crest should not imply it has received. | Remove certification acronyms and badges. After formation, “Women-owned” may be used as a factual ownership statement if legally accurate. Add WOSB/WBE/MBE only after approval and retain proof. |
| “Licensed & Insured,” “fully insured,” “bonded,” “$2,000,000 policy” | Unsupported without active policies and any jurisdiction-specific licenses. | Remove. Add exact coverage only after the policy is bound; state limits accurately and provide a certificate of insurance on request. Do not imply a general janitorial “license” unless one is actually required and held. |
| “SAM.gov registered,” “CAGE active,” UEI/DUNS “available upon request,” “GPC ready” | No entity registration or payment infrastructure exists. DUNS is also not the current federal entity identifier. | Hide the procurement credential block until SAM registration is active. Then show legal name, UEI, CAGE, SAM status/renewal, accepted payment methods, and exact codes. |
| “Background-cleared” or “background-screened staffing” | No screening program, criteria, vendor, or active workforce is established. “Cleared” can imply a government security clearance. | Remove. Once implemented, say “Personnel are screened under our written hiring policy” and describe the checks accurately. Reserve “security clearance” for actual adjudicated clearances. |
| “Fully compliant with federal and local procurement standards,” “100% compliant,” “strict security compliance” | Blanket compliance cannot be substantiated and varies by solicitation, site, and contract. | Replace with “We review and respond to the requirements of each facility and solicitation.” Name a specific standard only when the process demonstrably meets it. |
| CleanVerify™, SpaceScan™, SecureKey™, FacilityHub™, tamper-proof QR logs, digital chain of custody, encrypted tracking, live client portal, automated photo quote | These products and controls are unbuilt. Trademark styling makes concepts look operational. “Tamper-proof” and “encrypted” are security claims needing technical evidence. | Remove from launch. Describe only the actual quality-control workflow. If a simple timestamped checklist is implemented, call it a “service log,” not proprietary technology. Introduce product names only after a working product, privacy review, and customer validation. |
| Two-hour assessment, quote, response, or issue resolution | Repeated inconsistently, while the process also says 24 hours. No staffing or service-level system supports it. | Use one realistic, narrow commitment, e.g. “We respond to new inquiries within one business day,” only after the team can meet and measure it. Proposal timing follows the walkthrough and scope. |
| “30-day risk-free trial,” “month-to-month,” “zero lock-in,” “flat price” | These are contractual/commercial promises with no established terms. | Remove until pricing, cancellation, exclusions, and service agreements exist. Use “Terms are defined in each proposal.” |
| “Health-compliance certified,” “hospitality trained,” “hospital disinfectants,” “clinic-grade,” “zero cross-contamination,” “flawless compliance records” | These overstate personal credentials or imply healthcare/environmental outcomes. ServSafe is food-safety training, not a janitorial or medical sanitation certification. | Attribute verified experience precisely: “Founders bring leadership experience from high-volume casino and resort hospitality operations.” Mention active ServSafe credentials only by holder, credential, and valid status—and explain relevance without implying medical certification. Use “EPA-registered disinfectants used according to label directions” only when operationally true. |
| “15+ years,” “50,000+ sq. ft.,” “zero-failure inspections,” “every contract founder-inspected” | Unsupported or not yet documented as company performance. Prior employment experience is not Golden Crest past performance. | Verify dates and scope. Label it “founder experience,” never company past performance. Obtain permission before naming employers or using their brands. |
| Competitor claims such as “unscreened rotating subcontractors,” “single mop,” and “lowest bidder” | Sweeping, adversarial, and unsupported. It makes a new vendor sound less credible. | Replace the comparison matrix with Golden Crest’s own documented service standards and buyer-facing deliverables. |
| “Official capability statement” and “corporate capability statement” | The draft contains false certifications and placeholder identifiers. | Do not publish/download until legal name, contact data, capability scope, codes, insurance, and registrations are accurate. Mark internal drafts clearly. |

### B. Functional and content defects in `index.html`

- The hero displays Markdown asterisks literally around “tamper-proof…” and “digital chain-of-custody.”
- The intake form is nonfunctional: it has no action or submission integration, and its button is `type="button"`.
- The photo/solicitation upload area is a styled `div`, not a file input or accessible control; no document is uploaded.
- Commercial/government tabs have no JavaScript or semantic tab behavior and do not change the form.
- Facility-access “options” are static `div`s, not controls. Soliciting alarm, keycard, or lockbox details on an unsecured/unbuilt form is a security risk.
- The “2-hour” promise conflicts with “proposal delivered in 24 hours.”
- The header hides navigation on mobile but provides no mobile menu.
- Several two-column form rows remain two columns on the narrowest screens.
- The top bar and long CTA compete with the logo in a small mobile viewport.
- Footer phone is a placeholder, and the email/domain naming is inconsistent across files.
- The page offers no privacy notice despite proposing collection of contact information, facility photos, floor plans, solicitations, and access preferences.
- Emoji serve as interface icons without consistent accessible treatment.
- The animated ping and ambient motion do not respect `prefers-reduced-motion`.
- Labels lack explicit `for`/`id` associations; there is no validation, error summary, success state, or status announcement.
- The page depends on Tailwind’s runtime CDN and Google Fonts. A production build should use compiled/local assets, a content security policy, and performance-tested font loading.

---

## 2. Recommended positioning

### Core position

**Founder-led commercial cleaning with hospitality operations discipline.**

This is credible because it connects the founders’ actual backgrounds to outcomes facility buyers understand: detailed scopes, shift accountability, professional presentation, escalation ownership, and consistent inspections. It does not pretend prior employer experience is company past performance.

### Primary audience

1. Commercial property/facility managers who need recurring janitorial service.
2. Office, hospitality, and other facility operators where presentation and operational consistency matter.
3. Public-sector buyers only after Golden Crest has a legal entity, registration, insurance, capacity, and a solicitation-ready response process.

Do not lead with medical facilities until the team has appropriate procedures, products, training, and insurance for that scope. Do not imply infection-control or regulated clinical capability.

### Brand character

- Calm, exact, accountable, operational.
- Premium hospitality rather than luxury decoration.
- Procurement-readable rather than “government-themed.”
- Human leadership, not fictional software.

---

## 3. Hero redesign

### Recommended launch copy

**Eyebrow**  
FOUNDER-LED COMMERCIAL JANITORIAL SERVICE

**Headline**  
## Commercial cleaning managed with hospitality discipline.

**Support copy**  
Golden Crest brings high-volume casino and resort operations experience to recurring facility care—clear scopes, consistent routines, and direct owner communication.

Use “casino and resort operations experience” only after the founders approve the wording and the background can be substantiated.

**Primary CTA**  
`Request a site walkthrough`

**Secondary CTA**  
`Discuss your facility` or a working phone link

**Microcopy below CTA**  
`Tell us the facility type, location, approximate size, and service schedule. We’ll respond within [verified timeframe].`

Do not put government codes, certifications, response guarantees, or an intake portal in the hero. A contracting officer will scroll to a clearly labeled procurement section; a commercial buyer first needs to understand service, area, and fit.

### Hero visual direction

Use one commissioned, documentary-style photograph rather than gradients or stock “cleaner smiling at camera” imagery:

- One or both founders conducting a real walkthrough in a polished commercial environment.
- Visible operational detail: inspection sheet/tablet, floor or restroom detail, supplies organized on a cart, or a handoff conversation with a facility manager.
- Natural side light, quiet neutral color grade, architectural composition, authentic PPE/uniforms appropriate to the task.
- Crop with negative space for copy at desktop and an alternate vertical crop for mobile.
- Never stage government uniforms, badges, flags, seals, restricted spaces, or fake client interactions.

If original photography is not yet possible, launch with a restrained typographic hero and a close architectural/detail photograph licensed for commercial use. Do not generate fake founders, fake facilities, or fake proof-of-work with AI.

### Visual system

- **Palette:** warm white/stone background, deep charcoal/ink text, restrained muted brass or ochre accent, optional dark evergreen for operational callouts. “Golden Crest” can own a refined gold note without shiny metallic effects.
- **Typography:** highly legible grotesk or humanist sans for nearly everything; an editorial serif only for short display moments. Avoid italic gradient display text.
- **Layout:** strong grid, generous but controlled whitespace, thin rules, dense procurement tables where useful, square/soft-radius cards rather than pill-heavy UI.
- **Imagery:** real people, real processes, real surfaces, real equipment. Caption founder-experience images accurately.
- **Avoid:** violet/rose glows, glassmorphism, animated “ambient” blobs, emoji iconography, fictional app dashboards, gold foil everywhere, stars, shields, eagles, flags, government seals, or anything that suggests agency endorsement.

---

## 4. One-page information architecture

### 1. Header

- Wordmark/logo, Services, Our Standard, About, Government Buyers, Contact.
- One primary CTA: `Request a walkthrough`.
- On mobile, use a real menu button with an accessible expanded state; keep a compact CTA but do not crowd the wordmark.

### 2. Hero

Buyer outcome, grounded founder-experience sentence, two CTAs, service area if confirmed, and one authentic image.

### 3. Fast qualification strip

Three plain facts only, for example:

- `Recurring commercial janitorial service`
- `[Verified service area]`
- `Founder-led quality oversight`

Do not style unverified claims as badges.

### 4. Services and facility fit

Present services before verticals:

- Recurring janitorial service
- Restroom and breakroom care
- High-touch surface cleaning
- Floor/detail work within actual capability
- One-time/deep cleaning only if offered

Then list the facility types Golden Crest is prepared and insured to serve. Each card should identify scope and exclusions rather than use aspirational “clinic-grade” language.

### 5. The Golden Crest operating standard

Replace competitor attacks and fictional technology with 4–5 concrete process commitments, each tied to a deliverable:

1. **Defined scope** — site-specific schedule and task list.
2. **Consistent routine** — documented opening/closing and zone procedures.
3. **Quality review** — inspection cadence stated accurately.
4. **Issue ownership** — named escalation contact and realistic response window.
5. **Service record** — checklist or visit confirmation only if actually provided.

Show a real sample checklist after the SOP exists. A downloadable sample is stronger than abstract claims.

### 6. Founder credibility

Title: `Hospitality operations experience, applied to facility care.`

Include professional portraits, short bios for Miesha and Kimberly, specific verified responsibilities, relevant active training, and why the experience matters to the buyer. Distinguish individual experience from Golden Crest contract history. Avoid employer logos without permission.

### 7. How engagement works

1. Initial facility conversation.
2. On-site walkthrough and scope review.
3. Written proposal with service schedule, responsibilities, and terms.
4. Start-up plan and first quality review.

Do not promise a two-hour quote; janitorial scope usually depends on size, surfaces, frequency, occupancy, security, supplies, and performance requirements.

### 8. Government buyers / procurement

Keep this below operating capabilities and above contact. Use a clean data table, not a patriotic visual block.

**Before registration:** either omit the section or use a modest statement: `Golden Crest is preparing its public-sector vendor registrations. Procurement identifiers and certifications will be published only after activation.` Do not solicit federal bids before the business can responsibly accept them.

**After activation, show only verified fields:**

- Exact legal business name
- Business address/service area if intended for publication
- UEI
- CAGE
- Active SAM registration and expiration/renewal date
- Primary NAICS `561720` if selected in the active registration
- Relevant PSC `S201` as a service classification, not a credential
- Certification name, certifying body, identifier, and expiration date
- Insurance coverage and bonding capacity only as documented
- Payment methods actually accepted
- Capability statement download
- Procurement contact email and phone

CTA: `Request capability statement` or `Send a solicitation` only when both destinations work. For document upload, use a secure, privacy-reviewed service; otherwise provide a procurement email. Never ask for door codes, alarm codes, keycard details, or sensitive floor plans in a marketing form.

### 9. Contact / walkthrough request

Use a short, functional form:

- Name
- Work email
- Phone (optional unless operationally necessary)
- Organization
- Facility city/ZIP
- Facility type
- Approximate square footage range
- Desired frequency
- Short message

Do not accept sensitive files at launch. Add consent/privacy copy, spam protection, a clear success state, working delivery, and monitored ownership. Provide a phone and email alternative.

### 10. Footer

Legal business name after formation, real contact data, service area, privacy, terms, accessibility contact, and copyright. No certification badge wall. Procurement data can be linked, not repeated decoratively.

---

## 5. Copy hierarchy and proof strategy

### Copy hierarchy

1. **What the service is:** commercial janitorial/facility cleaning.
2. **Who it is for:** defined facility types in a verified service area.
3. **Why trust the team:** founders’ verified hospitality operations experience.
4. **How delivery is controlled:** actual scope, routines, inspections, and escalation.
5. **What happens next:** walkthrough, written scope, proposal.
6. **Procurement readiness:** exact registrations/certifications only when active.

### Evidence ladder

Every important claim should link to or be backed by one of these:

- Legal filing or active registration
- Certificate/policy document
- Written SOP or sample quality checklist
- Active credential with issuer and date
- Signed client permission, testimonial, or reference
- Actual working feature tested end-to-end
- Measured service record

Until Golden Crest has company past performance, use **founder experience**, process artifacts, and accurate readiness status as proof. Never manufacture testimonials, client logos, case studies, dashboards, or performance numbers.

### Claims language guide

- Prefer `designed to`, `we use`, `we document`, and `we provide` when those actions are operational.
- Avoid `guaranteed`, `tamper-proof`, `zero`, `flawless`, `fully compliant`, `clinic-grade`, `government-ready`, and `certified` without narrow evidence.
- Separate cleaning from disinfecting. State product use and dwell/contact-time procedures only when staff are trained and the process follows the product label.
- Avoid “sanitation” as a blanket promise where ordinary commercial cleaning is the actual scope.

---

## 6. CTA system

Use one conversion goal across the page: a qualified facility conversation.

- **Primary:** `Request a site walkthrough`
- **Secondary commercial:** `Call [real number]` or `Discuss your facility`
- **Government, once ready:** `Request capability statement` / `Send a solicitation`
- **Low-friction proof CTA:** `View our service standard` or `See a sample scope` once those documents exist

Avoid “free audit,” “instant assessment,” “risk-free trial,” and “submit bid” language. These either devalue the service, overpromise, or imply a procurement workflow that is not operating.

CTA behavior must be explicit: open a form, dial a number, compose an email, or download a real file. No dead controls.

---

## 7. Responsive/mobile requirements

- Design mobile first at 320px and test common widths through large desktop.
- Stack hero copy and imagery; use a dedicated portrait crop with an explicit focal point.
- Keep headline to roughly 3–5 mobile lines; body copy should not become a narrow wall of text.
- Replace hidden desktop navigation with an accessible menu. Trap focus only while the menu is open, support Escape, and restore focus on close.
- Use one-column form controls on narrow screens; minimum touch target approximately 44×44 CSS pixels.
- Keep only one prominent header CTA; do not let the top announcement bar consume the first viewport.
- Convert procurement data to labeled stacked rows rather than a squeezed multi-column grid.
- Do not horizontally scroll comparison tables; the redesign should not need a comparison matrix.
- Serve responsive images with width/height attributes, `srcset`, appropriate compression, and lazy loading below the fold.
- Test long names, real phone/email strings, validation errors, zoom to 200%, landscape phones, and on-screen keyboards.
- Performance target: no runtime Tailwind CDN, minimal JavaScript, optimized local assets, stable layout, and a fast first meaningful render on mobile data.

---

## 8. Accessibility requirements

Target WCAG 2.2 AA as the design/build baseline.

- Semantic landmarks: `header`, `nav`, `main`, sections with headings, and `footer`.
- One descriptive `h1`; logical heading order afterward.
- Visible `:focus-visible` styles with adequate contrast; never remove focus outlines without a replacement.
- Text and essential UI controls must meet AA contrast; test the actual gold accent before use.
- Every form field needs a persistent label tied with `for`/`id`, clear required status, instructions, and programmatic error association.
- On submit, focus an error summary; announce success/errors with an appropriate live region.
- Do not use placeholder text as the label.
- Buttons must be buttons, links must navigate, upload controls must be native and keyboard operable, and tabs require full tab semantics only if tabs are truly necessary.
- Give informative photography useful alt text; use empty alt text for decorative images. Decorative icons should be hidden from assistive technology.
- Respect `prefers-reduced-motion`; remove nonessential ping, floating, and marquee animation.
- Do not rely on color alone to express selection, status, errors, or credentials.
- Provide a skip link and ensure sticky navigation does not obscure anchored headings.
- Maintain readable line length, responsive text sizing, 200% text zoom, and 400% browser zoom without loss of content.
- Publish a plain privacy notice explaining form data, retention, access, and contact. Do not collect sensitive facility-security information through the marketing site.

---

## 9. Prioritized remediation plan

### P0 — before any public launch

1. Remove every unsupported certification, registration, insurance, bonding, screening, compliance, response-time, trial, and technology claim.
2. Disable or replace the fake intake portal with a functional, minimal, securely delivered contact form.
3. Remove access-code/fob/lockbox questions and all unimplemented file upload language.
4. Replace placeholder phone/email/domain data with monitored, consistent contacts.
5. Add privacy handling, form success/error behavior, and basic accessibility.
6. Correct founder wording so personal experience is not presented as company past performance.

### P1 — credible finished redesign

1. Implement the restrained visual system and authentic hero photography.
2. Rebuild IA around services, operating standard, founders, process, and contact.
3. Create and approve a real service scope template, quality checklist, escalation procedure, and onboarding workflow; use these as proof.
4. Test the form end-to-end, including delivery, spam handling, validation, and mobile behavior.
5. Compile CSS locally, optimize imagery/fonts, add metadata/social cards/favicon, and run accessibility/performance checks.

### P2 — add only after operational milestones

1. Populate the procurement table after formation, insurance, SAM activation, and any certifications.
2. Publish a corrected capability statement with active identifiers and no aspirational credentials.
3. Add testimonials, references, or case studies only with client permission and accurate results.
4. Add QR/service-log or portal features only after they are built, security/privacy reviewed, and used successfully in real operations.

---

## 10. Definition of done

The redesigned page is ready when:

- Every credential and performance statement has an owner and supporting document.
- No control, download, upload, tab, phone number, email, or CTA is fake or dead.
- The site clearly distinguishes founder experience from Golden Crest company experience.
- A commercial buyer can identify service fit, area, process, and next step in under a minute.
- A contracting officer can find accurate procurement data without encountering pseudo-government branding.
- The form has been submitted successfully on desktop and mobile and the inquiry was received by the monitored recipient.
- Keyboard, screen-reader semantics, reduced motion, zoom, contrast, and form errors have been tested.
- No government seal, certification logo, client logo, or employer logo appears without authorization.
- The page feels premium because it is specific, restrained, and verifiable—not because it imitates a software startup.
