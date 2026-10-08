import SERVICES from "../data/services.json";
import AREAS from "../data/areas.json";
import ARTICLES from "../data/articles.json";
import { BASE } from "../lib/site";

export function GET() {
  const paths = ["", "about", "services", ...SERVICES.map((s) => s.slug), "work", "service-area",
    ...AREAS.map((a) => `service-area-${a.slug}`), "blog", ...ARTICLES.map((a) => `blog-${a.slug}`), "faq", "contact"];
  const body = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${paths.map((p) => `  <url><loc>${BASE}/${p}</loc></url>`).join("\n")}
</urlset>
`;
  return new Response(body, { headers: { "Content-Type": "application/xml" } });
}
