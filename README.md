# Marker Plates — GitHub review build

This repository contains the editable Marker Plates website review build.

## Included

- Central catalogue with search, sorting, product type, network, width/height and orientation filters.
- Representative utility marker plate / marker post population.
- Product detail pages with prefilled enquiry forms.
- Design Studio with:
  - default sign size **180 mm × 200 mm**;
  - exact width:height working-area proportion;
  - **Helvetica Neue** as the default typeface;
  - editable text, text size and positioning;
  - draggable text, symbol and logo layers;
  - editable image width/height and X/Y position in millimetres;
  - visible vertical and horizontal midpoint guides;
  - 6 mm midpoint snapping tolerance;
  - Pantone-labelled background swatches;
  - no artwork image/PDF download control;
  - design-to-enquiry handoff.
- A local Python server for SMTP delivery or an offline JSONL outbox.

## GitHub Pages

The repository includes `.github/workflows/pages.yml` for GitHub Pages deployment. Enable Pages using **Settings → Pages → Source → GitHub Actions**.

The static Pages version does not expose the local Python API. When the enquiry endpoint is unavailable, the enquiry flow falls back to the visitor's configured email application using a mailto link.

## Local SMTP review

Run `python3 server.py` locally. Set SMTP environment variables as documented in `.env.example` to deliver live enquiries. Without SMTP, submissions are saved to `outbox/inquiries.jsonl`.

## Editing

- `data/products.js` contains the representative product population.
- `app.js` contains the catalogue, enquiry and Design Studio behaviour.
- `styles.css` contains the site styling and responsive layout.

Artwork remains proprietary: this build intentionally does not provide artwork download/export functionality.
