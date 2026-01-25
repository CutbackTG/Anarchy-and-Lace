document.addEventListener("DOMContentLoaded", () => {
  document.addEventListener("click", (e) => {

    /* Thumbnail switching */
    const thumb = e.target.closest(".pd-thumb");
    if (thumb) {
      const src = thumb.getAttribute("data-src");
      const mainImg = document.getElementById("pdMainImg");
      if (mainImg && src) {
        mainImg.src = src;
      }
      return;
    }

    /* Fit / Fill buttons */
    const btn = e.target.closest(".pd-viewerbtn");
    if (!btn) return;

    const mode = btn.getAttribute("data-mode");
    const viewer = document.querySelector(".pd-main");
    if (!viewer) return;

    // Reset state
    viewer.classList.remove("is-fill");

    // Apply mode
    if (mode === "fill") viewer.classList.add("is-fill");

    // Active button styling
    document.querySelectorAll(".pd-viewerbtn").forEach(b =>
      b.classList.remove("is-active")
    );
    btn.classList.add("is-active");

  });
});
