import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from build import *
from more import *

out = []

# ======================= ABOUT =======================
out.append(page("about.html", "About GrowVika | Website, App, CRM &amp; Marketing Agency in Delhi NCR",
 "GrowVika is a founder-led digital agency in Delhi NCR building websites, apps, CRMs and custom software — and marketing them. Meet the team and how we work.", "about", [
 page_hero([(None, "About us")], "One team that builds", "and <em class=\"s\">grows.</em>",
   "GrowVika is a founder-led digital agency in Delhi NCR. We design and build websites, apps, CRMs and custom software — and run the marketing that brings customers to them.", "team",
   b1=("fa-solid fa-user-tie","Founder-led","you work with the builder"), b2=("fa-solid fa-layer-group","11+ services","under one roof")),
 marquee(["Websites", "Mobile apps", "CRM", "Custom software", "SEO", "Social media", "Google &amp; Meta Ads"]),
 split("Our story", "Why we started", "<em class=\"s\">GrowVika.</em>",
   "Most local businesses end up with one person for the website, another for ads, and a spreadsheet for leads. Nothing talks to each other, and the owner is stuck in the middle. We started GrowVika to put it all under one roof — so the site, the app, the CRM and the marketing work together.",
   ["Founded and run by Md Sahil","Builders and marketers in one team","We use our own CRM to run the business","Clear quotes, honest advice, real support"], img="meeting", img2="desk"),
 incl("What we stand for", "Mission, vision", "&amp; <em class=\"s\">values.</em>", [
   ("fa-bullseye","Our mission","Give every growing business a professional online presence at a fair, fixed price."),
   ("fa-eye","Our vision","Be the first team NCR businesses call when they want to grow online."),
   ("fa-comments","Honest advice","We tell you what you need — and what you don't."),
   ("fa-file-signature","Transparent pricing","Fixed quotes before work starts. No surprise bills."),
   ("fa-clock","On-time delivery","Clear timelines and regular updates on WhatsApp."),
   ("fa-handshake","Long-term support","We stay after launch for fixes, updates and growth."),
   ("fa-mobile-screen","Mobile-first","Everything is designed for phones first."),
   ("fa-lock","You own it","Domain, code and data stay in your name.")], soft=True),
 nums([("11+","Services under one roof"),("6","Cities across Delhi NCR"),("1","Team for build &amp; marketing"),("7–15","Days to launch most websites")]),
 svc_cards(SERVICES, soft=True),
 split("Meet the founder", "Hi, I'm", "<em class=\"s\">Md Sahil.</em>",
   "I build the websites, apps and CRMs myself, with a small team of designers and marketers. When you work with GrowVika, you talk to me directly — about your business, your customers and what will actually bring results. No sales scripts.",
   ["You get my WhatsApp, not a ticket number","I'll tell you honestly if you don't need something","Every project is checked by me before launch"], img="smiling", rev=True,
   extra='<div class="sign rv" style="margin-top:26px"><div class="who"><span>MS</span><div><b>Md Sahil</b><small>Founder, GrowVika</small></div></div><a href="contact.html" class="link">Talk to me <i class="fa-solid fa-arrow-right"></i></a></div>'),
 process(),
 why(),
 industries(),
 promise(),
 faq(FAQ_GROUPS[0][3] + FAQ_GROUPS[5][3][:2]),
 enquiry(),
]))

