from gen_common import *

# ---------------- Destinos ----------------
DEST = [
 ('europa', 'Europa', 'santorini', 'Santorini', 'Grecia', 'Tres cúpulas azules de Oia sobre la caldera de Santorini',
  'Pueblos blancos colgados sobre la caldera, puestas de sol famosas y un mar que invita a combinar la isla con Atenas o con otras Cícladas.'),
 ('europa', 'Europa', 'lisboa', 'Lisboa', 'Portugal', 'Arco de la Rua Augusta en la Plaza del Comercio de Lisboa',
  'Tranvías, miradores y buena mesa a poco más de dos horas de vuelo. Perfecta para una escapada larga o para empezar una ruta por Portugal.'),
 ('europa', 'Europa', 'kirkjufell', 'Islandia', 'Europa del Norte', 'Montaña Kirkjufell y cascada en Islandia',
  'Cascadas, glaciares, playas negras y, con suerte, auroras boreales. Un viaje de naturaleza que conviene planificar bien por clima y distancias.'),
 ('asia', 'Asia', 'kyoto', 'Kioto', 'Japón', 'Calle Yasaka-dori con la pagoda Yasaka al fondo, en Kioto',
  'Templos, jardines y barrios tradicionales. Combina de maravilla con Tokio y Osaka en un primer viaje a Japón.'),
 ('asia', 'Asia', 'bangkok', 'Bangkok', 'Tailandia', 'Templo del Buda Esmeralda reflejado en el agua, Bangkok',
  'La puerta de entrada a Tailandia: templos dorados, mercados y comida callejera antes de seguir hacia el norte o las islas del sur.'),
 ('asia', 'Asia', 'bali', 'Bali', 'Indonesia', 'Arrozales en terrazas en Bali',
  'Arrozales, templos y playas en una misma isla. Muy elegida para lunas de miel y para viajes con calma.'),
 ('asia', 'Asia', 'maldivas', 'Maldivas', 'Océano Índico', 'Villas sobre el agua en una isla de Maldivas',
  'Villas sobre el agua, arrecifes y aguas turquesa. El destino de playa por excelencia para una ocasión especial.'),
 ('america', 'América', 'machu-picchu', 'Machu Picchu', 'Perú', 'Terrazas y ruinas de Machu Picchu con el Huayna Picchu al fondo',
  'La ciudadela inca entre montañas, dentro de una ruta por Cuzco y el Valle Sagrado. Las entradas son limitadas: mejor reservar con tiempo.'),
 ('america', 'América', 'nueva-york', 'Nueva York', 'Estados Unidos', 'Vista de Manhattan y el Empire State Building al atardecer',
  'Rascacielos, museos, musicales y barrios con personalidad propia. Recuerda tramitar la autorización de viaje antes de salir.'),
 ('america', 'América', 'la-habana', 'La Habana', 'Cuba', 'Coche clásico circulando por el Malecón de La Habana',
  'El Malecón, la Habana Vieja y los coches clásicos, con la opción de terminar en las playas de Varadero o de los cayos.'),
 ('africa', 'África', 'serengeti', 'Serengeti', 'Tanzania', 'Amanecer sobre la sabana del Serengeti',
  'Safaris en una de las sabanas más famosas del mundo, fácil de combinar con unos días de playa en Zanzíbar.'),
 ('africa', 'África', 'marrakech', 'Marrakech', 'Marruecos', 'Lámparas colgantes en un zoco de Marrakech',
  'Zocos, riads y el desierto a unas horas. Muy cerca de Canarias y con un contraste que no deja indiferente.'),
]
dest_cards = ''
for key, cont, img, name, where, alt, desc in DEST:
    dest_cards += f'''
      <article class="dest reveal" data-continente="{key}">
        <div class="ph"><img src="/img/destinos/{img}.webp" alt="{alt}" loading="lazy" width="1400" height="1050"><span class="cont">{cont}</span></div>
        <div class="body">
          <h3>{name}</h3>
          <div class="where">{where}</div>
          <p>{desc}</p>
          <a class="more" href="/hablamos/?destino={name.replace(' ', '%20')}">Quiero una propuesta para {name}</a>
        </div>
      </article>'''

