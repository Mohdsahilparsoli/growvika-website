/* =========================================================
   GrowVika — shared behaviour for every home page layout
   (no libraries; plain JavaScript)
   ========================================================= */
(function () {
  "use strict";

  // Where enquiries go. Forms open WhatsApp with the details filled in.
  var WHATSAPP = "919818186876";
  var EMAIL = "sahil@growvika.com";

  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var finePointer = window.matchMedia("(hover: hover) and (pointer: fine)").matches;

  /* ---------- Header: shadow after scrolling ---------- */
  var header = $(".header");
  var bar = $(".progress-bar");
  var toTop = $(".to-top");
  function onScroll() {
    var y = window.scrollY;
    if (header) header.classList.toggle("scrolled", y > 10);
    var max = document.documentElement.scrollHeight - window.innerHeight;
    var p = max > 0 ? y / max : 0;
    if (bar) bar.style.transform = "scaleX(" + p + ")";
    if (toTop) toTop.classList.toggle("show", y > 700);
    updateRingProgress(p);
  }

  /* ---------- Mega menu ---------- */
  var items = $$(".nav-item.has-mega");
  var isMobileNav = function () { return window.matchMedia("(max-width: 960px)").matches; };
  function closeAll(except) {
    items.forEach(function (it) {
      if (it !== except) {
        it.classList.remove("open");
        var b = $(".nav-link", it);
        if (b) b.setAttribute("aria-expanded", "false");
      }
    });
  }
  items.forEach(function (it) {
    var btn = $(".nav-link", it);
    var timer;
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      var open = !it.classList.contains("open");
      closeAll(it);
      it.classList.toggle("open", open);
      btn.setAttribute("aria-expanded", String(open));
    });
    it.addEventListener("mouseenter", function () {
      if (isMobileNav()) return;
      clearTimeout(timer);
      closeAll(it);
      it.classList.add("open");
      btn.setAttribute("aria-expanded", "true");
    });
    it.addEventListener("mouseleave", function () {
      if (isMobileNav()) return;
      timer = setTimeout(function () {
        it.classList.remove("open");
        btn.setAttribute("aria-expanded", "false");
      }, 160);
    });
  });
  document.addEventListener("click", function (e) {
    if (!e.target.closest(".nav-item.has-mega")) closeAll();
  });

  /* ---------- Mobile menu ---------- */
  var toggle = $(".menu-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = !document.body.classList.contains("nav-open");
      document.body.classList.toggle("nav-open", open);
      toggle.setAttribute("aria-expanded", String(open));
    });
  }
  $$(".nav-backdrop, .nav a[href^='#']").forEach(function (el) {
    el.addEventListener("click", function () {
      document.body.classList.remove("nav-open");
      if (toggle) toggle.setAttribute("aria-expanded", "false");
    });
  });

  /* ---------- Custom cursor ---------- */
  var dot = $(".cursor-dot");
  var ring = $(".cursor-ring");
  var ringProg = ring ? $(".prog", ring) : null;
  var ringLabel = ring ? $(".cursor-label", ring) : null;
  var CIRC = 2 * Math.PI * 20;
  if (ringProg) {
    ringProg.style.strokeDasharray = String(CIRC);
    ringProg.style.strokeDashoffset = String(CIRC);
  }
  function updateRingProgress(p) {
    if (ringProg) ringProg.style.strokeDashoffset = String(CIRC * (1 - p));
  }

  if (dot && ring && finePointer) {
    document.body.classList.add("has-cursor");
    var mx = window.innerWidth / 2, my = window.innerHeight / 2, rx = mx, ry = my;
    window.addEventListener("mousemove", function (e) {
      mx = e.clientX;
      my = e.clientY;
      dot.style.transform = "translate(" + mx + "px," + my + "px)";
      dot.classList.remove("hidden");
      ring.classList.remove("hidden");
    }, { passive: true });
    document.addEventListener("mouseleave", function () {
      dot.classList.add("hidden");
      ring.classList.add("hidden");
    });
    (function loop() {
      rx += (mx - rx) * (reduceMotion ? 1 : 0.16);
      ry += (my - ry) * (reduceMotion ? 1 : 0.16);
      ring.style.transform = "translate(" + rx + "px," + ry + "px)";
      requestAnimationFrame(loop);
    })();
    var hoverSel = "a, button, .chip-check span, [data-cursor]";
    document.addEventListener("mouseover", function (e) {
      var t = e.target.closest(hoverSel);
      if (!t) return;
      ring.classList.add("hover");
      if (ringLabel) ringLabel.textContent = t.getAttribute("data-cursor") || "";
    });
    document.addEventListener("mouseout", function (e) {
      var t = e.target.closest(hoverSel);
      if (t && !t.contains(e.relatedTarget)) {
        ring.classList.remove("hover");
        if (ringLabel) ringLabel.textContent = "";
      }
    });
  }

  /* ---------- Magnetic buttons (desktop) ---------- */
  if (finePointer && !reduceMotion) {
    $$("[data-magnetic]").forEach(function (el) {
      el.addEventListener("mousemove", function (e) {
        var r = el.getBoundingClientRect();
        var x = (e.clientX - r.left - r.width / 2) * 0.22;
        var y = (e.clientY - r.top - r.height / 2) * 0.3;
        el.style.transform = "translate(" + x + "px," + y + "px)";
      });
      el.addEventListener("mouseleave", function () { el.style.transform = ""; });
    });
  }

  /* ---------- Scroll reveal ---------- */
  $$("[data-stagger]").forEach(function (group) {
    var step = parseFloat(group.getAttribute("data-stagger")) || 0.08;
    $$(".reveal", group).forEach(function (el, i) { el.style.transitionDelay = (i * step) + "s"; });
  });
  if ("IntersectionObserver" in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          en.target.classList.add("in");
          io.unobserve(en.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
    $$(".reveal, .split-line, [data-split]").forEach(function (el) { io.observe(el); });
  } else {
    $$(".reveal, .split-line, [data-split]").forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- Counting numbers ---------- */
  function countUp(el) {
    var end = parseFloat(el.getAttribute("data-count"));
    var dec = (el.getAttribute("data-count").split(".")[1] || "").length;
    var dur = 1600, start = null;
    function tick(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var v = end * (1 - Math.pow(1 - p, 3));
      el.textContent = v.toLocaleString("en-IN", { minimumFractionDigits: dec, maximumFractionDigits: dec });
      if (p < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }
  var counters = $$("[data-count]");
  if ("IntersectionObserver" in window && !reduceMotion) {
    var co = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { countUp(en.target); co.unobserve(en.target); }
      });
    }, { threshold: 0.5 });
    counters.forEach(function (c) { co.observe(c); });
  } else {
    counters.forEach(function (c) { c.textContent = Number(c.getAttribute("data-count")).toLocaleString("en-IN"); });
  }

  /* ---------- Gentle parallax ---------- */
  var para = $$("[data-parallax]");
  if (para.length && !reduceMotion && window.innerWidth >= 960) { // desktop only: keeps phone layouts steady
    var ticking = false;
    window.addEventListener("scroll", function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        para.forEach(function (el) {
          var s = parseFloat(el.getAttribute("data-parallax")) || 0.1;
          var r = el.getBoundingClientRect();
          var off = (r.top + r.height / 2 - window.innerHeight / 2) * -s;
          el.style.transform = "translate3d(0," + off.toFixed(1) + "px,0)";
        });
        ticking = false;
      });
    }, { passive: true });
  }

  /* ---------- FAQ accordion ---------- */
  $$(".faq-item").forEach(function (item) {
    var q = $(".faq-q", item);
    q.addEventListener("click", function () {
      var open = !item.classList.contains("open");
      var group = item.closest(".faq");
      if (group) $$(".faq-item", group).forEach(function (o) {
        o.classList.remove("open");
        $(".faq-q", o).setAttribute("aria-expanded", "false");
      });
      item.classList.toggle("open", open);
      q.setAttribute("aria-expanded", String(open));
    });
  });

  /* ---------- Tabs (used by some layouts) ---------- */
  $$("[data-tabs]").forEach(function (wrap) {
    var tabs = $$("[role='tab']", wrap);
    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        tabs.forEach(function (t) {
          var on = t === tab;
          t.setAttribute("aria-selected", String(on));
          var panel = document.getElementById(t.getAttribute("aria-controls"));
          if (panel) {
            panel.hidden = !on;
            if (on) { panel.classList.remove("in"); void panel.offsetWidth; panel.classList.add("in"); }
          }
        });
      });
    });
  });

  /* ---------- Rotating words in a headline ---------- */
  $$("[data-rotate]").forEach(function (el) {
    var words = el.getAttribute("data-rotate").split("|");
    if (words.length < 2 || reduceMotion) return;
    var i = 0;
    setInterval(function () {
      el.classList.add("out");
      setTimeout(function () {
        i = (i + 1) % words.length;
        el.textContent = words[i];
        el.classList.remove("out");
      }, 380);
    }, 2600);
  });

  /* ---------- Simple slider (prev / next / dots, auto-plays) ---------- */
  $$("[data-slider]").forEach(function (slider) {
    var slides = $$("[data-slide]", slider);
    var dotsWrap = $("[data-dots]", slider);
    var cur = 0, timer;
    if (dotsWrap) slides.forEach(function (_, i) {
      var d = document.createElement("button");
      d.type = "button";
      d.setAttribute("aria-label", "Show slide " + (i + 1));
      d.addEventListener("click", function () { go(i); restart(); });
      dotsWrap.appendChild(d);
    });
    function go(n) {
      cur = (n + slides.length) % slides.length;
      slides.forEach(function (s, i) {
        s.classList.toggle("active", i === cur);
        s.setAttribute("aria-hidden", String(i !== cur));
      });
      if (dotsWrap) $$("button", dotsWrap).forEach(function (d, i) { d.classList.toggle("on", i === cur); });
    }
    function restart() {
      clearInterval(timer);
      if (!reduceMotion) timer = setInterval(function () { go(cur + 1); }, 6000);
    }
    var prev = $("[data-prev]", slider), next = $("[data-next]", slider);
    if (prev) prev.addEventListener("click", function () { go(cur - 1); restart(); });
    if (next) next.addEventListener("click", function () { go(cur + 1); restart(); });
    go(0);
    restart();
  });

  /* ---------- Sideways scroller buttons ---------- */
  $$("[data-hscroll]").forEach(function (wrap) {
    var track = $("[data-track]", wrap);
    $$("[data-scroll-by]", wrap).forEach(function (b) {
      b.addEventListener("click", function () {
        var dir = parseFloat(b.getAttribute("data-scroll-by"));
        track.scrollBy({ left: dir * track.clientWidth * 0.8, behavior: reduceMotion ? "auto" : "smooth" });
      });
    });
  });

  /* ---------- Portfolio filter ---------- */
  $$(".pf-filters").forEach(function (bar) {
    var section = bar.closest("section");
    var itemsP = $$(".pf-item", section);
    $$(".pf-btn", bar).forEach(function (btn) {
      btn.addEventListener("click", function () {
        var f = btn.getAttribute("data-filter");
        var grid = $(".pf-grid", section);
        if (grid) grid.classList.toggle("filtered", f !== "all");
        $$(".pf-btn", bar).forEach(function (b) {
          var on = b === btn;
          b.classList.toggle("on", on);
          b.setAttribute("aria-pressed", String(on));
        });
        itemsP.forEach(function (it) {
          var show = f === "all" || it.getAttribute("data-cat") === f;
          it.classList.toggle("hide", !show);
          it.classList.remove("show");
          if (show) { void it.offsetWidth; it.classList.add("show", "in"); }
        });
      });
    });
  });

  /* ---------- Popup: Start a new project ---------- */
  var modal = $("#project-modal");
  var lastFocus = null;
  function openModal() {
    if (!modal) return;
    lastFocus = document.activeElement;
    modal.classList.add("open");
    modal.setAttribute("aria-hidden", "false");
    document.body.classList.add("modal-open");
    document.body.classList.remove("nav-open");
    setTimeout(function () {
      var f = $("input, select, textarea, button", $(".modal-form", modal));
      if (f) f.focus({ preventScroll: true });
    }, 350);
    try { sessionStorage.setItem("gv_popup_seen", "1"); } catch (e) {}
  }
  function closeModal() {
    if (!modal) return;
    modal.classList.remove("open");
    modal.setAttribute("aria-hidden", "true");
    document.body.classList.remove("modal-open");
    if (lastFocus && lastFocus.focus) lastFocus.focus({ preventScroll: true });
  }
  $$("[data-open-project]").forEach(function (b) {
    b.addEventListener("click", function (e) { e.preventDefault(); openModal(); });
  });
  if (modal) {
    $$("[data-close-modal]", modal).forEach(function (b) { b.addEventListener("click", closeModal); });
    document.addEventListener("keydown", function (e) {
      if (!modal.classList.contains("open")) return;
      if (e.key === "Escape") closeModal();
      if (e.key === "Tab") { // keep keyboard focus inside the popup
        var f = $$("a[href], button:not([disabled]), input, select, textarea", modal).filter(function (x) { return x.offsetParent !== null; });
        if (!f.length) return;
        if (e.shiftKey && document.activeElement === f[0]) { e.preventDefault(); f[f.length - 1].focus(); }
        else if (!e.shiftKey && document.activeElement === f[f.length - 1]) { e.preventDefault(); f[0].focus(); }
      }
    });
    // Opens by itself once per visit, after the visitor has looked around
    var auto = parseInt(document.body.getAttribute("data-auto-popup") || "0", 10);
    var seen = false;
    try { seen = sessionStorage.getItem("gv_popup_seen") === "1"; } catch (e) {}
    if (auto > 0 && !seen) setTimeout(function () { if (!document.body.classList.contains("modal-open")) openModal(); }, auto * 1000);
  }

  /* ---------- Forms → WhatsApp enquiry ---------- */
  function collect(form) {
    var lines = [];
    var title = form.getAttribute("data-title") || "New enquiry";
    lines.push("*" + title + "* (from growvika.com)");
    var seen = {};
    $$("input, select, textarea", form).forEach(function (el) {
      if (!el.name || el.type === "submit") return;
      var label = el.getAttribute("data-label") || el.name;
      if (el.type === "checkbox" || el.type === "radio") {
        if (!el.checked) return;
        seen[label] = (seen[label] ? seen[label] + ", " : "") + el.value;
        return;
      }
      if (el.value.trim()) seen[label] = el.value.trim();
    });
    Object.keys(seen).forEach(function (k) { lines.push(k + ": " + seen[k]); });
    return lines.join("\n");
  }
  $$("form[data-enquiry]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var text = collect(form);
      window.open("https://wa.me/" + WHATSAPP + "?text=" + encodeURIComponent(text), "_blank", "noopener");
      form.classList.add("sent");
      var box = form.closest(".modal-form, .contact-form");
      if (box) box.classList.add("sent");
      form.reset();
    });
  });
  $$("[data-reset-form]").forEach(function (b) {
    b.addEventListener("click", function () {
      var box = b.closest(".sent");
      if (box) box.classList.remove("sent");
      $$(".sent", box || document).forEach(function (x) { x.classList.remove("sent"); });
    });
  });
  $$("form[data-newsletter]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var input = $("input", form);
      if (!input.value || !input.checkValidity()) { form.reportValidity(); return; }
      window.location.href = "mailto:" + EMAIL + "?subject=" + encodeURIComponent("Subscribe me to GrowVika updates") + "&body=" + encodeURIComponent("Please add " + input.value + " to your updates list.");
      input.value = "";
      input.placeholder = "Thanks! We'll be in touch.";
    });
  });

  /* ---------- Photo fallback: hide a photo that fails to load (the brand-coloured box shows instead) ---------- */
  document.addEventListener("error", function (e) {
    var t = e.target;
    if (t && t.tagName === "IMG") t.classList.add("img-fail");
  }, true);

  /* ---------- Misc ---------- */
  if (toTop) toTop.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" }); });
  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll);
  onScroll();
})();
