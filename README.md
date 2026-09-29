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
- A supplied symbol library with draggable assets.
- Symbols/logos are created behind text by default.
- Selected symbol/logo layers have a corner resize handle and numeric width/height controls.
- No artwork download/export.
- Enquiry flow addressed to sales@freestyle-signs.co.uk.

## Symbol library

Current supplied assets are in `symbols/` and were converted from the uploaded EPS/AI artwork into cropped SVG assets for browser use:

- Digger arm — NEW
- Digger arm — 2014
- No unauthorised hand — red
- No unauthorised hand — small
- Plough
- Warning triangle

To add another symbol later, add its SVG under `symbols/` and add an entry to the `SYMBOLS` array in `index.html` with its display name, asset path and aspect ratio.

## GitHub Pages

The repository includes `.github/workflows/pages.yml` for GitHub Pages deployment. Enable Pages using **Settings → Pages → Source → GitHub Actions**.

The static Pages version does not expose the local Python API. The enquiry flow opens the visitor's configured email application.

The previously supplied local Python package remains the option for automatic SMTP delivery.

Artwork remains proprietary: this build intentionally does not provide artwork download/export functionality.