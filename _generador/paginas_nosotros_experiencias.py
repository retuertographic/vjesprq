from gen_common import *

# ---------------- Quiénes te acompañamos ----------------
page('quienes-te-acompanamos/',
 'Quiénes te acompañamos: tu agencia en Tenerife | Viajes Parque',
 'Conoce Viajes Parque, agencia de viajes de Tenerife con oficinas en Santa Cruz y Tegueste: equipo cercano, viajes a medida y turismo responsable.',
 hero('Quiénes te acompañamos', 'Toda una vida en esto, y con ganas de seguir',
      'Somos una agencia de viajes de Tenerife con dos oficinas a pie de calle. Nos gusta que nos conozcas por nuestro nombre y que, cuando vuelvas de viaje, entres a contarnos qué tal te fue.',
      '/img/fotos/tour-guiado.webp', 'Grupo de viajeros con su guía durante una visita', [('Inicio', '/'), ('Quiénes te acompañamos', '/quienes-te-acompanamos/')]) + f'''
<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Lo que nos define</span>
      <h2>Cuatro cosas que no han cambiado</h2>
      <p>El sector ha cambiado mucho. Nuestra forma de tratar a la gente, no tanto.</p>
    </div>
    <div class="grid c2">
      <div class="card reveal">{icon('pin','coral')}
        <h3>Dos oficinas en Tenerife, no una web sin cara</h3>
        <p>Estamos en Santa Cruz (calle Santiago Beyro) y en Tegueste. Puedes pasarte, sentarte y decidir tu viaje mirando a alguien a los ojos. Y si prefieres teléfono o correo, también.</p>
      </div>
      <div class="card reveal">{icon('user','aqua')}
        <h3>El equipo que te atiende, con nombre y apellido</h3>
        <p>Detrás de cada reserva hay una persona que la conoce de principio a fin. Si surge un imprevisto, no empiezas de cero con alguien que nunca ha oído hablar de ti.</p>
      </div>
      <div class="card reveal">{icon('compass','yellow')}
        <h3>A medida, no de catálogo</h3>
        <p>Primero escuchamos: con quién viajas, qué te apetece, qué no soportas y cuánto quieres gastar. Luego proponemos. Así de sencillo, y así de poco habitual.</p>
      </div>
      <div class="card reveal">{icon('leaf','navy')}
        <h3>Turismo responsable y viajeros seguros</h3>
        <p>Preferimos proveedores serios, alojamientos que cuidan su entorno y experiencias que respetan a la gente del lugar. Y te acompañamos con información y asistencia durante todo el viaje.</p>
      </div>
    </div>
  </div>
</section>

<section class="section navy on-dark">
  <div class="wrap split">
    <div class="reveal">
      <span class="eyebrow">Respaldo</span>
      <h2>Pequeños en trato, grandes en opciones</h2>
      <p>Somos una agencia asociada al Grupo GEA, una de las mayores redes de agencias independientes. Eso nos da acceso a tarifas, mayoristas y proveedores de primer nivel sin dejar de ser la agencia de barrio que responde al teléfono.</p>
      <p>Además, usamos inteligencia artificial y comparadores propios para revisar opciones y resolver consultas más rápido. La tecnología busca; el consejo lo damos nosotros.</p>
      <ul class="checks">
        <li>Vuelos, hoteles, cruceros, circuitos y viajes corporativos.</li>
        <li>Seguimiento antes, durante y después del viaje.</li>
        <li>Respuestas ágiles sin perder el trato personal.</li>
      </ul>
    </div>
    <div class="split-media reveal"><img src="/img/fotos/hotel.webp" alt="Habitación de hotel con luz de atardecer" loading="lazy"></div>
  </div>
</section>

<section class="section white">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Nuestra forma de trabajar</span>
      <h2>Qué puedes esperar de nosotros</h2>
    </div>
    <div class="grid c3">
      <div class="card reveal">{icon('chat','coral')}<h3>1. Nos cuentas</h3><p>En la oficina, por teléfono o con el formulario. Dos líneas bastan para empezar.</p></div>
      <div class="card reveal">{icon('map','aqua')}<h3>2. Te proponemos</h3><p>Opciones claras, con lo que incluye y lo que no, para que decidas con calma.</p></div>
      <div class="card reveal">{icon('shield','yellow')}<h3>3. Te acompañamos</h3><p>Documentación, consejos antes de salir y alguien al otro lado si algo cambia.</p></div>
    </div>
  </div>
</section>

<section class="section tight">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Nuestras marcas</span>
      <h2>También nos encontrarás como</h2>
    </div>
    <div class="grid c2">
      <div class="card reveal center"><img src="/img/marca/tusmejoresviajes.webp" alt="tusmejoresviajes.com" loading="lazy" style="max-height:90px;margin:0 auto;"></div>
      <div class="card reveal center"><img src="/img/marca/tumejorhotel.webp" alt="tumejorhotel.com" loading="lazy" style="max-height:90px;margin:0 auto;"></div>
    </div>
  </div>
</section>
''' + cta('Pásate a conocernos', 'Santa Cruz o Tegueste, la que te quede más a mano. Y si no puedes venir, te llamamos nosotros.'),
 og_image='/img/fotos/tour-guiado.webp',
 jsonld=[breadcrumb([('Inicio', '/'), ('Quiénes te acompañamos', '/quienes-te-acompanamos/')])])

