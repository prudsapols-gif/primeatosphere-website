# Prime Atosphere website

Static, bilingual (TH/EN) company site. 6 pages: Home, Products, Solutions, 3M Novec replacement, About, Contact.

- Content: `src/partials/*.html` (one file per section) and the `PAGES` list in `build.py` (titles, SEO descriptions, which sections each page shows).
- Styles: `src/style.css` · Script: `src/main.js` (language toggle, enquiry form opens an email to BD@primeatosphere.com).
- Build: `python3 build.py` → `docs/` is what GitHub Pages publishes (Settings → Pages → Branch: main, folder: /docs).
- Adding a page: add a partial in `src/partials/`, add a row in `PAGES`, and (if it should be in the menu) in `NAV`.

Editing rules: only claims stated by the manufacturer (see ../sitemap-and-copy.md §8); no phone number; LINE OA to come.