page('destinos/',
 'Destinos desde Tenerife por continente | Viajes Parque',
 'Ideas de viaje desde Tenerife por continente: Santorini, Japón, Bali, Maldivas, Perú, Nueva York, Tanzania y más, con propuesta a tu medida.',
 hero('Destinos', 'El mundo, ordenado por continentes',
      'Una selección de destinos que nos piden a menudo. No es un catálogo cerrado: si tienes otro lugar en mente, también te lo organizamos.',
      None, '', [('Inicio', '/'), ('Destinos', '/destinos/')]) + f'''
<section class="section">
  <div class="wrap">
    <div class="filters" id="contFilters" role="group" aria-label="Filtrar destinos por continente">
      <button type="button" data-cont="" aria-pressed="true">Todos</button>
      <button type="button" data-cont="europa" aria-pressed="false">Europa</button>
      <button type="button" data-cont="asia" aria-pressed="false">Asia</button>
      <button type="button" data-cont="america" aria-pressed="false">América</button>
      <button type="button" data-cont="africa" aria-pressed="false">África</button>
    </div>
    <p class="sr-only" id="destCount" aria-live="polite"></p>
    <div class="dest-grid" id="destGrid">{dest_cards}
    </div>
  </div>
</section>

<section class="section white">
  <div class="wrap split">
    <div class="split-media reveal"><img src="/img/destinos/anaga.webp" alt="Acantilados de Anaga, Tenerife" loading="lazy"></div>
    <div class="reveal">
      <span class="eyebrow">Desde Tenerife</span>
      <h2>Salir de la isla tiene su ciencia</h2>
      <p>Viajar desde Canarias implica pensar bien las conexiones: por dónde enlazar, cuánto margen dejar entre vuelos y qué días salen las mejores combinaciones. Lo miramos por ti para que el viaje empiece bien desde el aeropuerto.</p>
      <ul class="checks">
        <li>Conexiones desde Tenerife Norte y Tenerife Sur.</li>
        <li>Márgenes de enlace pensados, no al límite.</li>
        <li>Documentación y requisitos de entrada revisados.</li>
      </ul>
      <a href="/diario-de-viaje/?categoria=antes-de-ir" class="btn ghost">Consejos antes de viajar</a>
    </div>
  </div>
</section>
''' + cta('¿No ves tu destino?', 'Esta es solo una muestra. Cuéntanos a dónde quieres ir y lo preparamos.'),
 og_image='/img/destinos/santorini.webp',
 jsonld=[breadcrumb([('Inicio', '/'), ('Destinos', '/destinos/')]),
         {"@context": "https://schema.org", "@type": "ItemList", "name": "Destinos destacados",
          "itemListElement": [{"@type": "ListItem", "position": i + 1,
             "item": {"@type": "TouristDestination", "name": f"{d[3]}, {d[4]}", "description": d[6],
                      "image": f"{SITE}/img/destinos/{d[2]}.webp"}} for i, d in enumerate(DEST)]}],
 scripts='''<script>
(function () {
  const bar = document.getElementById('contFilters');
  const cards = document.querySelectorAll('#destGrid .dest');
  const count = document.getElementById('destCount');
  const valid = ['europa', 'asia', 'america', 'africa'];
  function select(cont) {
    bar.querySelectorAll('button').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.cont === cont)));
    let n = 0;
    cards.forEach(c => { const show = !cont || c.dataset.continente === cont; c.hidden = !show; if (show) { n++; c.classList.add('in'); } });
    count.textContent = n + ' destinos mostrados';
  }
  bar.addEventListener('click', e => {
    const b = e.target.closest('button'); if (!b) return;
    history.replaceState(null, '', b.dataset.cont ? '?continente=' + b.dataset.cont : location.pathname);
    select(b.dataset.cont);
  });
  const p = new URLSearchParams(location.search).get('continente');
  if (valid.includes(p)) select(p);
})();
</script>''')