# ---------------- Experiencias (hub) ----------------
page('experiencias/',
 'Experiencias: viajes para particulares y empresas | Viajes Parque',
 'Viajes a medida para particulares, gestión de viajes de empresa entre islas y desplazamientos de grupo para clubes deportivos y ayuntamientos desde Tenerife.',
 hero('Experiencias', 'La misma cercanía, necesidades distintas',
      'Organizamos lo que hacemos según quién viaja: tú y los tuyos, tu empresa o tu institución. En cada caso, una persona de referencia y cero complicaciones.',
      None, '', [('Inicio', '/'), ('Experiencias', '/experiencias/')]) + '''
<section class="section">
  <div class="wrap">
    <div class="grid c3">
      <a class="audience reveal" href="/experiencias/particulares/">
        <img src="/img/fotos/luna-de-miel.webp" alt="" loading="lazy">
        <div class="in">
          <div class="num" style="background:var(--coral)">1</div>
          <h2 style="color:#fff;font-size:1.6rem">Particulares</h2>
          <div class="who">Familias, parejas y viajeros por libre</div>
          <p>Vacaciones, lunas de miel, escapadas, cruceros y aventuras a medida.</p>
          <span class="more">Ver experiencias</span>
        </div>
      </a>
      <a class="audience reveal" href="/experiencias/empresas/">
        <img src="/img/fotos/viaje-negocios.webp" alt="" loading="lazy">
        <div class="in">
          <div class="num" style="background:var(--aqua)">2</div>
          <h2 style="color:#fff;font-size:1.6rem">Empresas</h2>
          <div class="who">Compañías con equipos que viajan entre islas</div>
          <p>Gestión recurrente de vuelos y desplazamientos de trabajo dentro de Canarias.</p>
          <span class="more">Entre islas, sin perder el vuelo</span>
        </div>
      </a>
      <a class="audience reveal" href="/experiencias/instituciones/">
        <img src="/img/fotos/avion-pista.webp" alt="" loading="lazy">
        <div class="in">
          <div class="num" style="background:var(--yellow)">3</div>
          <h2 style="color:#fff;font-size:1.6rem">Instituciones</h2>
          <div class="who">Equipos deportivos y entidades públicas</div>
          <p>Desplazamientos de grupo, recurrentes y con calendario fijo.</p>
          <span class="more">Cuando viaja el equipo entero</span>
        </div>
      </a>
    </div>
  </div>
</section>

<section class="section white">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Lo que tienen en común</span>
      <h2>Tres públicos, una misma forma de trabajar</h2>
      <p>Da igual si organizamos una escapada de fin de semana, los vuelos semanales de un equipo comercial o la temporada de un club: hay cosas que no cambian.</p>
    </div>
    <div class="grid c3">
      <div class="card reveal">''' + icon('user','coral') + '''<h3>Una persona de referencia</h3><p>Siempre sabes a quién llamar, y esa persona ya conoce tu viaje, tu empresa o tu calendario.</p></div>
      <div class="card reveal">''' + icon('compass','aqua') + '''<h3>Propuestas a medida</h3><p>Escuchamos primero y proponemos después. Nada de paquetes cerrados que no encajan con lo que necesitas.</p></div>
      <div class="card reveal">''' + icon('shield','yellow') + '''<h3>Acompañamiento real</h3><p>Antes, durante y después del viaje. Si algo cambia, lo resolvemos contigo desde Tenerife.</p></div>
    </div>
  </div>
</section>
''' + cta(),
 og_image='/img/fotos/luna-de-miel.webp',
 jsonld=[breadcrumb([('Inicio', '/'), ('Experiencias', '/experiencias/')])])

