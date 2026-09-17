from gen_common import *

data = json.load(open(os.path.join(ROOT, 'diario-de-viaje/articulos.json')))
CATS = data['categorias']
POSTS = {a['slug']: a for a in data['articulos']}

BODY = {}

BODY['agencia-de-viajes-o-reservar-online'] = '''
<p>Reservar un vuelo y un hotel por internet se hace en diez minutos. Entonces, ¿para qué ir a una agencia de viajes? La pregunta es razonable y la respuesta honesta es: <strong>depende del viaje</strong>. Hay casos en los que hacerlo por tu cuenta tiene todo el sentido, y otros en los que una agencia te ahorra dinero, tiempo y más de un disgusto.</p>

<h2>Cuándo compensa reservar por tu cuenta</h2>
<ul>
  <li><strong>Viajes sencillos</strong>: un vuelo directo y un hotel en una ciudad que ya conoces.</li>
  <li><strong>Mucha flexibilidad</strong>: no te importa cambiar de fechas para cazar una oferta y asumes tú los imprevistos.</li>
  <li><strong>Tiempo libre para comparar</strong>: te gusta revisar opciones, leer letra pequeña y montar el puzle.</li>
</ul>
<p>Si es tu caso, adelante. No hay ninguna trampa en ello.</p>

<h2>Cuándo una agencia de viajes marca la diferencia</h2>
<h3>Viajes con varias piezas</h3>
<p>Un circuito por Japón, una luna de miel que combina ciudad y playa, un crucero con vuelos y noches de hotel antes de embarcar… Cuantas más piezas, más probable es que algo no encaje: un enlace demasiado justo, un traslado que no existe a esa hora, una noche que se queda sin cubrir. Revisar ese encaje es nuestro trabajo diario.</p>

<h3>Cuando algo se tuerce</h3>
<p>Una cancelación, una huelga, un vuelo que cambia de horario. Si reservaste por piezas en webs distintas, te toca reclamar a cada una por separado. Con una agencia, llamas a una persona que ya conoce tu reserva y que busca la solución contigo.</p>

<h3>Desde Canarias, las conexiones importan</h3>
<p>Salir desde Tenerife casi siempre implica enlazar. Elegir bien por dónde y con cuánto margen evita buena parte de los problemas. Es un detalle que los buscadores no siempre priorizan, pero que se nota el día del viaje.</p>

<h3>Tarifas a las que no llegas por tu cuenta</h3>
<p>Las agencias trabajamos con mayoristas y proveedores con los que tenemos acuerdos. En Viajes Parque, además, formamos parte del Grupo GEA, una gran red de agencias independientes. En muchos paquetes, cruceros y circuitos, eso se traduce en precios iguales o mejores que los que encuentras en internet, con asesoramiento incluido.</p>

<div class="table-scroll">
<table>
  <thead><tr><th>Situación</th><th>Por tu cuenta</th><th>Con una agencia local</th></tr></thead>
  <tbody>
    <tr><td>Vuelo directo + hotel conocido</td><td>Rápido y cómodo</td><td>También, si prefieres no dedicarle tiempo</td></tr>
    <tr><td>Circuito o viaje combinado</td><td>Muchas piezas que cuadrar</td><td>Un solo interlocutor para todo</td></tr>
    <tr><td>Crucero con vuelos y hotel</td><td>Tú coordinas horarios y traslados</td><td>Lo coordinamos nosotros</td></tr>
    <tr><td>Imprevisto en destino</td><td>Reclamas a cada proveedor</td><td>Llamas a quien lleva tu reserva</td></tr>
    <tr><td>Luna de miel o viaje especial</td><td>Detalles a tu cargo</td><td>Detalles preparados con antelación</td></tr>
  </tbody>
</table>
</div>

<h2>Qué preguntar antes de contratar una agencia de viajes</h2>
<ul>
  <li>¿Tiene oficina física y un teléfono al que te contesta una persona?</li>
  <li>¿Quién te atiende si hay un problema durante el viaje?</li>
  <li>¿Te explica con claridad qué incluye el precio y qué no?</li>
  <li>¿Qué opinan otros clientes? Las reseñas en Google son un buen termómetro.</li>
</ul>

<div class="callout"><p>Nuestra recomendación es simple: si el viaje es sencillo y te apetece organizarlo, hazlo. Si tiene varias piezas, es especial o prefieres tener a alguien de tu lado, pásate por Santa Cruz o por Tegueste y lo vemos juntos, sin compromiso.</p></div>
'''