# ======================= SERVICES LISTING =======================
out.append(page("services.html", "Services | Websites, Apps, CRM, Software &amp; Marketing | GrowVika",
 "All GrowVika services: website development, e-commerce stores, mobile apps, CRM, custom software and digital marketing for businesses in Delhi NCR.", "services", [
 page_hero([(None, "Services")], "Everything you need", "to <em class=\"s\">grow online.</em>",
   "Websites, online stores, mobile apps, CRMs, custom software and digital marketing — designed, built and grown by one team in Delhi NCR.", "code",
   b1=("fa-solid fa-bolt","Live in 7–15 days","for most business websites"), b2=("fa-solid fa-file-signature","Fixed quotes","no hidden charges"),
   chips=[s["short"] for s in SERVICES]),
 svc_cards(SERVICES, "Our services", "Six ways we", "<em class=\"s\">help you grow.</em>", "Each service has its own page with what's included, process and FAQs."),
 marquee(["Design", "Develop", "Launch", "Rank", "Advertise", "Automate", "Support"]),
 split("Build + grow", "Build it right.", "<em class=\"s\">Then grow it.</em>",
   "Most agencies either build or market. We do both — so your website is made to convert, your ads land on the right page, and every lead goes straight into your CRM. One team, one plan, one point of contact.",
   ["Websites, stores and apps that convert","SEO, social media and ads that bring traffic","CRM and software that manage every lead","One WhatsApp group with the whole team"], img="team", img2="marketing"),
 incl("What's always included", "Included in", "<em class=\"s\">every project.</em>", [
   ("fa-comments","Free consultation","We understand your business before quoting."),
   ("fa-file-signature","Fixed quote","Scope and cost agreed before we start."),
   ("fa-mobile-screen","Mobile-first","Designed and tested for phones first."),
   ("fa-magnifying-glass","SEO foundations","Clean structure that Google can read."),
   ("fa-brands fa-whatsapp","WhatsApp updates","Progress shared regularly, in plain words."),
   ("fa-graduation-cap","Training","We show your team how to use everything."),
   ("fa-lock","Full ownership","Domain, code and data in your name."),
   ("fa-headset","Post-launch support","Fixes and help after you go live.")], soft=True),
 process(),
 types("Packages", "Common", "<em class=\"s\">starting points.</em>", [
   ("Launch kit","Business website + Google Business Profile + WhatsApp setup."),
   ("Sell online","E-commerce store + payments + shipping + Meta catalogue."),
   ("Lead machine","Landing page + Meta/Google ads + CRM for follow-ups."),
   ("Automate","Custom CRM or software to replace spreadsheets.")], "Not sure what you need? These combinations work for most businesses — we'll tailor the exact scope."),
 why(),
 work_grid(WORK[:6], soft=True),
 stack("Tools &amp; tech", "Modern tools,", "<em class=\"s\">proven stack.</em>"),
 industries(),
 promise(),
 faq(FAQ_GROUPS[1][3] + FAQ_GROUPS[2][3][:2]),
 enquiry(),
]))

