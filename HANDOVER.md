# Handover Document — Wedding Website (Alexandra & Bruno)

**Purpose:** complete record of the October 2026 development push, so work can be resumed in a few weeks without losing context.
**Live site:** https://duracellplusaaa6.github.io/wedding/
**Repository:** https://github.com/DuracellPlusAAA6/wedding (branch `main`, GitHub Pages auto-deploys on push, ~1–3 min)
**Companion doc:** `DEVELOPMENT.md` (site structure, key facts, edit workflow — kept current).

---

## 1. Architecture

### Pages (site root)
| File | Purpose |
|---|---|
| `index.html` | Home — hero (venue_05 photo), countdown, Our Story, venue & church cards, RSVP CTA |
| `info.html` | Wedding info — date/time, dress code, hotel, locations with Maps links, FAQ |
| `plan.html` | Wedding-day timeline (15:30 → 04:00) |
| `rsvp.html` | RSVP form → FormSubmit → email to wedding@marquessilva.eu → redirects to thank-you page |
| `news.html` | News items (dates are placeholders/plan markers) |
| `gallery.html` | Album hub — six album cards (Us, Church, Venue, Iași, Hotel, International Package) |
| `international.html` | Travel guide, weekend plan, Weekend/Week packages, local tips |
| `contact.html` | Email, WhatsApp groups (placeholders), team, RSVP callback |
| `thank_you.html` | Post-RSVP confirmation (reached via FormSubmit `_next` redirect) |

### Album pages (`gallery/<name>/index.html`, served at `/wedding/gallery/<name>/`)
| Album | Content | Images |
|---|---|---|
| `gallery/us/` | Couple photo + Our Story | `assets/images/optimized/signal-..._optimized.jpg` |
| `gallery/church/` | 8 photos, lightbox; Details (address, ceremony, official website, Maps, Wikipedia) | `assets/images/church/church_01–08.jpg` |
| `gallery/venue/` | 24 photos in 3 themed groups (First Look / Wedding Magic / Food), square mosaic, venue Website/Facebook/Instagram buttons | `assets/images/venue/venue_01–33` (9 files unused, deleted) |
| `gallery/iasi/` | 6 landmark photos (Palace of Culture, Golia, Botanical Garden, Union Square, Metropolitan Cathedral, Copou) + explore/tips sections | **Served from Wikimedia Commons CDN** (attribution links on page) |
| `gallery/hotel/` | Grand Hotel Traian details (photos pending) | — |
| `gallery/international/` | Weekend/Week package details (photos pending) | — |

### Assets
- `assets/css/style.css` — all styling. Notable recent additions: `.album-grid`/`.album-card` (album hub cards), `.venue-gallery .gallery-item img` (square-crop mosaic), `.language-flags-desktop { display: none }` (flags hidden).
- `assets/js/script.js` — countdown (guarded: only runs when `#countdown` exists) + `addGuestFields()` for the RSVP guest-count dropdown.
- `assets/images/<topic>/` folders: `us/`, `church/`, `venue/`, `iasi/` (empty — CDN images), `hotel/`, `international/` — each with a README describing the naming convention (`church_01.jpg`, `venue_01.jpg`, …).
- `assets/images/favicon.svg` — A&B monogram, linked from all pages.
- Lightbox2 + jQuery via cdnjs, only on pages that use `data-lightbox` (us, church, venue, iasi).

### External services
- **FormSubmit** (`formsubmit.co/wedding@marquessilva.eu`) — RSVP backend. Endpoint is activated; test submission succeeded 8 Oct 2026 (a "TEST - please ignore" email was sent — delete it). Hidden `_next` field redirects to `thank_you.html`. Note: FormSubmit requires a real browser Origin — curl/plain HTTP tests are rejected (a 403-style bounce to their homepage), which is expected bot protection, not a bug.
- **Wikimedia Commons CDN** — Iași album images (thumb URLs, 1280px, verified stable). Attribution links on the album page satisfy the CC licenses.

---

## 2. Development history (chronological)

