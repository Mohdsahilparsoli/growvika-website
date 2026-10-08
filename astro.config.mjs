import { defineConfig } from "astro/config";

// Static site. Pages are emitted as about.html, services.html … so every
// existing link (and Vercel cleanUrls: /about) keeps working.
export default defineConfig({
  site: "https://growvika-website.vercel.app",
  build: { format: "file" },
  compressHTML: false,
  trailingSlash: "ignore",
});
