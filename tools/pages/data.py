# Content for the GrowVika multi-page site. Honest copy: no invented clients, ratings or prices.

IMG = {
 "team":"photo-1522071820081-009f0129c71c","meeting":"photo-1603201667230-bd139210db18","smiling":"photo-1572021335469-31706a17aaef",
 "pair":"photo-1629904853893-c2c8981a1dc5","code":"photo-1498050108023-c5249f4df085","desk":"photo-1499951360447-b19be8fe80f5",
 "data":"photo-1686061592689-312bbfb5c055","social":"photo-1759215524600-7971d6a4dac0","mobile":"photo-1551650975-87deedd944c3",
 "phone":"photo-1542641728-6ca359b085f4","shop":"photo-1563013544-824ae1b704d3","site":"photo-1658297063569-162817482fb6",
 "sketch":"photo-1576153192396-180ecef2a715","marketing":"photo-1557838923-2985c318be48","screen":"photo-1547658719-da2b51169166",
 "laptop_mug":"photo-1487014679447-9f8336841d58","india_gate":"photo-1587474260584-136574528ed5","gurugram":"photo-1715870251864-64fd4a6ae4ad",
 "noida":"photo-1688978022482-00702c9eb83c","clinic":"photo-1629909613654-28e377c37b09","restaurant":"photo-1551632436-cbf8dd35adfa",
 "gnoida":"photo-1661858435242-ed971767e954","ghaziabad":"photo-1645938374241-7f0e5f520663","faridabad":"photo-1645938374927-d74b9349be51",
 "qutub":"photo-1668520516758-495804c78078","lotus":"photo-1667201814086-9d9104d90283",
}
def U(key, w=900):
    i = IMG.get(key, key)
    return f"https://images.unsplash.com/{i}?auto=format&fit=crop&w={w}&q=70"

WA = "919818186876"

