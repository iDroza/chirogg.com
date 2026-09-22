# Chiro Growth Group
Public website: https://chirogg.com/
GitHub: https://github.com/iDroza/chirogg.com

Cloudflare Pages automatically deploys root index.html and its assets on each push to main. The complete React source is included in app/, with its package lock and local tooling.

## Updating the page
1. npm install
2. Edit app/page.tsx and app/globals.css.
3. Run npm run build, then npm run dev.
4. With the local server running, run python scripts/export-static.py.
5. Verify index.html, then commit and push to main.

The exported page uses native links and needs no client JavaScript. All inquiry CTAs open the visitor's email application with ads@chirogg.com and a prefilled clinic brief. They do not send automatically.

Stock photography provenance is in PHOTO-SOURCES.md. Images are illustrative, not client endorsements. No invented performance claims, patient data forms, or third-party tracking are included. The separate Sites publication is recorded in .openai/hosting.json; chirogg.com is served by the GitHub-connected Cloudflare Pages project.
