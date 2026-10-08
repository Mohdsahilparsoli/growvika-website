import IMG from "../data/img.json";

export const BASE = "https://growvika-website.vercel.app";
export const WA = "919818186876";
export const PHONE = "+91-9818186876";
export const EMAIL = "sahil@growvika.com";

/** Cache-busting version for CSS/JS — set once per build. */
export const VER = new Date().toISOString().replace(/\D/g, "").slice(0, 12);

/** Search engines: keep the whole site out of the index until launch. */
export const NOINDEX = true;

/** Unsplash image URL from a key in data/img.json (or a raw photo id). */
export function U(key: string, w = 900): string {
  const id = (IMG as Record<string, string>)[key] ?? key;
  return `https://images.unsplash.com/${id}?auto=format&fit=crop&w=${w}&q=70`;
}

/** Two-digit index: 1 -> "01". */
export const pad = (n: number) => String(n).padStart(2, "0");

/** Data strings are stored HTML-escaped (&amp;). Decode for attributes (Astro re-escapes). */
export const dec = (s: string) => s.replace(/&amp;/g, "&");

/** Strip tags + decode — for JSON-LD and plain-text uses. */
export const plain = (s: string) => s.replace(/<[^>]+>/g, "").replace(/&amp;/g, "&");

export const ld = (obj: unknown) =>
  `<script type="application/ld+json">${JSON.stringify(obj)}</script>`;
