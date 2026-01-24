document.addEventListener("DOMContentLoaded", () => {
  document.addEventListener("click", (e) => {
    const btn = e.target.closest(".pd-thumb");
    if (!btn) return;

    const src = btn.getAttribute("data-src");
    const main = document.getElementById("pdMainImg");
    if (main && src) {
      main.src = src;
    }
  });
});
