# Wedding Website — Alexandra & Bruno

**Live site**: https://duracellplusaaa6.github.io/wedding/
**Repository**: https://github.com/DuracellPlusAAA6/wedding
**Last updated**: 8 October 2026

Deployed automatically via GitHub Pages — every push to `main` goes live within a few minutes.

## Site structure

- `index.html` — Home (hero, countdown, venue & church cards)
- `info.html` — Wedding info (ceremony, venue, hotel, FAQ)
- `plan.html` — Wedding day schedule
- `rsvp.html` — RSVP form (FormSubmit → wedding@marquessilva.eu; redirects to `thank_you.html`)
- `news.html` — News & updates
- `gallery.html` — Album hub with six albums:
  - `gallery/us/` — Alexandra & Bruno (couple photos)
  - `gallery/church/` — Our Lady Queen Cathedral (`assets/images/church/`, church_01–08)
  - `gallery/venue/` — Chalette Events (`assets/images/venue/`, 24 photos in 3 themed groups)
  - `gallery/iasi/` — Iași city (images served from the Wikimedia Commons CDN, attribution on the page)
  - `gallery/hotel/` — Grand Hotel Traian (photos pending)
  - `gallery/international/` — Weekend/Week packages (photos pending)
- `thank_you.html` — post-RSVP confirmation page
- `contact.html` — contact info, team, RSVP callback

## Key facts

- **Wedding**: 10 September 2027, Iași, Romania
- **Ceremony**: 4:00 PM, Our Lady Queen Cathedral, B-dul Ștefan cel Mare și Sfânt 26, Iași 700064
- **Reception**: Chalette Events (the Glass Garden), DN 24, Păun, Iași 707037
- **Hotel**: Grand Hotel Traian, Piața Unirii 1 — 70€/night, breakfast included
- **RSVP deadline**: 1 March 2027

## How to edit

1. Pull first: `git pull --ff-only` (parallel edits happen — always sync before changing files).
2. Edit the HTML/CSS, commit, push to `main`, or use the GitHub web UI.
3. Hard refresh in the browser (Ctrl+F5 / Cmd+Shift+R) — HTML and especially CSS are cached aggressively.

## Adding photos to an album

1. Upload to the matching folder under `assets/images/<album>/` following the naming convention (`church_01.jpg`, `venue_01.jpg`, ...).
2. Add a `gallery-item` block to the album page with `data-lightbox="<album>"`.
3. Note: the agent tooling can push text files but not binary images — upload photos via the GitHub web UI or a local `git push`.

## Notes & known limitations

- The RSVP form uses formsubmit.co; the endpoint is activated. Every submission is emailed to wedding@marquessilva.eu.
- Language flags are currently hidden via CSS (`.language-flags-desktop`) — the site is English-only until translations exist.
- WhatsApp group invite links are pending; footers point guests to the email address for now.
- Old Liria/OIP images and unused venue photos were removed from the repo (October 2026); they remain recoverable from git history.
