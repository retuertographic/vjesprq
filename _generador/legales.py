from gen_common import *

TODO = lambda s: f'<span class="todo">{s}</span>'

def legal(path, title, h1, desc, html):
    page(path, f'{title} | Viajes Parque', desc,
         hero('Información legal', h1, 'Última actualización: septiembre de 2026.', None, '',
              [('Inicio', '/'), (h1, '/' + path)]) +
         f'<section class="section white"><div class="wrap"><div class="legal prose">{html}</div></div></section>')

legal('aviso-legal/', 'Aviso legal', 'Aviso legal',
 'Aviso legal de viajesparque.com: datos identificativos de Viajes Parque, S.L., condiciones de uso, propiedad intelectual y legislación aplicable.', f'''
<p>En cumplimiento de la Ley 34/2002, de 11 de julio, de Servicios de la Sociedad de la Información y de Comercio Electrónico (LSSI-CE), se informa de los datos del titular de este sitio web.</p>
<h2>1. Datos identificativos</h2>
<table>
  <tr><th>Titular</th><td>Viajes Parque, S.L.</td></tr>
  <tr><th>Nombre comercial</th><td>Viajes Parque</td></tr>
  <tr><th>NIF</th><td>B38404927</td></tr>
  <tr><th>Domicilio social</th><td>Calle Santiago Beyro, 24-A, 38007 Santa Cruz de Tenerife (España)</td></tr>
  <tr><th>Otra oficina</th><td>Ctra. Gral. La Laguna a Punta del Hidalgo, 202, 38280 Tegueste (Santa Cruz de Tenerife)</td></tr>
  <tr><th>Teléfonos</th><td>922 215 012 (Santa Cruz) · 922 546 111 (Tegueste)</td></tr>
  <tr><th>Correo electrónico</th><td><a href="mailto:gestion@viajesparque.com">gestion@viajesparque.com</a></td></tr>
  <tr><th>Datos registrales</th><td>{TODO('Inscrita en el Registro Mercantil de Santa Cruz de Tenerife, tomo __, folio __, hoja __')}</td></tr>
  <tr><th>Agencia de viajes</th><td>{TODO('Nº de inscripción en el Registro General Turístico de Canarias: ________')}</td></tr>
  <tr><th>Sitio web</th><td>www.viajesparque.com</td></tr>
</table>
<h2>2. Objeto y condiciones de uso</h2>
<p>Este sitio web ofrece información sobre los servicios de Viajes Parque como agencia de viajes y permite a los usuarios ponerse en contacto con ella. El acceso es gratuito y atribuye la condición de usuario, que se compromete a hacer un uso adecuado de los contenidos, conforme a la ley, la buena fe y el orden público.</p>
<p>La información publicada tiene carácter orientativo. Precios, disponibilidad, horarios y requisitos de viaje (documentación, visados, sanitarios) pueden variar, y se confirman siempre en el momento de solicitar un presupuesto o formalizar una reserva. La contratación de viajes combinados y servicios de viaje se rige por las condiciones generales que se entregan antes de la contratación y por el Real Decreto Legislativo 1/2007, de 16 de noviembre.</p>
<h2>3. Propiedad intelectual e industrial</h2>
<p>Los textos, diseños, logotipos, marcas (incluidas Viajes Parque, tusmejoresviajes.com y tumejorhotel.com) y demás elementos del sitio son titularidad de Viajes Parque, S.L. o de terceros que han autorizado su uso. Queda prohibida su reproducción, distribución o transformación sin autorización expresa, salvo para uso personal y privado.</p>
<p>Algunas fotografías se publican bajo licencias libres (Creative Commons). Su autoría y licencia se detallan en la página de <a href="/creditos/">créditos de imágenes</a>.</p>
<h2>4. Responsabilidad</h2>
<p>Viajes Parque no se hace responsable de los daños derivados de un uso indebido del sitio, de interrupciones técnicas ajenas a su control ni de los contenidos de sitios de terceros enlazados desde esta web, que se ofrecen únicamente a título informativo.</p>
<h2>5. Protección de datos y cookies</h2>
<p>El tratamiento de datos personales se describe en la <a href="/politica-de-privacidad/">Política de privacidad</a>, y el uso de cookies y tecnologías similares, en la <a href="/politica-de-cookies/">Política de cookies</a>.</p>
<h2>6. Resolución de litigios</h2>
<p>Para cualquier reclamación puedes dirigirte a nuestras oficinas o escribir a <a href="mailto:gestion@viajesparque.com">gestion@viajesparque.com</a>. Tienes a tu disposición hojas de reclamaciones en ambas oficinas. También puedes acudir a la plataforma europea de resolución de litigios en línea: <a href="https://ec.europa.eu/consumers/odr" target="_blank" rel="noopener">ec.europa.eu/consumers/odr</a>.</p>
<h2>7. Legislación aplicable</h2>
<p>Este aviso legal se rige por la legislación española. Para cualquier controversia, las partes se someten a los juzgados y tribunales que correspondan conforme a la normativa de consumidores y usuarios.</p>
''')

