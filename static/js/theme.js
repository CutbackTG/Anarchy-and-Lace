// static/js/theme.js

(function () {
  const root = document.documentElement;
  const btn = document.getElementById("themeToggle");
  const icon = btn ? btn.querySelector(".theme-toggle__icon") : null;

  function applyIcon(theme) {
    if (!icon) return;
    icon.textContent = theme === "dark" ? "☀" : "☾";
  }

  function getSystemTheme() {
    return window.matchMedia &&
      window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  }

  function setTheme(theme) {
    root.setAttribute("data-theme", theme);
    localStorage.setItem("theme", theme);
    applyIcon(theme);
  }

  function init() {
    const saved = localStorage.getItem("theme");
    const theme = saved || getSystemTheme();
    root.setAttribute("data-theme", theme);
    applyIcon(theme);

    if (!btn) return;
    btn.addEventListener("click", function () {
      const current = root.getAttribute("data-theme") || getSystemTheme();
      setTheme(current === "dark" ? "light" : "dark");
    });
  }

  document.addEventListener("DOMContentLoaded", init);
})();