# ======================= SINGLE SERVICES =======================
for s in SERVICES:
    others = [x for x in SERVICES if x["slug"] != s["slug"]]
    rel = [w for w in WORK if (s["slug"].split("-")[0] in w[3]) or (s["slug"] == "website-development" and w[3] == "website") or (s["slug"] == "ecommerce-development" and w[3] == "ecommerce") or (s["slug"] == "mobile-app-development" and w[3] == "app") or (s["slug"] == "crm-development" and w[3] == "crm") or (s["slug"] == "custom-software-development" and w[3] == "software") or (s["slug"] == "digital-marketing" and w[3] == "marketing")]
    rel = (rel + [w for w in WORK if w not in rel])[:3]
    out.append(page(f'{s["slug"]}.html', f'{s["name"]} in Delhi NCR | GrowVika',
     f'{s["name"]} by GrowVika for businesses in Delhi, Gurugram, Noida and NCR. {s["card"]} Free consultation and fixed quotes.', "services", [
     page_hero([("services.html", "Services"), (None, s["name"])], s["h1"][0], s["h1"][1], s["lead"], s["img"],
        b1=("fa-solid " + s["icon"], s["name"], s["tag"]), b2=("fa-solid fa-file-signature","Fixed quote","free first consultation")),
     marquee([s["short"]] + s["stack"][:6]),
     split("Overview", s["overview"][0], None, s["overview"][1], s["overview"][2], img=s["img2"], img2=s["img"]),
     incl("What's included", "Everything you", "<em class=\"s\">need.</em>", s["incl"], soft=True),
     types("Types", "What we", "<em class=\"s\">build.</em>", s["types"], "Tell us which one fits — or describe your idea and we'll suggest the right approach."),
     service_guide(s),
     process([(t, d, w) for t, d, w in s["steps"]], a="How it", b="<em class=\"s\">works.</em>"),
     why(),
     industries([(i, f"{s['name']} for {i.lower() if i[0].isupper() and not i.isupper() else i} — planned around how your customers search, compare and contact you, with mobile-first design, WhatsApp enquiries and SEO built in from day one.", INDUSTRIES[k % 6][2]) for k, i in enumerate(s["inds"])], "Who it's for", f"Built for <em class=\"s\">your industry.</em>", "Industries we regularly build for."),
     stack("Tools &amp; tech", "Technology", "<em class=\"s\">we trust.</em>", s["stack"], "Proven, well-supported tools — so your project is easy to maintain."),
     work_grid(rel, "Related work", "Examples of", "<em class=\"s\">our work.</em>", soft=True),
     svc_cards(SERVICES, "Other services", "Works great", "<em class=\"s\">together.</em>", "Combine services for the best results.", exclude=s["slug"]),
     promise(),
     faq(s["faq"], a=f"{s['short']}", b="<em class=\"s\">questions.</em>"),
     enquiry(a=f"Let's talk about your", b=f"<em class=\"s\">{s['short'].lower()}.</em>"),
    ]))

