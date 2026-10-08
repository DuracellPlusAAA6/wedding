# AGENTS.md — Wedding Website Project (Alexandra & Bruno)

This file gives every future agent session working in this repo the essential context.
**Read `HANDOVER.md` (full history, architecture, open items, tooling constraints) and
`DEVELOPMENT.md` (site structure, key facts, edit workflow) before making changes.**

## Project

- Live site: https://duracellplusaaa6.github.io/wedding/ (GitHub Pages, auto-deploys from `main`, 1–3 min)
- Repo: https://github.com/DuracellPlusAAA6/wedding
- Local checkout: `/home/bruno_silva/wedding`
- Wedding: 10 September 2027, Iași, Romania

## Hard constraints — read before editing

1. **Always `git fetch` + fast-forward before editing.** Multiple Vibe sessions have worked on this repo in parallel (the `venue_01–33` rename came from another session).
2. **Binary files cannot be pushed through the GitHub connector** (UTF-8 corruption, empirically verified). Text files (HTML/CSS/JS/SVG/MD) push fine via `push_files`. Images must be uploaded by the user via the GitHub web UI (they must click "Commit changes") or a credentialed local `git push` (none configured: `git push` over HTTPS fails with no credential helper). File deletion remotely works via the connector's `delete_file`.
3. **After remote-only pushes**, reconcile local with `git update-ref refs/heads/main origin/main` after verifying identical trees (`git diff HEAD origin/main`), or simply `git pull`.
4. **Browser caching causes false "it didn't apply" reports.** Verify against the live site with `curl` before believing them; tell the user to hard-refresh (Ctrl+F5).
5. Git identity: repo-local `Vibe Nuage Agent <vibe@mistral.ai>`.

## Key facts (verified, do not regress)

- Ceremony: **Our Lady Queen Cathedral**, B-dul Ștefan cel Mare și Sfânt 26, Iași 700064, 4:00 PM
- Reception: **Chalette Events** (the Glass Garden), DN 24, Păun, Iași 707037
- Hotel: **Grand Hotel Traian**, Piața Unirii 1, Iași 700056, 70€/night incl. breakfast
- Branding: "Alexandra & Bruno" (never "Bruno & Alexandra")
- Maps links: church `https://maps.app.goo.gl/V1szCWX216XLgVrq5`, venue `https://maps.app.goo.gl/mzd4LSpz8icfi1ib7`
- RSVP: formsubmit.co → wedding@marquessilva.eu, `_next` redirects to `thank_you.html`; endpoint is activated and tested (2026-10-08)

## Conventions

- Album pages live at `gallery/<name>/index.html` (URL `/wedding/gallery/<name>/`); photos in `assets/images/<album>/` named `<album>_NN.jpg`.
- Venue album: 24 photos in 3 themed groups (First Look / Wedding Magic / Food Experience), square-crop mosaic.
- Iași album images are served from the Wikimedia Commons CDN (attribution on the page) — not repo files.
- Language flags are hidden via CSS (`.language-flags-desktop`); site is English-only for now.
- WhatsApp group links in all footers are intentional `href="#"` placeholders — the user has the real URLs pending. Do not "fix" them without asking.

## Open items (user parked on 2026-10-08)

WhatsApp group URLs · TBD team card (MC name) · countdown target time (13:00 vs 16:00) · contact double `<h1>` · `user-scalable=no` removal · hero image resize · photos for Hotel/International albums · manual browser RSVP test · translations decision (flags) · optional custom domain. Full details in `HANDOVER.md` §4.
