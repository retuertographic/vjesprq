import os, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://www.viajesparque.com'
FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 96 96'%3E%3Crect width='96' height='96' rx='20' fill='%230F1E3D'/%3E%3Crect x='14' y='22' width='22' height='52' rx='4' fill='%23FC5E46'/%3E%3Crect x='37' y='22' width='22' height='52' rx='4' fill='%237AF2E9'/%3E%3Crect x='60' y='22' width='22' height='52' rx='4' fill='%23FECC32'/%3E%3C/svg%3E"

ICONS = {
 'compass': '<path d="M12 22a10 10 0 1 0 0-20 10 10 0 0 0 0 20z"/><path d="M16.2 7.8l-2.1 6.3-6.3 2.1 2.1-6.3z"/>',
 'plane': '<path d="M17.8 19.2L16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"/>',
 'map': '<path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2-6-2z"/><path d="M9 4v14M15 6v14"/>',
 'chat': '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/><path d="M8.5 11h.01M12 11h.01M15.5 11h.01"/>',
 'heart': '<path d="M20.8 5.6a5.5 5.5 0 0 0-7.8 0L12 6.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 22l8.8-8.6a5.5 5.5 0 0 0 0-7.8z"/>',
 'ship': '<path d="M2 20c1.5 1 3 1 4.5 0s3-1 4.5 0 3 1 4.5 0 3-1 4.5 0"/><path d="M4 17l-1-5h18l-1 5"/><path d="M6 12V7h12v5M12 3v4"/>',
 'calendar': '<rect x="3" y="4.5" width="18" height="17" rx="2"/><path d="M16 2.5v4M8 2.5v4M3 10h18"/>',
 'receipt': '<path d="M5 2h14v20l-3-2-2 2-2-2-2 2-2-2-3 2z"/><path d="M9 7h6M9 11h6M9 15h4"/>',
 'bolt': '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
 'user': '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
 'users': '<circle cx="9" cy="8" r="3.5"/><path d="M2 20a7 7 0 0 1 14 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 13.5a7 7 0 0 1 4 6.5"/>',
 'bus': '<rect x="4" y="3" width="16" height="15" rx="3"/><path d="M4 11h16M8 21v-3M16 21v-3"/><path d="M8 14.5h.01M16 14.5h.01"/>',
 'leaf': '<path d="M11 20A7 7 0 0 1 4 13c0-6 6-10 16-10 0 10-4 16-9 17z"/><path d="M4 21c3-5 6-8 10-10"/>',
 'shield': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>',
 'pin': '<path d="M12 22s7-7 7-12a7 7 0 0 0-14 0c0 5 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>',
 'phone': '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
 'sparkle': '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 17l.7 1.8 1.8.7-1.8.7L19 22l-.7-1.8-1.8-.7 1.8-.7z"/>',
}

def icon(name, color='coral'):
    return (f'<div class="dot {color}" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg></div>')

def page(path, title, desc, body, og_image='/img/destinos/santorini.webp', og_type='website',
         scripts='', jsonld=None, noindex=False, extra_head=''):
    url = SITE + '/' + (path if path.endswith('/') or path == '' else path)
    url = url.replace('index.html', '')
    ld = ''
    for block in (jsonld or []):
        ld += '<script type="application/ld+json">\n' + json.dumps(block, ensure_ascii=False, indent=2) + '\n</script>\n'
    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
{'<meta name="robots" content="noindex">' if noindex else f'<link rel="canonical" href="{url}">'}
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Viajes Parque">
<meta property="og:locale" content="es_ES">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0F1E3D">
<link rel="icon" href="{FAVICON}">
<link rel="apple-touch-icon" href="/img/marca/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@700;800;900&family=Nunito+Sans:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
{extra_head}{ld}</head>
<body>
<a class="skip" href="#main">Saltar al contenido</a>
<div id="site-header-slot"></div>

<main id="main">
{body.strip()}
</main>

<div id="site-footer-slot"></div>
<script src="/assets/site-common.js"></script>
{scripts}
</body>
</html>
'''
    out = os.path.join(ROOT, path, 'index.html') if (path.endswith('/') and path) else os.path.join(ROOT, path or 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(html)
    print('ok', out.replace(ROOT, ''))

def breadcrumb(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u}
                                for i, (n, u) in enumerate(items)]}

def crumbs(items):
    parts = [f'<a href="{u}">{n}</a>' for n, u in items[:-1]] + [items[-1][0]]
    return '<nav class="crumbs" aria-label="Estás en">' + ' / '.join(parts) + '</nav>'

def hero(eyebrow, h1, p, img=None, alt='', crumb=None):
    media = f'<div class="ph-img"><img src="{img}" alt="{alt}"></div>' if img else ''
    return f'''<section class="page-hero{'' if img else ' simple'}">
  <div class="wrap">
    <div>
      {crumbs(crumb) if crumb else ''}
      <span class="eyebrow light">{eyebrow}</span>
      <h1>{h1}</h1>
      <p>{p}</p>
    </div>
    {media}
  </div>
</section>'''

def cta(h2='¿Hablamos de tu próximo viaje?', p='Cuéntanoslo en dos líneas y te respondemos con una propuesta pensada para ti.', extra=''):
    return f'''<section class="section tight">
  <div class="wrap">
    <div class="cta-band reveal">
      <div>
        <h2>{h2}</h2>
        <p>{p}</p>
      </div>
      <div class="btns">
        <a href="/hablamos/" class="btn">Hablamos</a>
        {extra or '<a href="tel:+34922215012" class="btn ghost">Llamar: 922 215 012</a>'}
      </div>
    </div>
  </div>
</section>'''