# ---------------- Particulares ----------------
servicios = [
 ('a-tu-manera', 'A tu manera', 'Paquetes personalizados', 'compass', 'coral', '/img/destinos/kyoto.webp', 'Calle tradicional de Kioto al amanecer',
  'Nada de elegir entre el paquete A y el paquete B. Partimos de lo que te apetece —playa, ciudad, naturaleza, gastronomía, o todo junto— y montamos el viaje a tu ritmo y a tu presupuesto.',
  ['Itinerario diseñado contigo, pieza a pieza.', 'Vuelos, alojamiento, traslados y actividades en una sola reserva.', 'Ajustes hasta que el viaje sea exactamente el tuyo.']),
 ('vuelos-y-hoteles', 'Vuela y aterriza en buenas manos', 'Vuelos y hoteles', 'plane', 'aqua', '/img/fotos/avion-pista.webp', 'Avión en pista preparado para embarcar',
  'Buscamos las mejores combinaciones de vuelos desde Tenerife y alojamientos que merecen la pena, con acceso a las tarifas de una gran red de agencias. Tú eliges; nosotros comparamos.',
  ['Conexiones desde Tenerife Norte y Tenerife Sur.', 'Hoteles revisados, no solo bien puntuados.', 'Cambios e incidencias gestionados por nosotros.']),
 ('tours-guiados', 'Con quien sabe y por dónde', 'Tours guiados', 'map', 'yellow', '/img/fotos/tour-guiado.webp', 'Guía turística explicando un monumento a un grupo',
  'Circuitos y visitas con guías que conocen el terreno, para ver lo importante sin perder tiempo y entender lo que estás viendo.',
  ['Circuitos en grupo o visitas privadas.', 'Guías en español siempre que el destino lo permite.', 'Combinables con días libres por tu cuenta.']),
 ('asesoria-de-viaje', 'Te lo explicamos antes de ir', 'Asesoría de viaje', 'chat', 'navy', '/img/fotos/tarjeta-embarque.webp', 'Viajero con pasaporte y tarjeta de embarque',
  'Documentación, visados, vacunas recomendadas, clima, enchufes, propinas, seguro de viaje… Te lo contamos con calma y por escrito, para que salgas de casa sin dudas.',
  ['Requisitos de entrada y documentación al día.', 'Recomendaciones prácticas para cada destino.', 'Seguro de viaje adaptado a tu plan.']),
 ('luna-de-miel', 'El viaje que no se olvida', 'Luna de miel', 'heart', 'coral', '/img/fotos/luna-de-miel.webp', 'Pareja de recién casados al atardecer junto al mar',
  'Planificamos lunas de miel y viajes románticos con el mimo que merecen: el destino, los tiempos, los detalles y esas sorpresas que se preparan con antelación.',
  ['Destinos de playa, aventura o combinados.', 'Organización pensada para no estresaros antes de la boda.', 'Detalles especiales en alojamientos seleccionados.']),
 ('cruceros', 'A flote, sin sustos', 'Cruceros', 'ship', 'aqua', '/img/destinos/crucero.webp', 'Crucero atracado en puerto al atardecer',
  'Te ayudamos a elegir naviera, barco, itinerario y camarote según cómo te gusta viajar, y nos ocupamos de vuelos, traslados y excursiones para que solo tengas que embarcar.',
  ['Mediterráneo, norte de Europa, Caribe, islas atlánticas y más.', 'Comparamos navieras y tipos de camarote contigo.', 'Salidas y escalas cercanas a Canarias cuando las hay.']),
]
cards = ''.join(f'''<a class="card reveal" href="#{s[0]}">{icon(s[3], s[4])}<h3>{s[1]}</h3><p>{s[7].split('.')[0]}.</p><span class="tag">{s[2]}</span></a>''' for s in servicios)
blocks = ''
for i, s in enumerate(servicios):
    lis = ''.join(f'<li>{x}</li>' for x in s[8])
    extra = ''
    blocks += f'''
<section class="section {'white' if i % 2 == 0 else ''}" id="{s[0]}">
  <div class="wrap split {'rev' if i % 2 else ''}">
    <div class="split-media reveal"><img src="{s[5]}" alt="{s[6]}" loading="lazy"></div>
    <div class="reveal">
      <span class="eyebrow">{s[2]}</span>
      <h2>{s[1]}</h2>
      <p>{s[7]}</p>
      <ul class="checks">{lis}</ul>{extra}
      <a href="/hablamos/?tipo=particular&amp;interes={s[0]}" class="btn">Quiero información</a>
    </div>
  </div>
</section>'''