# ======================= WORK =======================
out.append(page("work.html", "Our Work | Websites, Apps &amp; CRM Projects | GrowVika",
 "Examples of websites, online stores, mobile apps, CRMs, custom software and marketing GrowVika builds for businesses in Delhi NCR.", "work", [
 page_hero([(None, "Work")], "Work that", "<em class=\"s\">works.</em>",
   "Websites, stores, apps, CRMs and campaigns for clinics, restaurants, retailers, institutes and manufacturers across Delhi NCR.", "desk",
   b1=("fa-solid fa-layer-group","8+ project types","websites to CRMs"), b2=("fa-solid fa-mobile-screen","Mobile-first","tested on real phones")),
 work_grid(WORK, "All projects", "Selected", "<em class=\"s\">projects.</em>", filt=True, lead="Filter by type. Each card is an example of the kind of project we build for that industry."),
 work_deep(WORK),
 incl("Every project", "What every project", '<em class="s">includes.</em>', [
   ("fa-comments","Discovery call","We learn your customers, competitors and goals."),
   ("fa-pen-ruler","Design approval","You approve designs before any code is written."),
   ("fa-mobile-screen","Mobile testing","Tested on real Android and iPhone devices."),
   ("fa-gauge-high","Speed checks","Optimised images and code for fast loading."),
   ("fa-magnifying-glass","SEO setup","Titles, meta, sitemap, Search Console and analytics."),
   ("fa-brands fa-whatsapp","Lead capture","Call, WhatsApp and forms wired to you or your CRM."),
   ("fa-graduation-cap","Handover &amp; training","Logins, documentation and a walkthrough for your team."),
   ("fa-headset","Post-launch support","Fixes and help after you go live.")], soft=True),
 seo_copy("Our work", "Websites, apps &amp; CRM", '<em class="s">built for Delhi NCR.</em>', [
   ("What kind of projects do we build?","<p>From <a href=\"website-development.html\">business websites</a> and <a href=\"ecommerce-development.html\">online stores</a> to <a href=\"mobile-app-development.html\">mobile apps</a>, <a href=\"crm-development.html\">CRMs</a> and <a href=\"custom-software-development.html\">custom software</a> — plus the <a href=\"digital-marketing.html\">SEO, social media and ads</a> that bring customers to them.</p>"),
   ("Industries we build for","<p>Clinics and dentists, restaurants and cafés, fashion and lifestyle brands, coaching institutes, salons and gyms, real-estate developers, manufacturers and B2B suppliers across Delhi, Gurugram, Noida, Greater Noida, Ghaziabad and Faridabad.</p>"),
   ("How we measure success","<ul><li>Faster pages that work well on mobile</li><li>More calls, WhatsApp chats and form enquiries — tracked, not guessed</li><li>Fewer lost leads thanks to follow-up reminders</li><li>Less time spent on spreadsheets and manual work</li></ul>"),
   ("Want to see a project like yours?","<p>Many clients prefer privacy, so we share live links and references one-to-one. Message us on WhatsApp with your industry and we'll send relevant examples.</p>")],
   "Ask for examples", ["Live links on request","Projects in your industry","Talk to the builder","Free consultation"]),
 split("Case study", "Dental clinic:", "<em class=\"s\">from Google to booked.</em>",
   "<b>The challenge:</b> patients searched on Google Maps, found an outdated site and called a competitor. <b>What we built:</b> a fast treatment-focused website with online appointment requests, WhatsApp booking, Google Business Profile optimisation and review requests after every visit.",
   ["Treatment pages written for patients, not doctors","Appointment request → WhatsApp in one tap","Google Maps profile, photos and posts","Simple CRM to follow up on enquiries"], img="clinic", img2="phone", soft=True),
 marquee(["Clinics", "Restaurants", "Fashion", "Coaching", "Salons", "Manufacturers", "Real estate", "Gyms"]),
 svc_cards(SERVICES, "By service", "What we", "<em class=\"s\">build.</em>", "Explore each service to see what's included."),
 process(),
 split("Our approach", "Simple, fast", "<em class=\"s\">and measurable.</em>",
   "Every project starts with your customer: what they search, what they need to see, and what makes them call. We design for that, build it fast, and track enquiries after launch so we can keep improving.",
   ["Designed around real customer questions","Speed and mobile tested before launch","Analytics and lead tracking from day one"], img="sketch", rev=True),
 industries(),
 stack("Tools &amp; tech", "Built with", "<em class=\"s\">modern tools.</em>"),
 why(),
 promise(),
 faq([("Can I see live examples?","Yes — ask us on WhatsApp and we'll share live links to projects similar to yours."),("Why don't you show client names?","Many clients prefer privacy. We share references and links one-to-one when you ask."),("Can you redesign my current website?","Yes. We'll review it first and tell you honestly whether to improve or rebuild."),("Do you work with startups?","Yes — from first websites and MVP apps to CRMs as you grow.")]),
 enquiry(),
]))

