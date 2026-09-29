# Website Add-ons — Marker Plates review build

Static GitHub Pages review build for the Marker Plates website.

## Included
- Central catalogue search by type, network and dimensions.
- Representative utility-sign catalogue.
- Design Studio with default 180 × 200 mm sign.
- Proportional working area based on quoted dimensions.
- Helvetica Neue default type.
- Draggable text and image/logo layers.
- Editable text size and object dimensions/position in mm.
- Visible horizontal and vertical midpoint guides.
- 6 mm midpoint snapping.
- Pantone-labelled background swatches.
- Select-and-delete controls plus Delete/Backspace keyboard shortcut.
- Supplied symbol library with draggable assets.
- Symbols/logos are created behind text by default.
- Symbol/logo corner resize handle plus numeric width/height controls.
- Studio undo support.
- Multiline text entry with persistent caret/focus during editing.
- Design Studio enquiry handoff with an optional high-quality PNG attachment generated in memory at 300-dpi-equivalent pixel dimensions.
- No artwork download/export control.

## Private design attachment delivery

GitHub Pages itself is static and does not support server-side languages, so it cannot directly act as the private mail server. The current build therefore supports an optional EmailJS delivery path. EmailJS supports programmatic variable attachments generated from a canvas.

1. Create an EmailJS service connected to the company's email provider.
2. Create a template addressed to `sales@freestyle-signs.co.uk`.
3. In the template Attachments tab, add a **Variable Attachment** with parameter name `design_attachment`.
4. Use `{{attachment_filename}}` for the attachment filename if desired.
5. Add the form/design variables used by the build: `name`, `email`, `company`, `phone`, `message`, `design_dimensions`, `design_background`, and `design_layers`.
6. Put the EmailJS Service ID, Template ID and Public Key in the `EMAILJS` object near the top of `index.html`.

The PNG is generated in browser memory and is not given a download button. The browser sends it directly to the email service. For stronger protection of proprietary artwork, use a server-side mail endpoint instead; client-side delivery cannot be a security boundary because the browser necessarily has access to the design data.

When EmailJS is not configured, the enquiry falls back to the visitor's email client and explains that an attachment cannot be included through `mailto:`.

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

The repository includes the existing Pages workflow. The static site can be hosted from GitHub Pages; the repository remains the source for the review build.

Artwork remains proprietary: the build intentionally does not provide artwork download/export functionality.