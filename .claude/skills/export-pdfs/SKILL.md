---
name: export-pdfs
description: Export track HTML workbooks to shareable PDFs using Puppeteer screenshots. Trigger on "export pdfs", "generate pdfs", "build pdfs", "make pdfs".
user_invocable: true
---

# Export Track PDFs

Export all `track-*.html` workbooks to pixel-perfect PDFs using Puppeteer + pdf-lib.

## Workflow

### Step 1: Ensure dependencies

Check if `node_modules/puppeteer` and `node_modules/pdf-lib` exist in the project root. If not, run:

```bash
cd /Users/david.okeeffe/Repos/coles-vibe-workshop && npm init -y --silent 2>/dev/null && npm install puppeteer pdf-lib --silent
```

### Step 2: Ensure export script

Check if `export-pdf.js` exists in the project root. If not, copy it:

```bash
cp ~/.claude/plugins/cache/fe-vibe/fe-html-slides/*/skills/html-slides/resources/export-pdf.js /Users/david.okeeffe/Repos/coles-vibe-workshop/
```

### Step 3: Find all track HTML files

Glob for `track-*.html` in the project root. These are the workbooks to export.

### Step 4: Export each HTML to PDF

For each `track-*.html` file found, run the export in parallel:

```bash
node export-pdf.js track-common.html
node export-pdf.js track-de.html
node export-pdf.js track-ds.html
node export-pdf.js track-analyst.html
```

Each produces a corresponding `.pdf` file (e.g., `track-de.html` -> `track-de.pdf`).

### Step 5: Report results

List the generated PDFs with file sizes:

```bash
ls -lh track-*.pdf
```

Then open all PDFs for the user:

```bash
open track-*.pdf
```

## Notes

- The export script uses Puppeteer to screenshot each `<section class="slide">` at 1920x1080 @2x retina, then stitches them into a PDF with pdf-lib
- Each slide becomes a 960x540 PDF page — pixel-perfect with all backgrounds, gradients, and SVGs preserved
- Re-run after any HTML changes to regenerate PDFs
- PDFs are .gitignored — only the HTML source is tracked
