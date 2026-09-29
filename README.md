# Website Add-ons — Marker Plates review build

Static GitHub Pages review build plus an optional server-side enquiry endpoint.

## Design Studio enquiry attachments

The Design Studio creates a high-resolution PNG in browser memory at a **300-dpi-equivalent pixel density**. It is only prepared for submission and is never offered as a customer download.

When the enquiry reaches `/api/inquiry`, the server attaches that PNG directly to the company email. The SVG remains available as a vector fallback.

The customer-facing enquiry text does **not** include export/pixel dimensions, sign dimensions, per-layer X/Y coordinates, or per-layer artwork dimensions. It contains the normal enquiry fields and a plain-language design summary.

For a GitHub Pages-only deployment, the existing EmailJS path can send the PNG as a variable attachment. EmailJS supports programmatic variable attachments generated from canvas data. Configure a **Variable Attachment** in the EmailJS template with parameter name `design_attachment`.

No artwork download/export control is provided to the customer.

## Design Studio editing

Text editing remains persistent while typing: the text textarea is not rebuilt on each character, line breaks are preserved, and Backspace/Delete are treated as normal editing keys while a text field is focused. Studio-level undo is available with the Undo button and Ctrl/Cmd+Z when not typing.

## Symbol library

Current supplied assets are in `symbols/`:
- Digger arm — NEW
- Digger arm — 2014
- No unauthorised hand — red
- No unauthorised hand — small
- Plough
- Warning triangle

## GitHub Pages

GitHub Pages is static and cannot run the Python SMTP endpoint. Automated attachment delivery therefore uses the configured endpoint or EmailJS, with a `mailto:` fallback when neither is configured.

## Local review

Run `python3 server.py`.

SMTP settings:
`SMTP_HOST`, `SMTP_PORT` (default 587), `SMTP_USER`, `SMTP_PASSWORD`, `SMTP_FROM`, `SMTP_TO` (default sales@freestyle-signs.co.uk), `SMTP_SECURE`, `SMTP_STARTTLS`, `ALLOWED_ORIGIN`, `PORT`.

Without SMTP settings, enquiries and private artwork are kept under `outbox/` for local review.

Artwork remains proprietary: no consumer artwork download/export functionality is provided.