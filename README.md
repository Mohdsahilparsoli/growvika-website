# GrowVika website

Built with **[Astro](https://astro.build)**: a static site with no client framework. The output is plain HTML, CSS and JS in `dist/`.

```bash
npm install
npm run dev      # local dev server at http://localhost:4321
npm run build    # static build into dist/
npm run preview  # serve the build
```

Vercel builds the site automatically from `vercel.json` (`npm run build`, output `dist`, `cleanUrls`, so `/about` serves `about.html`).

## Folder structure

```
src/
  layouts/Base.astro       ← <head> (SEO, Open Graph, JSON-LD), header, footer, popup, scripts
  pages/                   ← one file per page (routes)
    index.astro            ← home
    about.astro  services.astro  work.astro  service-area.astro  blog.astro  faq.astro  contact.astro
    [service].astro        ← 6 service pages  (website-development.html …)
    service-area-[city].astro ← 6 city pages (service-area-delhi.html …)
    blog-[slug].astro      ← 9 article pages  (blog-*.html)
    sitemap.xml.ts         ← sitemap generated from the data
  components/              ← reusable sections (PageHero, Split, Incl, SvcCards, Faq, Promise, Enquiry …)
    home/                  ← homepage-only sections
  data/*.json              ← ALL content: services, areas, work, articles, FAQs, reviews, images …
  lib/site.ts              ← BASE url, WhatsApp number, image helper, NOINDEX switch
public/
  assets/css/agency.css    ← site styles
  assets/js/agency.js      ← menus, sliders, cursor, popup, forms, animations
  robots.txt
  home-1/2/3.html, layouts.html ← old layouts (kept for reference, e.g. /home-2)
```

## Editing content
- **Text, services, cities, projects, FAQs and articles** live in `src/data/*.json`. Edit the JSON and rebuild. Every page that uses that item updates.
- **Page layout** (which sections a page shows, and in what order) is in `src/pages/*.astro`.
- **Section numbers** (01, 02 …) are added automatically in page order by `Base.astro`.
- **Reviews ("Our promise")** are SAMPLE data in `src/data/sample_reviews.json`, with the shape `[tag, icon, stars, business, city, text]`. Replace them with real Google reviews, or load them dynamically in `src/components/Promise.astro`.
- **Images** are Unsplash ids in `src/data/img.json`. Use `U("key", width)` in components.

## Search engines (noindex)
The site is currently **hidden from Google**. Three settings do this:
1. `<meta name="robots" content="noindex, nofollow">` on every page, controlled by `NOINDEX` in `src/lib/site.ts`.
2. `Disallow: /` in `public/robots.txt`.
3. An `X-Robots-Tag: noindex, nofollow` header in `vercel.json`.

**At launch:** set `NOINDEX = false`, remove `Disallow: /`, delete the X-Robots-Tag header, and change `BASE` (in `src/lib/site.ts`) and `site` (in `astro.config.mjs`) to `https://growvika.com`.

## How the forms work
The "Start a new project" popup and the enquiry forms send the details to **sahil@growvika.com** through the free FormSubmit service.
- The **first** enquiry triggers a one-time activation email to that inbox. Click the link in it once, and every enquiry after that arrives automatically.
- If FormSubmit is unreachable, the visitor's email app opens with the details filled in.
- To change the inbox, edit `INBOX` in `public/assets/js/agency.js`.

## Popup timing
The popup opens by itself once per visit after 25 seconds on the home page. This is the `popup={25}` prop in `src/pages/index.astro`; use `0` to turn it off.

## Things to update before going live
- Real client reviews, the Google rating, and the Google reviews link (`.gr-btn` in `Promise.astro`).
- Social links in the footer (`href="#"`).
- Privacy policy, Terms and Refunds pages.
- The portfolio projects in `src/data/work.json`: replace the example projects with real ones.

## Brand
- Navy `#0A0F1E`, indigo `#5C6BFF` (logo square), button indigo `#4453F0`.
- Fonts: **Syne** for headings, **Fraunces** italic for accent words, **Plus Jakarta Sans** for body text.
- Icons: Font Awesome.
