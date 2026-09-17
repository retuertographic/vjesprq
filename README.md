# Viajes Parque — web

Web estática de [Viajes Parque](https://www.viajesparque.com), agencia de viajes con oficinas en Santa Cruz de Tenerife y Tegueste. Se publica con GitHub Pages desde `main`, con dominio propio en `CNAME`. Sigue el mismo esquema que la web de El Capricho: HTML plano, CSS y JS comunes, y cabecera y pie cargados como parciales.

## Estructura

```
index.html                     Inicio
quienes-te-acompanamos/        Quiénes te acompañamos (antes "Quiénes somos")
experiencias/                  Hub + particulares/, empresas/, instituciones/
destinos/                      Destinos con filtro por continente (?continente=asia)
diario-de-viaje/               Blog: índice, articulos.json y un directorio por artículo
hablamos/                      Contacto: formulario para particulares y para empresas
aviso-legal/ politica-de-privacidad/ politica-de-cookies/ creditos/
viajes-parque/ servicios/ contacto/ consentimiento-.../   Redirecciones de las URLs de la web anterior
partials/header.html, partials/footer.html
assets/site.css                Estilos y paleta (coral, turquesa y amarillo sobre azul marino)
assets/site-common.js          Carga de parciales, menú, animaciones, compartir y Biscotti (opcional)
assets/diario.js               Listado de artículos a partir de articulos.json
assets/formularios.js          Pestañas, validación y envío de "Hablamos"
_generador/                    Scripts de Python que generaron las páginas interiores
```

Las rutas son absolutas (`/assets/...`), así que la web tiene que servirse desde la raíz del dominio.

## Ver la web en local

```bash
python3 -m http.server 4175
```

Después abre http://localhost:4175. No funciona abriendo el archivo directamente, porque los parciales se cargan con `fetch`.

## Añadir un artículo al Diario de viaje

1. Añade una entrada en `diario-de-viaje/articulos.json` con `slug`, `categoria`, `fecha`, `imagen`, `titulo`, `titulo_seo` (60 caracteres como máximo), `resumen` y, si el resumen supera los 160 caracteres, `descripcion`.
2. Escribe el cuerpo en `BODY['<slug>']` dentro de `_generador/articulos.py` y ejecuta `python3 articulos.py` desde `_generador/`.
3. Añade la URL a `sitemap.xml`.

Las categorías disponibles son `destinos`, `antes-de-ir`, `historias`, `trabajo` y `novedades`. Los artículos de novedades se escriben en presente y no fechan las iniciativas.

Aviso: los scripts de `_generador/` sobrescriben las páginas que generan. `index.html` y `diario-de-viaje/index.html` se editan a mano.

## Pendiente antes de publicar

- **Formularios**: rellenar las claves de EmailJS en `assets/formularios.js`. Mientras estén vacías, el formulario abre el programa de correo del usuario con la consulta ya redactada para gestion@viajesparque.com.
- **Aviso legal**: datos del Registro Mercantil y número de inscripción como agencia de viajes en el Registro General Turístico de Canarias (aparecen resaltados en amarillo).
- **Privacidad**: confirmar el correo lopd-rgpd@viajesparque.com y la lista de encargados del tratamiento.
- **Cookies**: la web no instala cookies. Si se añade analítica, hay que dar de alta el sitio en Biscotti, poner el ID en `BISCOTTI_WEBSITE_ID` (en `assets/site-common.js`) y actualizar la política de cookies.
- **DNS**: el dominio está ahora en IONOS (con el correo en `mx00/mx01.ionos.es`). Para apuntarlo a GitHub Pages solo hay que cambiar los registros A/AAAA del apex y el CNAME de `www`. Los MX no se tocan.

## Imágenes

Las fotos de `img/fotos/` y los logotipos proceden de la web anterior de Viajes Parque. Las de `img/destinos/` son de Wikimedia Commons con licencias CC BY / CC BY-SA. Su autoría figura en `img/destinos/creditos.json` y en la página `/creditos/`, que es obligatorio mantener.