BODY['como-elegir-tu-primer-crucero'] = '''
<p>Hacer un primer crucero es una de las formas más cómodas de conocer varios lugares en un solo viaje: deshaces la maleta una vez y el hotel se mueve contigo. Pero entre zonas, navieras, barcos y camarotes, elegir puede abrumar. Esta comparativa te ayuda a acertar.</p>

<h2>1. Elige la zona según la época y lo que buscas</h2>
<div class="table-scroll">
<table>
  <thead><tr><th>Zona</th><th>Temporada habitual</th><th>Ideal para</th></tr></thead>
  <tbody>
    <tr><td>Mediterráneo</td><td>Sobre todo de primavera a otoño</td><td>Ciudades, historia y gastronomía. Buen primer crucero.</td></tr>
    <tr><td>Norte de Europa y fiordos</td><td>Verano</td><td>Paisajes espectaculares y temperaturas suaves.</td></tr>
    <tr><td>Caribe</td><td>Principalmente invierno y primavera</td><td>Playa, calor y ambiente relajado.</td></tr>
    <tr><td>Islas atlánticas</td><td>Otoño e invierno</td><td>Itinerarios que suelen incluir Canarias y Madeira; a veces sin necesidad de volar lejos.</td></tr>
    <tr><td>Grandes travesías y cruceros fluviales</td><td>Variable</td><td>Viajeros con experiencia o que buscan un ritmo pausado.</td></tr>
  </tbody>
</table>
</div>
<p>Las fechas concretas cambian cada año según la naviera, así que conviene consultarlas antes de decidir.</p>

<h2>2. Barco grande o barco pequeño</h2>
<ul>
  <li><strong>Barcos grandes</strong>: muchas piscinas, espectáculos, restaurantes y actividades. Muy recomendables para familias con niños.</li>
  <li><strong>Barcos medianos y pequeños</strong>: ambiente más tranquilo, menos colas y, a menudo, acceso a puertos donde los grandes no llegan.</li>
</ul>

<h2>3. Qué tipo de camarote elegir</h2>
<ul>
  <li><strong>Interior</strong>: sin ventana y el más económico. Perfecto si solo vas a dormir.</li>
  <li><strong>Exterior</strong>: con ventana o ojo de buey, luz natural.</li>
  <li><strong>Con balcón</strong>: tu propia terraza al mar. Es el que más se disfruta en itinerarios de paisaje, como los fiordos.</li>
  <li><strong>Suite</strong>: más espacio y servicios extra.</li>
</ul>
<p>Un consejo: si te preocupa el mareo, los camarotes en cubiertas intermedias y hacia el centro del barco suelen notar menos el movimiento.</p>

<h2>4. Lo que el precio suele incluir (y lo que no)</h2>
<p>Normalmente incluye alojamiento, pensión completa en los restaurantes principales y buena parte del entretenimiento a bordo. Suelen pagarse aparte las bebidas (salvo paquete), las excursiones, algunos restaurantes de especialidad y las propinas o cargos de servicio, según la naviera. Pregunta siempre por estos conceptos antes de comparar precios.</p>

<h2>5. No olvides el antes y el después</h2>
<p>Desde Tenerife casi siempre hay que volar al puerto de salida. Recomendamos llegar el día anterior para no depender de un retraso, y reservar los traslados con tiempo. Nosotros coordinamos vuelos, noche de hotel, traslados y excursiones para que solo tengas que embarcar.</p>

<div class="callout"><p>¿Dudas entre dos opciones? Tráenos las dos y las comparamos contigo: itinerario, barco, camarote y lo que incluye cada una.</p></div>
'''

