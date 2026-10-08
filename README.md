# GrowVika website

Plain HTML, CSS and JavaScript. No build step and no libraries.

**Pages:** `index.html` (home), `about.html`, `services.html` + 6 service pages (`website-development.html`, `ecommerce-development.html`, `mobile-app-development.html`, `crm-development.html`, `custom-software-development.html`, `digital-marketing.html`), `work.html`, `service-area.html` + 6 city pages (`service-area-delhi.html` …), `blog.html` + 9 article pages (`blog-*.html`), `faq.html`, `contact.html`. SEO: every generated page has a canonical URL, Open Graph tags and JSON-LD (organisation, breadcrumbs, FAQ, blog posting); `sitemap.xml` and `robots.txt` are in the root — change the domain in `tools/pages/build.py` (`BASE`) when the site moves to growvika.com.

The inner pages are generated from `tools/pages/` (content in `data.py` and `articles.py`, sections in `build.py` and `more.py`, page layouts in `pages.py`). To regenerate after editing content: `python3 tools/pages/pages.py <version>`. Hand edits to generated pages are overwritten by regenerating.

**Main home page:** `index.html` (premium agency design) uses `assets/css/agency.css` and `assets/js/agency.js`. Fonts: Syne (headings), Fraunces italic (accent words), Plus Jakarta Sans (body). Icons: Font Awesome.

The older 3 layouts are kept for reference at `layouts.html` (they use `base.css`, `home-*.css`, `main.js`).

```
index.html          ← main home page (new agency design)
layouts.html        ← old preview page: choose one of 3 layouts
home-1.html         ← Layout 1: Classic Agency
home-2.html         ← Layout 2: Editorial Split
home-3.html         ← Layout 3: Bento
assets/css/base.css ← shared styles: brand colours, logo, header + mega menu, cursor, popup, footer
assets/css/home-1.css, home-2.css, home-3.css ← styles for each layout
assets/js/main.js   ← mega menu, mobile menu, custom cursor, scroll animations, popup, FAQ, forms
assets/img/favicon.svg
```

## Going live with one layout
1. Pick the layout you like, e.g. `home-2.html`.
2. Rename it to `index.html` (replacing the preview page).
3. You can delete the other two `home-*.html` files and their CSS files.
4. Upload the folder to your hosting, or to Vercel or Netlify.

## Photos
Photos are free Unsplash images loaded from `images.unsplash.com` (free for commercial use). To use your own photo, replace the `src`/`srcset` of that `<img>` with your file, e.g. `assets/img/team.jpg`. **Best:** use real photos of your team, office and projects.

## Things to update before going live
- **Portfolio:** the 8 projects are examples by industry (no client names). Replace them with your real projects, photos and links.
- **About the company:** check the story, mission, vision and the "Founder: Md Sahil" line.
- **Testimonials:** the reviews are placeholders in `[brackets]`. Replace them with real client reviews (for example from your Google Business Profile). Search for `[Client name]`.
- **Social links:** in the footer, `href="#"` on Instagram, LinkedIn, Facebook and YouTube.
- **Blog:** the 3 article cards link to `#blog`. Point them to real article pages once written.
- **Legal pages:** Privacy policy, Terms and Refund policy links in the footer.
- **Prices & FAQ answers:** taken from your current plans (website from ₹9,999, etc.). Check they are still correct.

## How the forms work
The "Start a new project" popup and the contact form open **WhatsApp** with the visitor's details filled in, sent to **+91-9818186876**. To change the number or email, edit the top of `assets/js/agency.js` (and `main.js` for the old layouts):

```js
var WHATSAPP = "919818186876";
var EMAIL = "sahil@growvika.com";
```

## Popup timing
The popup also opens by itself **once per visit after 25 seconds**. Change or turn it off on the `<body>` tag:
`<body data-auto-popup="25">` → use `"0"` to turn auto-open off.

## Brand
- Navy `#0A0F1E`, indigo `#5C6BFF` (logo square), button indigo `#4453F0` (darker, for readable white text)
- Logo and headings: **Syne**; body text: **Manrope** (Google Fonts)
- The logo is built in code (text + square), so it stays sharp at any size.