legal('politica-de-privacidad/', 'Política de privacidad', 'Política de privacidad',
 'Cómo trata Viajes Parque, S.L. tus datos personales: finalidades, base jurídica, conservación, destinatarios y cómo ejercer tus derechos.', f'''
<p>En Viajes Parque tratamos tus datos con el mismo cuidado con el que preparamos tus viajes. Esta política explica qué datos recogemos y para qué, conforme al Reglamento (UE) 2016/679 (RGPD) y a la Ley Orgánica 3/2018 (LOPDGDD).</p>
<h2>1. Responsable del tratamiento</h2>
<p>Viajes Parque, S.L. · NIF B38404927 · Calle Santiago Beyro, 24-A, 38007 Santa Cruz de Tenerife · Tel. 922 215 012 · Correo para protección de datos: <a href="mailto:lopd-rgpd@viajesparque.com">lopd-rgpd@viajesparque.com</a>.</p>
<h2>2. Qué datos tratamos y para qué</h2>
<table>
  <tr><th>Finalidad</th><th>Datos</th><th>Base jurídica</th><th>Conservación</th></tr>
  <tr><td>Responder a las consultas enviadas por los formularios, el correo o el teléfono</td><td>Nombre, correo, teléfono, empresa o entidad y lo que nos cuentes en el mensaje</td><td>Tu consentimiento y la aplicación de medidas precontractuales a tu solicitud</td><td>El tiempo necesario para atender la consulta y, como máximo, un año si no llega a contratarse ningún servicio</td></tr>
  <tr><td>Gestionar presupuestos, reservas y viajes contratados</td><td>Datos identificativos y de contacto, documentación de viaje, preferencias y, en su caso, datos de pago</td><td>Ejecución del contrato</td><td>Mientras dure la relación y, después, durante los plazos legales (fiscales, contables y de consumo)</td></tr>
  <tr><td>Facturación a particulares, empresas e instituciones</td><td>Datos fiscales y de facturación</td><td>Obligación legal</td><td>Plazos exigidos por la normativa tributaria y mercantil</td></tr>
  <tr><td>Enviarte ofertas y novedades</td><td>Nombre y correo o teléfono</td><td>Tu consentimiento expreso, que puedes retirar en cualquier momento</td><td>Hasta que te des de baja</td></tr>
</table>
<p>Si en una consulta o reserva facilitas datos de otras personas (acompañantes, empleados, deportistas), declaras contar con su autorización e informarles de esta política. Los datos de menores solo se tratan con autorización de sus padres o tutores.</p>
<h2>3. Destinatarios</h2>
<p>Para organizar tu viaje, comunicamos los datos imprescindibles a los proveedores que lo hacen posible: aerolíneas, navieras, hoteles, mayoristas, receptivos, aseguradoras y el Grupo GEA, al que estamos asociados. Algunos de ellos pueden estar fuera del Espacio Económico Europeo cuando el destino del viaje lo exige; en ese caso, la comunicación es necesaria para ejecutar el contrato que solicitas.</p>
<p>También contamos con proveedores tecnológicos que actúan como encargados del tratamiento (alojamiento web, correo electrónico, envío de formularios y herramientas de atención al cliente), con los que tenemos firmados los acuerdos exigidos por el RGPD. {TODO('Revisar la lista de encargados: EmailJS, proveedor de correo y sistema de atención con IA.')}</p>
<p>No cedemos tus datos a terceros para fines comerciales ajenos.</p>
<h2>4. Tus derechos</h2>
<p>Puedes ejercer tus derechos de acceso, rectificación, supresión, oposición, limitación del tratamiento y portabilidad, así como retirar tu consentimiento, escribiendo a <a href="mailto:lopd-rgpd@viajesparque.com">lopd-rgpd@viajesparque.com</a> o por correo postal a nuestra sede, indicando el derecho que ejerces. Si consideras que no hemos atendido correctamente tu solicitud, puedes reclamar ante la Agencia Española de Protección de Datos (<a href="https://www.aepd.es" target="_blank" rel="noopener">www.aepd.es</a>).</p>
<h2>5. Seguridad</h2>
<p>Aplicamos medidas técnicas y organizativas adecuadas para proteger tus datos frente a pérdidas, accesos no autorizados o alteraciones. La web funciona siempre con conexión cifrada (HTTPS).</p>
''')

