/* Diario de viaje: listado de artículos desde /diario-de-viaje/articulos.json */
window.VPDiario = (function () {
  let cache = null;
  async function load() {
    if (!cache) {
      const res = await fetch('/diario-de-viaje/articulos.json', { cache: 'no-cache' });
      cache = await res.json();
      cache.articulos.sort((a, b) => new Date(b.fecha) - new Date(a.fecha) || (b.orden || 0) - (a.orden || 0));
    }
    return cache;
  }
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  function card(a, cats) {
    const url = `/diario-de-viaje/${a.slug}/`;
    return `<article class="post-card reveal" data-href="${url}">
      <div class="thumb"><img src="${a.imagen}" alt="" loading="lazy"></div>
      <div class="body">
        <span class="cat">${esc(cats[a.categoria] ? cats[a.categoria].nombre : '')}</span>
        <h3><a href="${url}">${esc(a.titulo)}</a></h3>
        <p>${esc(a.resumen)}</p>
        <span class="meta">${a.minutos} min de lectura</span>
      </div>
    </article>`;
  }
  async function render(containerId, { limit, categoria, exclude } = {}) {
    const el = document.getElementById(containerId);
    if (!el) return;
    try {
      const data = await load();
      let list = data.articulos;
      if (categoria) list = list.filter(a => a.categoria === categoria);
      if (exclude) list = list.filter(a => a.slug !== exclude);
      if (limit) list = list.slice(0, limit);
      el.innerHTML = list.length
        ? list.map(a => card(a, data.categorias)).join('')
        : `<div class="empty">Todavía no hay artículos en esta categoría. Estamos en ello: vuelve pronto.</div>`;
      if (window.VPReveal) window.VPReveal(el); else el.querySelectorAll('.reveal').forEach(n => n.classList.add('in'));
    } catch (err) {
      el.innerHTML = `<div class="empty">No hemos podido cargar los artículos. Prueba a recargar la página.</div>`;
    }
  }
  return {
    load,
    render,
    renderLatest: (id, n) => render(id, { limit: n }),
  };
})();