# ---------------- SERVICES ----------------
SERVICES = [
 dict(slug="website-development", name="Website Development", short="Websites", icon="fa-code", img="code", img2="desk",
  tag="Business websites", group="Build",
  h1=("Websites that bring", "you <em class=\"s\">enquiries.</em>"),
  lead="Fast, mobile-first business websites and landing pages — designed to look premium, rank on Google and turn visitors into calls and WhatsApp messages.",
  card="Business sites, landing pages and portals that load fast and bring enquiries.",
  overview=("Your website is your best salesperson.",
   "Most visitors decide in a few seconds whether to call you or go back to Google. We build sites that answer their questions quickly, look trustworthy on a phone, and make it one tap to call or WhatsApp you.",
   ["Custom design for your brand — no cheap templates","Built mobile-first and tested on real phones","SEO basics, Google Analytics and Search Console set up","Click-to-call, WhatsApp and enquiry forms on every page"]),
  incl=[("fa-pen-ruler","Custom UI design","Layouts designed around your services and customers."),("fa-mobile-screen","Mobile-first build","Looks and works great on every phone size."),("fa-gauge-high","Speed optimised","Compressed images, clean code, fast hosting."),("fa-magnifying-glass","On-page SEO","Titles, meta, headings, schema and sitemap."),("fa-brands fa-whatsapp","WhatsApp & call buttons","One-tap contact on every page."),("fa-envelope-open-text","Enquiry forms","Leads to WhatsApp, email or your CRM."),("fa-shield-halved","SSL & security","HTTPS, backups and basic hardening."),("fa-chart-line","Analytics setup","Google Analytics & Search Console.")],
  types=[("Business website","5–10 pages for clinics, shops, consultants and service businesses."),("Landing page","One focused page for an ad campaign or offer."),("Corporate site","Multi-section company site with careers, blog and downloads."),("Portfolio / catalogue","Showcase products or projects with filters and enquiry.")],
  steps=[("Discover","We learn your services, customers and competitors.","Day 1"),("Sitemap & design","Pages and design for your approval before code.","Week 1"),("Build & content","We build, add content and connect forms.","Week 1–2"),("Launch & SEO","Go live, submit to Google, track visits.","Week 2")],
  stack=["HTML5 / CSS3","JavaScript","WordPress","Next.js","Tailwind","Google Analytics","Search Console","Cloudflare"],
  inds=["Clinics & doctors","Restaurants & cafés","Coaching institutes","Real estate","Salons & gyms","Manufacturers"],
  faq=[("How long does a website take?","Most business websites go live in 7–15 days after we receive your content."),("Will I be able to update it myself?","Yes. We can build on WordPress or give you a simple editor, and show you how to make changes."),("Do you write the content?","We can. Share your details and we'll write clear, SEO-friendly copy for each page."),("Is hosting and domain included?","We help you buy them in your own name and set everything up, so you always own your website."),("Will it rank on Google?","We set up the SEO foundations. Ranking higher for competitive searches usually needs ongoing SEO — we offer that too.")]),
 dict(slug="ecommerce-development", name="E-commerce Stores", short="E-commerce", icon="fa-bag-shopping", img="shop", img2="phone",
  tag="Online stores", group="Build",
  h1=("Online stores that", "<em class=\"s\">sell</em> every day."),
  lead="Your products online with secure payments, shipping, discount codes and an easy admin — so you can take orders 24×7 without paying marketplace commissions.",
  card="Online stores with payments, shipping and an easy admin to manage orders.",
  overview=("Sell directly — keep your margins.",
   "Marketplaces take a big cut and own your customers. Your own store lets you build a brand, run your own offers and get repeat orders on WhatsApp and email.",
   ["Razorpay / UPI / cards and cash on delivery","Shipping partner integration (e.g. Shiprocket)","Inventory, variants, coupons and GST invoices","Abandoned-cart reminders and order updates"]),
  incl=[("fa-store","Store design","A branded storefront that builds trust."),("fa-credit-card","Payments","UPI, cards, wallets, net-banking and COD."),("fa-truck-fast","Shipping","Courier integration and tracking links."),("fa-boxes-stacked","Inventory","Stock, variants, sizes and colours."),("fa-ticket","Coupons & offers","Discount codes, combos and free shipping."),("fa-file-invoice","GST invoices","Automatic invoices for every order."),("fa-bell","Order alerts","Email / WhatsApp updates for customers."),("fa-chart-pie","Sales reports","See what sells and who buys again.")],
  types=[("D2C brand store","Fashion, beauty, food and lifestyle brands."),("Catalogue + enquiry","B2B products where customers ask for a quote."),("Single-product store","Fast landing-page style store for one hero product."),("Multi-vendor (custom)","Marketplace-style platforms built to order.")],
  steps=[("Plan the catalogue","Categories, products, shipping and payment flow.","Week 1"),("Design & build","Storefront, cart and checkout.","Week 1–3"),("Connect & test","Payments, shipping, invoices, test orders.","Week 3"),("Launch & market","Go live and plan ads / SEO for sales.","Week 4")],
  stack=["Shopify","WooCommerce","Custom (Next.js)","Razorpay","PhonePe / UPI","Shiprocket","Meta Pixel","GA4 e-commerce"],
  inds=["Fashion & apparel","Food & bakery","Beauty & wellness","Home & décor","Electronics accessories","B2B suppliers"],
  faq=[("Shopify or WooCommerce?","It depends on your products and budget. We'll recommend one after understanding your catalogue."),("Can I accept cash on delivery?","Yes, along with UPI, cards and wallets through a payment gateway."),("Who uploads the products?","We can upload them for you, or train your team to do it."),("Can customers track orders?","Yes — tracking links are sent automatically when you ship."),("Do you help with selling after launch?","Yes. We run Meta and Google shopping ads and SEO for stores.")]),
 dict(slug="mobile-app-development", name="Mobile App Development", short="Mobile apps", icon="fa-mobile-screen", img="mobile", img2="phone",
  tag="Android & iOS", group="Build",
  h1=("Apps your customers", "<em class=\"s\">love</em> to use."),
  lead="Android and iOS apps for bookings, orders, memberships and field teams — with an admin panel to run it all, built by the same team that builds your website.",
  card="Android and iOS apps for bookings, orders, memberships and more.",
  overview=("An app when you really need one.",
   "We'll tell you honestly if a website is enough. When an app makes sense — repeat bookings, loyalty, delivery or a field team — we build one that is simple, fast and easy to maintain.",
   ["One codebase for Android and iOS","Admin panel to manage users, orders and content","Push notifications, payments and maps","Play Store & App Store publishing support"]),
  incl=[("fa-object-group","App UI/UX","Clean screens designed for thumbs."),("fa-mobile","Android & iOS","Cross-platform build, native feel."),("fa-user-lock","Login & profiles","OTP, email or social login."),("fa-bell","Push notifications","Offers, reminders and order updates."),("fa-credit-card","In-app payments","UPI, cards and wallets."),("fa-map-location-dot","Maps & location","Tracking, store locator, delivery."),("fa-table-columns","Admin panel","Manage everything from a browser."),("fa-upload","Store publishing","Play Store & App Store listing help.")],
  types=[("Booking app","Clinics, salons, gyms and services."),("Ordering / delivery app","Restaurants, grocery and local delivery."),("Membership & loyalty","Gyms, clubs and coaching."),("Field-team app","Sales, service and attendance tracking.")],
  steps=[("Scope the app","Screens, users and must-have features.","Week 1"),("Design screens","Clickable design to approve before code.","Week 1–2"),("Build & test","App + admin panel, tested on real devices.","Week 2–7"),("Publish & support","Store listing, launch and updates.","Week 8")],
  stack=["Flutter","React Native","Firebase","Node.js","PostgreSQL","Razorpay","Google Maps","OneSignal"],
  inds=["Clinics & healthcare","Restaurants","Gyms & fitness","Coaching institutes","Logistics","Field services"],
  faq=[("Android or iOS first?","We usually build both together from one codebase, so you don't pay twice."),("How long does an app take?","A focused first version typically takes 4–8 weeks depending on features."),("Do you publish it on the stores?","Yes, we help with Play Store and App Store accounts, listings and approval."),("What about updates later?","We offer monthly support for fixes, updates and new features."),("Do I get the source code?","Yes, the app and its code belong to you.")]),
 dict(slug="crm-development", name="CRM Development", short="CRM", icon="fa-users-gear", img="data", img2="laptop_mug",
  tag="Leads & follow-ups", group="Grow",
  h1=("Never lose a lead", "<em class=\"s\">again.</em>"),
  lead="A CRM built around how your team actually works — every enquiry, follow-up, client, payment and renewal in one place, on desktop and phone.",
  card="Track every lead, follow-up, client and payment in one place.",
  overview=("Built on our own experience.",
   "We run GrowVika on a CRM we built ourselves — lead stages, follow-up reminders, plan renewals and income tracking. We build the same kind of system for your business, shaped around your process.",
   ["Lead stages that match your sales process","Follow-up reminders so nobody is forgotten","Clients, payments, renewals and due amounts","Works on phone like an app"]),
  incl=[("fa-filter","Lead pipeline","Custom stages from new enquiry to won."),("fa-clock","Follow-up reminders","Today's calls and overdue tasks at a glance."),("fa-address-book","Client records","History, notes and documents per client."),("fa-indian-rupee-sign","Payments & dues","Received, pending and next due date."),("fa-rotate","Renewals","Monthly / yearly plans with reminders."),("fa-users","Team roles","Admin, sales and staff permissions."),("fa-chart-column","Reports","Income, conversions and team performance."),("fa-mobile-screen","Mobile-friendly","Feels like an app on any phone.")],
  types=[("Sales CRM","Leads, stages, follow-ups and conversions."),("Admissions CRM","Enquiries, counselling and fee follow-ups."),("Service CRM","Clients, AMC, renewals and visits."),("Real-estate CRM","Site visits, inventory and broker leads.")],
  steps=[("Map your process","How leads come in and who follows up.","Week 1"),("Design the screens","Dashboards and forms for your team.","Week 1–2"),("Build & import","Build the CRM and import your existing data.","Week 2–5"),("Train & improve","Team training and changes after real use.","Week 6")],
  stack=["Next.js","Node.js","PostgreSQL","Supabase","WhatsApp links","Google Sheets import","Vercel","PWA"],
  inds=["Agencies & consultants","Coaching institutes","Real estate","Clinics","Insurance & finance","B2B sales teams"],
  faq=[("Why not use a ready-made CRM?","Ready-made tools charge per user and force their process on you. A custom CRM fits your workflow and you own it."),("Can you import my Excel data?","Yes, we import leads and clients from Excel or Google Sheets."),("Does it work on mobile?","Yes. It works in the phone browser and can be added to the home screen like an app."),("Can it send WhatsApp messages?","It can open WhatsApp with a ready message for each lead. Full WhatsApp API automation can be added."),("Is my data safe?","Data is stored securely with logins and role-based access, and backed up regularly.")]),
 dict(slug="custom-software-development", name="Custom Software", short="Software", icon="fa-gears", img="screen", img2="sketch",
  tag="Billing, booking & tools", group="Grow",
  h1=("Software that fits", "your <em class=\"s\">business.</em>"),
  lead="Billing, booking, inventory, HR and internal dashboards — custom tools that replace messy spreadsheets and save your team hours every week.",
  card="Billing, booking, inventory and internal tools that replace spreadsheets.",
  overview=("Stop forcing your work into spreadsheets.",
   "If your team copies data between Excel files, WhatsApp groups and notebooks, a small custom tool can save hours every day. We build exactly what you need — nothing you'll never use.",
   ["Built around your exact workflow","Works in the browser — no installation","Role-based access for your team","Can grow with your business over time"]),
  incl=[("fa-file-invoice-dollar","Billing & invoicing","GST invoices, quotations and receipts."),("fa-calendar-check","Booking systems","Appointments, slots and reminders."),("fa-warehouse","Inventory","Stock in/out, alerts and reports."),("fa-user-clock","HR & attendance","Staff, attendance and payroll inputs."),("fa-gauge","Dashboards","Live numbers for owners and managers."),("fa-plug","Integrations","Payment gateways, SMS, email, Sheets."),("fa-lock","Secure logins","Roles and permissions for each user."),("fa-cloud","Cloud hosted","Access from anywhere, backed up.")],
  types=[("Billing software","Invoices, payments and GST reports."),("Booking & scheduling","Appointments, classes and resources."),("Inventory & orders","Stock, purchase and dispatch."),("Admin dashboards","Reports that pull data together.")],
  steps=[("Understand the work","Watch how your team works today.","Week 1"),("Plan the modules","What to build first for quick value.","Week 1–2"),("Build in stages","Usable versions every couple of weeks.","Week 2–8"),("Roll out & support","Training, fixes and improvements.","Ongoing")],
  stack=["Next.js","React","Node.js","Python","PostgreSQL","Supabase","REST APIs","Vercel / AWS"],
  inds=["Manufacturers","Distributors","Clinics & labs","Schools & institutes","Service companies","Retail chains"],
  faq=[("How do you price custom software?","After understanding your needs, we give a fixed quote for the first version — no open-ended hourly billing."),("Can you start small?","Yes. We usually build the most useful module first, then add more."),("Can it connect to my existing tools?","Most likely — payment gateways, Google Sheets, SMS and email are common integrations."),("Who owns the software?","You do — including the code and the data."),("Do you provide support?","Yes, monthly support plans cover fixes, hosting and small improvements.")]),
 dict(slug="digital-marketing", name="Digital Marketing", short="Marketing", icon="fa-bullhorn", img="marketing", img2="social",
  tag="SEO, social & ads", group="Grow",
  h1=("Marketing that fills", "your <em class=\"s\">pipeline.</em>"),
  lead="SEO, Google Business Profile, social media and Meta & Google Ads — run by the team that built your website, so every click lands on a page made to convert.",
  card="SEO, Google Business Profile, social media and Ads that bring leads.",
  overview=("Traffic is easy. Enquiries are the goal.",
   "We focus on calls, WhatsApp messages and form fills — not vanity likes. Because we also build websites and CRMs, we can track a lead from the ad all the way to a paying client.",
   ["Local SEO and Google Maps ranking","Social media content and reels","Meta and Google Ads with clear reporting","Landing pages built for each campaign"]),
  incl=[("fa-magnifying-glass-chart","SEO","Keywords, on-page fixes and content."),("fa-location-dot","Google Business Profile","Maps ranking, posts and reviews strategy."),("fa-hashtag","Social media","Monthly content calendar and reels."),("fa-brands fa-meta","Meta Ads","Facebook & Instagram lead campaigns."),("fa-brands fa-google","Google Ads","Search and local campaigns."),("fa-pen-nib","Content writing","Blogs, captions and ad copy."),("fa-chart-line","Monthly reports","Leads, cost and what to improve."),("fa-flask","Landing pages","Fast pages built for each campaign.")],
  types=[("Local SEO","Rank in Google Maps for searches near you."),("Social media management","Consistent posting that builds trust."),("Lead-generation ads","Meta and Google campaigns for enquiries."),("Content & blogs","Articles that answer customer questions.")],
  steps=[("Audit","Your website, Google profile, competitors.","Week 1"),("Plan","Channels, budget split and content calendar.","Week 1"),("Launch","Campaigns, posts and SEO fixes go live.","Week 2"),("Report & improve","Monthly report and changes.","Monthly")],
  stack=["Google Business Profile","Search Console","GA4","Meta Ads Manager","Google Ads","Canva","Semrush-style tools","Looker Studio"],
  inds=["Clinics & dentists","Restaurants","Real estate","Coaching","Salons & spas","Local retail"],
  faq=[("How soon will I see results?","Ads can bring enquiries within days. SEO usually takes 3–6 months to build steady results."),("How much should I spend on ads?","It depends on your city and industry. We suggest a test budget first, then scale what works."),("Do you guarantee rankings?","No honest agency can guarantee rankings. We guarantee clear work, monthly reports and honest advice."),("Do you make reels and creatives?","Yes — graphics, short videos and captions as part of social media plans."),("Is there a long contract?","Plans are monthly; we recommend at least 3 months to judge results fairly.")]),
]
SVC = {s["slug"]: s for s in SERVICES}

