(function () {
  const STORAGE_KEY = "virksomhed-lang";

  function currentLang() {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored === "en" || stored === "da") {
      return stored;
    }
    return "da";
  }

  function updateButtons(lang) {
    document.querySelectorAll("[data-set-lang]").forEach((btn) => {
      btn.setAttribute("aria-pressed", String(btn.dataset.setLang === lang));
    });
  }

  function setLanguage(lang) {
    if (lang !== "da" && lang !== "en") {
      return;
    }
    const doc = document.documentElement;
    const before = Math.max(doc.scrollHeight, 1);
    const y = window.scrollY;
    const ratio = y / before;
    doc.lang = lang;
    localStorage.setItem(STORAGE_KEY, lang);
    updateButtons(lang);
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        window.scrollTo(0, ratio * doc.scrollHeight);
      });
    });
  }

  document.addEventListener("click", (event) => {
    const btn = event.target.closest("[data-set-lang]");
    if (!btn) {
      return;
    }
    setLanguage(btn.dataset.setLang);
  });

  const lang = currentLang();
  document.documentElement.lang = lang;
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", () => {
      updateButtons(lang);
      const toc = document.querySelector(".toc");
      if (toc && window.matchMedia("(min-width: 960px)").matches) {
        toc.open = true;
      }
    });
  } else {
    updateButtons(lang);
    const toc = document.querySelector(".toc");
    if (toc && window.matchMedia("(min-width: 960px)").matches) {
      toc.open = true;
    }
  }
})();

(function () {
  let tooltip = null;
  let activeTerm = null;
  let hideTimer = null;
  let currentAudio = null;

  function ensureTooltip() {
    if (tooltip) {
      return tooltip;
    }
    tooltip = document.createElement("div");
    tooltip.className = "vocab-tooltip";
    tooltip.setAttribute("role", "tooltip");
    tooltip.hidden = true;
    tooltip.innerHTML = [
      '<span class="vocab-tooltip-label"></span>',
      '<strong class="vocab-tooltip-translation"></strong>',
      '<button class="vocab-tts" type="button" aria-label="Play Danish pronunciation"',
      ' title="Play Danish pronunciation">🔊</button>',
    ].join("");
    tooltip.addEventListener("pointerenter", cancelHide);
    tooltip.addEventListener("pointerleave", scheduleHide);
    tooltip.querySelector(".vocab-tts").addEventListener("click", playDanish);
    document.body.appendChild(tooltip);
    return tooltip;
  }

  function cancelHide() {
    if (hideTimer) {
      window.clearTimeout(hideTimer);
      hideTimer = null;
    }
  }

  function scheduleHide() {
    cancelHide();
    hideTimer = window.setTimeout(hideTooltip, 180);
  }

  function hideTooltip() {
    cancelHide();
    if (tooltip) {
      tooltip.hidden = true;
    }
    if (activeTerm) {
      activeTerm.setAttribute("aria-expanded", "false");
      activeTerm = null;
    }
  }

  function positionTooltip(term) {
    const tip = ensureTooltip();
    const rect = term.getBoundingClientRect();
    const gap = 8;
    const margin = 10;
    let left = rect.left + rect.width / 2 - tip.offsetWidth / 2;
    left = Math.max(margin, Math.min(left, window.innerWidth - tip.offsetWidth - margin));
    let top = rect.top - tip.offsetHeight - gap;
    if (top < margin) {
      top = rect.bottom + gap;
    }
    tip.style.left = `${left}px`;
    tip.style.top = `${top}px`;
  }

  function showTooltip(term) {
    cancelHide();
    const tip = ensureTooltip();
    if (activeTerm && activeTerm !== term) {
      activeTerm.setAttribute("aria-expanded", "false");
    }
    activeTerm = term;
    activeTerm.setAttribute("aria-expanded", "true");
    const langHost = term.closest("[lang]");
    const isDanish = !langHost || langHost.lang === "da";
    tip.querySelector(".vocab-tooltip-label").textContent = isDanish ? "English" : "Dansk";
    tip.querySelector(".vocab-tooltip-translation").textContent =
      isDanish ? term.dataset.en : term.dataset.da;
    tip.dataset.tts = term.dataset.tts;
    tip.hidden = false;
    positionTooltip(term);
  }

  function googleTtsUrl(text) {
    const params = new URLSearchParams({
      ie: "UTF-8",
      client: "tw-ob",
      tl: "da",
      q: text,
    });
    return `https://translate.google.com/translate_tts?${params.toString()}`;
  }

  function playDanish(event) {
    event.stopPropagation();
    const text = ensureTooltip().dataset.tts;
    if (!text) {
      return;
    }
    if (currentAudio) {
      currentAudio.pause();
      currentAudio.src = "";
    }
    const button = event.currentTarget;
    const audio = new Audio();
    currentAudio = audio;
    audio.preload = "auto";
    audio.referrerPolicy = "no-referrer";
    audio.src = googleTtsUrl(text);
    audio.onended = () => {
      currentAudio = null;
    };
    audio.onerror = () => {
      currentAudio = null;
      button.title = "Google Translate TTS was blocked. Try again.";
    };
    const playPromise = audio.play();
    if (playPromise) {
      playPromise.catch(() => {
        currentAudio = null;
        button.title = "Google Translate TTS playback was blocked. Try again.";
      });
    }
  }

  document.addEventListener("pointerover", (event) => {
    const term = event.target.closest(".vocab-term");
    if (term) {
      showTooltip(term);
    }
  });

  document.addEventListener("pointerout", (event) => {
    const term = event.target.closest(".vocab-term");
    if (term && !term.contains(event.relatedTarget)) {
      scheduleHide();
    }
  });

  document.addEventListener("focusin", (event) => {
    const term = event.target.closest(".vocab-term");
    if (term) {
      showTooltip(term);
    }
  });

  document.addEventListener("focusout", (event) => {
    const term = event.target.closest(".vocab-term");
    if (term) {
      scheduleHide();
    }
  });

  document.addEventListener("click", (event) => {
    const term = event.target.closest(".vocab-term");
    if (term) {
      showTooltip(term);
      return;
    }
    if (!event.target.closest(".vocab-tooltip")) {
      hideTooltip();
    }
  });

  document.addEventListener("keydown", (event) => {
    if ((event.key === "Enter" || event.key === " ") && event.target.matches(".vocab-term")) {
      event.preventDefault();
      showTooltip(event.target);
    } else if (event.key === "Escape") {
      hideTooltip();
    }
  });

  window.addEventListener("scroll", hideTooltip, { passive: true });
  window.addEventListener("resize", hideTooltip);
})();