1. **Branding**: swapped all "Bruno & Alexandra" → "Alexandra & Bruno" across every page, footer, alt, and title.
2. **Venue change Liria → Chalette Events**: photos swapped on gallery tile and homepage (hero → `venue_05.jpg`, venue card → `venue_08.webp` then `venue_01.jpg`), all text references updated site-wide, Maps link → `https://maps.app.goo.gl/mzd4LSpz8icfi1ib7`, address "DN 24, Păun, Iași 707037".
3. **Venue album**: 33 uploaded photos renamed to `venue_01–33` (duplicates removed after byte/dimension verification); dedicated page `gallery/venue/`; organized by a vision-based classification into themed groups; then curated down to **24 photos in 3 groups** (First Look, Wedding Magic, Food Experience) with combined per-section descriptions; square-crop mosaic grid.
4. **Gallery restructure**: `gallery.html` became an album hub; created album pages for Us, Church, Iași, Hotel, International Package; created `assets/images/<topic>/` folders with READMEs; removed the old tiles that referenced never-existing images.
5. **Church album**: user uploaded 8 photos via GitHub web UI; renamed to `church_01–08.jpg`; cover changed to `church_01` (the Catedrala photo); homepage church card + venue-church section use `church_01.jpg` too. Links: Maps (`https://maps.app.goo.gl/V1szCWX216XLgVrq5`), Wikipedia (Our Lady Queen Cathedral), official website (`https://ercis.ro/`).
6. **Name/address corrections** (verified via Wikipedia/OpenStreetMap/chalette.ro, propagated everywhere):
   - Church: "Iași Catholic Church, Strada Cuza Vodă 12" → **Our Lady Queen Cathedral, B-dul Ștefan cel Mare și Sfânt 26, Iași 700064**
   - Hotel: "Hotel Traian, Strada Cuza Vodă 1" → **Grand Hotel Traian, Piața Unirii 1, Iași 700056**
   - Venue: **Chalette Events, DN 24, Păun, Iași 707037**
   - "10 minutes from the venue" → "a short drive" (accuracy).
7. **Venue page buttons**: Website / Facebook / Instagram (chalette.ro, facebook.com/ChaletteEvents, instagram.com/chaletteevents).
8. **RSVP flow**: created `thank_you.html`; added hidden `_next` to the form; tested the endpoint end-to-end via FormSubmit's AJAX API (success). The non-AJAX browser redirect has not been visually verified — worth one manual submit.
9. **Contact page**: added RSVP callback block ("Have you RSVP'ed yet? → RSVP Now").
10. **Homepage**: removed "Learn More" and "View Album" buttons (photos speak for themselves); both venue-section images pinned to 4:3 via CSS.
11. **Mobile flags**: initially made visible next to the hamburger; **later hidden entirely** (site is English-only) — user decision pending on translations.
12. **Full-site audit** (8 Oct 2026): all internal links/images verified, external links probed, JS checked, content consistency reviewed. Fixes applied:
    - Dead Berăria H domain → `https://berariah.ro/`
    - Countdown crash on RSVP page (null element) → guarded in `script.js`
    - Dead Grădina Veche domain (DNS gone) → Google Maps search link
    - Open Graph + meta description + Twitter card on all 15 pages (og:image = couple photo)
    - SVG favicon (`assets/images/favicon.svg`) linked from all pages
    - 24 unreferenced files deleted (old Liria/OIP images, `.txt` placeholders, 9 unused venue photos; all recoverable from git history)
    - `DEVELOPMENT.md` rewritten
13. **WhatsApp links**: dead `href="#"` placeholders were temporarily replaced with an email-invite line, then **reverted to the original placeholders at the user's request** — real group URLs are still pending.

---

## 3. Tooling constraints (important for resuming)