# ---------------- AREAS ----------------
AREAS = [
 dict(slug="delhi", name="Delhi", tag="The capital", img="india_gate", img2="qutub", img3="lotus",
  intro="From Connaught Place showrooms to South Delhi clinics, Delhi businesses compete hard for every search. We build websites, run local SEO and set up CRMs that help you win your neighbourhood.",
  locs=["Connaught Place","Karol Bagh","Laxmi Nagar","Dwarka","Rohini","Saket","Janakpuri","Pitampura","Rajouri Garden","Lajpat Nagar","Preet Vihar","Vasant Kunj"],
  pop=["website-development","digital-marketing","crm-development"], inds=["Clinics & doctors","Showrooms & retail","Coaching centres","Restaurants & cafés","CA & legal firms","Real estate"],
  near=["gurugram","noida","ghaziabad"], q="Delhi"),
 dict(slug="gurugram", name="Gurugram", tag="Offices & startups", img="gurugram", img2="team", img3="meeting",
  intro="Startups, corporate offices and premium services around Cyber City and Golf Course Road need fast products and sharp lead generation. We build apps, CRMs and landing pages that keep up.",
  locs=["Cyber City","Golf Course Road","Sohna Road","Udyog Vihar","DLF Phase 1–5","Sector 29","MG Road","Sushant Lok","Sector 56","Golf Course Extension"],
  pop=["mobile-app-development","custom-software-development","digital-marketing"], inds=["Startups & SaaS","Corporate offices","Real estate","Premium salons & gyms","Restaurants","Consultants"],
  near=["delhi","faridabad","noida"], q="Gurugram"),
 dict(slug="noida", name="Noida", tag="IT & education hub", img="noida", img2="code", img3="desk",
  intro="IT parks, coaching institutes and retail along the Expressway make Noida one of the most digital-first markets in NCR. We build online stores, admission CRMs and SEO that brings students and customers.",
  locs=["Sector 18","Sector 62","Sector 63","Sector 132","Noida Extension","Film City","Sector 50","Sector 76","Sector 15","Sector 137"],
  pop=["ecommerce-development","crm-development","digital-marketing"], inds=["Coaching institutes","IT services","Retail & e-commerce","Clinics","Real estate","Restaurants"],
  near=["greater-noida","delhi","ghaziabad"], q="Noida"),
 dict(slug="greater-noida", name="Greater Noida", tag="Fast-growing", img="gnoida", img2="sketch", img3="smiling",
  intro="New businesses around Pari Chowk, Knowledge Park and Gaur City are growing fast. Get found online from day one with a professional website, Google Business Profile and social media.",
  locs=["Pari Chowk","Knowledge Park","Alpha & Beta","Gaur City","Jagat Farm","Greater Noida West","Delta","Techzone"],
  pop=["website-development","digital-marketing","crm-development"], inds=["Colleges & coaching","New retail","Clinics","Restaurants","Real estate","Manufacturing units"],
  near=["noida","ghaziabad","delhi"], q="Greater Noida"),
 dict(slug="ghaziabad", name="Ghaziabad", tag="Retail & services", img="ghaziabad", img2="phone", img3="pair",
  intro="Shops, clinics and service businesses in Indirapuram, Vaishali and Raj Nagar win customers on Google Maps and Instagram. We set up both — and the website and CRM behind them.",
  locs=["Indirapuram","Vaishali","Raj Nagar","Kaushambi","Vasundhara","Crossings Republik","Raj Nagar Extension","Kavi Nagar"],
  pop=["digital-marketing","website-development","ecommerce-development"], inds=["Clinics & diagnostics","Retail shops","Salons","Coaching","Restaurants","Home services"],
  near=["noida","delhi","greater-noida"], q="Ghaziabad"),
 dict(slug="faridabad", name="Faridabad", tag="Industry & B2B", img="faridabad", img2="screen", img3="laptop_mug",
  intro="Manufacturers and B2B suppliers in NIT and the industrial sectors need catalogue websites, enquiry systems and custom software. We build tools that help you get and manage bulk orders.",
  locs=["NIT","Sector 15","Sector 21","Ballabgarh","Neharpar","Industrial Area","Sector 16","Old Faridabad"],
  pop=["website-development","custom-software-development","crm-development"], inds=["Manufacturers","B2B suppliers","Exporters","Schools","Clinics","Retail"],
  near=["delhi","gurugram","noida"], q="Faridabad"),
]
AREA = {a["slug"]: a for a in AREAS}