# ======================= SERVICE AREA LISTING =======================
area_slider = AREA_SLIDER.replace('<div class="idx rv"><b>08</b><span>Service area</span></div>', idx("Explore"))
out.append(page("service-area.html", "Service Area | Delhi, Gurugram, Noida, Ghaziabad, Faridabad | GrowVika",
 "GrowVika serves businesses across Delhi NCR — Delhi, Gurugram, Noida, Greater Noida, Ghaziabad and Faridabad — with websites, apps, CRM and digital marketing.", "areas", [
 page_hero([(None, "Service area")], "Your neighbourhood", "<em class=\"s\">digital team.</em>",
   "We work with businesses across Delhi NCR — in person at your office or fully online. Pick your city to see the areas we cover and what local businesses need most.", "india_gate",
   b1=("fa-solid fa-city","6 cities","across Delhi NCR"), b2=("fa-solid fa-handshake","Free first meeting","at your office"),
   chips=[a["name"] for a in AREAS]),
 city_cards(),
 seo_copy("Delhi NCR guide", "Digital agency for", '<em class="s">all of Delhi NCR.</em>', [
   ("One team across six cities","<p>GrowVika works with businesses in " + ", ".join(f'<a href="service-area-{a["slug"]}.html">{a["name"]}</a>' for a in AREAS) + ". Each city has its own customers, competitors and search habits — so we build local pages, local SEO and campaigns targeted to the areas you actually serve.</p>"),
   ("Websites and local SEO","<p>Customers search “near me” on their phones. We build fast, mobile-first websites with service and area pages, and set up your Google Business Profile so you appear in Google Maps for your neighbourhood.</p>"),
   ("Apps, CRM and software","<p>From restaurant ordering apps in Gurugram to admission CRMs in Noida and B2B portals in Faridabad, we build software that fits how NCR businesses work — with UPI payments, WhatsApp and Hindi/English content.</p>"),
   ("How we work with you","<ul><li>Free first meeting at your office anywhere in Delhi NCR</li><li>Fixed quote before work begins</li><li>Updates on WhatsApp and video calls</li><li>Support after launch, one message away</li></ul>")],
   "Serving Delhi NCR", [a["name"] for a in AREAS]),
 area_slider,
 split("Local + online", "Local when it helps,", "<em class=\"s\">online when it's faster.</em>",
   "Meet us at your office for the first conversation, then work together on WhatsApp and video calls. You get a local team that understands NCR customers — without wasting time in traffic.",
   ["Free first meeting anywhere in Delhi NCR","Updates on WhatsApp, calls when needed","Online projects across India too"], img="meeting", img2="pair", soft=True),
 incl("Why local matters", "Built for", "<em class=\"s\">NCR customers.</em>", [
   ("fa-location-dot","Local SEO","Rank for searches like “near me” in your area."),
   ("fa-language","Hindi + English","Content that speaks to your customers."),
   ("fa-brands fa-whatsapp","WhatsApp-first","How NCR customers prefer to enquire."),
   ("fa-indian-rupee-sign","UPI & COD","Payments customers here trust."),
   ("fa-map","Google Maps","Profile, photos, posts and reviews strategy."),
   ("fa-mobile-screen","Mobile-first","Most local searches happen on phones."),
   ("fa-handshake","In-person meetings","Meet the team before you decide."),
   ("fa-clock","Same-day replies","Quick answers during business hours.")]),
 svc_cards(SERVICES, "Available everywhere", "Services in", "<em class=\"s\">every city.</em>", "All services are available across Delhi NCR.", soft=True),
 marquee([l for a in AREAS for l in a["locs"][:2]]),
 process(),
 industries(),
 why(),
 promise(),
 faq([("Do you only work in Delhi NCR?","Our home market is Delhi NCR, but we work online with businesses across India."),("Is the first meeting really free?","Yes. We'll meet at your office in Delhi NCR or on a video call — no charge, no obligation."),("Is my area covered?","If you're anywhere in Delhi, Gurugram, Noida, Greater Noida, Ghaziabad or Faridabad — yes."),("Do you charge more for travel?","No. Meetings within Delhi NCR are part of the project.")]),
 enquiry(),
]))

