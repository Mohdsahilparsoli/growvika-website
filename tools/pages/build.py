import re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from data import *

SITE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
VER = sys.argv[1] if len(sys.argv) > 1 else "1"
INDEX = open(f"{SITE}/index.html").read()

def block(src, start, end):
    i = src.index(start); j = src.index(end, i)
    return src[i:j]

POPUP = block(INDEX, "<!-- ============ POPUP ============ -->", "<script src=")
ENQ = block(INDEX, "<!-- ============ 12. ENQUIRY ============ -->", "</main>")
AREA_SLIDER = block(INDEX, "<!-- ============ 9. SERVICE AREA ============ -->", "<!-- ============ 10. BLOG ============ -->")

ON = ' class="on"'
EMS = '<em class="s">'
SON = " on"
def esc(s): return s.replace("&", "&amp;").replace("&amp;amp;", "&amp;").replace("&amp;#", "&#")

# ---------------- shell ----------------
BASE = "https://growvika-website.vercel.app"
def head(title, desc, popup=0, path="", schema="", ogimg="team"):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}/{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="GrowVika">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{BASE}/{path}">
<meta property="og:image" content="{U(ogimg,1200)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0A0F1E">
{schema}
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://images.unsplash.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;1,9..144,300;1,9..144,400&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Syne:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
<link rel="stylesheet" href="assets/css/agency.css?v={VER}">
</head>
<body data-auto-popup="{popup}">

<div class="cur" aria-hidden="true"><svg viewBox="0 0 46 46"><circle class="tr" cx="23" cy="23" r="21"/><circle class="pr" cx="23" cy="23" r="21"/></svg><span class="lbl">View</span></div>
<div class="cur-dot" aria-hidden="true"></div>

'''

def header(cur=""):
    def li(href, label, key):
        c = ' class="cur-page" aria-current="page"' if key == cur else ""
        return f'        <li><a href="{href}"{c}>{label}</a></li>'
    build = [s for s in SERVICES if s["group"] == "Build"]; grow = [s for s in SERVICES if s["group"] == "Grow"]
    def svc_link(s): return f'              <a href="{s["slug"]}.html"><span class="ic"><i class="fa-solid {s["icon"]}"></i></span><span><b>{s["name"]}</b><small>{s["tag"]}</small></span></a>'
    cities = "\n".join(f'              <a href="service-area-{a["slug"]}.html"><span class="mc-n">0{k+1}</span><span><b>{a["name"]}</b><small>{a["tag"]}</small></span><i class="fa-solid fa-arrow-right"></i></a>' for k, a in enumerate(AREAS))
    scur = ' cur-page' if cur == "services" else ""
    acur = ' cur-page' if cur == "areas" else ""
    return f'''<!-- ============ TOPBAR + HEADER ============ -->
<div class="topbar">
  <div class="wrap">
    <div class="tb-l">
      <a href="tel:+919818186876"><i class="fa-solid fa-phone"></i>+91-9818186876</a>
      <a href="mailto:sahil@growvika.com"><i class="fa-solid fa-envelope"></i>sahil@growvika.com</a>
      <span><i class="fa-solid fa-location-dot"></i>Serving all of Delhi NCR</span>
    </div>
    <div class="tb-r">
      <div class="soc">
        <a href="#" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
        <a href="#" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>
        <a href="#" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
        <a href="#" aria-label="YouTube"><i class="fa-brands fa-youtube"></i></a>
      </div>
    </div>
  </div>
</div>

<header class="header" id="top">
  <div class="wrap">
    <a href="index.html" class="logo" aria-label="GrowVika home">GrowVika<i></i></a>
    <nav class="nav" aria-label="Main">
      <ul>
{li("about.html","About","about")}
        <li class="has-mega">
          <button type="button" class="{scur.strip()}" aria-expanded="false" aria-controls="mega">Services <i class="fa-solid fa-chevron-down"></i></button>
          <div class="mega" id="mega">
            <div class="mega-col">
              <h5>Build</h5>
{chr(10).join(svc_link(s) for s in build)}
            </div>
            <div class="mega-col">
              <h5>Grow &amp; automate</h5>
{chr(10).join(svc_link(s) for s in grow)}
            </div>
            <div class="mega-feat">
              <img src="{U('team',600)}" alt="GrowVika team planning a project" loading="lazy">
              <small>All services</small>
              <h4>Websites, apps, CRM, software &amp; marketing.</h4>
              <a href="services.html" class="ma-all">View all services <i class="fa-solid fa-arrow-right"></i></a>
            </div>
          </div>
        </li>
{li("work.html","Work","work")}
        <li class="has-mega">
          <button type="button" class="{acur.strip()}" aria-expanded="false" aria-controls="mega-areas">Service Area <i class="fa-solid fa-chevron-down"></i></button>
          <div class="mega mega-areas" id="mega-areas">
            <div class="mega-col">
              <h5>Cities we serve</h5>
              <div class="mc-grid">
{cities}
              </div>
            </div>
            <div class="mega-feat ma-feat">
              <img src="{U('india_gate',600)}" alt="India Gate, New Delhi" loading="lazy">
              <small>Delhi NCR</small>
              <h4>Free first meeting at your office.</h4>
              <a href="service-area.html" class="ma-all">View service area <i class="fa-solid fa-arrow-right"></i></a>
            </div>
          </div>
        </li>
{li("blog.html","Blog","blog")}
{li("faq.html","FAQ","faq")}
{li("contact.html","Contact Us","contact")}
      </ul>
    </nav>
    <div class="h-right">
    <a href="tel:+919818186876" class="hcall"><span class="ic"><i class="fa-solid fa-phone-volume"></i></span><span><small>Call us</small><b>+91-9818186876</b></span></a>
    <button type="button" class="btn btn-d" data-open-modal>Start a project <i class="fa-solid fa-arrow-right"></i></button>
    <button type="button" class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="mnav"><i class="fa-solid fa-bars-staggered"></i></button>
    </div>
  </div>
</header>

<div class="mnav-bd"></div>
<aside class="mnav" id="mnav" aria-label="Mobile menu">
  <div class="top"><span class="logo">GrowVika<i></i></span><button type="button" class="mnav-x" aria-label="Close menu"><i class="fa-solid fa-xmark"></i></button></div>
  <a class="l1" href="index.html">Home <i class="fa-solid fa-arrow-right"></i></a>
  <a class="l1" href="about.html">About <i class="fa-solid fa-arrow-right"></i></a>
  <a class="l1" href="services.html">Services <i class="fa-solid fa-arrow-right"></i></a>
  <div class="sub">{''.join(f'<a href="{s["slug"]}.html">{s["short"]}</a>' for s in SERVICES)}</div>
  <a class="l1" href="work.html">Work <i class="fa-solid fa-arrow-right"></i></a>
  <a class="l1" href="service-area.html">Service Area <i class="fa-solid fa-arrow-right"></i></a>
  <div class="sub">{''.join(f'<a href="service-area-{a["slug"]}.html">{a["name"]}</a>' for a in AREAS)}</div>
  <a class="l1" href="blog.html">Blog <i class="fa-solid fa-arrow-right"></i></a>
  <a class="l1" href="faq.html">FAQ <i class="fa-solid fa-arrow-right"></i></a>
  <a class="l1" href="contact.html">Contact Us <i class="fa-solid fa-arrow-right"></i></a>
  <button type="button" class="btn btn-i" data-open-modal>Start a new project <i class="fa-solid fa-arrow-right"></i></button>
  <div class="ct">Call or WhatsApp<a href="tel:+919818186876">+91-9818186876</a><a href="mailto:sahil@growvika.com">sahil@growvika.com</a></div>
</aside>
'''

def footer():
    return f'''<!-- ============ FOOTER ============ -->
<footer class="foot">
  <div class="wrap">
    <div class="f-cta">
      <h3>Let's grow your<br>business <em class="s">online.</em></h3>
      <div class="f-cta-b">
        <button type="button" class="btn btn-w" data-open-modal>Start a new project <i class="fa-solid fa-arrow-right"></i></button>
        <a href="https://wa.me/{WA}" target="_blank" rel="noopener" class="btn f-wa"><i class="fa-brands fa-whatsapp"></i> WhatsApp us</a>
      </div>
    </div>
    <div class="foot-top">
      <div class="about-f">
        <a href="index.html" class="logo">GrowVika<i></i></a>
        <p>Website, app, CRM, custom software and digital marketing agency serving businesses across Delhi NCR.</p>
        <div class="soc">
          <a href="#" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
          <a href="#" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>
          <a href="#" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
          <a href="#" aria-label="YouTube"><i class="fa-brands fa-youtube"></i></a>
        </div>
      </div>
      <div class="f-col"><h5>Services</h5><ul>{''.join(f'<li><a href="{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES)}</ul></div>
      <div class="f-col"><h5>Company</h5><ul><li><a href="about.html">About us</a></li><li><a href="work.html">Our work</a></li><li><a href="service-area.html">Service area</a></li><li><a href="blog.html">Blog</a></li><li><a href="faq.html">FAQ</a></li><li><a href="contact.html">Contact us</a></li></ul></div>
      <div class="f-col f-contact"><h5>Get in touch</h5><ul>
        <li><i class="fa-solid fa-phone"></i><span><small>Call</small><a href="tel:+919818186876">+91-9818186876</a></span></li>
        <li><i class="fa-regular fa-envelope"></i><span><small>Email</small><a href="mailto:sahil@growvika.com">sahil@growvika.com</a></span></li>
        <li><i class="fa-solid fa-location-dot"></i><span><small>Location</small>Delhi NCR, India</span></li>
      </ul></div>
    </div>
    <div class="foot-bot"><span>© <span data-year>2026</span> GrowVika. All rights reserved.</span><nav aria-label="Legal"><a href="#">Privacy policy</a><a href="#">Terms</a><a href="#">Refunds</a></nav></div>
  </div>
</footer>

<a class="wa" href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
<button type="button" class="totop" aria-label="Back to top"><i class="fa-solid fa-arrow-up"></i></button>

'''

def page(fname, title, desc, cur, sections, popup=0, schema="", ogimg="team", crumbs_ld=None):
    n = [0]
    def num(m):
        n[0] += 1
        return f'<b>{n[0]:02d}</b>'
    body = "\n".join(sections)
    body = re.sub(r"<b>##</b>", num, body)
    path = "" if fname == "index.html" else fname[:-5]
    if crumbs_ld is None:
        nm = re.sub(r"\s*\|.*$", "", title).replace("&amp;", "&")
        if fname in [s["slug"] + ".html" for s in SERVICES]: crumbs_ld = [("Services", "services"), (nm, path)]
        elif fname.startswith("service-area-"): crumbs_ld = [("Service area", "service-area"), (nm, path)]
        else: crumbs_ld = [(nm, path)]
    ld = schema_org() + (breadcrumb_ld(crumbs_ld) if crumbs_ld else "") + faq_ld(body) + schema
    html = head(title, desc, popup, path, ld, ogimg) + header(cur) + "\n<main>\n" + body + "\n</main>\n\n" + footer() + POPUP + f'<script src="assets/js/agency.js?v={VER}" defer></script>\n</body>\n</html>\n'
    open(f"{SITE}/{fname}", "w").write(html)
    return fname, html.count('<section')

# ---------------- components ----------------
def idx(label): return f'<div class="idx rv"><b>##</b><span>{label}</span></div>'
def h2(a, b=None):
    if b: return f'<h2 class="h2 rv"><span class="mask"><span>{a}</span></span><span class="mask"><span>{b}</span></span></h2>'
    return f'<h2 class="h2 rv"><span class="mask"><span>{a}</span></span></h2>'
def headrow(label, a, b=None, lead=None, right=None):
    r = right or (f'<p class="lead rv">{lead}</p>' if lead else "")
    return f'''    <div class="head-row">
      <div>
        {idx(label)}
        {h2(a, b)}
      </div>
      {r}
    </div>'''

def crumbs(items):
    out = ['<a href="index.html">Home</a>']
    for href, label in items:
        out.append('<i class="fa-solid fa-chevron-right"></i>')
        out.append(f'<a href="{href}">{label}</a>' if href else f'<span>{label}</span>')
    return f'<nav class="crumb" aria-label="Breadcrumb">{"".join(out)}</nav>'

def page_hero(cr, h1a, h1b, lead, img, b1=("fa-brands fa-whatsapp","Same-day reply","on WhatsApp &amp; call"), b2=("fa-solid fa-handshake","Free first meeting","at your office in Delhi NCR"), ctas=None, chips=None):
    ctas = ctas or f'''<button type="button" class="btn btn-i" data-open-modal>Start a new project <i class="fa-solid fa-arrow-right"></i></button>
        <a href="https://wa.me/{WA}" target="_blank" rel="noopener" class="btn btn-o"><i class="fa-brands fa-whatsapp"></i> WhatsApp us</a>'''
    ch = f'<div class="ph-chips">{"".join(f"<span>{c}</span>" for c in chips)}</div>' if chips else ""
    return f'''<!-- PAGE HERO -->
<section class="ph">
  <div class="wrap">
    <div class="ph-txt rv">
      {crumbs(cr)}
      <h1><span class="mask"><span>{h1a}</span></span><span class="mask"><span>{h1b}</span></span></h1>
      <p class="lead">{lead}</p>
      <div class="hero-ctas">
        {ctas}
      </div>
      {ch}
    </div>
    <div class="ph-vis rv">
      <div class="img ph-img"><img src="{U(img,1000)}" alt="" fetchpriority="high"></div>
      <div class="h-badge ph-b1"><span class="ic"><i class="{b1[0]}"></i></span><span><b>{b1[1]}</b><small>{b1[2]}</small></span></div>
      <div class="h-badge ph-b2"><span class="ic"><i class="{b2[0]}"></i></span><span><b>{b2[1]}</b><small>{b2[2]}</small></span></div>
    </div>
  </div>
</section>'''

def marquee(words):
    sp = "".join(f'{w} <i class="fa-solid fa-asterisk"></i> ' if k % 2 == 0 else f'<em>{w}</em> <i class="fa-solid fa-asterisk"></i> ' for k, w in enumerate(words))
    return f'''<div class="marq-wrap"><div class="marq" aria-hidden="true"><div class="tr"><span>{sp}</span><span>{sp}</span></div></div></div>'''

def split(label, a, b, text, bullets=None, img="meeting", img2=None, rev=False, soft=False, extra="", sid=""):
    bl = "".join(f'<li><i class="fa-solid fa-check"></i>{x}</li>' for x in (bullets or []))
    ul = f'<ul class="ticklist rv">{bl}</ul>' if bullets else ""
    pics = f'<div class="sp-pics{" two" if img2 else ""}"><div class="p1 img rv cl"><img src="{U(img)}" alt="" loading="lazy"></div>' + (f'<div class="p2 img rv cl d2"><img src="{U(img2,700)}" alt="" loading="lazy"></div>' if img2 else "") + '</div>'
    i = f' id="{sid}"' if sid else ""
    return f'''<section class="sec split{' rev' if rev else ''}{' soft' if soft else ''}"{i}>
  <div class="wrap">
    {pics}
    <div class="sp-txt">
      {idx(label)}
      {h2(a, b)}
      <p class="rv sp-p">{text}</p>
      {ul}
      {extra}
    </div>
  </div>
</section>'''

def svc_cards(svcs, label="What we do", a="Everything you need", b="to <em class=\"s\">grow online.</em>", lead="Pick one service or the whole stack.", soft=False, exclude=None):
    cards = "\n".join(f'''      <a href="{s["slug"]}.html" class="sc rv" data-cursor="view"><div class="img"><img src="{U(s["img"],800)}" alt="{s["name"]}" loading="lazy"></div><div class="sc-b"><span class="sc-ic"><i class="fa-solid {s["icon"]}"></i></span><h3>{s["name"]}</h3><p>{SVC_LONG.get(s["slug"], s["card"])}</p><span class="go">Explore <i class="fa-solid fa-arrow-right"></i></span></div></a>''' for s in svcs if s["slug"] != exclude)
    return f'''<section class="sec{' soft' if soft else ''}">
  <div class="wrap">
{headrow(label, a, b, lead)}
    <div class="sc-grid">
{cards}
    </div>
  </div>
</section>'''

def incl(label, a, b, items, lead=None, soft=False, dark=False):
    cards = "\n".join(f'''      <div class="ic-card rv"><span class="ic"><i class="{ic if ic.startswith('fa-brands') else 'fa-solid '+ic}"></i></span><h3>{t}</h3><p>{d}</p></div>''' for ic, t, d in items)
    cls = "sec incl" + (" soft" if soft else "") + (" dark" if dark else "")
    return f'''<section class="{cls}">
  <div class="wrap">
{headrow(label, a, b, lead)}
    <div class="ic-grid">
{cards}
    </div>
  </div>
</section>'''

def types(label, a, b, items, lead=None, soft=False):
    rows = "\n".join(f'''      <div class="ty rv"><span class="n">{k+1:02d}</span><div><h3>{t}</h3><p>{d}</p></div><button type="button" class="ty-go" data-open-modal aria-label="Ask about {t}"><i class="fa-solid fa-arrow-right"></i></button></div>''' for k, (t, d) in enumerate(items))
    return f'''<section class="sec types{' soft' if soft else ''}">
  <div class="wrap">
{headrow(label, a, b, lead)}
    <div class="ty-grid">
{rows}
    </div>
  </div>
</section>'''

def why(label="Why choose us", a="Six reasons clients", b="<em class=\"s\">stay with us.</em>", items=WHY, img="smiling", stat=("10+","cities served across Delhi NCR")):
    cells = "\n".join(f'''        <div class="wy rv"><span class="n">— {k+1:02d}</span><i class="fa-solid {ic}"></i><h3>{t}</h3><p>{d}</p></div>''' for k, (ic, t, d) in enumerate(items))
    return f'''<section class="sec soft why2">
  <div class="wrap">
{headrow(label, a, b, right='<button type="button" class="btn btn-o rv" data-open-modal>Talk to us <i class="fa-solid fa-arrow-right"></i></button>')}
    <div class="why-wrap">
      <div class="why-g">
{cells}
      </div>
      <div class="why-img img rv cl"><img src="{U(img,700)}" alt="" loading="lazy"><div><b>{stat[0]}</b><span>{stat[1]}</span></div></div>
    </div>
  </div>
</section>'''

def process(steps=None, label="How we work", a="Simple process.", b="<em class=\"s\">No surprises.</em>"):
    steps = steps or [(t, d, w) for t, d, w, _ in PROCESS]
    imgs = ["meeting", "sketch", "code", "data"]
    pics = "\n".join(f'        <img{ON if k==0 else ""} src="{U(imgs[k%4])}" alt="" loading="lazy">' for k in range(len(steps)))
    rows = "\n".join(f'      <div class="step{SON if k==0 else ""} rv"><span class="n">{k+1:02d}</span><div><h3>{t}</h3><p>{d}</p></div><span class="wk-t">{w}</span></div>' for k, (t, d, w) in enumerate(steps))
    return f'''<section class="sec soft proc">
  <div class="wrap">
    <div class="proc-l">
      {idx(label)}
      {h2(a, b)}
      <div class="proc-img rv">
{pics}
      </div>
    </div>
    <div class="steps">
{rows}
    </div>
  </div>
</section>'''

def stack(label, a, b, chips, lead=None):
    c = "".join(f'<span class="rv">{x}</span>' for x in chips)
    return f'''<section class="sec stack-sec">
  <div class="wrap">
{headrow(label, a, b, lead)}
    <div class="stack">{c}</div>
  </div>
</section>'''

def industries(items=None, label="Industries", a="Who we <em class=\"s\">help.</em>", lead="We know what customers in these industries search for, and what makes them call."):
    items = items or INDUSTRIES
    rows = "\n".join(f'      <a href="contact.html" data-open-modal class="ind-row rv" data-img="{U(img,600)}"><span class="n">{k+1:02d}</span><h3>{t}</h3><p>{d}</p><span class="ar"><i class="fa-solid fa-arrow-right"></i></span></a>' for k, (t, d, img) in enumerate(items))
    return f'''<section class="sec">
  <div class="wrap">
{headrow(label, a, None, lead)}
    <div class="ind-list">
{rows}
    </div>
  </div>
  <div class="follower" aria-hidden="true"></div>
</section>'''

def work_grid(items, label="Selected work", a="Built for real", b="<em class=\"s\">businesses.</em>", filt=False, lead="A look at the kind of projects we build — by industry.", soft=False):
    chips = ""
    if filt:
        chips = '<div class="wf rv" role="tablist">' + "".join(f'<button type="button" class="{"on" if k==0 else ""}" data-wf="{c}">{l}</button>' for k, (c, l) in enumerate(WORK_CATS)) + '</div>'
    cards = "\n".join(f'''      <a href="contact.html" class="wk2 rv" data-cat="{cat}" data-open-modal data-cursor="view"><div class="img"><img src="{U(img,800)}" alt="{t}" loading="lazy"></div><span class="wk2-tag">{tag}</span><div class="wk2-b"><small>{sub}</small><h3>{t}</h3><p>{d}</p></div></a>''' for t, sub, img, cat, tag, d in items)
    return f'''<section class="sec{' soft' if soft else ''}" id="work">
  <div class="wrap">
{headrow(label, a, b, lead)}
    {chips}
    <div class="wk2-grid">
{cards}
    </div>
    <p class="note rv">Examples by industry. Ask us for live links to similar projects.</p>
  </div>
</section>'''

def promise():
    tq = "\n".join(f'''        <div class="tq{' on' if k==0 else ''}"><span class="mark">“</span><blockquote>{q}</blockquote><div class="who"><span class="av">MS</span><div><b>Md Sahil</b><span>Founder, GrowVika · {t}</span></div></div></div>''' for k, (q, t) in enumerate(PROMISE))
    return f'''<section class="sec tst2">
  <div class="wrap">
    <div class="t-img img rv cl"><img src="{U('pair',900)}" alt="GrowVika team working with a client" loading="lazy"><div class="badge"><b>1:1</b><div class="st"><i class="fa-solid fa-circle-check"></i> Founder-led</div><span>You work directly with the builder</span></div></div>
    <div class="t-r">
      {idx("Our promise")}
      <div class="tst-sl rv">
{tq}
      </div>
      <div class="t-nav"><span class="sl-count" data-t-cnt><b>01</b> / 03</span><span class="t-prog"><i data-t-prog></i></span><div class="sl-ctrl"><button type="button" data-t-prev aria-label="Previous"><i class="fa-solid fa-arrow-left"></i></button><button type="button" data-t-next aria-label="Next"><i class="fa-solid fa-arrow-right"></i></button></div></div>
    </div>
  </div>
</section>'''

def faq(items, label="FAQ", a="Questions,", b="<em class=\"s\">answered.</em>", sid="", more=True, card=True):
    qs = "\n".join(f'''      <div class="qa{' open' if k==0 else ''} rv"><button type="button" aria-expanded="{'true' if k==0 else 'false'}">{q}<i class="fa-solid fa-plus"></i></button><div class="ans"><div><p>{ans}</p></div></div></div>''' for k, (q, ans) in enumerate(items))
    link = '<a href="faq.html" class="link" style="margin-top:18px">All questions <i class="fa-solid fa-arrow-right"></i></a>' if more else ""
    i = f' id="{sid}"' if sid else ""
    fc = ('<div class="faq-card rv"><h4>Still have a question?</h4><p>Message us on WhatsApp. You\'ll get a reply from the person who builds your project.</p><a href="https://wa.me/' + WA + '" target="_blank" rel="noopener" class="btn btn-w"><i class="fa-brands fa-whatsapp"></i> Chat on WhatsApp</a></div>') if card else f'<p class="lead rv" style="margin-top:20px">{len(items)} questions</p>'
    return f'''<section class="sec faq"{i}>
  <div class="wrap">
    <div class="faq-l">
      {idx(label)}
      {h2(a, b)}
      {fc}
      {link}
    </div>
    <div class="qas">
{qs}
    </div>
  </div>
</section>'''

def enquiry(label="Enquiry", a="Let's build something", b="<em class=\"s\">that grows.</em>"):
    e = ENQ.replace('<section class="sec enq" id="contact">', '<section class="sec enq" id="enquiry">')
    e = re.sub(r'<div class="idx rv"><b>\d+</b><span>[^<]*</span></div>', idx(label), e)
    e = re.sub(r'<h2 class="h2 rv">.*?</h2>', h2(a, b), e, count=1, flags=re.S)
    return e

def nums(items, label="In numbers", a="Small team.", b="<em class=\"s\">Serious focus.</em>"):
    cells = "".join(f'<div class="rv"><b>{v}</b><span>{t}</span></div>' for v, t in items)
    return f'''<section class="sec nums2">
  <div class="wrap">
{headrow(label, a, b)}
    <div class="n2-grid">{cells}</div>
  </div>
</section>'''

def city_cards(exclude=None, label="Cities we serve", a="Pick your", b="<em class=\"s\">city.</em>", lead="Local pages for every part of Delhi NCR — with the areas we cover and what businesses there need most.", soft=False):
    cards = "\n".join(f'''      <a href="service-area-{c["slug"]}.html" class="cc rv" data-cursor="view"><img src="{U(c["img"],800)}" alt="{c["name"]}" loading="lazy"><div class="cc-b"><span class="cc-tag">{c["tag"]}</span><h3>{c["name"]}</h3><p>{", ".join(c["locs"][:4])} &amp; more</p><span class="go">View {c["name"]} <i class="fa-solid fa-arrow-right"></i></span></div></a>''' for c in AREAS if c["slug"] != exclude)
    return f'''<section class="sec{' soft' if soft else ''}">
  <div class="wrap">
{headrow(label, a, b, lead)}
    <div class="cc-grid">
{cards}
    </div>
  </div>
</section>'''

TPL = [
 "{l} in {c} is home to {biz}. Customers here compare options on Google Maps before they call, so we focus on a fast website, a complete Google Business Profile and local SEO for searches like “near me in {l}”.",
 "For {biz} in {l}, most enquiries start on a phone. We build mobile-first pages, add one-tap WhatsApp and call buttons, and run ads targeted to people within a few kilometres of {l}, {c}.",
 "Competition is close in {l} — {biz} often sit a few doors apart. A professional website, genuine reviews, regular Instagram posts and quick replies on WhatsApp help {c} businesses here stand out and win the first call.",
 "We work with {biz} across {l}. Popular projects here include {svc}, Google Maps optimisation and a simple CRM so every enquiry from {l} gets a follow-up — with a free first meeting at your office.",
]
def localities(city, soft=True):
    cards = []
    for k, l in enumerate(city["locs"]):
        key = l.replace("&", "&amp;").replace("&amp;amp;", "&amp;")
        info = LOC_INFO.get(key) or LOC_INFO.get(l) or ("Local business area", "shops, clinics and services", "website-development")
        if city["slug"] == "faridabad" and l == "Sector 15": info = LOC_INFO["Sector 15 (Faridabad)"]
        kind, biz, svc = info; sv = SVC[svc]
        cards.append(f'''      <div class="lc rv"><div class="lc-h"><span class="lc-ic"><i class="fa-solid fa-location-dot"></i></span><div><h3>{l}</h3><small>{kind}</small></div></div><p>{TPL[k % len(TPL)].format(l=l, c=city["name"], biz=biz, svc=sv["name"].lower())}</p><div class="lc-f"><span>Popular: <a href="{sv["slug"]}.html">{sv["name"]}</a></span><button type="button" data-open-modal>Free meeting in {l} <i class="fa-solid fa-arrow-right"></i></button></div></div>''')
    return f'''<section class="sec loc-sec{' soft' if soft else ''}">
  <div class="wrap">
{headrow("Areas we cover", "Across", EMS + city["name"] + ".</em>", f"We work with businesses in every part of {city['name']} — meetings at your office or online. Here are the areas we serve most often, and what businesses there usually need.")}
    <div class="lc-grid">
{chr(10).join(cards)}
    </div>
    <p class="lc-more rv">Don't see your area? We cover all of {city["name"]} and nearby — <a href="contact.html">get in touch</a>.</p>
  </div>
</section>'''

def map_sec(q, label="Find us", a="Serving", b=None):
    b = b or f'<em class="s">{q}.</em>'
    return f'''<section class="sec map-sec">
  <div class="wrap">
{headrow(label, a, b, "We visit businesses across the city for the first meeting — free.")}
    <div class="map rv" style="margin-top:0"><iframe title="Map of {q}" src="https://www.google.com/maps?q={q.replace(' ','+')},+India&z=11&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe><a class="map-open" href="https://www.google.com/maps?q={q.replace(' ','+')}" target="_blank" rel="noopener">Open in Maps <i class="fa-solid fa-arrow-up-right-from-square"></i></a></div>
  </div>
</section>'''

def blog_slider(posts=POSTS[:6]):
    cards = "\n".join(f'''      <a href="blog-{sl}.html" class="bc" data-cursor="view"><div class="img"><img src="{U(img,800)}" alt="{t}" loading="lazy"><span class="cat">{c}</span></div><div class="meta"><span><i class="fa-regular fa-folder"></i>{f}</span><span><i class="fa-regular fa-clock"></i>{m}</span></div><h3>{t}</h3><p>{d}</p><span class="rm">Read article <i class="fa-solid fa-arrow-right"></i></span></a>''' for c, f, m, img, t, d, sl in posts)
    return f'''<section class="sec soft blog2">
  <div class="wrap">
{headrow("Journal", "From the " + EMS + "blog.</em>", right='<div class="sl-ctrl rv"><a href="blog.html" class="btn btn-o">All articles</a><button type="button" data-b-prev aria-label="Previous articles"><i class="fa-solid fa-arrow-left"></i></button><button type="button" data-b-next aria-label="Next articles"><i class="fa-solid fa-arrow-right"></i></button></div>')}
    <div class="bl-track rv">
{cards}
    </div>
  </div>
</section>'''

def cta_strip(t1, t2, sub):
    return f'''<section class="sec cta2">
  <div class="wrap">
    <div class="cta2-box rv">
      <div><h2>{t1} <em class="s">{t2}</em></h2><p>{sub}</p></div>
      <div class="cta2-b"><button type="button" class="btn btn-w" data-open-modal>Start a new project <i class="fa-solid fa-arrow-right"></i></button><a href="tel:+919818186876" class="btn f-wa"><i class="fa-solid fa-phone"></i> +91-9818186876</a></div>
    </div>
  </div>
</section>'''

def contact_cards(label="Reach us", a="Pick what's <em class=\"s\">easiest.</em>"):
    return f'''<section class="sec ways">
  <div class="wrap">
{headrow(label, a, None, "Every message reaches the founder and the build team — no call centre, no ticket numbers.")}
    <div class="way-grid">
      <a href="tel:+919818186876" class="way rv"><span class="ic"><i class="fa-solid fa-phone"></i></span><small>Call us</small><b>+91-9818186876</b><p>Talk through your idea in a quick call.</p><span class="go">Call now <i class="fa-solid fa-arrow-right"></i></span></a>
      <a href="https://wa.me/{WA}" target="_blank" rel="noopener" class="way wa-way rv d1"><span class="ic"><i class="fa-brands fa-whatsapp"></i></span><small>WhatsApp</small><b>Chat with us</b><p>Fastest reply — share photos, links or voice notes.</p><span class="go">Open WhatsApp <i class="fa-solid fa-arrow-right"></i></span></a>
      <a href="mailto:sahil@growvika.com" class="way rv d2"><span class="ic"><i class="fa-regular fa-envelope"></i></span><small>Email</small><b>sahil@growvika.com</b><p>Send a brief, documents or a proposal request.</p><span class="go">Write an email <i class="fa-solid fa-arrow-right"></i></span></a>
      <button type="button" class="way rv d3" data-open-modal><span class="ic"><i class="fa-solid fa-location-dot"></i></span><small>Meet in person</small><b>Delhi NCR</b><p>Delhi, Gurugram, Noida, Ghaziabad, Faridabad.</p><span class="go">Book a meeting <i class="fa-solid fa-arrow-right"></i></span></button>
    </div>
  </div>
</section>'''


# ---------------- structured data ----------------
import json
def ld(obj): return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>\n'
def schema_org():
    return ld({"@context":"https://schema.org","@type":"ProfessionalService","name":"GrowVika","url":BASE,"telephone":"+91-9818186876","email":"sahil@growvika.com",
      "description":"Website development, mobile apps, CRM, custom software and digital marketing agency in Delhi NCR.",
      "areaServed":[a["name"] for a in AREAS],"address":{"@type":"PostalAddress","addressRegion":"Delhi NCR","addressCountry":"IN"},
      "founder":{"@type":"Person","name":"Md Sahil"}})
def breadcrumb_ld(items):
    els=[{"@type":"ListItem","position":1,"name":"Home","item":BASE+"/"}]
    for k,(name,path) in enumerate(items):
        els.append({"@type":"ListItem","position":k+2,"name":name,"item":f"{BASE}/{path}"})
    return ld({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":els})
def faq_ld(body):
    qs=re.findall(r'<div class="qa[^"]*"><button type="button" aria-expanded="[a-z]+">(.*?)<i class="fa-solid fa-plus"></i></button><div class="ans"><div><p>(.*?)</p>',body)
    if not qs: return ""
    strip=lambda s: re.sub(r"<[^>]+>","",s).replace("&amp;","&")
    return ld({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":strip(q),"acceptedAnswer":{"@type":"Answer","text":strip(a)}} for q,a in qs[:30]]})

# ---------------- tools & tech (categorised) ----------------
TECH = [
 ("fa-pen-ruler","Design &amp; UX","Wireframes, UI design and clickable prototypes you approve before code.",[("Figma","UI design &amp; prototypes"),("Canva","Social creatives"),("Adobe XD","Legacy design files")]),
 ("fa-code","Frontend","Fast, accessible interfaces that work on every screen.",[("HTML5 / CSS3","Semantic, SEO-friendly markup"),("JavaScript","Interactions"),("React","Component UIs"),("Next.js","Fast, SEO-ready sites &amp; apps"),("Tailwind","Consistent styling")]),
 ("fa-server","Backend &amp; data","Secure APIs, databases and logins behind your product.",[("Node.js","APIs &amp; servers"),("Python","Automation &amp; data"),("PostgreSQL","Reliable database"),("Supabase","Auth, storage &amp; database"),("Firebase","Realtime &amp; push")]),
 ("fa-store","CMS &amp; e-commerce","Editable websites and online stores you can manage yourself.",[("WordPress","Editable business sites"),("Shopify","Hosted online stores"),("WooCommerce","WordPress stores")]),
 ("fa-mobile-screen","Mobile apps","One codebase for Android and iOS with a native feel.",[("Flutter","Cross-platform apps"),("React Native","Cross-platform apps"),("OneSignal","Push notifications")]),
 ("fa-plug","Payments &amp; integrations","The services your customers already use in India.",[("Razorpay","UPI, cards &amp; wallets"),("UPI / PhonePe","Instant payments"),("Shiprocket","Shipping &amp; tracking"),("WhatsApp","Click-to-chat &amp; alerts"),("Google Maps","Locations &amp; directions")]),
 ("fa-chart-line","Marketing &amp; analytics","Track every visit, call and lead — and improve every month.",[("Google Analytics 4","Visits &amp; conversions"),("Search Console","Google rankings"),("Google Ads","Search campaigns"),("Meta Ads","Facebook &amp; Instagram"),("Looker Studio","Monthly reports")]),
 ("fa-shield-halved","Hosting &amp; security","Fast global hosting with SSL, backups and monitoring.",[("Vercel","Fast hosting"),("Cloudflare","CDN &amp; protection"),("AWS","Scalable cloud"),("SSL / HTTPS","Encrypted connections"),("Backups","Daily safety copies")]),
]
PRINCIPLES = [("fa-bolt","Fast by default","Lightweight code and optimised images for quick mobile loading."),("fa-lock","Secure","HTTPS, safe logins, updates and regular backups."),("fa-key","You own it","Accounts, code and data in your name — no lock-in."),("fa-screwdriver-wrench","Easy to maintain","Popular, well-supported tools any good developer knows.")]

def stack(label, a, b, chips=None, lead=None):
    hl = set(re.sub(r"&amp;", "&", c).lower() for c in (chips or []))
    def tool(n, d):
        on = re.sub(r"&amp;", "&", n).lower() in hl or any(h in re.sub(r"&amp;", "&", n).lower() for h in hl if len(h) > 3)
        return f'<li class="{"hl" if on else ""}"><b>{n}</b><span>{d}</span></li>'
    cards = "\n".join(f'''      <div class="tc rv"><div class="tc-h"><span class="ic"><i class="fa-solid {ic}"></i></span><div><h3>{t}</h3><p>{d}</p></div></div><ul>{"".join(tool(n, dd) for n, dd in tools)}</ul></div>''' for ic, t, d, tools in TECH)
    pr = "".join(f'<div class="tp rv"><i class="fa-solid {ic}"></i><div><b>{t}</b><span>{d}</span></div></div>' for ic, t, d in PRINCIPLES)
    note = '<p class="tc-note rv"><i class="fa-solid fa-circle"></i> Highlighted tools are the ones we use most for this service.</p>' if chips else ""
    return f'''<section class="sec tech">
  <div class="wrap">
{headrow(label, a, b, lead or "We pick proven, well-supported tools — so your project is fast, secure and easy for anyone to maintain.")}
    <div class="tp-row">{pr}</div>
    <div class="tc-grid">
{cards}
    </div>
    {note}
  </div>
</section>'''

# ---------------- long-form SEO copy ----------------
def seo_copy(label, a, b, blocks, aside_title, aside_items, soft=False):
    body = "\n".join(f'<h3>{h}</h3>\n{p}' for h, p in blocks)
    toc = "".join(f'<li><i class="fa-solid fa-check"></i>{x}</li>' for x in aside_items)
    return f'''<section class="sec seo{' soft' if soft else ''}">
  <div class="wrap">
{headrow(label, a, b)}
    <div class="seo-g">
      <article class="prose rv">
{body}
      </article>
      <aside class="seo-aside rv">
        <div class="sa-card"><h4>{aside_title}</h4><ul>{toc}</ul><button type="button" class="btn btn-i" data-open-modal>Get a free quote <i class="fa-solid fa-arrow-right"></i></button><a href="https://wa.me/{WA}" target="_blank" rel="noopener" class="sa-wa"><i class="fa-brands fa-whatsapp"></i> Ask on WhatsApp</a></div>
      </aside>
    </div>
  </div>
</section>'''

# ---------------- modern 'types' (cards) ----------------
def types(label, a, b, items, lead=None, soft=False):
    cards = "\n".join(f'''      <div class="ty2 rv"><span class="n">{k+1:02d}</span><h3>{t}</h3><p>{d}</p><button type="button" class="ty2-go" data-open-modal>Ask about this <i class="fa-solid fa-arrow-right"></i></button></div>''' for k, (t, d) in enumerate(items))
    return f'''<section class="sec types{' soft' if soft else ''}">
  <div class="wrap">
{headrow(label, a, b, lead)}
    <div class="ty2-grid">
{cards}
    </div>
  </div>
</section>'''