# ---------------- WORK (examples by industry, no client names) ----------------
WORK = [
 ("Dental clinic website","Healthcare · South Delhi","clinic","website","Website + Local SEO","Online appointment booking, treatment pages and Google Maps optimisation."),
 ("Restaurant ordering app","Food · Gurugram","restaurant","app","Mobile app","Direct ordering with menu, cart, UPI and order tracking."),
 ("Fashion e-commerce store","Retail · Noida","shop","ecommerce","E-commerce","Catalogue with sizes, coupons, COD and courier tracking."),
 ("Coaching institute CRM","Education · Delhi","data","crm","CRM","Admission enquiries, counselling stages and fee follow-ups."),
 ("Salon local SEO growth","Beauty · Ghaziabad","social","marketing","SEO + Social","Google Business Profile, reels calendar and offer campaigns."),
 ("Manufacturer B2B portal","Industry · Faridabad","screen","software","Custom software","Product catalogue, RFQ forms and dealer login."),
 ("Real-estate lead website","Property · Gurugram","site","website","Website + Ads","Project landing pages with lead forms and Meta ads."),
 ("Gym membership app","Fitness · Noida","mobile","app","Mobile app","Plans, renewals, attendance and push reminders."),
]
WORK_CATS = [("all","All"),("website","Websites"),("ecommerce","E-commerce"),("app","Apps"),("crm","CRM"),("software","Software"),("marketing","Marketing")]