legal('politica-de-cookies/', 'Política de cookies', 'Política de cookies',
 'Información sobre el uso de cookies y tecnologías similares en viajesparque.com, la web de la agencia Viajes Parque, S.L., y cómo gestionarlas.', '''
<p>Esta política explica qué son las cookies y cómo las utiliza este sitio web, conforme al artículo 22.2 de la LSSI-CE y a la Guía sobre el uso de las cookies de la Agencia Española de Protección de Datos.</p>
<h2>1. ¿Qué son las cookies?</h2>
<p>Son pequeños archivos que un sitio web guarda en tu navegador para recordar información sobre tu visita. Algunas son necesarias para que la web funcione y otras sirven para analizar el uso del sitio o mostrar publicidad.</p>
<h2>2. Cookies que utiliza esta web</h2>
<p>A día de hoy, <strong>viajesparque.com no instala cookies propias ni cookies de analítica o publicidad</strong>. Tampoco incrusta mapas ni vídeos de terceros que las instalen: los enlaces a Google Maps o a redes sociales solo te llevan a esos servicios si haces clic en ellos, y a partir de ese momento se aplican sus propias políticas.</p>
<p>Para mostrar correctamente los textos, la web descarga tipografías desde Google Fonts. Este servicio no instala cookies, aunque tu navegador comunica a Google la dirección IP necesaria para descargar los archivos.</p>
<p>Si en el futuro incorporamos herramientas de analítica u otras cookies no necesarias, te lo pediremos antes mediante un panel de configuración y actualizaremos esta política con el detalle de cada cookie.</p>
<h2>3. Cómo gestionar las cookies en tu navegador</h2>
<p>Puedes consultar, bloquear o eliminar las cookies desde la configuración de tu navegador:</p>
<ul>
  <li><a href="https://support.google.com/chrome/answer/95647" target="_blank" rel="noopener">Google Chrome</a></li>
  <li><a href="https://support.mozilla.org/es/kb/Borrar%20cookies" target="_blank" rel="noopener">Mozilla Firefox</a></li>
  <li><a href="https://support.apple.com/es-es/guide/safari/sfri11471/mac" target="_blank" rel="noopener">Safari</a></li>
  <li><a href="https://support.microsoft.com/es-es/microsoft-edge" target="_blank" rel="noopener">Microsoft Edge</a></li>
</ul>
<h2>4. Contacto</h2>
<p>Para cualquier duda sobre esta política, escríbenos a <a href="mailto:gestion@viajesparque.com">gestion@viajesparque.com</a>.</p>
''')

# Créditos
cred = json.load(open(os.path.join(ROOT, 'img/destinos/creditos.json')))
NAMES = {'santorini': 'Oia, Santorini (Grecia)', 'kirkjufell': 'Kirkjufell (Islandia)', 'lisboa': 'Plaza del Comercio, Lisboa (Portugal)',
         'kyoto': 'Yasaka-dori, Kioto (Japón)', 'bangkok': 'Templo del Buda Esmeralda, Bangkok (Tailandia)', 'bali': 'Arrozales en Bali (Indonesia)',
         'maldivas': 'Maldivas', 'machu-picchu': 'Machu Picchu (Perú)', 'nueva-york': 'Manhattan, Nueva York (EE. UU.)',
         'la-habana': 'Malecón de La Habana (Cuba)', 'serengeti': 'Serengeti (Tanzania)', 'marrakech': 'Zoco de Marrakech (Marruecos)',
         'anaga': 'Chinamada, Anaga (Tenerife)', 'roque-nublo': 'Roque Nublo (Gran Canaria)', 'crucero': 'Crucero en el puerto de Sète (Francia)'}
LIC = {'CC BY-SA 4.0': 'https://creativecommons.org/licenses/by-sa/4.0/deed.es', 'CC BY-SA 3.0': 'https://creativecommons.org/licenses/by-sa/3.0/deed.es',
       'CC BY 4.0': 'https://creativecommons.org/licenses/by/4.0/deed.es', 'CC BY 3.0': 'https://creativecommons.org/licenses/by/3.0/deed.es'}
items = ''.join(
    f'<li><strong>{NAMES[k]}</strong> — foto de {v["artist"]}, <a href="{v["page"]}" target="_blank" rel="noopener">Wikimedia Commons</a>, '
    f'licencia <a href="{LIC[v["license"]]}" target="_blank" rel="noopener">{v["license"]}</a>. Imagen recortada y redimensionada.</li>'
    for k, v in cred.items())
legal('creditos/', 'Créditos de imágenes', 'Créditos de imágenes',
 'Autoría y licencias Creative Commons de las fotografías de destinos utilizadas en la web de Viajes Parque, agencia de viajes en Tenerife.', f'''
<p>Estas fotografías se publican gracias a sus autores bajo licencias Creative Commons. Las imágenes adaptadas con licencia “CompartirIgual” (BY-SA) se distribuyen bajo la misma licencia.</p>
<ul class="credits">{items}</ul>
<p>El resto de imágenes y los logotipos son propiedad de Viajes Parque, S.L. o se usan con licencia de sus titulares. Los logotipos de financiación pertenecen a la Unión Europea, al Gobierno de España y a sus respectivos organismos.</p>
''')
