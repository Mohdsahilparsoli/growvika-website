from build import *
from articles import ARTICLES

# ---------------- work details ----------------
WORK_DETAIL = {
 "Dental clinic website": ("Patients searched on Google Maps, found an outdated site with no booking option and called the next clinic.",
   ["Treatment pages written for patients","Appointment request with WhatsApp confirmation","Google Business Profile photos, services and posts","Review request flow after every visit"], ["WordPress","Google Business Profile","GA4","WhatsApp"]),
 "Restaurant ordering app": ("Most online orders came through aggregator apps with high commissions and no customer data.",
   ["Menu with categories, add-ons and combos","Cart, UPI / card / COD checkout","Order status updates and push offers","Admin panel for menu, orders and timings"], ["Flutter","Firebase","Razorpay","OneSignal"]),
 "Fashion e-commerce store": ("The brand sold on Instagram DMs — slow replies, manual payments and lost orders.",
   ["Catalogue with sizes, colours and stock","Coupons, combos and COD","Courier booking and tracking links","Meta catalogue for Instagram shopping"], ["Shopify","Razorpay","Shiprocket","Meta Pixel"]),
 "Coaching institute CRM": ("Admission enquiries lived in notebooks and WhatsApp; follow-ups depended on memory.",
   ["Enquiry capture from website and ads","Counselling stages and reminders","Fee instalments and due dates","Reports by course, source and counsellor"], ["Next.js","PostgreSQL","Supabase","PWA"]),
 "Salon local SEO growth": ("A great salon with few online reviews was invisible in “salon near me” searches.",
   ["Google Business Profile optimisation","Monthly reels and offer calendar","Review collection on WhatsApp","Landing page for bridal packages"], ["Google Business Profile","Instagram","Canva","GA4"]),
 "Manufacturer B2B portal": ("Dealers called for prices and stock; quotes were made manually in Excel.",
   ["Product catalogue with specifications","Request-for-quote forms","Dealer login with price lists","Enquiry dashboard for the sales team"], ["Next.js","Node.js","PostgreSQL","Vercel"]),
 "Real-estate lead website": ("Ads sent buyers to a slow brochure PDF — leads were few and poorly qualified.",
   ["Fast project landing pages","Lead forms with budget and timeline","Meta lead campaigns","CRM for site-visit follow-ups"], ["Next.js","Meta Ads","Google Ads","CRM"]),
 "Gym membership app": ("Renewals were tracked on paper and members forgot to renew.",
   ["Membership plans and online renewal","Attendance check-in","Renewal and class reminders","Owner dashboard for revenue and dues"], ["Flutter","Supabase","Razorpay","OneSignal"]),
}

def work_deep(items, label="Project deep-dives", a="How we", b='<em class="s">solved it.</em>'):
    rows = []
    for k, (t, sub, img, cat, tag, d) in enumerate(items):
        ch, built, st = WORK_DETAIL[t]
        rows.append(f'''    <div class="wd{' rev' if k % 2 else ''} rv">
      <div class="wd-img img rv cl"><img src="{U(img,1000)}" alt="{t}" loading="lazy"><span class="wk2-tag">{tag}</span></div>
      <div class="wd-b">
        <small>{sub}</small>
        <h3>{t}</h3>
        <div class="wd-ch"><b>The challenge</b><p>{ch}</p></div>
        <div class="wd-built"><b>What we built</b><ul>{"".join(f'<li><i class="fa-solid fa-check"></i>{x}</li>' for x in built)}</ul></div>
        <div class="wd-st">{"".join(f'<span>{x}</span>' for x in st)}</div>
      </div>
    </div>''')
    return f'''<section class="sec deep">
  <div class="wrap">
{headrow(label, a, b, "A closer look at the problems behind these projects and what we built to fix them.")}
{chr(10).join(rows)}
  </div>
</section>'''