# ---------------- BLOG ----------------
from articles import ARTICLES
# (category, folder, minutes, image, title, description, slug)
POSTS = [(a["cat"], a["folder"], a["mins"], a["img"], a["title"], a["desc"], a["slug"]) for a in ARTICLES]
BLOG_CATS = ["All","Websites","Local SEO","CRM","Apps","Social","Ads","E-commerce","Software"]

# ---------------- FAQ ----------------
FAQ_GROUPS = [
 ("general","General","fa-circle-info",[
  ("What does GrowVika do?","We build websites, online stores, mobile apps, CRMs and custom software, and run digital marketing (SEO, Google Business Profile, social media and ads) for businesses in Delhi NCR."),
  ("Where are you based?","We serve all of Delhi NCR — Delhi, Gurugram, Noida, Greater Noida, Ghaziabad and Faridabad — and work online with businesses across India."),
  ("Who will I talk to?","You talk directly to the founder and the people who build your project. No sales desk or call centre."),
  ("Can we meet in person?","Yes. The first meeting at your office in Delhi NCR is free, or we can talk on a video call.")]),
 ("pricing","Pricing & payments","fa-file-invoice",[
  ("How much will my project cost?","It depends on the pages, features and integrations you need. After a free call we send a clear, fixed quote."),
  ("Are there hidden charges?","No. The quote lists everything included. If you ask for something new later, we quote it separately before starting."),
  ("How do payments work?","Usually a part in advance to start, and the rest in milestones or on launch. Details are written in the quote."),
  ("Do you offer monthly plans?","Yes — for maintenance, hosting, SEO, social media and ads. Monthly and yearly options are available.")]),
 ("websites","Websites & stores","fa-code",[
  ("How long does a website take?","Most business websites go live in 7–15 days. Online stores usually take 3–4 weeks."),
  ("Will my website work on mobile?","Yes. Everything we build is designed for phones first and tested on real devices."),
  ("Do I own my website and domain?","Yes. Domain, hosting and code are in your name — we help you set them up."),
  ("Can I edit the website myself?","Yes. We can use WordPress or a simple editor and train you to update text, images and blogs.")]),
 ("apps","Apps, CRM & software","fa-mobile-screen",[
  ("Do you build for both Android and iOS?","Yes, usually from one codebase so you get both without paying twice."),
  ("Can you build a CRM like yours?","Yes. We run GrowVika on our own CRM and build similar systems shaped around your process."),
  ("Can you import my Excel data?","Yes, we import leads, clients and products from Excel or Google Sheets."),
  ("Who owns the code?","You do — the software, code and data belong to your business.")]),
 ("marketing","SEO & marketing","fa-bullhorn",[
  ("How soon does SEO work?","SEO usually takes 3–6 months to build steady results. Ads can bring enquiries within days."),
  ("Do you guarantee first rank on Google?","No honest agency can guarantee rankings. We promise clear work, monthly reports and honest advice."),
  ("Do you make reels and creatives?","Yes — graphics, short videos and captions as part of social media plans."),
  ("What do monthly reports include?","Leads, calls, cost per lead, rankings and what we'll improve next month.")]),
 ("support","Support after launch","fa-headset",[
  ("What happens after my website goes live?","We stay with you for fixes, updates and growth. Support is one WhatsApp message away."),
  ("Do you provide hosting and maintenance?","Yes. Maintenance plans cover hosting, backups, security updates and small changes."),
  ("What if something breaks?","Message us on WhatsApp. Critical issues are looked at the same day."),
  ("Can you take over an existing website?","Yes. We'll review it first and tell you honestly whether to fix or rebuild.")]),
]