# ======================= SINGLE AREAS =======================
for a in AREAS:
    svcs = [SVC[x] for x in a["pop"]]
    near = [AREA[x] for x in a["near"]]
    out.append(page(f'service-area-{a["slug"]}.html', f'Website, App &amp; Digital Marketing Agency in {a["name"]} | GrowVika',
     f'GrowVika builds websites, apps, CRMs and runs digital marketing for businesses in {a["name"]} — {", ".join(a["locs"][:5])} and nearby. Free first meeting.', "areas", [
     page_hero([("service-area.html", "Service area"), (None, a["name"])], "Digital agency in", f'<em class="s">{a["name"]}.</em>', a["intro"], a["img"],
        b1=("fa-solid fa-location-dot", a["name"], a["tag"]), b2=("fa-solid fa-handshake","Free first meeting",f"at your office in {a['name']}"),
        chips=a["locs"][:6]),
     marquee(a["locs"]),
     split("Why GrowVika", f"A local team for", f'<em class="s">{a["name"]} businesses.</em>',
        f'Customers in {a["name"]} search on their phones, compare a few options on Google Maps, and message the one that looks most trustworthy. We help you be that business — with a fast website, an optimised Google profile, social media that builds trust and a CRM so no enquiry is missed.',
        ["Free first meeting at your office", "Local SEO for your exact area", "Websites, apps, CRM and marketing in one team", "Replies on WhatsApp the same day"], img=a["img2"], img2=a["img3"]),
     localities(a),
     area_guide(a),
     svc_cards(SERVICES, f"Services in {a['name']}", "Everything you need", f'<em class="s">in {a["name"]}.</em>', "All our services are available here."),
     incl("Popular here", f"What {a['name']}", '<em class="s">businesses ask for.</em>', [(s["icon"], s["name"], SVC_LONG[s["slug"]]) for s in svcs] + [("fa-location-dot","Google Business Profile",f"Complete, active Google Business Profile with the right categories, services, photos, posts and a review strategy — so you show up in Google Maps and “near me” searches across {a['name']}."),("fa-brands fa-whatsapp","WhatsApp enquiries",f"Click-to-chat buttons on your website, ads and profile, with ready message templates — the way most customers in {a['name']} prefer to enquire."),("fa-hashtag","Social media",f"Monthly content calendar with reels, posts and stories that show your work, your team and your offers to people around {a['name']}."),("fa-chart-line","Monthly reports","Clear monthly reports showing calls, WhatsApp chats, form leads, rankings and ad costs — plus what we'll improve next month."),("fa-handshake","Local meetings",f"Free first meeting at your office in {a['name']}, then regular updates on WhatsApp and video calls, with visits whenever they help.")], soft=True),
     industries([(i, f"Websites, local SEO, social media and CRM for {i.lower()} in {a['name']} — so nearby customers find you on Google Maps, trust what they see and contact you on WhatsApp.", INDUSTRIES[k % 6][2]) for k, i in enumerate(a["inds"])], f"Industries in {a['name']}", f'Who we help <em class="s">here.</em>', "Common businesses we work with in this area."),
     process(),
     work_grid(WORK[:3], "Examples", "The kind of work", '<em class="s">we do.</em>', soft=True),
     why(stat=("1:1", f"founder-led for {a['name']}")),
     map_sec(a["q"]),
     city_cards(exclude=a["slug"], label="Nearby", a="We also", b='<em class="s">serve.</em>', lead="Other cities across Delhi NCR.", soft=True),
     faq([(f"Do you have clients in {a['name']}?", f"We work with businesses across Delhi NCR including {a['name']}. Ask us for examples similar to your business."),
          (f"Can we meet in {a['name']}?", f"Yes. The first meeting at your office in {a['name']} is free, or we can talk on a video call."),
          (f"Which areas of {a['name']} do you cover?", f"All of {a['name']} — including {', '.join(a['locs'][:5])} and nearby."),
          ("How long does a website take?", "Most business websites go live in 7–15 days after we receive your content."),
          ("Do you also run local ads?", f"Yes — Google and Meta ads targeted to customers in and around {a['name']}.")], a=a["name"], b='<em class="s">FAQs.</em>'),
     enquiry(a="Let's grow your business", b=f'<em class="s">in {a["name"]}.</em>'),
    ]))