# ---------------- service SEO guide ----------------
def service_guide(s):
    n = s["name"]; low = n.lower()
    blocks = [
     (f"What is included in {low}?", f"<p>{s['lead']} Every project includes {', '.join(t for _, t, _ in s['incl'][:5])} and more — scoped clearly in a fixed quote before work begins.</p>"),
     (f"Who needs {low}?", f"<p>We regularly build for {', '.join(i.lower() for i in s['inds'][:5])} and other growing businesses across Delhi, Gurugram, Noida, Greater Noida, Ghaziabad and Faridabad. If your customers find you on their phones and contact you on WhatsApp, this service is built for that journey.</p>"),
     (f"How long does {low} take?", f"<p>Our process has four clear stages — {', '.join(t.lower() for t, _, _ in s['steps'])}. Timelines depend on scope; you'll see a realistic schedule in your quote and get progress updates on WhatsApp at every stage.</p>"),
     (f"What does {low} cost in Delhi NCR?", "<p>The cost depends on the features, number of pages or screens, integrations and content. Instead of hourly billing, we send a <strong>fixed quote</strong> after a free consultation, so you know the full investment upfront — with no hidden charges later.</p>"),
     (f"How to choose the right {low} partner", "<ul><li>Ask to see similar projects and speak to the people who will build yours.</li><li>Make sure domain, code and data will be in your name.</li><li>Check that SEO basics, speed and mobile testing are included.</li><li>Ask what support looks like after launch.</li></ul>"),
     ("Why businesses choose GrowVika", f"<p>One team builds and markets your project, so {low} connects directly to SEO, ads and a CRM that tracks every lead. You talk directly to the founder, get honest advice and a fixed price — and we stay with you after launch.</p>"),
    ]
    aside = [t for _, t, _ in s["incl"][:6]]
    return seo_copy("Complete guide", f"{n}", '<em class="s">in Delhi NCR.</em>', blocks, f"{s['short']} — what you get", aside, soft=True)

# ---------------- area SEO guide ----------------
def area_guide(a):
    c = a["name"]; pops = [SVC[x] for x in a["pop"]]
    blocks = [
     (f"Growing a business online in {c}", f"<p>{a['intro']} Whether you're in {', '.join(a['locs'][:4])} or anywhere else in {c}, customers compare businesses on Google and Instagram before they call. A clear website, a strong Google Business Profile and fast replies on WhatsApp make the difference.</p>"),
     (f"Website development in {c}", f"<p>We build fast, mobile-first websites for {c} businesses with service pages, area pages and click-to-call and WhatsApp buttons — so visitors from local searches turn into enquiries. Every site includes on-page SEO, Google Analytics and Search Console.</p>"),
     (f"Local SEO and Google Maps in {c}", f"<p>Ranking in Google Maps for searches like “near me” in {c} depends on a complete, active Google Business Profile, consistent contact details, real photos and genuine reviews. We set this up and keep it active with posts and review requests.</p>"),
     (f"Apps, CRM and software for {c} businesses", f"<p>For {', '.join(i.lower() for i in a['inds'][:3])} and more, we build mobile apps, CRMs and custom tools that replace spreadsheets — so every lead is followed up and every booking, payment and renewal is tracked.</p>"),
     (f"Popular services in {c}", "<ul>" + "".join(f'<li><a href="{s["slug"]}.html">{s["name"]}</a> — {s["card"]}</li>' for s in pops) + "</ul>"),
     (f"Meet us in {c}", f"<p>The first meeting at your office in {c} is free. After that, most work happens on WhatsApp and video calls, with in-person visits whenever they help.</p>"),
    ]
    return seo_copy(f"{c} guide", "Digital marketing &amp;", f'<em class="s">development in {c}.</em>', blocks, f"Why {c} businesses choose us", ["Free first meeting in " + c, "Local SEO for your area", "Websites, apps, CRM &amp; ads", "Fixed quotes, no hidden cost", "Same-day WhatsApp replies", "You own everything"], soft=True)