PROCESS = [("Discover","A free call to understand your business, customers and goals. You get a clear plan and a fixed quote.","Day 1","meeting"),
 ("Plan & design","We map the pages or screens and design the look. You review and suggest changes before any code.","Week 1","sketch"),
 ("Build & test","We build it mobile-first, connect forms, WhatsApp and payments, and test on real phones.","Week 1–3","code"),
 ("Launch & grow","We go live, set up Google and analytics, and keep improving with SEO, ads and support.","Ongoing","data")]

WHY = [("fa-layer-group","Build + grow, one team","Website, app, CRM and marketing from the same people. No juggling vendors."),
 ("fa-mobile-screen-button","Mobile-first & fast","Designed for phones first and built to load fast — where your customers are."),
 ("fa-magnifying-glass-chart","SEO-ready from day one","Clean code, Google setup and local SEO built in, not added later."),
 ("fa-file-signature","Clear, fixed quotes","You know the full scope and cost before we start. No hidden charges."),
 ("fa-code-branch","We build our own software","We run our business on a CRM we built ourselves — so we know what works."),
 ("fa-headset","Support after launch","Updates, fixes and growth help on WhatsApp — we don't disappear after go-live.")]

PROMISE = [("You talk to the people who actually build your project — not a sales desk. If something isn't clear, we explain it in <em>plain words</em>.","Plain talk"),
 ("Every project starts with a fixed quote. What we agree is what you pay — <em>no surprise bills</em> halfway through.","Fixed quotes"),
 ("We don't disappear after launch. Your website, app or CRM keeps getting looked after — <em>one WhatsApp away</em>.","After launch")]

INDUSTRIES = [("Clinics &amp; healthcare","Appointment booking, Google Maps ranking, patient trust.","clinic"),
 ("Restaurants &amp; cafés","Online menus, direct ordering apps, Instagram reels.","restaurant"),
 ("Retail &amp; e-commerce","Online stores, payments, shipping and catalogue ads.","shop"),
 ("Real estate","Project landing pages, lead ads and a CRM for site visits.","site"),
 ("Education &amp; coaching","Admission enquiries, student CRM and course pages.","smiling"),
 ("Manufacturing &amp; B2B","Catalogue sites, RFQ forms, dealer portals and software.","screen")]

