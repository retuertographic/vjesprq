/* Comportamiento compartido: carga header/footer, menú móvil, scroll, animaciones y compartir. */

/* Banner de cookies (Biscotti CMP). Rellenar el ID cuando se dé de alta el sitio en Biscotti.
   Mientras la web no use cookies de analítica ni publicidad, puede quedarse vacío. */
const BISCOTTI_WEBSITE_ID = '';

(async function () {
  if (BISCOTTI_WEBSITE_ID) {
    window.BiscottiConfig = { websiteId: BISCOTTI_WEBSITE_ID, apiUrl: 'https://api.biscotti-cmp.com/api/v1' };
    ['biscotti-boot.js', 'biscotti.min.js'].forEach(f => {
      const s = document.createElement('script');
      s.src = 'https://api.biscotti-cmp.com/scripts/' + f;
      s.async = false;
      document.head.appendChild(s);
    });
  }

  async function injectPartial(slotId, file) {
    const slot = document.getElementById(slotId);
    if (!slot) return;
    try {
      const res = await fetch(file, { cache: 'no-cache' });
      slot.outerHTML = await res.text();
    } catch (err) {
      console.error('No se pudo cargar ' + file, err);
    }
  }

  await Promise.all([
    injectPartial('site-header-slot', '/partials/header.html'),
    injectPartial('site-footer-slot', '/partials/footer.html'),
  ]);

  const year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  /* Marca la sección activa en el menú */
  const path = location.pathname.replace(/index\.html$/, '');
  document.querySelectorAll('#navLinks a').forEach(a => {
    const href = a.getAttribute('href');
    if (href === '/' ? path === '/' : path.startsWith(href)) a.setAttribute('aria-current', 'page');
  });

  const header = document.getElementById('site-header');
  const toTop = document.getElementById('toTop');
  if (header && toTop) {
    const onScroll = () => {
      header.classList.toggle('scrolled', window.scrollY > 20);
      toTop.classList.toggle('show', window.scrollY > 600);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
    toTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  }

  const burger = document.getElementById('burgerBtn');
  const navLinks = document.getElementById('navLinks');
  if (burger && navLinks) {
    burger.addEventListener('click', () => {
      const open = navLinks.classList.toggle('open');
      burger.setAttribute('aria-expanded', open);
    });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape' && navLinks.classList.contains('open')) {
        navLinks.classList.remove('open');
        burger.setAttribute('aria-expanded', 'false');
        burger.focus();
      }
    });
  }

  /* Aparición suave al hacer scroll */
  const io = 'IntersectionObserver' in window ? new IntersectionObserver(entries => {
    entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
  }, { rootMargin: '0px 0px -8% 0px' }) : null;
  window.VPReveal = root => (root || document).querySelectorAll('.reveal:not(.in)').forEach(el => io ? io.observe(el) : el.classList.add('in'));
  window.VPReveal();

  /* Tarjetas enteras clicables sin anidar enlaces */
  document.addEventListener('click', e => {
    const card = e.target.closest('[data-href]');
    if (card && !e.target.closest('a,button')) location.href = card.dataset.href;
  });
})();

/* Botones para compartir artículos */
window.VPShare = {
  render(containerId, url, title) {
    const el = document.getElementById(containerId);
    if (!el) return;
    const u = encodeURIComponent(url);
    const t = encodeURIComponent(title);
    const icons = {
      whatsapp: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.5 2 2 6.5 2 12c0 1.8.5 3.5 1.4 5L2 22l5.2-1.4c1.4.8 3.1 1.2 4.8 1.2 5.5 0 10-4.5 10-10S17.5 2 12 2zm0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3.1.8.8-3-.2-.3C4 14 3.5 13 3.5 12c0-4.7 3.8-8.5 8.5-8.5s8.5 3.8 8.5 8.5-3.8 8.5-8.5 8.5z"/><path d="M17.1 14.4c-.3-.1-1.6-.8-1.9-.9-.2-.1-.4-.1-.6.1-.2.3-.7.9-.9 1.1-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.6-2.1-.2-.3 0-.5.1-.6.1-.1.3-.4.4-.5.1-.2.2-.3.2-.5.1-.2 0-.4 0-.5-.1-.1-.6-1.5-.9-2.1-.2-.5-.5-.5-.6-.5h-.6c-.2 0-.5.1-.7.4-.3.3-1 1-1 2.4s1 2.8 1.2 3c.1.2 2.1 3.3 5.2 4.6.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.6-.7 1.9-1.3.2-.6.2-1.2.2-1.3-.1-.1-.3-.2-.6-.4z"/></svg>',
      facebook: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12c0-5.5-4.5-10-10-10S2 6.5 2 12c0 5 3.7 9.1 8.4 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.4v7C18.3 21.1 22 17 22 12z"/></svg>',
      linkedin: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3zM9 9h3.8v1.7h.1c.5-1 1.8-2 3.8-2 4 0 4.8 2.6 4.8 6V21h-4v-5.6c0-1.3 0-3-1.9-3s-2.1 1.5-2.1 2.9V21H9z"/></svg>',
      link: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.5.5l2-2a5 5 0 0 0-7-7l-1.5 1.5"/><path d="M14 11a5 5 0 0 0-7.5-.5l-2 2a5 5 0 0 0 7 7l1.5-1.5"/></svg>',
    };
    const links = [
      { href: `https://wa.me/?text=${t}%20${u}`, label: 'Compartir por WhatsApp', icon: icons.whatsapp },
      { href: `https://www.facebook.com/sharer/sharer.php?u=${u}`, label: 'Compartir en Facebook', icon: icons.facebook },
      { href: `https://www.linkedin.com/sharing/share-offsite/?url=${u}`, label: 'Compartir en LinkedIn', icon: icons.linkedin },
    ];
    el.innerHTML = links.map(l =>
      `<a href="${l.href}" target="_blank" rel="noopener noreferrer" aria-label="${l.label}">${l.icon}</a>`
    ).join('') + `<button type="button" class="share-copy" aria-label="Copiar enlace">${icons.link}</button>`;
    const copyBtn = el.querySelector('.share-copy');
    copyBtn.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(url);
        copyBtn.classList.add('copied');
        setTimeout(() => copyBtn.classList.remove('copied'), 1800);
      } catch (e) { /* sin portapapeles: no pasa nada */ }
    });
  }
};