BODY['luna-de-miel-desde-tenerife'] = '''
<p>Preparar una boda ya da bastante trabajo como para que la luna de miel sea otra fuente de estrés. La buena noticia es que, con algo de antelación y las decisiones en el orden correcto, se organiza con calma.</p>

<h2>Cuándo empezar a planificar</h2>
<p>Lo ideal es empezar a hablarlo <strong>entre seis y nueve meses antes</strong>, sobre todo si pensáis en destinos lejanos o en fechas de mucha demanda. Así hay margen para elegir vuelos y alojamientos, revisar documentación y, si hace falta, vacunas.</p>

<h2>Primero el estilo, luego el destino</h2>
<p>Antes de mirar mapas, poneos de acuerdo en qué tipo de viaje os apetece:</p>
<ul>
  <li><strong>Relax total</strong>: playa, buen alojamiento y poco más. Maldivas, Mauricio o el Caribe encajan aquí.</li>
  <li><strong>Aventura y paisaje</strong>: safari en Tanzania, Islandia, Costa Rica.</li>
  <li><strong>Cultura y ciudad</strong>: Japón, Nueva York, una ruta por Italia.</li>
  <li><strong>Combinado</strong>: unos días de ciudad o naturaleza y cierre en la playa, como Tailandia con sus islas o Tanzania con Zanzíbar.</li>
</ul>

<h2>Cómo repartir el presupuesto</h2>
<p>Los vuelos de largo radio y el alojamiento suelen llevarse la mayor parte. Nuestro consejo es no recortar en las noches que más vais a disfrutar (por ejemplo, las de playa al final) y ser más prácticos en las de paso. También merece la pena reservar una parte para experiencias: una cena especial, una excursión privada.</p>

<h2>Detalles que conviene dejar atados</h2>
<ul>
  <li><strong>Documentación</strong>: pasaportes en vigor con la validez que exija el destino, y visados o autorizaciones si hacen falta.</li>
  <li><strong>Nombres en los billetes</strong>: tal y como aparecen en el documento con el que vais a viajar.</li>
  <li><strong>Seguro de viaje</strong> con buena cobertura médica y de cancelación.</li>
  <li><strong>Avisar de que es vuestra luna de miel</strong>: muchos alojamientos tienen detalles para recién casados.</li>
  <li><strong>Días de margen</strong> entre la boda y el vuelo, si es posible. Lo agradeceréis.</li>
</ul>

<h2>Salir desde Tenerife</h2>
<p>La mayoría de destinos de luna de miel requieren al menos una conexión. Elegir bien el punto de enlace y el margen entre vuelos hace el viaje mucho más cómodo, sobre todo a la ida.</p>

<div class="callout"><p>En Viajes Parque organizamos lunas de miel a medida. Venid a vernos a Santa Cruz o a Tegueste, contadnos cómo os imagináis el viaje y nos ponemos con ello.</p></div>
'''

BODY['viajes-de-empresa-entre-islas'] = '''
<p>En Canarias, muchas empresas tienen clientes, delegaciones o proveedores repartidos entre islas. El resultado es conocido: alguien del equipo reservando vuelos a última hora, facturas sueltas por todas partes y algún que otro susto en el aeropuerto. Hay otra forma de organizarlo.</p>

<h2>El problema de gestionar cada vuelo por separado</h2>
<ul>
  <li><strong>Tiempo perdido</strong>: cada reserva implica buscar, comparar, pagar y archivar.</li>
  <li><strong>Facturación dispersa</strong>: justificantes de distintas webs y tarjetas que administración tiene que cuadrar.</li>
  <li><strong>Sin margen ante imprevistos</strong>: si un vuelo cambia, cada persona se busca la vida.</li>
  <li><strong>Sin visión de conjunto</strong>: es difícil saber cuánto se gasta al mes en desplazamientos.</li>
</ul>

<h2>Cómo lo organizamos con una agencia</h2>
<h3>Rutas y preferencias registradas</h3>
<p>Si tu equipo vuela con frecuencia entre Tenerife y Gran Canaria, La Palma o Lanzarote, lo sabemos desde el primer día: horarios preferidos, aeropuertos, necesidades de hotel. Cada nueva reserva parte de ahí.</p>
<h3>Un solo interlocutor</h3>
<p>Una persona de la agencia conoce a tu equipo y su calendario. Las peticiones llegan a alguien que ya tiene el contexto.</p>
<h3>Facturación centralizada</h3>
<p>Agrupamos los servicios y facturamos a la empresa con el detalle que necesite vuestra contabilidad.</p>
<h3>Última hora, sin drama</h3>
<p>Cuando la reunión de mañana surge hoy, basta con una llamada o un correo.</p>

<h2>Checklist para ordenar los viajes de tu empresa</h2>
<ol>
  <li>Haz una lista de quién viaja y con qué frecuencia.</li>
  <li>Anota las rutas y horarios más habituales.</li>
  <li>Define quién puede solicitar viajes y quién los aprueba.</li>
  <li>Decide cómo queréis recibir la facturación (por viaje, mensual, por departamento).</li>
  <li>Comparte esa información con tu agencia y fija un canal para urgencias.</li>
</ol>

<div class="callout"><p>Si tu empresa se mueve entre islas, <a href="/experiencias/empresas/">conoce cómo trabajamos con empresas</a> o <a href="/hablamos/?tipo=empresa">cuéntanos sobre tu equipo</a>.</p></div>
'''