page('experiencias/particulares/',
 'Viajes a medida, luna de miel y cruceros en Tenerife | Viajes Parque',
 'Paquetes a medida, vuelos y hoteles, tours guiados, asesoría, lunas de miel y cruceros desde Tenerife, con atención personal en Santa Cruz y Tegueste.',
 hero('Experiencias · Particulares', 'Viajes pensados para ti (y para los tuyos)',
      'Vacaciones en familia, lunas de miel, escapadas y aventuras. Tú pones las ganas; nosotros, la experiencia para que todo encaje.',
      '/img/fotos/luna-de-miel.webp', 'Pareja al atardecer junto al mar',
      [('Inicio', '/'), ('Experiencias', '/experiencias/'), ('Particulares', '/experiencias/particulares/')]) + f'''
<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Qué hacemos por ti</span>
      <h2>Seis formas de ayudarte a viajar mejor</h2>
      <p>Antes lo llamábamos “servicios”. Ahora preferimos contarte lo que vas a vivir.</p>
    </div>
    <div class="grid c3">{cards}</div>
  </div>
</section>
{blocks}
''' + cta('¿Por dónde empezamos?', 'Dinos destino (o ni eso), fechas aproximadas y con quién viajas. Con eso ya tenemos para empezar.'),
 og_image='/img/fotos/luna-de-miel.webp',
 jsonld=[breadcrumb([('Inicio', '/'), ('Experiencias', '/experiencias/'), ('Particulares', '/experiencias/particulares/')]),
         {"@context": "https://schema.org", "@type": "ItemList", "name": "Experiencias para particulares",
          "itemListElement": [{"@type": "ListItem", "position": i + 1,
             "item": {"@type": "Service", "name": f"{s[1]} ({s[2]})", "description": s[7],
                      "provider": {"@id": SITE + "/#agencia"}, "areaServed": "Islas Canarias"}} for i, s in enumerate(servicios)]}])

