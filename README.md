# Website Add-ons — Marker Plates review build

Static GitHub Pages review build plus an optional server-side enquiry endpoint.

## Design Studio enquiry attachments

The Design Studio can generate a self-contained, high-quality SVG in memory. When the enquiry form posts to \`/api/inquiry\`, the bundled \`server.py\` sends that SVG directly to \`sales@freestyle-signs.co.uk\` as an email attachment.

The customer is not offered a download link or an exported artwork file.

The human-readable enquiry summary intentionally contains only:
- sign size;
- background;
- entered text;
- symbol/logo names.

Internal per-layer X/Y coordinates and per-layer artwork dimensions are **not** included in the customer-facing submission text. The exact geometry remains inside the SVG attachment for company review.

## GitHub Pages

GitHub Pages is static and cannot run the Python SMTP endpoint. The page therefore falls back to the visitor's email application when \`/api/inquiry\` is unavailable.

For automatic attachment delivery from a live GitHub Pages site, deploy \`server.py\` to a server/runtime that can receive the POST request and set \`window.MARKERPLATES_INQUIRY_API\` in \`index.html\` to that endpoint.

## Local review

Run \`python3 server.py\`.

SMTP settings:
\`SMTP_HOST\`, \`SMTP_PORT\` (default 587), \`SMTP_USER\`, \`SMTP_PASSWORD\`, \`SMTP_FROM\`, \`SMTP_TO\` (default sales@freestyle-signs.co.uk), \`SMTP_SECURE\`, \`SMTP_STARTTLS\`, \`ALLOWED_ORIGIN\`, \`PORT\`.

Without SMTP settings, the enquiry and SVG are kept under \`outbox/\` for local review.

Artwork remains proprietary: no consumer artwork download/export functionality is provided.