# ======================= BLOG LISTING =======================
feat = POSTS[0]
grid = "\n".join(f'''      <a href="blog-{sl}.html" class="bc rv" data-cat="{c}" data-cursor="view"><div class="img"><img src="{U(img,800)}" alt="{t}" loading="lazy"><span class="cat">{c}</span></div><div class="meta"><span><i class="fa-regular fa-folder"></i>{f}</span><span><i class="fa-regular fa-clock"></i>{m}</span></div><h3>{t}</h3><p>{d}</p><span class="rm">Read article <i class="fa-solid fa-arrow-right"></i></span></a>''' for c, f, m, img, t, d, sl in POSTS)
blog_list = f'''<section class="sec">
  <div class="wrap">
{headrow("Latest articles", "Practical guides", '<em class="s">for growing businesses.</em>', "Short, useful articles about websites, Google, social media, apps and CRM.")}
    <div class="wf rv" role="tablist">{"".join(f'<button type="button" class="{"on" if k==0 else ""}" data-bf="{c}">{c}</button>' for k, c in enumerate(BLOG_CATS))}</div>
    <div class="bl-grid">
{grid}
    </div>
  </div>
</section>'''
featured = f'''<section class="sec soft">
  <div class="wrap">
    <a href="blog-{feat[6]}.html" class="feat-post rv" data-cursor="view">
      <div class="img"><img src="{U(feat[3],1100)}" alt="" loading="lazy"></div>
      <div class="fp-b"><span class="cat">Featured · {feat[0]}</span><h2>{feat[4]}</h2><p>{feat[5]} We break down the pages, features and content that actually bring enquiries — and what you can skip.</p><div class="meta"><span><i class="fa-regular fa-folder"></i>{feat[1]}</span><span><i class="fa-regular fa-clock"></i>{feat[2]} read</span></div><span class="rm">Read article <i class="fa-solid fa-arrow-right"></i></span></div>
    </a>
  </div>
</section>'''
cats = incl("Topics", "Browse by", '<em class="s">topic.</em>', [("fa-code","Websites","Design, speed, content and conversions."),("fa-location-dot","Local SEO","Google Maps, reviews and near-me searches."),("fa-users-gear","CRM","Leads, follow-ups and sales process."),("fa-mobile-screen","Apps","When you need one and what it costs to run."),("fa-hashtag","Social media","Reels, posting plans and content ideas."),("fa-bullhorn","Ads","Meta and Google ads for local businesses."),("fa-bag-shopping","E-commerce","Stores, payments, shipping and growth."),("fa-gears","Software","Automating the work spreadsheets can't handle.")], soft=True)
start_here = types("Start here", "New to", '<em class="s">going online?</em>', [("Get your Google Business Profile right","The free listing that brings the most local calls."),("Build a website that answers questions","What to say on each page so visitors call you."),("Set up WhatsApp enquiries","Make it one tap for customers to message you."),("Track every lead","A simple CRM so no enquiry is ever forgotten.")], "Four steps we recommend to every local business.")
tips = incl("Quick tips", "Six tips you can", '<em class="s">use today.</em>', [("fa-image","Compress your images","Big photos are the #1 reason sites are slow on phones."),("fa-star","Ask for reviews","Send a review link on WhatsApp after every happy customer."),("fa-phone","Show your number","Put a click-to-call button at the top of every page."),("fa-clock","Reply fast","Leads answered in 5 minutes convert far better than next day."),("fa-camera","Post real photos","Real photos of your team and work build trust."),("fa-bullseye","One goal per page","Each page should ask for one action: call, chat or book.")], dark=True)
ask = split("Ask us", "Have a question", '<em class="s">we should answer?</em>', "Tell us what you'd like to learn — we write articles based on real questions from business owners in Delhi NCR. Or just ask us directly on WhatsApp.", ["Websites, SEO, apps, CRM or ads","Answered in plain words","Free — no strings attached"], img="laptop_mug", rev=True,
   extra=f'<a href="https://wa.me/{WA}" target="_blank" rel="noopener" class="btn btn-i rv" style="margin-top:24px"><i class="fa-brands fa-whatsapp"></i> Ask on WhatsApp</a>')