# ---------------- Empresas ----------------
emp = [
 ('plane', 'coral', 'Vuelos inter-insulares gestionados de forma recurrente', 'No se empieza de cero cada vez que alguien tiene que volar a otra isla. Conocemos vuestras rutas y horarios habituales y lo gestionamos de forma continuada.'),
 ('receipt', 'aqua', 'Facturación centralizada', 'Un solo interlocutor y una sola factura para toda la empresa, con el detalle que necesite vuestro departamento de administración.'),
 ('bolt', 'yellow', 'Reservas rápidas de última hora', 'Para cuando la reunión de mañana en otra isla surge hoy. Nos escribes o nos llamas y lo resolvemos.'),
 ('user', 'navy', 'Un interlocutor que ya conoce al equipo', 'Sus rutas habituales, sus preferencias y su calendario. Nada de explicar lo mismo cada vez.'),
]
emp_cards = ''.join(f'<div class="card reveal">{icon(a,b)}<h3>{c}</h3><p>{d}</p></div>' for a, b, c, d in emp)
page('experiencias/empresas/',
 'Viajes corporativos entre islas Canarias | Viajes Parque',
 'Viajes corporativos en Canarias: vuelos entre islas recurrentes, facturación centralizada, reservas de última hora e interlocutor fijo para tu empresa.',
 hero('Experiencias · Empresas', 'Entre islas, sin perder el vuelo',
      'Para compañías con equipos que se mueven entre las islas por trabajo. Nosotros nos ocupamos de vuelos, hoteles y cambios; tu equipo, de lo suyo.',
      '/img/fotos/viaje-negocios.webp', 'Profesionales con traje caminando hacia el aeropuerto',
      [('Inicio', '/'), ('Experiencias', '/experiencias/'), ('Empresas', '/experiencias/empresas/')]) + f'''
<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Viajes corporativos</span>
      <h2>Menos gestiones, más reuniones que salen bien</h2>
      <p>Si en tu empresa alguien cruza a Gran Canaria, La Palma o Lanzarote cada semana, sabes lo que cuesta coordinarlo reserva a reserva. Lo organizamos de otra manera.</p>
    </div>
    <div class="grid c2">{emp_cards}</div>
    <div class="quip reveal"><p>Que tu equipo comercial pierda el vuelo de las 7 a Gran Canaria no debería ser noticia de cada mes.</p></div>
  </div>
</section>

<section class="section white">
  <div class="wrap split">
    <div class="split-media reveal"><img src="/img/destinos/roque-nublo.webp" alt="Roque Nublo, Gran Canaria" loading="lazy"></div>
    <div class="reveal">
      <span class="eyebrow">Cómo empezamos</span>
      <h2>Una conversación y un plan</h2>
      <p>Nos cuentas cuántas personas viajan, con qué frecuencia y entre qué islas. Con eso preparamos una forma de trabajar a vuestra medida.</p>
      <ul class="checks">
        <li>Rutas y horarios habituales registrados desde el primer día.</li>
        <li>Canal directo para peticiones urgentes.</li>
        <li>Facturación agrupada y adaptada a vuestra contabilidad.</li>
        <li>También viajes nacionales e internacionales, ferias y convenciones.</li>
      </ul>
      <a href="/hablamos/?tipo=empresa" class="btn">Cuéntanos sobre tu equipo</a>
    </div>
  </div>
</section>
''' + cta('¿Tu equipo viaja entre islas?', 'Cuéntanos cuántas personas y con qué frecuencia. Te proponemos cómo trabajar juntos.',
          '<a href="tel:+34922215012" class="btn ghost">Llamar: 922 215 012</a>').replace('href="/hablamos/"', 'href="/hablamos/?tipo=empresa"'),
 og_image='/img/fotos/viaje-negocios.webp',
 jsonld=[breadcrumb([('Inicio', '/'), ('Experiencias', '/experiencias/'), ('Empresas', '/experiencias/empresas/')]),
         {"@context": "https://schema.org", "@type": "Service", "name": "Gestión de viajes de empresa entre islas",
          "serviceType": "Viajes corporativos", "provider": {"@id": SITE + "/#agencia"}, "areaServed": "Islas Canarias",
          "description": "Vuelos inter-insulares recurrentes, facturación centralizada, reservas de última hora e interlocutor fijo."}])

