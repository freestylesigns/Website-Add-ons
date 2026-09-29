# Website Add-ons — Marker Plates review build

Static GitHub Pages review build plus an optional server-side enquiry endpoint.

## Design Studio enquiry attachments

The Design Studio creates a high-resolution PNG in browser memory at a **300-dpi-equivalent pixel density**. The PNG is never exposed through a customer-facing download control.

When the enquiry reaches `/api/inquiry`, the server attaches that PNG directly to the company email. The SVG is also sent in the request as a vector fallback; the server uses it when no PNG is available.

The customer-facing enquiry text does **not** include export/pixel dimensions, per-layer X/Y coordinates, or per-layer artwork dimensions. It contains the normal enquiry fields and a plain-language design summary.

For a GitHub Pages-only deployment, the EmailJS fallback can send the PNG as a variable attachment. EmailJS supports programmatic variable attachments generated from a canvas. Configure a **Variable Attachment** in the EmailJS template with parameter name `design_attachment`, and optionally use `{{attachment_filename}}` as its filename. Use the company's own EmailJS service, template and public key.

The browser never creates a download link or export button for the proprietary artwork.

## Symbol library

Current supplied assets are in `symbols/`:
- Digger arm — NEW
- Digger arm — 2014
- No unauthorised hand — red
- No unauthorised hand — small
- Plough
- Warning triangle

Add further SVG symbols to that folder and register them in the `SYMBOLS` array in `index.html`.

## GitHub Pages

GitHub Pages is static and cannot run the Python SMTP endpoint. The site therefore uses the configured server endpoint or EmailJS for automated attachment delivery, with a `mailto:` fallback when neither is configured.

## Local review

Run `python3 server.py`.

SMTP settings:
`SMTP_HOST`, `SMTP_PORT` (default 587), `SMTP_USER`, `SMTP_PASSWORD`, `SMTP_FROM`, `SMTP_TO` (default sales@freestyle-signs.co.uk), `SMTP_SECURE`, `SMTP_STARTTLS`, `ALLOWED_ORIGIN`, `PORT`.

Without SMTP settings, the enquiry and private artwork are kept under `outbox/` for local review.

Artwork remains proprietary: no consumer artwork download/export functionality is provided.