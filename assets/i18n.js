(function () {
  const STORAGE_KEY = "afs-lang";

  function currentLang() {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored === "en" || stored === "da") return stored;
    return "da";
  }

  function updateButtons(lang) {
    document.querySelectorAll("[data-set-lang]").forEach((btn) => {
      btn.setAttribute("aria-pressed", String(btn.dataset.setLang === lang));
    });
  }

  function setLanguage(lang) {
    if (lang !== "da" && lang !== "en") return;
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
    if (!btn) return;
    setLanguage(btn.dataset.setLang);
  });

  const lang = currentLang();
  document.documentElement.lang = lang;
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", () => {
      updateButtons(lang);
      const toc = document.querySelector(".toc");
      if (toc && window.matchMedia("(min-width: 960px)").matches) toc.open = true;
    });
  } else {
    updateButtons(lang);
    const toc = document.querySelector(".toc");
    if (toc && window.matchMedia("(min-width: 960px)").matches) toc.open = true;
  }
})();