# ---------------- Instituciones ----------------
ins = [
 ('calendar', 'coral', 'Desplazamientos por calendario', 'Competiciones, plenos, actos oficiales y convenciones. Planificamos la temporada completa y no solo el próximo viaje.'),
 ('users', 'aqua', 'Gestión de grupos grandes', 'Vuelos, alojamiento, traslados y comidas, todo coordinado para que el grupo llegue junto y a tiempo.'),
 ('receipt', 'yellow', 'Facturación adaptada', 'A la administración pública o a la entidad, como corresponda, con la documentación que necesitéis.'),
 ('user', 'navy', 'El mismo interlocutor, temporada tras temporada', 'Que ya conoce el calendario y no hay que explicarle todo de nuevo.'),
]
ins_cards = ''.join(f'<div class="card reveal">{icon(a,b)}<h3>{c}</h3><p>{d}</p></div>' for a, b, c, d in ins)
page('experiencias/instituciones/',
 'Viajes para clubes deportivos y ayuntamientos | Viajes Parque',
 'Desplazamientos de grupo para equipos deportivos y entidades públicas en Canarias: calendario de temporada, facturación adaptada e interlocutor fijo.',
 hero('Experiencias · Instituciones', 'Cuando viaja el equipo entero',
      'Para equipos deportivos y entidades públicas, como ayuntamientos, con desplazamientos recurrentes y calendario fijo.',
      '/img/fotos/avion-pista.webp', 'Avión en pista con escalerillas de embarque',
      [('Inicio', '/'), ('Experiencias', '/experiencias/'), ('Instituciones', '/experiencias/instituciones/')]) + f'''
<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Grupos y temporadas</span>
      <h2>Todo el grupo, en el mismo sitio y a la misma hora</h2>
      <p>Mover a un equipo o a una delegación no es sumar billetes: es cuadrar horarios, habitaciones, traslados y comidas. De eso nos encargamos.</p>
    </div>
    <div class="grid c2">{ins_cards}</div>
    <div class="quip reveal"><p>Porque coordinar autobuses, hoteles y horarios para veintitrés personas no debería recaer en quien lleva la equipación.</p></div>
  </div>
</section>

<section class="section white">
  <div class="wrap split rev">
    <div class="split-media reveal"><img src="/img/fotos/aeropuerto.webp" alt="Viajera consultando los paneles de salidas del aeropuerto" loading="lazy"></div>
    <div class="reveal">
      <span class="eyebrow">Para quién</span>
      <h2>Clubes, federaciones y administraciones</h2>
      <p>Trabajamos con entidades que necesitan moverse con regularidad y rendir cuentas de cada gasto.</p>
      <ul class="checks">
        <li>Clubes y equipos deportivos de base y competición.</li>
        <li>Ayuntamientos y otras entidades públicas.</li>
        <li>Asociaciones, colegios profesionales y grupos organizados.</li>
      </ul>
      <a href="/hablamos/?tipo=institucion" class="btn">Planifiquemos la temporada</a>
    </div>
  </div>
</section>
''' + cta('¿Empieza la temporada?', 'Pásanos el calendario y te devolvemos un plan de desplazamientos.').replace('href="/hablamos/"', 'href="/hablamos/?tipo=institucion"'),
 og_image='/img/fotos/avion-pista.webp',
 jsonld=[breadcrumb([('Inicio', '/'), ('Experiencias', '/experiencias/'), ('Instituciones', '/experiencias/instituciones/')]),
         {"@context": "https://schema.org", "@type": "Service", "name": "Viajes de grupo para equipos deportivos e instituciones",
          "serviceType": "Viajes de grupo", "provider": {"@id": SITE + "/#agencia"}, "areaServed": "Islas Canarias",
          "description": "Desplazamientos por calendario, gestión de grupos grandes, facturación adaptada e interlocutor fijo."}])