- **The agent tooling (Vibe + GitHub App connector) can push TEXT files but NOT binary images** — the connector UTF-8-encodes string content before base64, corrupting binary. Verified empirically (checksum test, 8 Oct 2026). Images must be added via the GitHub web UI ("Add file → Upload files", then **Commit changes** — staging alone doesn't upload) or a local `git push` with credentials (none configured on the working machine; `git push` over HTTPS fails with no credential helper).
- **Deleting files remotely** works via the connector's delete-file API (one commit per file).
- **Browser caching** causes frequent "the change didn't apply" false alarms — always hard-refresh (Ctrl+F5 / Cmd+Shift+R); CSS is the most aggressively cached.
- **Parallel sessions**: multiple Vibe sessions have worked on this repo simultaneously (the `venue_01–33` rename came from a parallel session). Always `git fetch` + fast-forward before editing; after remote-only pushes, reconcile local with `git update-ref refs/heads/main origin/main` (trees verified identical) — or simply `git pull`.
- **Commit identity** on the working machine: repo-local `user.name "Vibe Nuage Agent" / vibe@mistral.ai` (matches earlier agent commits).

---

## 4. Open / ignored topics (punch list)

Explicitly parked by the user on 8 Oct 2026 — resume points:

| # | Topic | Status / decision needed |
|---|---|---|
| 4 | **WhatsApp group links** | 48 `href="#"` placeholders across all footers + contact card. Need the three real invite URLs; then replace in every footer block and the contact card. |
| 5 | **Language flags** | Hidden via CSS (`.language-flags-desktop`). Decide: implement PT/EN/RO translations (big job) or remove the flag markup entirely. |
| 6 | **TBD team card** (contact.html) | Placeholder for the Portuguese-Romanian MC. Needs a name or removal. |
| 8 | **Countdown target** | `script.js` counts to 10 Sep 2027 **13:00**; ceremony is 16:00. Pick one (day-start vs ceremony moment). |
| 9 | **Double `<h1>` on contact.html** | "Meet the Team" should be an `<h2>` (minor, cosmetic/SEO). |
| 10 | **`user-scalable=no`** on index/international/contact | Blocks pinch-zoom on Android (accessibility). Remove `maximum-scale=1.0, user-scalable=no` from those viewports. |
| 11 | **Hero image weight** | `venue_05.jpg` (2048px, ~320KB) served full-size on homepage. Resize to ~1200px (a resized copy must be uploaded via web UI / local push — see tooling constraints). |
| — | **RSVP browser test** | One manual submit to visually confirm the redirect to `thank_you.html`; also confirm the test email arrived. |
| — | **Photos pending** | Hotel album and International Package album say "Photos coming soon" — upload to `assets/images/hotel/`, `assets/images/international/` then wire into the album grids. Us album has only one photo. |

---

## 5. Suggested next steps (in order)

1. **Content first**: get the WhatsApp group URLs, the MC's name, and the pending photos (hotel, packages, more couple photos). These are the only things a guest would notice.
2. **Manual RSVP test** on a phone: submit → confirm thank-you redirect → confirm the email lands in the inbox.
3. **Small polish batch** (30 min): countdown time, contact `<h1>`→`<h2>`, pinch-zoom fix, hero image resize.
4. **Translations decision**: if PT/EN/RO is happening, start with the highest-traffic pages (home, info, RSVP) and re-enable the flags; otherwise remove the flag markup.
5. **Later/optional**: custom domain (e.g. `wedding.marquessilva.eu` — the email domain already exists; point DNS at GitHub Pages and add a CNAME file), a news-page content plan for the year ahead, and possibly swapping the Iași CDN images for self-hosted copies if Wikimedia hotlinking ever feels fragile.

---

## 6. Quick reference

- Edit cycle: `git fetch && git merge --ff-only origin/main` → edit → commit → push (or web UI) → hard-refresh browser.
- Photo upload: GitHub web UI → `assets/images/<album>/` → commit; then add a `gallery-item` block with `data-lightbox="<album>"` to the album page.
- Naming conventions: `venue_01–33`, `church_01–08`; new albums: `us_01…`, `iasi_01…`, `hotel_01…`, `international_01…`.
- Recovery: everything deleted is in git history (`git log --all -- <path>`).