BODY['tecnologia-con-trato-de-siempre'] = '''
<p>Llevamos toda una vida organizando viajes desde Tenerife y seguimos creyendo en lo mismo: escuchar bien a quien viaja y acompañarle de principio a fin. Lo que sí ha cambiado son las herramientas que usamos para hacerlo.</p>

<h2>Para qué usamos la tecnología</h2>
<ul>
  <li><strong>Responder antes</strong>: contamos con un sistema de atención al cliente apoyado en inteligencia artificial que nos ayuda a resolver consultas frecuentes con rapidez y a organizar las peticiones que nos llegan.</li>
  <li><strong>Comparar más opciones</strong>: nuestros comparadores propios nos permiten revisar muchas combinaciones de vuelos y alojamientos en poco tiempo.</li>
  <li><strong>No perder detalle</strong>: tener la información ordenada nos ayuda a recordar tus preferencias la próxima vez.</li>
</ul>

<h2>Para qué no</h2>
<p>La tecnología no decide tu viaje. No sabe que tu madre no soporta los vuelos nocturnos ni que ese hotel que parece perfecto está lejos de todo. Eso lo sabe una persona que te escucha. Por eso, en Viajes Parque, <strong>las propuestas y los consejos los sigue dando el equipo</strong>, en la oficina, por teléfono o por correo.</p>

<h2>Lo que significa para ti</h2>
<ul>
  <li>Respuestas más rápidas a tus consultas.</li>
  <li>Propuestas mejor comparadas.</li>
  <li>El mismo trato cercano de siempre, con nombre y apellido.</li>
</ul>

<p>Este proyecto de atención al cliente con inteligencia artificial se ha desarrollado con el apoyo del programa Última Milla de la Secretaría de Estado de Turismo, financiado por la Unión Europea – NextGenerationEU.</p>

<div class="callout"><p>¿Quieres probarlo? <a href="/hablamos/">Escríbenos</a> y verás lo rápido que te contestamos… una persona.</p></div>
'''

for slug, a in POSTS.items():
    cat = CATS[a['categoria']]
    url = f'/diario-de-viaje/{slug}/'
    body = f'''
<section class="page-hero simple">
  <div class="wrap">
    <div>
      {crumbs([('Inicio', '/'), ('Diario de viaje', '/diario-de-viaje/'), (a['titulo'], url)])}
      <a class="eyebrow light" href="/diario-de-viaje/?categoria={a['categoria']}">{cat['nombre']}</a>
      <h1>{a['titulo']}</h1>
      <p>{a['resumen']}</p>
      <p class="post-meta">{a['minutos']} min de lectura · Equipo de Viajes Parque</p>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <article class="article">
      <div class="cover"><img src="{a['imagen']}" alt=""></div>
      <div class="prose">{BODY[slug]}</div>
      <div class="post-share"><span class="label">Compartir:</span><div class="socials" id="shareIcons"></div></div>
      <div class="post-cta">
        <h2>¿Lo preparamos juntos?</h2>
        <p>Cuéntanos qué tienes en mente y te respondemos con una propuesta a tu medida.</p>
        <a href="/hablamos/" class="btn">Hablamos</a>
      </div>
      <a class="back-link" href="/diario-de-viaje/">← Volver al diario de viaje</a>
    </article>
  </div>
</section>
<section class="section white">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Sigue leyendo</span><h2>Más del diario</h2></div>
    <div class="post-grid" id="morePosts"></div>
  </div>
</section>
'''
    page(f'diario-de-viaje/{slug}/', f"{a['titulo_seo']} | Viajes Parque", a.get('descripcion', a['resumen']), body,
         og_image=a['imagen'], og_type='article',
         jsonld=[breadcrumb([('Inicio', '/'), ('Diario de viaje', '/diario-de-viaje/'), (a['titulo'], url)]),
                 {"@context": "https://schema.org", "@type": "BlogPosting", "headline": a['titulo'],
                  "description": a['resumen'], "image": SITE + a['imagen'], "datePublished": a['fecha'],
                  "inLanguage": "es", "mainEntityOfPage": SITE + url, "articleSection": cat['nombre'],
                  "author": {"@type": "Organization", "name": "Viajes Parque"},
                  "publisher": {"@id": SITE + "/#agencia", "@type": "TravelAgency", "name": "Viajes Parque",
                                "logo": {"@type": "ImageObject", "url": SITE + "/img/marca/logo-viajes-parque.webp"}}}],
         scripts=f'''<script src="/assets/diario.js"></script>
<script>
VPShare.render('shareIcons', 'https://www.viajesparque.com{url}', {json.dumps(a['titulo'], ensure_ascii=False)});
VPDiario.render('morePosts', {{ limit: 3, exclude: '{slug}' }});
</script>''')