# ---------------- localities: what each area is known for (used in detailed area cards) ----------------
LOC_INFO = {
 # Delhi
 "Connaught Place": ("Central business district", "offices, showrooms, restaurants and cafés", "website-development"),
 "Karol Bagh": ("Busy market hub", "retail shops, jewellers, hotels and wholesalers", "ecommerce-development"),
 "Laxmi Nagar": ("Education &amp; retail area", "coaching institutes, CA firms and local retail", "crm-development"),
 "Dwarka": ("Planned residential sub-city", "clinics, schools, gyms and neighbourhood services", "digital-marketing"),
 "Rohini": ("Large residential area", "clinics, coaching centres, retail and home services", "digital-marketing"),
 "Saket": ("South Delhi hub", "hospitals, clinics, malls and premium services", "website-development"),
 "Janakpuri": ("West Delhi neighbourhood", "clinics, institutes, restaurants and showrooms", "website-development"),
 "Pitampura": ("North-west Delhi hub", "coaching, clinics, retail and food businesses", "digital-marketing"),
 "Rajouri Garden": ("Shopping &amp; dining area", "fashion retail, restaurants and salons", "ecommerce-development"),
 "Lajpat Nagar": ("Popular market area", "fashion, home décor, clinics and wholesalers", "ecommerce-development"),
 "Preet Vihar": ("East Delhi neighbourhood", "coaching institutes, clinics and professional services", "crm-development"),
 "Vasant Kunj": ("South-west Delhi residential area", "premium clinics, salons, schools and malls", "digital-marketing"),
 # Gurugram
 "Cyber City": ("Corporate &amp; tech hub", "IT companies, startups, co-working spaces and cafés", "custom-software-development"),
 "Golf Course Road": ("Premium business corridor", "corporate offices, premium real estate and clinics", "website-development"),
 "Sohna Road": ("Fast-growing commercial belt", "real-estate projects, retail and services", "digital-marketing"),
 "Udyog Vihar": ("Industrial &amp; office area", "manufacturers, exporters and corporate offices", "custom-software-development"),
 "DLF Phase 1–5": ("Established residential areas", "clinics, salons, gyms and home services", "digital-marketing"),
 "Sector 29": ("Food &amp; nightlife hub", "restaurants, bars, cafés and event venues", "mobile-app-development"),
 "MG Road": ("Retail &amp; office corridor", "malls, showrooms, offices and restaurants", "website-development"),
 "Sushant Lok": ("Residential &amp; commercial mix", "clinics, coaching centres and local businesses", "crm-development"),
 "Sector 56": ("Growing residential sector", "neighbourhood services, clinics and retail", "digital-marketing"),
 "Golf Course Extension": ("New-age residential corridor", "real estate, premium services and retail", "website-development"),
 # Noida
 "Sector 18": ("Noida's main market", "retail, restaurants, malls and showrooms", "ecommerce-development"),
 "Sector 62": ("IT &amp; institutional hub", "IT companies, institutes and offices", "custom-software-development"),
 "Sector 63": ("Industrial &amp; startup area", "manufacturers, startups and service companies", "custom-software-development"),
 "Sector 132": ("Expressway business district", "corporate offices and IT companies", "crm-development"),
 "Noida Extension": ("Large residential area", "clinics, schools, gyms and local retail", "digital-marketing"),
 "Film City": ("Media &amp; production hub", "media houses, studios and production companies", "website-development"),
 "Sector 50": ("Residential sector", "clinics, salons and neighbourhood services", "digital-marketing"),
 "Sector 76": ("High-rise residential area", "home services, clinics and retail", "digital-marketing"),
 "Sector 15": ("Established residential sector", "clinics, coaching and local businesses", "website-development"),
 "Sector 137": ("Expressway residential corridor", "neighbourhood retail, gyms and services", "digital-marketing"),
 # Greater Noida
 "Pari Chowk": ("Central commercial area", "retail, restaurants and services", "website-development"),
 "Knowledge Park": ("Education hub", "colleges, institutes and student services", "crm-development"),
 "Alpha &amp; Beta": ("Residential sectors", "clinics, schools and local retail", "digital-marketing"),
 "Gaur City": ("Large residential township", "retail, food, salons and home services", "digital-marketing"),
 "Jagat Farm": ("Local market area", "shops, eateries and services", "website-development"),
 "Greater Noida West": ("Fast-growing residential belt", "new retail, clinics, gyms and schools", "digital-marketing"),
 "Delta": ("Residential sectors", "neighbourhood services and retail", "website-development"),
 "Techzone": ("Industrial &amp; IT zone", "manufacturers, IT units and offices", "custom-software-development"),
 # Ghaziabad
 "Indirapuram": ("Busy residential &amp; retail hub", "clinics, restaurants, salons and coaching", "digital-marketing"),
 "Vaishali": ("Metro-connected business area", "offices, clinics, retail and services", "website-development"),
 "Raj Nagar": ("Central residential area", "clinics, schools, retail and services", "digital-marketing"),
 "Kaushambi": ("Commercial &amp; hospital area", "hospitals, offices and hotels", "website-development"),
 "Vasundhara": ("Residential sectors", "local retail, clinics and home services", "digital-marketing"),
 "Crossings Republik": ("Residential township", "neighbourhood retail, gyms and services", "digital-marketing"),
 "Raj Nagar Extension": ("Growing residential area", "new retail, clinics and schools", "website-development"),
 "Kavi Nagar": ("Established residential &amp; industrial area", "manufacturers, retail and services", "custom-software-development"),
 # Faridabad
 "NIT": ("Main commercial area", "markets, showrooms, clinics and services", "website-development"),
 "Sector 21": ("Residential &amp; commercial sector", "clinics, schools and retail", "digital-marketing"),
 "Ballabgarh": ("Industrial &amp; market town", "manufacturers, traders and retail", "custom-software-development"),
 "Neharpar": ("Greater Faridabad residential area", "new retail, clinics and schools", "digital-marketing"),
 "Industrial Area": ("Manufacturing belt", "factories, suppliers and exporters", "custom-software-development"),
 "Sector 16": ("Central residential sector", "clinics, coaching and local businesses", "website-development"),
 "Old Faridabad": ("Traditional market area", "traders, retail and local services", "ecommerce-development"),
}
LOC_INFO["Sector 15 (Faridabad)"] = ("Commercial &amp; residential sector", "markets, clinics and offices", "website-development")

