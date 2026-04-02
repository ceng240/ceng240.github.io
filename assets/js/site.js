document.addEventListener("DOMContentLoaded", () => {
  const nav = document.querySelector("[data-nav-track]");
  if (!nav) return;

  const links = Array.from(nav.querySelectorAll(".page-link[href^='#']"));
  const indicator = nav.querySelector(".site-nav-indicator");
  const sectionEntries = links
    .map((link) => {
      const section = document.querySelector(link.getAttribute("href"));
      return section ? { link, section } : null;
    })
    .filter(Boolean);

  if (!links.length || !indicator || !sectionEntries.length) return;

  let activeLink = links[0];
  let ticking = false;

  const getHeaderOffset = () => {
    const header = document.querySelector(".site-header");
    return (header ? header.getBoundingClientRect().height : 0) + 20;
  };

  const moveIndicator = (link) => {
    const navRect = nav.getBoundingClientRect();
    const linkRect = link.getBoundingClientRect();
    indicator.style.setProperty("--indicator-width", `${linkRect.width}px`);
    indicator.style.setProperty("--indicator-left", `${linkRect.left - navRect.left}px`);
  };

  const revealActiveLink = (link) => {
    const trigger = nav;
    const linkLeft = link.offsetLeft;
    const linkCenter = linkLeft + link.offsetWidth / 2;
    const targetLeft = Math.max(0, linkCenter - trigger.clientWidth / 2);
    trigger.scrollTo({ left: targetLeft, behavior: "smooth" });
  };

  const activate = (link, force = false) => {
    if (!link) return;

    if (link !== activeLink || force) {
      links.forEach((item) => item.classList.toggle("is-active", item === link));
      activeLink = link;
    }

    moveIndicator(link);
    revealActiveLink(link);
  };

  const syncActiveLink = () => {
    const scrollPosition = window.scrollY;
    const probeLine = scrollPosition + window.innerHeight * 0.32;
    let currentLink = sectionEntries[0].link;
    let bestEntry = null;

    sectionEntries.forEach((entry) => {
      const rect = entry.section.getBoundingClientRect();
      const sectionTop = rect.top + window.scrollY;
      const sectionBottom = sectionTop + entry.section.offsetHeight;

      if (probeLine >= sectionTop && probeLine < sectionBottom) {
        bestEntry = entry;
      }
    });

    if (bestEntry) {
      currentLink = bestEntry.link;
    } else {
      let bestTop = Number.NEGATIVE_INFINITY;

      sectionEntries.forEach(({ link, section }) => {
        const sectionTop = section.getBoundingClientRect().top + window.scrollY;
        if (probeLine >= sectionTop && sectionTop > bestTop) {
          currentLink = link;
          bestTop = sectionTop;
        }
      });
    }

    activate(currentLink);
    ticking = false;
  };

  const requestSync = () => {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(syncActiveLink);
  };

  links.forEach((link, index) => {
    link.classList.toggle("is-active", index === 0);
    link.addEventListener("click", () => {
      activate(link);
      window.setTimeout(requestSync, 0);
    });
  });

  const hashLink = links.find((link) => link.getAttribute("href") === window.location.hash);
  activate(hashLink || activeLink, true);

  requestSync();

  window.addEventListener("scroll", requestSync, { passive: true });
  window.addEventListener("resize", () => {
    activate(activeLink, true);
    requestSync();
  });
  nav.addEventListener("scroll", () => {
    moveIndicator(activeLink);
  }, { passive: true });
  window.addEventListener("hashchange", requestSync);
  window.addEventListener("load", requestSync);
});