out.append(page("blog.html", "Blog | Website, SEO, CRM &amp; Marketing Tips | GrowVika",
 "Practical guides for Delhi NCR businesses on websites, Google Maps ranking, social media, ads, apps and CRM from the GrowVika team.", "blog", [
 page_hero([(None, "Blog")], "Ideas to help you", '<em class="s">grow online.</em>',
   "Practical guides on websites, Google Maps, social media, ads, apps and CRM — written for business owners, not developers.", "laptop_mug",
   b1=("fa-solid fa-book-open","Plain-English guides","no jargon"), b2=("fa-solid fa-lightbulb","Real questions","from NCR businesses"),
   ctas='<a href="#posts" class="btn btn-i">Read the latest <i class="fa-solid fa-arrow-down"></i></a><a href="https://wa.me/919818186876" target="_blank" rel="noopener" class="btn btn-o"><i class="fa-brands fa-whatsapp"></i> Ask a question</a>'),
 featured,
 blog_list.replace('<section class="sec">', '<section class="sec" id="posts">', 1),
 marquee(["Websites", "Local SEO", "CRM", "Apps", "Social media", "Ads", "E-commerce", "Software"]),
 cats,
 start_here,
 tips,
 svc_cards(SERVICES, "Need help?", "Let us", '<em class="s">do it for you.</em>', "Every topic here is something we can set up for you.", soft=True),
 ask,
 why(),
 promise(),
 faq([("How often do you publish?","We add new guides regularly based on questions from business owners."),("Can I suggest a topic?","Yes — send it on WhatsApp and we'll try to cover it."),("Is the advice free to use?","Absolutely. Use it for your business; ask us if you'd like help."),("Do you write blogs for clients?","Yes, SEO blog writing is part of our marketing services.")], a="Blog", b='<em class="s">questions.</em>'),
 enquiry(),
]))

# ======================= FAQ =======================
tabs = "".join(f'<a href="#faq-{g[0]}" class="ft rv"><i class="fa-solid {g[2]}"></i>{g[1]}</a>' for g in FAQ_GROUPS)
search = f'''<section class="sec faq-top">
  <div class="wrap">
    <div class="fq-search rv"><i class="fa-solid fa-magnifying-glass"></i><input type="search" id="fq-q" placeholder="Search questions — e.g. “how long”, “ownership”, “SEO”" aria-label="Search FAQs"><span class="fq-n" id="fq-n"></span></div>
    <div class="ft-row">{tabs}</div>
  </div>
</section>'''
groups = []
for k, (gid, gname, gic, qs) in enumerate(FAQ_GROUPS):
    groups.append(faq(qs, gname, gname.split(" ")[0], '<em class="s">questions.</em>', sid=f"faq-{gid}", more=False, card=False).replace('<section class="sec faq"', f'<section class="sec faq fq-group{" soft" if k % 2 else ""}"', 1))
out.append(page("faq.html", "FAQ | Websites, Apps, CRM, SEO &amp; Pricing Questions | GrowVika",
 "Answers to common questions about GrowVika's websites, online stores, apps, CRM, custom software, SEO, pricing, payments and support.", "faq", [
 page_hero([(None, "FAQ")], "Questions,", '<em class="s">answered.</em>',
   "Everything business owners usually ask us — timelines, pricing, ownership, SEO and support. Can't find yours? Ask us on WhatsApp.", "pair",
   b1=("fa-solid fa-circle-question","24+ answers","in 6 topics"), b2=("fa-brands fa-whatsapp","Ask anything","reply the same day"),
   ctas='<a href="#faq-general" class="btn btn-i">Browse questions <i class="fa-solid fa-arrow-down"></i></a><a href="https://wa.me/919818186876" target="_blank" rel="noopener" class="btn btn-o"><i class="fa-brands fa-whatsapp"></i> Ask on WhatsApp</a>'),
 search,
 *groups,
 marquee(["Timelines", "Pricing", "Ownership", "SEO", "Apps", "CRM", "Support", "Payments"]),
 svc_cards(SERVICES, "Popular services", "Explore our", '<em class="s">services.</em>', "Each service page has its own detailed FAQs.", soft=True),
 contact_cards("Still need help?", 'Talk to a <em class="s">real person.</em>'),
 cta_strip("Ready to start", "your project?", "Free consultation, fixed quote, and a reply the same day."),
 enquiry(),
]))

for art in ARTICLES:
    out.append(article_page(art))

for f, n in out:
    print(f"{f}: {n} sections (+ header + footer)")