# Longer, SEO-friendly descriptions for cards
SVC_LONG = {
 "website-development": "Custom, mobile-first business websites and landing pages that load fast, rank on Google and turn visitors into calls and WhatsApp enquiries. Every site includes on-page SEO, analytics, click-to-call and WhatsApp buttons, enquiry forms and full ownership of your domain and code.",
 "ecommerce-development": "Online stores on Shopify, WooCommerce or custom code with UPI, card and COD payments, courier integration, GST invoices, coupons and an easy admin. Sell directly to customers across India without marketplace commissions and build a brand you own.",
 "mobile-app-development": "Android and iOS apps from a single codebase for bookings, food ordering, memberships, loyalty and field teams — with push notifications, in-app payments, maps and an admin panel. We help publish on Play Store and App Store and support you after launch.",
 "crm-development": "Custom CRM software built around your sales process — lead stages, follow-up reminders, client history, payments, dues and plan renewals in one place. Works on mobile like an app, imports your Excel data and has no per-user fees.",
 "custom-software-development": "Custom billing, booking, inventory, HR and dashboard software that replaces messy spreadsheets and WhatsApp groups. Browser-based, secure, role-based access for your team, and built in stages so you get value quickly — with code and data in your name.",
 "digital-marketing": "SEO, local SEO and Google Business Profile, social media management, and Meta and Google Ads focused on real enquiries — calls, WhatsApp chats and form fills. Clear monthly reports, landing pages built for each campaign and honest advice on budgets.",
}
WHY = [("fa-layer-group","Build + grow, one team","Website, app, CRM and digital marketing from the same people — so your ads land on pages built to convert and every lead flows into one system. No juggling separate developers and marketing agencies."),
 ("fa-mobile-screen-button","Mobile-first &amp; fast","Most of your customers find you on a phone. Every page and screen is designed for mobile first, optimised for speed and tested on real Android and iPhone devices before launch."),
 ("fa-magnifying-glass-chart","SEO-ready from day one","Clean code, proper headings, meta tags, sitemaps, schema, Google Analytics and Search Console are part of every build — not an expensive add-on later."),
 ("fa-file-signature","Clear, fixed quotes","After a free consultation you get a written scope and a fixed price. What we agree is what you pay — no hourly surprises or hidden charges halfway through the project."),
 ("fa-code-branch","We build our own software","GrowVika runs on a CRM we built ourselves for leads, follow-ups and renewals. We know what works in real businesses because we use it every day."),
 ("fa-headset","Support after launch","We don't disappear after go-live. Updates, fixes, hosting help and growth advice are one WhatsApp message away, with monthly support plans if you need them.")]
INDUSTRIES = [("Clinics &amp; healthcare","Patient-friendly websites, online appointment requests, Google Maps ranking, review strategy and CRM follow-ups for clinics, dentists, physiotherapists and diagnostic centres.","clinic"),
 ("Restaurants &amp; cafés","Online menus, direct ordering apps without aggregator commissions, table bookings, Instagram reels and local ads that bring regular customers back.","restaurant"),
 ("Retail &amp; e-commerce","Online stores with UPI and COD, courier tracking, catalogue ads on Meta and Google, and WhatsApp order updates for fashion, lifestyle and local retail brands.","shop"),
 ("Real estate","Fast project landing pages, lead ads on Meta and Google, site-visit scheduling and a CRM for brokers and developers to follow up every enquiry.","site"),
 ("Education &amp; coaching","Course pages, admission enquiry forms, counselling CRMs, fee follow-ups and local SEO for coaching institutes, schools and training centres.","smiling"),
 ("Manufacturing &amp; B2B","Product catalogue websites, request-for-quote forms, dealer portals and custom software for manufacturers, distributors and exporters.","screen")]
