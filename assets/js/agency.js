/* GrowVika agency home — interactions (no libraries) */
(function () {
  "use strict";
  var WHATSAPP = "919818186876";
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var fine = window.matchMedia("(hover:hover) and (pointer:fine)").matches;
  var reduce = window.matchMedia("(prefers-reduced-motion:reduce)").matches;
  var y = $("[data-year]"); if (y) y.textContent = new Date().getFullYear();

  /* image fallback */
  $$("img").forEach(function (im) {
    im.addEventListener("error", function () { var p = im.closest(".img"); if (p) p.classList.add("fail"); else im.style.visibility = "hidden"; }, { once: true });
  });

  /* header shadow + to-top */
  var header = $(".header"), totop = $(".totop");
  function onScroll() {
    var sy = window.scrollY;
    header.classList.toggle("scrolled", sy > 10);
    totop.classList.toggle("on", sy > 900);
  }
  window.addEventListener("scroll", onScroll, { passive: true }); onScroll();
  totop.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" }); });

  /* mega menus (Services, Service Area) */
  var megas = $$(".has-mega");
  megas.forEach(function (mega) {
    var btn = $("button", mega), timer;
    var set = function (o) {
      if (o) megas.forEach(function (m) { if (m !== mega) { m.classList.remove("open"); $("button", m).setAttribute("aria-expanded", "false"); } });
      mega.classList.toggle("open", o); btn.setAttribute("aria-expanded", o);
    };
    btn.addEventListener("click", function () { set(!mega.classList.contains("open")); });
    if (fine) {
      mega.addEventListener("mouseenter", function () { clearTimeout(timer); set(true); });
      mega.addEventListener("mouseleave", function () { timer = setTimeout(function () { set(false); }, 180); });
    }
    document.addEventListener("click", function (e) { if (!mega.contains(e.target)) set(false); });
    $$(".mega a", mega).forEach(function (a) { a.addEventListener("click", function () { set(false); }); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && mega.classList.contains("open")) { set(false); btn.focus(); } });
  });

  /* mobile nav */
  var mnav = $(".mnav"), mbd = $(".mnav-bd"), burger = $(".burger");
  function setNav(o) {
    mnav.classList.toggle("open", o); mbd.classList.toggle("open", o);
    burger.setAttribute("aria-expanded", o);
    document.body.style.overflow = o ? "hidden" : "";
    if (o) $(".mnav-x").focus();
  }
  burger.addEventListener("click", function () { setNav(true); });
  $(".mnav-x").addEventListener("click", function () { setNav(false); burger.focus(); });
  mbd.addEventListener("click", function () { setNav(false); });
  $$(".mnav a, .mnav [data-open-modal]").forEach(function (a) { a.addEventListener("click", function () { setNav(false); }); });

  /* reveal */
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
  }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
  $$(".rv").forEach(function (el) { io.observe(el); });
  /* hero animates on load */
  requestAnimationFrame(function () { $$(".hero .rv").forEach(function (el) { el.classList.add("in"); }); });

  /* counters */
  var cio = new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (!e.isIntersecting) return; cio.unobserve(e.target);
      var el = e.target, to = +el.getAttribute("data-count"), t0 = null, dur = 1600;
      function fmt(n) { return n.toLocaleString("en-IN"); }
      if (reduce) { el.textContent = fmt(to); return; }
      (function step(t) {
        if (!t0) t0 = t; var p = Math.min((t - t0) / dur, 1), v = Math.round(to * (1 - Math.pow(1 - p, 3)));
        el.textContent = fmt(v); if (p < 1) requestAnimationFrame(step);
      })(performance.now());
    });
  }, { threshold: 0.5 });
  $$("[data-count]").forEach(function (el) { cio.observe(el); });

  /* hero slider with progress bars */
  var hs = $("[data-hs]");
  if (hs) {
    var slides = $$(".s", hs), bars = $(".bars", hs), hi = 0, htimer;
    var caps = [["Website development", "Sites that turn visitors into enquiries"], ["Clean, fast code", "Built mobile-first, ready for Google"], ["Mobile apps", "Android & iOS apps your customers love"], ["Digital marketing", "SEO & ads that fill your CRM with leads"]];
    slides.forEach(function (_, i) { var b = document.createElement("button"); b.type = "button"; b.setAttribute("aria-label", "Slide " + (i + 1)); b.addEventListener("click", function () { go(i); }); bars.appendChild(b); });
    var bs = $$("button", bars);
    function go(i) {
      hi = (i + slides.length) % slides.length;
      slides.forEach(function (s, k) { s.classList.toggle("on", k === hi); });
      bs.forEach(function (b, k) { b.classList.remove("on"); b.classList.toggle("done", k < hi); });
      void bs[hi].offsetWidth; bs[hi].classList.add("on");
      $("[data-hs-k]", hs).textContent = caps[hi][0]; $("[data-hs-t]", hs).textContent = caps[hi][1];
      clearTimeout(htimer); htimer = setTimeout(function () { go(hi + 1); }, 5000);
    }
    go(0);
  }

  /* pinned horizontal services rail (desktop) */
  var pin = $(".pin"), rail = $(".rail"), rbar = $("[data-rail-bar]"), rcnt = $("[data-rail-cnt]");
  var pinOn = false, maxX = 0;
  function setupPin() {
    if (!pin || !rail) return;
    pinOn = window.innerWidth > 980;
    if (!pinOn) { pin.style.height = ""; rail.style.transform = ""; return; }
    var rl = rail.lastElementChild; maxX = rl ? Math.max(0, rl.offsetLeft + rl.offsetWidth - rail.clientWidth) : 0;
    pin.style.height = (window.innerHeight + maxX) + "px";
    movePin();
  }
  function movePin() {
    if (!pinOn || !pin) return;
    var r = pin.getBoundingClientRect(), total = pin.offsetHeight - window.innerHeight;
    var p = total > 0 ? Math.min(Math.max(-r.top / total, 0), 1) : 0;
    rail.style.transform = "translate3d(" + (-maxX * p) + "px,0,0)";
    rbar.style.width = (p * 100) + "%";
    var n = Math.min(6, Math.floor(p * 6) + 1);
    rcnt.textContent = "0" + n + " / 06";
  }
  window.addEventListener("scroll", movePin, { passive: true });
  window.addEventListener("resize", setupPin);
  window.addEventListener("load", setupPin);
  setupPin();

  /* process: swap image on hover/scroll */
  var steps = $$(".step"), pimgs = $$(".proc-img img");
  function setStep(i) { steps.forEach(function (s, k) { s.classList.toggle("on", k === i); }); pimgs.forEach(function (im, k) { im.classList.toggle("on", k === i); }); }
  steps.forEach(function (s, i) { s.addEventListener("mouseenter", function () { setStep(i); }); });
  var sio = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) setStep(steps.indexOf(e.target)); }); }, { rootMargin: "-45% 0px -45% 0px" });
  steps.forEach(function (s) { sio.observe(s); });

  /* industries: image follows cursor */
  var fol = $(".follower");
  if (fol && fine) {
    var rows = $$(".ind-row"), fx = 0, fy = 0, tx = 0, ty = 0, frun = false;
    rows.forEach(function (r) { var im = new Image(); im.src = r.getAttribute("data-img"); im.alt = ""; fol.appendChild(im); });
    var fimgs = $$("img", fol);
    function loop() { fx += (tx - fx) * 0.16; fy += (ty - fy) * 0.16; fol.style.left = fx + "px"; fol.style.top = fy + "px"; if (frun) requestAnimationFrame(loop); }
    rows.forEach(function (r, i) {
      r.addEventListener("mouseenter", function (e) { tx = fx = e.clientX; ty = fy = e.clientY; fimgs.forEach(function (im, k) { im.classList.toggle("on", k === i); }); fol.classList.add("on"); if (!frun) { frun = true; loop(); } });
      r.addEventListener("mousemove", function (e) { tx = e.clientX; ty = e.clientY; });
      r.addEventListener("mouseleave", function () { fol.classList.remove("on"); frun = false; });
    });
  }

  /* testimonials */
  var tqs = $$(".tq"), ti = 0, tcnt = $("[data-t-cnt]"), ttimer;
  function tgo(i) { ti = (i + tqs.length) % tqs.length; tqs.forEach(function (q, k) { q.classList.toggle("on", k === ti); }); tcnt.innerHTML = "<b>0" + (ti + 1) + "</b> / 0" + tqs.length; var tp = $("[data-t-prog]"); if (tp) { tp.classList.remove("run"); void tp.offsetWidth; tp.classList.add("run"); } clearTimeout(ttimer); ttimer = setTimeout(function () { tgo(ti + 1); }, 7000); }
  if (tqs.length && tcnt) {
    $("[data-t-prev]").addEventListener("click", function () { tgo(ti - 1); });
    $("[data-t-next]").addEventListener("click", function () { tgo(ti + 1); });
    tgo(0);
  }


  /* about video: play/pause, pause when off-screen */
  var vid = $(".vid video"), vbtn = $(".vbtn");
  if (vid) {
    var userPaused = false;
    if (reduce) { vid.removeAttribute("autoplay"); vid.pause(); userPaused = true; }
    var setIcon = function () { var p = vid.paused; vbtn.innerHTML = '<i class="fa-solid fa-' + (p ? "play" : "pause") + '"></i>'; vbtn.setAttribute("aria-label", p ? "Play video" : "Pause video"); };
    vbtn.addEventListener("click", function () { if (vid.paused) { userPaused = false; vid.play(); } else { userPaused = true; vid.pause(); } });
    vid.addEventListener("play", setIcon); vid.addEventListener("pause", setIcon); setIcon();
    new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { if (!userPaused) { var pr = vid.play(); if (pr && pr.catch) pr.catch(function () {}); } } else vid.pause(); }); }, { threshold: 0.2 }).observe(vid);
    vid.addEventListener("error", function () { vid.closest(".vid").classList.add("fail"); }, true);
  }

  /* blog slider */
  var bt = $(".bl-track");
  if (bt) {
    var bstep = function (d) { var c = $(".bc", bt); bt.scrollBy({ left: d * (c.offsetWidth + 26), behavior: reduce ? "auto" : "smooth" }); };
    $("[data-b-prev]").addEventListener("click", function () { bstep(-1); });
    $("[data-b-next]").addEventListener("click", function () { if (bt.scrollLeft + bt.clientWidth >= bt.scrollWidth - 5) bt.scrollTo({ left: 0, behavior: "smooth" }); else bstep(1); });
  }

  /* enquiry form -> WhatsApp */
  var ef = $("#eform");
  if (ef) ef.addEventListener("submit", function (e) {
    e.preventDefault();
    var F = ef.elements;
    var req = [F["name"], F["phone"], F["svc"]], ok = true;
    req.forEach(function (i) { var bad = !i.value.trim(); i.classList.toggle("err", bad); if (bad && ok) { i.focus(); ok = false; } });
    if (!ok) return;
    var L = ["Hi GrowVika, new enquiry from the website.", "", "Name: " + F["name"].value.trim(), "Phone: " + F["phone"].value.trim(), "Service: " + F["svc"].value];
    if (F["email"].value.trim()) L.push("Email: " + F["email"].value.trim());
    if (F["biz"].value.trim()) L.push("Business: " + F["biz"].value.trim());
    if (F["time"].value) L.push("Timeline: " + F["time"].value);
    if (F["msg"].value.trim()) L.push("Requirement: " + F["msg"].value.trim());
    window.open("https://wa.me/" + WHATSAPP + "?text=" + encodeURIComponent(L.join("\n")), "_blank", "noopener");
    $(".form-msg", ef).classList.add("ok"); ef.reset();
  });


  /* service area city slider */
  var atabs = $$(".ar-tab"), aslides = $$(".ar-slide"), acnt = $("[data-ar-cnt]"), ai = 0, atimer, apaused = false;
  if (atabs.length) {
    var ago = function (i, user) {
      ai = (i + atabs.length) % atabs.length;
      atabs.forEach(function (t, k) { var on = k === ai; t.classList.toggle("on", on); t.setAttribute("aria-selected", on); var g = $(".pg i", t); g.classList.remove("run"); if (on) { void g.offsetWidth; g.classList.add("run"); } });
      aslides.forEach(function (s, k) { s.classList.toggle("on", k === ai); });
      acnt.textContent = "0" + (ai + 1);
      if (user && window.innerWidth <= 980) atabs[ai].scrollIntoView({ block: "nearest", inline: "center", behavior: "smooth" });
      clearTimeout(atimer); if (!apaused && !reduce) atimer = setTimeout(function () { ago(ai + 1); }, 6000);
    };
    atabs.forEach(function (t, k) { t.addEventListener("click", function () { ago(k, true); }); });
    $("[data-ar-prev]").addEventListener("click", function () { ago(ai - 1, true); });
    $("[data-ar-next]").addEventListener("click", function () { ago(ai + 1, true); });
    var stage = $(".ar-stage");
    stage.addEventListener("mouseenter", function () { apaused = true; clearTimeout(atimer); $$(".ar-tab .pg i").forEach(function (g) { g.style.animationPlayState = "paused"; }); });
    stage.addEventListener("mouseleave", function () { apaused = false; $$(".ar-tab .pg i").forEach(function (g) { g.style.animationPlayState = ""; }); clearTimeout(atimer); atimer = setTimeout(function () { ago(ai + 1); }, 3000); });
    var tsx = 0; stage.addEventListener("touchstart", function (e) { tsx = e.touches[0].clientX; }, { passive: true });
    stage.addEventListener("touchend", function (e) { var dx = e.changedTouches[0].clientX - tsx; if (Math.abs(dx) > 50) ago(ai + (dx < 0 ? 1 : -1), true); }, { passive: true });
    new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) ago(ai); else clearTimeout(atimer); }); }, { threshold: 0.25 }).observe(stage);
  }
  /* links like #areas-2 open the service area on that city */
  function cityFromHash() {
    var m = /^#areas-(\d)$/.exec(location.hash), sec = $("#areas");
    if (!m || !sec) return;
    if (atabs.length) ago(+m[1]);
    setTimeout(function () { sec.scrollIntoView({ behavior: reduce ? "auto" : "smooth" }); }, 30);
  }
  window.addEventListener("hashchange", cityFromHash);
  cityFromHash();


  /* rotating word in hero */
  var rot = $(".rot");
  if (rot && !reduce) {
    var rw = $$("span", rot), ri = 0;
    setInterval(function () {
      var cur = rw[ri]; cur.classList.remove("on"); cur.classList.add("out");
      setTimeout(function () { cur.classList.remove("out"); }, 700);
      ri = (ri + 1) % rw.length; rw[ri].classList.add("on");
    }, 2400);
  }


  /* work + blog filters */
  function setupFilter(btnSel, attr, itemSel) {
    var btns = $$(btnSel); if (!btns.length) return;
    btns.forEach(function (b) {
      b.addEventListener("click", function () {
        var v = b.getAttribute(attr);
        btns.forEach(function (x) { x.classList.toggle("on", x === b); });
        $$(itemSel).forEach(function (it) {
          var show = v === "all" || v === "All" || it.getAttribute("data-cat") === v;
          it.classList.toggle("hide", !show); if (show) it.classList.add("in");
        });
      });
    });
  }
  setupFilter("[data-wf]", "data-wf", ".wk[data-cat], .wk2[data-cat]");
  $$("[data-wf]").forEach(function (b) { b.addEventListener("click", function () { var g = $(".work-grid"); if (g) g.classList.toggle("filtered", b.getAttribute("data-wf") !== "all"); }); });
  setupFilter("[data-bf]", "data-bf", ".bl-grid .bc[data-cat]");

  /* FAQ page search */
  var fq = $("#fq-q");
  if (fq) {
    var fqn = $("#fq-n");
    fq.addEventListener("input", function () {
      var q = fq.value.trim().toLowerCase(), total = 0;
      $$(".fq-group").forEach(function (g) {
        var n = 0;
        $$(".qa", g).forEach(function (qa) {
          var hit = !q || qa.textContent.toLowerCase().indexOf(q) > -1;
          qa.classList.toggle("hide", !hit); if (hit) { n++; qa.classList.add("in"); }
          if (q && hit) { qa.classList.add("open"); $("button", qa).setAttribute("aria-expanded", "true"); }
        });
        g.classList.toggle("hide", n === 0); total += n;
      });
      fqn.textContent = q ? total + (total === 1 ? " result" : " results") : "";
    });
  }


  /* copy-link buttons (blog share) */
  $$("[data-copy]").forEach(function (b) {
    b.addEventListener("click", function () {
      var url = b.getAttribute("data-copy");
      var done = function () { b.innerHTML = '<i class="fa-solid fa-check"></i>'; setTimeout(function () { b.innerHTML = '<i class="fa-solid fa-link"></i>'; }, 1500); };
      if (navigator.clipboard) navigator.clipboard.writeText(url).then(done, done); else done();
    });
  });
  /* article table of contents: highlight current section */
  var tocLinks = $$(".toc a");
  if (tocLinks.length) {
    var heads = tocLinks.map(function (a) { return document.getElementById(a.getAttribute("href").slice(1)); }).filter(Boolean);
    var tocObs = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { var id = "#" + e.target.id; tocLinks.forEach(function (a) { a.classList.toggle("on", a.getAttribute("href") === id); }); } }); }, { rootMargin: "-20% 0px -70% 0px" });
    heads.forEach(function (h) { tocObs.observe(h); });
  }


  /* feature tabs: list on the right swaps the image on the left */
  $$("[data-ft2]").forEach(function (box) {
    var its = $$(".ft2-it", box), ims = $$(".ft2-imgs img", box), n = $("[data-ft2-n]", box), t = $("[data-ft2-t]", box);
    function set(i) {
      its.forEach(function (it, k) { it.classList.toggle("on", k === i); $("button", it).setAttribute("aria-expanded", k === i); });
      ims.forEach(function (im, k) { im.classList.toggle("on", k === i); });
      n.textContent = (i < 9 ? "0" : "") + (i + 1); t.textContent = $(".t", its[i]).textContent;
    }
    its.forEach(function (it, k) {
      $("button", it).addEventListener("click", function () { set(k); });
      if (fine) it.addEventListener("mouseenter", function () { set(k); });
    });
  });

  /* swiper-style sliders: pinned on desktop (vertical scroll moves the slider), swipe on touch */
  $$("[data-sl2]").forEach(function (sl) {
    var sec = sl.closest("section"), tr = $(".sl2-track", sl), bar = $(".sl2-bar i", sec), pinned = false, maxX = 0;
    function setBar(p) { if (bar) bar.style.width = (15 + p * 85) + "%"; }
    function step() { var c = $(".sl2-c", tr); return c ? c.offsetWidth + 24 : 400; }
    function setup() {
      pinned = window.innerWidth > 980;
      sec.classList.toggle("pinned", pinned);
      tr.style.transform = "";
      if (!pinned) { sec.style.height = ""; return; }
      var cs = $$(".sl2-c", tr), last = cs[cs.length - 1];
      maxX = last ? Math.max(0, last.offsetLeft + last.offsetWidth - tr.clientWidth) : 0;
      sec.style.height = (window.innerHeight + maxX) + "px";
      move();
    }
    function move() {
      if (!pinned) return;
      var r = sec.getBoundingClientRect(), tot = sec.offsetHeight - window.innerHeight;
      var p = tot > 0 ? Math.min(Math.max(-r.top / tot, 0), 1) : 0;
      tr.style.transform = "translate3d(" + (-maxX * p) + "px,0,0)"; setBar(p);
    }
    function nprog() { if (pinned) return; var m = tr.scrollWidth - tr.clientWidth; setBar(m > 0 ? tr.scrollLeft / m : 1); }
    window.addEventListener("scroll", move, { passive: true });
    window.addEventListener("resize", setup);
    window.addEventListener("load", setup);
    tr.addEventListener("scroll", nprog, { passive: true });
    setup(); nprog();
    function go(d) {
      if (pinned) { window.scrollBy({ top: d * step(), behavior: reduce ? "auto" : "smooth" }); return; }
      if (d > 0 && tr.scrollLeft + tr.clientWidth >= tr.scrollWidth - 5) tr.scrollTo({ left: 0, behavior: "smooth" });
      else tr.scrollBy({ left: d * step(), behavior: "smooth" });
    }
    var pv = $("[data-sl2-prev]", sec), nx = $("[data-sl2-next]", sec);
    if (pv) pv.addEventListener("click", function () { go(-1); });
    if (nx) nx.addEventListener("click", function () { go(1); });
  });

  /* FAQ */
  $$(".qa").forEach(function (qa) {
    var b = $("button", qa);
    b.addEventListener("click", function () {
      var open = !qa.classList.contains("open");
      $$(".qa", qa.parentNode).forEach(function (o) { o.classList.remove("open"); $("button", o).setAttribute("aria-expanded", "false"); });
      qa.classList.toggle("open", open); b.setAttribute("aria-expanded", open);
    });
  });

  /* custom cursor with scroll-progress ring */
  if (fine && !reduce) {
    document.documentElement.classList.add("has-cursor");
    var cur = $(".cur"), dot = $(".cur-dot"), pr = $(".cur .pr"), C = 2 * Math.PI * 21;
    pr.style.strokeDasharray = C; pr.style.strokeDashoffset = C;
    var mx = -100, my = -100, cx = -100, cy = -100;
    document.addEventListener("mousemove", function (e) { mx = e.clientX; my = e.clientY; dot.style.transform = "translate(" + mx + "px," + my + "px)"; });
    (function raf() { cx += (mx - cx) * 0.18; cy += (my - cy) * 0.18; cur.style.transform = "translate(" + cx + "px," + cy + "px)"; requestAnimationFrame(raf); })();
    var ring = function () { var h = document.documentElement.scrollHeight - innerHeight; pr.style.strokeDashoffset = C * (1 - (h > 0 ? scrollY / h : 0)); };
    window.addEventListener("scroll", ring, { passive: true }); ring();
    document.addEventListener("mouseover", function (e) {
      var v = e.target.closest("[data-cursor=view]"), a = e.target.closest("a,button,input,select,textarea,label");
      cur.classList.toggle("view", !!v); cur.classList.toggle("hov", !v && !!a);
    });
    document.addEventListener("mouseleave", function () { cur.style.opacity = dot.style.opacity = 0; });
    document.addEventListener("mouseenter", function () { cur.style.opacity = dot.style.opacity = 1; });
  }

  /* popup */
  var modal = $("#modal"), form = $("#pform"), lastFocus = null;
  function openModal(svc) {
    lastFocus = document.activeElement;
    modal.classList.remove("sent"); modal.classList.add("open"); modal.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
    if (svc) $$('input[name=svc]', form).forEach(function (c) { c.checked = c.value === svc; });
    setTimeout(function () { $("#f-name").focus({ preventScroll: true }); }, 60);
    try { sessionStorage.setItem("gv_popup", "1"); } catch (e) {}
  }
  function closeModal() {
    modal.classList.remove("open"); modal.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
    if (lastFocus && lastFocus.focus) lastFocus.focus({ preventScroll: true });
  }
  $$("[data-open-modal]").forEach(function (b) {
    b.addEventListener("click", function (e) { e.preventDefault(); openModal(b.getAttribute("data-svc")); });
  });
  $$("[data-close]", modal).forEach(function (b) { b.addEventListener("click", closeModal); });
  document.addEventListener("keydown", function (e) {
    if (!modal.classList.contains("open")) return;
    if (e.key === "Escape") closeModal();
    if (e.key === "Tab") {
      var f = $$("a[href],button,input,select,textarea", modal).filter(function (x) { return x.offsetParent !== null; });
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var name = $("#f-name"), phone = $("#f-phone"), ok = true;
    var checks = [[name, !name.value.trim()], [phone, phone.value.replace(/\D/g, "").length < 10]];
    checks.forEach(function (c) {
      var fl = c[0].closest(".fl"); fl.classList.remove("err");
      if (c[1]) { void fl.offsetWidth; fl.classList.add("err"); if (ok) { c[0].focus(); ok = false; } }
    });
    if (!ok) return;
    var svcs = $$('input[name=svc]:checked', form).map(function (c) { return c.value; }).join(", ");
    var lines = ["Hi GrowVika, I want to start a new project.", "", "Name: " + name.value.trim(), "Phone: " + phone.value.trim()];
    if (svcs) lines.push("Need: " + svcs);
    if (form.biz.value.trim()) lines.push("Business: " + form.biz.value.trim());
    if (form.budget.value) lines.push("Timeline: " + form.budget.value);
    if (form.msg.value.trim()) lines.push("Details: " + form.msg.value.trim());
    window.open("https://wa.me/" + WHATSAPP + "?text=" + encodeURIComponent(lines.join("\n")), "_blank", "noopener");
    modal.classList.add("sent"); form.reset();
  });
  $$(".fl input", form).forEach(function (i) { i.addEventListener("input", function () { i.closest(".fl").classList.remove("err"); }); });
  var auto = +document.body.getAttribute("data-auto-popup") || 0, seen = false;
  try { seen = sessionStorage.getItem("gv_popup") === "1"; } catch (e) {}
  if (auto > 0 && !seen) setTimeout(function () { if (!modal.classList.contains("open") && !$(".mnav.open")) openModal(); }, auto * 1000);
})();
