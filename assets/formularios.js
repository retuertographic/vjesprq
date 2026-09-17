/* Formularios de "Hablamos": pestañas, validación y envío.
   El envío usa EmailJS (igual que El Capricho). Mientras no haya claves configuradas,
   se abre el correo del usuario con la consulta ya redactada para gestion@viajesparque.com. */
const EMAILJS_PUBLIC_KEY = '';
const EMAILJS_SERVICE_ID = '';
const EMAILJS_TEMPLATE_ID = '';
const DESTINO_CORREO = 'gestion@viajesparque.com';

(function () {
  const emailjsReady = window.emailjs && EMAILJS_PUBLIC_KEY && EMAILJS_SERVICE_ID && EMAILJS_TEMPLATE_ID;
  if (emailjsReady) emailjs.init({ publicKey: EMAILJS_PUBLIC_KEY });

  /* ---- Pestañas ---- */
  const tabs = [...document.querySelectorAll('[role="tab"]')];
  function selectTab(tab, focus) {
    tabs.forEach(t => {
      const on = t === tab;
      t.setAttribute('aria-selected', on);
      t.tabIndex = on ? 0 : -1;
      document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
    });
    if (focus) tab.focus();
  }
  tabs.forEach((t, i) => {
    t.addEventListener('click', () => selectTab(t));
    t.addEventListener('keydown', e => {
      if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
      const next = tabs[(i + (e.key === 'ArrowRight' ? 1 : tabs.length - 1)) % tabs.length];
      selectTab(next, true);
    });
  });

  /* ---- Parámetros de la URL: ?tipo=empresa|institucion, ?destino=, ?interes= ---- */
  const params = new URLSearchParams(location.search);
  const tipo = params.get('tipo');
  if (tipo === 'empresa' || tipo === 'institucion') {
    selectTab(document.getElementById('tab-empresa'));
    if (tipo === 'institucion') document.getElementById('e_tipo').value = 'Club o equipo deportivo';
  }
  const INTERESES = {
    'a-tu-manera': 'un viaje a medida', 'vuelos-y-hoteles': 'vuelos y hotel', 'tours-guiados': 'un circuito o tour guiado',
    'asesoria-de-viaje': 'asesoramiento para un viaje', 'luna-de-miel': 'nuestra luna de miel', 'cruceros': 'un crucero',
  };
  const destino = (params.get('destino') || '').slice(0, 60).replace(/[<>]/g, '');
  const interes = INTERESES[params.get('interes')];
  const viaje = document.getElementById('p_viaje');
  if (destino) viaje.value = `Me interesa un viaje a ${destino}. `;
  else if (interes) viaje.value = `Me interesa ${interes}. `;

  /* ---- Validación ---- */
  const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const PHONE_RE = /^\+?[0-9\s]{9,16}$/;
  function setError(input, msg) {
    const err = document.getElementById(input.id + '_err');
    input.classList.toggle('invalid', !!msg);
    input.setAttribute('aria-invalid', msg ? 'true' : 'false');
    if (err) { err.textContent = msg; err.classList.toggle('show', !!msg); input.setAttribute('aria-describedby', err.id); }
  }
  function validate(form) {
    let first = null;
    form.querySelectorAll('input:not([type=hidden]):not(.hp), textarea').forEach(el => {
      let msg = '';
      const v = el.type === 'checkbox' ? el.checked : el.value.trim();
      if (el.required && !v) msg = el.type === 'checkbox' ? 'Necesitamos tu conformidad para poder responderte.' : 'Este campo es obligatorio.';
      else if (el.type === 'email' && v && !EMAIL_RE.test(v)) msg = 'Revisa el correo: parece que falta algo.';
      else if (el.type === 'tel' && v && !PHONE_RE.test(v)) msg = 'Escribe un teléfono válido (9 cifras como mínimo).';
      setError(el, msg);
      if (msg && !first) first = el;
    });
    if (first) first.focus();
    return !first;
  }

  function status(form, kind, html) {
    const el = form.querySelector('.form-status');
    el.className = 'form-status show ' + kind;
    el.innerHTML = html;
  }

  function summary(data) {
    const labels = {
      tipo_consulta: 'Tipo de consulta', entidad: 'Empresa o entidad', tipo_entidad: 'Tipo de entidad', nombre: 'Nombre',
      email: 'Correo', telefono: 'Teléfono', oficina: 'Oficina preferida', personas: 'Personas que viajan',
      frecuencia: 'Frecuencia', mensaje: 'Mensaje',
    };
    return Object.entries(labels).filter(([k]) => data[k]).map(([k, l]) => `${l}: ${data[k]}`).join('\n');
  }

  const startedAt = Date.now();
  document.querySelectorAll('#formParticular, #formEmpresa').forEach(form => {
    form.addEventListener('submit', async e => {
      e.preventDefault();
      if (form.querySelector('.hp').value || Date.now() - startedAt < 2500) return; // bots
      if (!validate(form)) return;
      const data = Object.fromEntries(new FormData(form).entries());
      delete data.web;
      delete data.privacidad;
      const asunto = data.tipo_consulta === 'Particular'
        ? `Consulta de viaje · ${data.nombre}`
        : `Viajes de empresa · ${data.entidad}`;
      const btn = form.querySelector('button[type=submit]');

      if (!emailjsReady) {
        const href = `mailto:${DESTINO_CORREO}?subject=${encodeURIComponent(asunto)}&body=${encodeURIComponent(summary(data))}`;
        status(form, 'ok', `Vamos a abrir tu programa de correo con la consulta ya escrita: solo tienes que darle a enviar. Si no se abre, escríbenos a <a href="mailto:${DESTINO_CORREO}">${DESTINO_CORREO}</a> o llámanos al <a href="tel:+34922215012">922 215 012</a>.`);
        location.href = href;
        return;
      }

      btn.disabled = true;
      btn.textContent = 'Enviando…';
      try {
        await emailjs.send(EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, {
          asunto, resumen: summary(data), reply_to: data.email, nombre: data.nombre, ...data,
        });
        form.reset();
        status(form, 'ok', '¡Recibido! Te respondemos lo antes posible, normalmente en el mismo día laborable.');
      } catch (err) {
        status(form, 'error', `No hemos podido enviar el formulario. Puedes llamarnos al <a href="tel:+34922215012">922 215 012</a> (Santa Cruz) o al <a href="tel:+34922546111">922 546 111</a> (Tegueste), o escribirnos a <a href="mailto:${DESTINO_CORREO}">${DESTINO_CORREO}</a>.`);
      } finally {
        btn.disabled = false;
        btn.textContent = 'Enviar consulta';
      }
    });
  });
})();