# ---------------- article pages ----------------
def article_page(art):
    rel = [x for x in ARTICLES if x["slug"] != art["slug"]][:3]
    secs = art["sections"]
    def sid(h): return "s-" + re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", h).lower()).strip("-")
    toc = "".join(f'<li><a href="#{sid(h)}">{h}</a></li>' for h, _ in secs)
    body = "\n".join(f'<h2 id="{sid(h)}">{h}</h2>\n{html}' for h, html in secs)
    take = "".join(f'<li><i class="fa-solid fa-check"></i>{t}</li>' for t in art["takeaways"])
    faqh = "\n".join(f'''<div class="qa{' open' if k==0 else ''}"><button type="button" aria-expanded="{'true' if k==0 else 'false'}">{q}<i class="fa-solid fa-plus"></i></button><div class="ans"><div><p>{a}</p></div></div></div>''' for k, (q, a) in enumerate(art["faq"]))
    url = f"{BASE}/blog-{art['slug']}"
    share = f'''<div class="share"><span>Share</span><a href="https://wa.me/?text={art['title'].replace(' ','%20')}%20{url}" target="_blank" rel="noopener" aria-label="Share on WhatsApp"><i class="fa-brands fa-whatsapp"></i></a><a href="https://www.linkedin.com/sharing/share-offsite/?url={url}" target="_blank" rel="noopener" aria-label="Share on LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a><a href="https://twitter.com/intent/tweet?url={url}" target="_blank" rel="noopener" aria-label="Share on X"><i class="fa-brands fa-x-twitter"></i></a><button type="button" data-copy="{url}" aria-label="Copy link"><i class="fa-solid fa-link"></i></button></div>'''
    hero = f'''<section class="art-hero">
  <div class="wrap">
    <div class="ah-txt rv">
      {crumbs([("blog.html","Blog"),(None, art["cat"])])}
      <span class="ah-cat">{art["cat"]}</span>
      <h1>{art["title"]}</h1>
      <p class="lead">{art["desc"]}</p>
      <div class="ah-meta"><span class="av">MS</span><div><b>Md Sahil</b><small>Founder, GrowVika</small></div><span class="dot"></span><span><i class="fa-regular fa-calendar"></i>8 Oct 2026</span><span><i class="fa-regular fa-clock"></i>{art["mins"]} read</span></div>
    </div>
    <div class="ah-img img rv cl"><img src="{U(art['img'],1400)}" alt="{art['title']}" fetchpriority="high"></div>
  </div>
</section>'''
    main = f'''<section class="sec art">
  <div class="wrap art-g">
    <aside class="art-side">
      <div class="toc"><h4>In this article</h4><ol>{toc}</ol></div>
      {share}
    </aside>
    <article class="prose art-body">
      <p class="art-intro">{art["intro"]}</p>
{body}
      <div class="takeaways"><h3><i class="fa-solid fa-lightbulb"></i> Key takeaways</h3><ul>{take}</ul></div>
      <h2 id="faq">Frequently asked questions</h2>
      <div class="art-faq">{faqh}</div>
      <div class="author"><span class="av">MS</span><div><b>Written by Md Sahil</b><p>Founder of GrowVika. Builds websites, apps and CRMs for businesses across Delhi NCR — and runs the marketing that brings them customers.</p><a href="about.html" class="link">About GrowVika <i class="fa-solid fa-arrow-right"></i></a></div></div>
      <div class="art-cta"><div><h3>Want us to do this for you?</h3><p>Free consultation, fixed quote and a reply the same day.</p></div><button type="button" class="btn btn-w" data-open-modal>Start a project <i class="fa-solid fa-arrow-right"></i></button></div>
    </article>
  </div>
</section>'''
    relc = "\n".join(f'''      <a href="blog-{r['slug']}.html" class="bc rv" data-cursor="view"><div class="img"><img src="{U(r['img'],800)}" alt="{r['title']}" loading="lazy"><span class="cat">{r['cat']}</span></div><div class="meta"><span><i class="fa-regular fa-folder"></i>{r['folder']}</span><span><i class="fa-regular fa-clock"></i>{r['mins']}</span></div><h3>{r['title']}</h3><p>{r['desc']}</p><span class="rm">Read article <i class="fa-solid fa-arrow-right"></i></span></a>''' for r in rel)
    related = f'''<section class="sec soft">
  <div class="wrap">
{headrow("Keep reading", "Related", '<em class="s">articles.</em>', right='<a href="blog.html" class="btn btn-o rv">All articles</a>')}
    <div class="bl-grid">
{relc}
    </div>
  </div>
</section>'''
    art_ld = ld({"@context":"https://schema.org","@type":"BlogPosting","headline":art["title"],"description":art["desc"],"image":U(art["img"],1200),
       "datePublished":"2026-10-08","dateModified":"2026-10-08","author":{"@type":"Person","name":"Md Sahil"},
       "publisher":{"@type":"Organization","name":"GrowVika"},"mainEntityOfPage":url})
    return page(f"blog-{art['slug']}.html", f"{art['title']} | GrowVika Blog", art["desc"], "blog",
       [hero, main, related, svc_cards(SERVICES, "Need help?", "Let us", '<em class="s">do it for you.</em>', "Everything in this article is something we can set up for you.", soft=False), enquiry()],
       schema=art_ld, ogimg=art["img"], crumbs_ld=[("Blog","blog"),(art["title"], f"blog-{art['slug']}")])
