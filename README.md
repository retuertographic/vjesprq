# Viajes Parque — web

Web de [Viajes Parque](https://www.viajesparque.com), agencia de viajes con oficinas en Santa Cruz de Tenerife y Tegueste. Está hecha con **Jekyll** y se publica con **GitHub Pages**: al hacer push a `main`, GitHub la compila y la sirve con el dominio que indica `CNAME`. No hace falta ningún paso de compilación manual.

## Qué es común y dónde se cambia

| Quiero cambiar… | Archivo |
|---|---|
| `<head>` (meta, fuentes, favicon, datos estructurados) | `_includes/head.html` |
| Menú de navegación | `_data/navegacion.yml` (estructura en `_includes/header.html`) |
| Pie de página | `_includes/footer.html` |
| Teléfonos, direcciones, horario, correo, NIF | `_data/agencia.yml`. Se usan en el pie, en Hablamos, en el aviso legal y en los datos estructurados |
| Cabecera azul de las páginas interiores | `_includes/hero.html`, con los textos en el `hero:` del front matter de cada página |
| Bloque naranja "¿Hablamos…?" | `_includes/cta.html` |
| Tarjetas de los tres públicos | `_includes/audiencias.html` |
| Iconos | `_data/iconos.yml` y `_includes/icono.html` |
| Destinos | `_data/destinos.yml` |
| Las seis experiencias para particulares | `_data/experiencias_particulares.yml` |
| Categorías del diario | `_data/categorias.yml` |
| Créditos de fotos | `_data/creditos.json` |
| Estilos | `assets/site.css` |

Los layouts están en `_layouts/`: `default.html` (todas las páginas), `legal.html` (textos legales) y `articulo.html` (entradas del diario).

## Cada página

Cada página es un `index.html` con un bloque de datos al principio (front matter) y su contenido propio:

```yaml
---
title: "Entre islas, sin perder el vuelo"          # H1
title_seo: "Viajes corporativos entre islas Canarias"  # <title> (se añade " | Viajes Parque")
miga: "Empresas"                                    # nombre en las migas de pan
description: "…"                                    # meta descripción (≤ 160 caracteres)
image: /img/fotos/viaje-negocios.webp               # imagen al compartir
migas:                                              # secciones padre
  - titulo: "Experiencias"
    url: /experiencias/
hero:
  eyebrow: "Experiencias · Empresas"
  texto: "…"
  imagen: /img/fotos/viaje-negocios.webp
  alt: "…"
---
```

Las URLs de la web anterior redirigen con `redirect_from:` (plugin `jekyll-redirect-from`), y el `sitemap.xml` se genera solo (plugin `jekyll-sitemap`).

## Publicar un artículo en el Diario de viaje

Crea un archivo en `_posts/` con el nombre `AAAA-MM-DD-slug-del-articulo.md`:

```markdown
---
title: "Título largo que aparece como H1"
title_seo: "Título corto para Google (≤ 55 caracteres)"
description: "Meta descripción, ≤ 160 caracteres."
resumen: "Entradilla que aparece en la tarjeta y bajo el título."
categoria: antes-de-ir        # destinos | antes-de-ir | historias | trabajo | novedades
minutos: 5
image: /img/fotos/hotel.webp
---

Texto en **Markdown**. Para un recuadro destacado:

Texto del recuadro.
{: .callout}
```

El artículo aparece automáticamente en el diario, en la portada, en "Sigue leyendo" y en el sitemap. Jekyll no publica artículos con fecha u hora futuras. Los de la categoría "novedades" se escriben en presente y no fechan las iniciativas.

## Ver la web en local

Requiere Ruby de Homebrew (`brew install ruby`) y, la primera vez, `bundle install`.

```bash
sh herramientas/servir.sh
```

Abre http://localhost:4000, que se recarga sola al guardar. `sh herramientas/servir.sh build` solo compila en `_site/`.

GitHub Pages usa Jekyll 3.9, que no es compatible con Ruby 3.2 o superior. `herramientas/servir.sh` carga una pequeña capa de compatibilidad (`herramientas/ruby-compat.rb`) solo en local. GitHub no la necesita.

## Pendiente antes de publicar

- **Formularios**: rellenar las claves de EmailJS en `assets/formularios.js`. Mientras estén vacías, el formulario abre el programa de correo del usuario con la consulta ya redactada.
- **Aviso legal**: datos del Registro Mercantil y número de inscripción como agencia de viajes en el Registro General Turístico de Canarias (resaltados en amarillo).
- **Privacidad**: confirmar el correo `email_rgpd` de `_data/agencia.yml` y la lista de encargados del tratamiento.
- **Cookies**: la web no instala cookies. Si se añade analítica, hay que dar de alta el sitio en Biscotti, poner el ID en `BISCOTTI_WEBSITE_ID` (en `assets/site-common.js`) y actualizar la política de cookies.
- **DNS**: el dominio está ahora en IONOS (con el correo en `mx00/mx01.ionos.es`). Para apuntarlo a GitHub Pages solo hay que cambiar los registros A/AAAA del apex y el CNAME de `www`. Los MX no se tocan.

## Imágenes

Las fotos de `img/fotos/` y los logotipos proceden de la web anterior de Viajes Parque. Las de `img/destinos/` son de Wikimedia Commons con licencias CC BY / CC BY-SA, y su autoría figura en `/creditos/`, que es obligatorio mantener.