# ---------------- Hablamos ----------------
OFFICE_HOURS = 'Lunes a viernes: 9:00–13:15 y 16:00–19:00<br>Sábados: 10:00–13:00<br>Domingos: cerrado'
page('hablamos/',
 'Hablamos · Contacto de Viajes Parque en Santa Cruz y Tegueste',
 'Contacta con Viajes Parque: formulario para particulares, vía directa para empresas y oficinas en Santa Cruz de Tenerife (922 215 012) y Tegueste.',
 hero('Hablamos', 'Cuéntanos qué viaje tienes en la cabeza',
      'Escríbenos, llámanos o pásate por cualquiera de nuestras dos oficinas. Contestamos personas, y lo hacemos rápido.',
      None, '', [('Inicio', '/'), ('Hablamos', '/hablamos/')]) + f'''
<section class="section">
  <div class="wrap contact-layout">
    <div>
      <div class="contact-tabs" role="tablist" aria-label="Tipo de consulta">
        <button type="button" role="tab" id="tab-particular" aria-controls="panel-particular" aria-selected="true">
          <strong>Viajo por placer</strong>Formulario corto para particulares
        </button>
        <button type="button" role="tab" id="tab-empresa" aria-controls="panel-empresa" aria-selected="false" tabindex="-1">
          <strong>¿Viajas por trabajo entre islas?</strong>Vía directa para empresas e instituciones
        </button>
      </div>

      <div class="form-card" role="tabpanel" id="panel-particular" aria-labelledby="tab-particular">
        <h2>Tu próximo viaje, en dos líneas</h2>
        <p>Un formulario corto, no un cuestionario de agencia. Con esto ya podemos empezar.</p>
        <form id="formParticular" novalidate>
          <input type="hidden" name="tipo_consulta" value="Particular">
          <div class="fields">
            <div class="field"><label for="p_nombre">Nombre</label><input id="p_nombre" name="nombre" autocomplete="name" required><span class="err" id="p_nombre_err"></span></div>
            <div class="field"><label for="p_email">Correo electrónico</label><input id="p_email" name="email" type="email" autocomplete="email" required><span class="err" id="p_email_err"></span></div>
            <div class="field"><label for="p_tel">Teléfono <small>(opcional)</small></label><input id="p_tel" name="telefono" type="tel" autocomplete="tel" inputmode="tel"><span class="err" id="p_tel_err"></span></div>
            <div class="field"><label for="p_oficina">Oficina que prefieres</label>
              <select id="p_oficina" name="oficina"><option>Me da igual</option><option>Santa Cruz de Tenerife</option><option>Tegueste</option></select></div>
            <div class="field full"><label for="p_viaje">¿Qué viaje tienes en la cabeza?</label><textarea id="p_viaje" name="mensaje" required placeholder="Destino (o idea), fechas aproximadas, con quién viajas…"></textarea><span class="err" id="p_viaje_err"></span></div>
            <label class="check"><input type="checkbox" id="p_ok" name="privacidad" required><span>He leído la <a href="/politica-de-privacidad/" target="_blank">política de privacidad</a> y acepto que Viajes Parque use estos datos para responder a mi consulta.</span></label>
            <span class="err" id="p_ok_err"></span>
            <input class="hp" type="text" name="web" tabindex="-1" autocomplete="off" aria-hidden="true">
          </div>
          <div class="form-actions"><button class="btn" type="submit">Enviar consulta</button></div>
          <div class="form-status" role="status" aria-live="polite"></div>
        </form>
      </div>

      <div class="form-card" role="tabpanel" id="panel-empresa" aria-labelledby="tab-empresa" hidden>
        <h2>Cuéntanos sobre tu equipo</h2>
        <p>Cuántas personas viajan, con qué frecuencia y entre qué islas. Te respondemos con una propuesta de trabajo.</p>
        <form id="formEmpresa" novalidate>
          <input type="hidden" name="tipo_consulta" value="Empresa / institución">
          <div class="fields">
            <div class="field"><label for="e_entidad">Empresa o entidad</label><input id="e_entidad" name="entidad" autocomplete="organization" required><span class="err" id="e_entidad_err"></span></div>
            <div class="field"><label for="e_tipo">Tipo</label>
              <select id="e_tipo" name="tipo_entidad"><option value="Empresa">Empresa</option><option value="Club o equipo deportivo">Club o equipo deportivo</option><option value="Ayuntamiento o entidad pública">Ayuntamiento o entidad pública</option><option value="Otra">Otra</option></select></div>
            <div class="field"><label for="e_nombre">Persona de contacto</label><input id="e_nombre" name="nombre" autocomplete="name" required><span class="err" id="e_nombre_err"></span></div>
            <div class="field"><label for="e_tel">Teléfono</label><input id="e_tel" name="telefono" type="tel" autocomplete="tel" inputmode="tel" required><span class="err" id="e_tel_err"></span></div>
            <div class="field full"><label for="e_email">Correo electrónico</label><input id="e_email" name="email" type="email" autocomplete="email" required><span class="err" id="e_email_err"></span></div>
            <div class="field"><label for="e_personas">Personas que viajan</label>
              <select id="e_personas" name="personas"><option>1–5</option><option>6–15</option><option>16–30</option><option>Más de 30</option></select></div>
            <div class="field"><label for="e_frecuencia">Frecuencia de viaje</label>
              <select id="e_frecuencia" name="frecuencia"><option>Varias veces por semana</option><option>Semanal</option><option>Mensual</option><option>Por temporada o calendario</option><option>Puntual</option></select></div>
            <div class="field full"><label for="e_msg">Rutas habituales y lo que necesitáis</label><textarea id="e_msg" name="mensaje" required placeholder="Ej.: Tenerife Norte – Gran Canaria dos veces por semana, hotel una noche, factura mensual…"></textarea><span class="err" id="e_msg_err"></span></div>
            <label class="check"><input type="checkbox" id="e_ok" name="privacidad" required><span>He leído la <a href="/politica-de-privacidad/" target="_blank">política de privacidad</a> y acepto que Viajes Parque use estos datos para responder a mi consulta.</span></label>
            <span class="err" id="e_ok_err"></span>
            <input class="hp" type="text" name="web" tabindex="-1" autocomplete="off" aria-hidden="true">
          </div>
          <div class="form-actions"><button class="btn" type="submit">Enviar consulta</button><a href="tel:+34922215012">o llámanos: 922 215 012</a></div>
          <div class="form-status" role="status" aria-live="polite"></div>
        </form>
      </div>
    </div>

    <aside class="offices" aria-label="Oficinas">
      <div class="office">
        <span class="kind">Oficina central (sede)</span>
        <h3>Santa Cruz de Tenerife</h3>
        <dl>
          <div><dt>Dirección</dt><dd>C/ Santiago Beyro, 24-A<br>38007 Santa Cruz de Tenerife</dd></div>
          <div><dt>Teléfono</dt><dd><a href="tel:+34922215012">922 215 012</a></dd></div>
          <div><dt>Correo</dt><dd><a href="mailto:gestion@viajesparque.com">gestion@viajesparque.com</a></dd></div>
          <div><dt>Horario</dt><dd>{OFFICE_HOURS}</dd></div>
        </dl>
        <a class="btn yellow" href="https://www.google.com/maps/search/?api=1&amp;query=Viajes+Parque+Calle+Santiago+Beyro+24+Santa+Cruz+de+Tenerife" target="_blank" rel="noopener">Cómo llegar</a>
      </div>
      <div class="office">
        <span class="kind">Oficina</span>
        <h3>Tegueste</h3>
        <dl>
          <div><dt>Dirección</dt><dd>Ctra. Gral. La Laguna a Punta del Hidalgo, 202<br>38280 Tegueste</dd></div>
          <div><dt>Teléfono</dt><dd><a href="tel:+34922546111">922 546 111</a></dd></div>
          <div><dt>Correo</dt><dd><a href="mailto:gestion@viajesparque.com">gestion@viajesparque.com</a></dd></div>
          <div><dt>Horario</dt><dd>{OFFICE_HOURS}</dd></div>
        </dl>
        <a class="btn yellow" href="https://www.google.com/maps/search/?api=1&amp;query=Viajes+Parque+Tegueste+Carretera+General+La+Laguna+Punta+del+Hidalgo+202" target="_blank" rel="noopener">Cómo llegar</a>
      </div>
    </aside>
  </div>
</section>
''',
 og_image='/img/fotos/tarjeta-embarque.webp',
 jsonld=[breadcrumb([('Inicio', '/'), ('Hablamos', '/hablamos/')]),
         {"@context": "https://schema.org", "@type": "ContactPage", "name": "Hablamos · Contacto de Viajes Parque",
          "about": {"@id": SITE + "/#agencia"}}],
 scripts='<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>\n<script src="/assets/formularios.js"></script>')
