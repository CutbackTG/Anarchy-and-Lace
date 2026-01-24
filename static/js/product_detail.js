document.addEventListener("DOMContentLoaded", () => {
  document.addEventListener("click", (e) => {

    /* Handle thumbnail clicks */
    const thumb = e.target.closest(".pd-thumb");
    if (thumb) {
      const src = thumb.getAttribute("data-src");
      const mainImg = document.getElementById("pdMainImg");
      if (mainImg && src) {
        mainImg.src = src;
      }
      return;
    }

    /* Handle Fit / Fill / Zoom buttons */
    const btn = e.target.closest(".pd-viewerbtn");
    if (!btn) return;

    const mode = btn.getAttribute("data-mode");
    const viewer = document.querySelector(".pd-main");
    if (!viewer) return;

    // Remove existing modes
    viewer.classList.remove("is-fill", "is-zoom");

    // Apply selected mode
    if (mode === "fill") viewer.classList.add("is-fill");
    if (mode === "zoom") viewer.classList.add("is-zoom");

    // Update active button state
    document.querySelectorAll(".pd-viewerbtn").forEach(b => b.classList.remove("is-active"));
    btn.classList.add("is-active");

  });
});
