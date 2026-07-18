# Aloha Fest Japan — Vendor Landing Preview

A bilingual, mobile-first vendor-interest landing page for a Hawaii × Japan fusion community event.

## Preview locally

```bash
cd /Users/kingdomstuff/workspace/apps/aloha-fest-japan-preview
python3 -m http.server 4173
```

Then open: `http://localhost:4173`

## Included

- `index.html` — vendor landing page / bilingual Japanese-first splash
- `logo.svg` — original Aloha Fest mark
- `qr-preview.svg` — intentionally non-live QR for visual review only
- `vendor-contact-sheet.csv` — festival walk-around contact tracker
- `vendor-interest-form-blueprint.md` — publish-ready form content

## Before publishing

1. Confirm event name, date/location, and organizer contact channel.
2. Connect a live form destination (Tally / Google Form / equivalent).
3. Deploy the landing page to a public URL.
4. Regenerate the QR with that verified URL.

Do not distribute `qr-preview.svg`; it intentionally encodes only a preview message.
