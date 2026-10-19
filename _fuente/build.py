# -*- coding: utf-8 -*-
"""
Genera el sitio estático a partir de contenido.py y la carpeta ./recursos.

Uso:
    python3 build.py                 -> versión final (salida en ./sitio)
    python3 build.py --vista-previa  -> versión para la vista previa en Claude (./vista-previa)

Diferencias de la vista previa: la página de inicio se escribe sin el esqueleto
<html>/<head>/<body> (el visor lo agrega) y los videos se muestran como enlace
a YouTube en vez de reproducirse dentro de la página.
"""
import hashlib
import html
import shutil
import sys
from pathlib import Path

from contenido import SITIO, PROYECTOS, FICHAS, NOTAS, FOCO_FOTOS

VISTA_PREVIA = "--vista-previa" in sys.argv
BASE = Path(__file__).parent
# Las fotos, fichas y PDF viven en ./recursos (o en ../recursos dentro del repositorio)
RECURSOS = BASE / "recursos" if (BASE / "recursos").exists() else BASE.parent / "recursos"
SALIDA = BASE / ("vista-previa" if VISTA_PREVIA else "sitio")

FUENTES = (
    "https://fonts.googleapis.com/css2?"
    "family=Archivo:wdth,wght@62..125,400..800&"
    "family=IBM+Plex+Mono:wght@400;500&"
    "family=Source+Serif+4:ital,opsz,wght@0,8..60,400..700;1,8..60,400..600&display=swap"
)

# Huella de estilos y script: cambia cuando se editan, para que el navegador no use copias viejas.
VERSION = hashlib.sha1(
    (BASE / "estilos.css").read_bytes() + (BASE / "sitio.js").read_bytes()
).hexdigest()[:8]

P_POR_ID = {p["id"]: p for p in PROYECTOS}
F_POR_SLUG = {f["slug"]: f for f in FICHAS}
N_POR_SLUG = {n["slug"]: n for n in NOTAS}
LISTOS = [p for p in PROYECTOS if p["estado"] != "preparacion"]

# En qué proyectos aparece cada ficha (una ficha puede estar en varios)
PROYECTOS_DE_FICHA = {f["slug"]: [] for f in FICHAS}
for p in LISTOS:
    for s in p["fichas"]:
        PROYECTOS_DE_FICHA[s].append(p)

esc = html.escape


# ---------------------------------------------------------------------------
# Piezas comunes
# ---------------------------------------------------------------------------
def documento(titulo, cuerpo, pre, activo="", es_inicio=False):
    titulo_completo = f"{titulo} · {SITIO['nombre']}" if titulo else SITIO["nombre"]
    cabeza = (
        f"<title>{esc(titulo_completo)}</title>\n"
        '<meta name="claude:viewport-fit-sides" content="cover">\n'
        f'<meta name="description" content="{esc(SITIO["subtitulo"])}: {esc(SITIO["lugar"])}">\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        f'<link rel="stylesheet" href="{FUENTES}">\n'
        f'<link rel="stylesheet" href="{pre}estilos.css?v={VERSION}">\n'
    )
    contenido = (
        f"{banda_borrador()}{encabezado(pre, activo)}"
        f'<main id="contenido">{cuerpo}</main>{pie(pre)}'
        f'<script src="{pre}sitio.js?v={VERSION}"></script>\n'
    )
    if VISTA_PREVIA and es_inicio:
        return cabeza + contenido
    return (
        '<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        f"{cabeza}</head>\n<body>\n{contenido}</body>\n</html>\n"
    )


def banda_borrador():
    if not SITIO.get("borrador"):
        return ""
    return (
        '<div class="borrador"><div class="envoltura">'
        "<strong>Borrador.</strong> Faltan proyectos, videos y notas científicas; se irán agregando."
        "</div></div>"
    )


def encabezado(pre, activo):
    enlaces = [
        ("proyectos", f"{pre}index.html#proyectos", "Proyectos"),
        ("fichas", f"{pre}fichas/index.html", "Fichas"),
        ("notas", f"{pre}notas/index.html", "Notas científicas"),
        ("acerca", f"{pre}acerca.html", "Acerca de"),
    ]
    nav = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if k == activo else ""}>{t}</a>'
        for k, h, t in enlaces
    )
    return (
        '<header class="cabecera"><div class="envoltura cabecera__fila">'
        f'<a class="marca" href="{pre}index.html">'
        '<span class="marca__sello" aria-hidden="true"></span>'
        f'<span class="marca__texto">{esc(SITIO["nombre"])}<small>{esc(SITIO["subtitulo"])}</small></span></a>'
        f'<nav class="nav" aria-label="Principal">{nav}</nav>'
        "</div></header>"
    )


def pie(pre):
    return (
        '<footer class="pie"><div class="envoltura pie__fila">'
        f'<p><strong>{esc(SITIO["nombre"])}</strong> · {esc(SITIO["subtitulo"])}<br>'
        f'{esc(SITIO["creditos"])} · {SITIO["periodo"].replace("-", "&#8209;")}<br>{esc(SITIO["lugar"])}</p>'
        f'<p>Contenido bajo licencia {esc(SITIO["licencia"])}: puede usarse y adaptarse citando la fuente. '
        f'<a href="{pre}acerca.html#licencia">Cómo citar</a></p>'
        "</div></footer>"
    )


def migas(pre, *pasos):
    items = [f'<a href="{pre}index.html">Inicio</a>']
    for texto, href in pasos:
        items.append(f'<a href="{href}">{esc(texto)}</a>' if href else f'<span aria-current="page">{esc(texto)}</span>')
    return f'<nav class="migas" aria-label="Ruta">{"<span aria-hidden=\"true\">/</span>".join(items)}</nav>'


def foto(pre, num, alt, leyenda=None, clase=""):
    cap = f"<figcaption>{esc(leyenda)}</figcaption>" if leyenda else ""
    return (
        f'<figure class="foto {clase}"><div class="foto__marco">'
        f'<img src="{pre}recursos/fotos/{num}.jpg" alt="{esc(alt)}"{foco(num)} loading="lazy" decoding="async"></div>{cap}</figure>'
    )


def foco(num):
    return f' style="object-position: {FOCO_FOTOS[num]}"' if num in FOCO_FOTOS else ""


def lista_def(pares, clase="datos"):
    filas = "".join(f"<div><dt>{esc(k)}</dt><dd>{v}</dd></div>" for k, v in pares)
    return f'<dl class="{clase}">{filas}</dl>'


def nombre_organismo(f):
    n = f'<em>{esc(f["organismo"])}</em>' if f.get("cientifico") else esc(f["organismo"])
    if f.get("comun"):
        n = f'{esc(f["comun"])} · {n}'
    return n


def tipo_ficha(f):
    return "Ficha de especie" if f["tipo"] == "especie" else "Ficha de ecosistema"


def chip(texto, estado):
    return f'<span class="chip chip--{estado}">{esc(texto)}</span>'


def estado_proyecto(p):
    n_fichas = len(p["fichas"])
    return "".join([
        chip("Video", "si" if p.get("video") else "no"),
        chip(f"Fichas {n_fichas}/3", "si" if n_fichas >= 3 else "parcial"),
        chip("Nota", "si" if p.get("nota") else "no"),
    ])


# ---------------------------------------------------------------------------
# Tarjetas
# ---------------------------------------------------------------------------
def tarjeta_proyecto(p, pre):
    if p["estado"] == "preparacion":
        return (
            '<li class="pt pt--pendiente"><div class="pt__vacio" aria-hidden="true"></div><div class="pt__cuerpo">'
            f'<p class="pt__codigo">{p["codigo"]}</p>'
            f'<h3 class="pt__titulo">{esc(p["titulo"])}</h3>'
            '<p class="pt__lugar pt__lugar--mono">En preparación</p></div></li>'
        )
    sub = f'<p class="pt__lugar">{esc(p["subtitulo"])}</p>' if p.get("subtitulo") else ""
    estado = f'<p class="pt__estado">{estado_proyecto(p)}</p>' if SITIO.get("borrador") else ""
    return (
        f'<li class="pt"><a class="pt__enlace" href="{pre}proyectos/{p["id"]}.html">'
        f'{foto(pre, p["foto"], p["foto_texto"], clase="foto--tarjeta")}'
        '<div class="pt__cuerpo">'
        f'<p class="pt__codigo">{p["codigo"]} <span>· {esc(p["ecosistema"])}</span></p>'
        f'<h3 class="pt__titulo">{esc(p["titulo"])}</h3>{sub}{estado}'
        "</div></a></li>"
    )


def tarjeta_ficha(f, pre, mostrar_proyecto=True):
    proyectos = ""
    if mostrar_proyecto:
        proyectos = f'<span class="mt__proy">{" · ".join(p["codigo"] for p in PROYECTOS_DE_FICHA[f["slug"]])}</span>'
    return (
        f'<li class="mt" data-tipo="{f["tipo"]}"><a href="{pre}fichas/{f["slug"]}.html">'
        f'<div class="mt__foto"><img src="{pre}recursos/fotos/{f["img"]}.jpg" alt=""{foco(f["img"])} loading="lazy" decoding="async"></div>'
        '<div class="mt__cuerpo">'
        f'<p class="mt__tipo">{tipo_ficha(f)}{proyectos}</p>'
        f'<h3 class="mt__titulo">{esc(f["titulo"])}</h3>'
        f'<p class="mt__cient">{nombre_organismo(f)}</p>'
        f'<div class="mt__pie"><span class="mt__ir">Ver ficha →</span></div>'
        "</div></a></li>"
    )


def tarjeta_pendiente(tipo, detalle):
    return (
        '<li class="mt mt--pendiente"><div class="mt__cuerpo">'
        f'<p class="mt__tipo">{esc(tipo)}</p>'
        f'<h3 class="mt__titulo">Pendiente</h3><p class="mt__cient">{esc(detalle)}</p>'
        "</div></li>"
    )


def tarjeta_nota(n, pre, mostrar_proyecto=True):
    p = P_POR_ID[n["proyecto"]]
    proyecto = f'<span class="mt__proy">{p["codigo"]}</span>' if mostrar_proyecto else ""
    return (
        f'<li class="mt mt--nota"><a href="{pre}notas/{n["slug"]}.html"><div class="mt__cuerpo">'
        f'<p class="mt__tipo">Nota científica{proyecto}</p>'
        f'<h3 class="mt__titulo mt__titulo--serif">{esc(n["titulo"])}</h3>'
        f'<p class="mt__cient">{esc(", ".join(n["autores"]))} ({n["anio"]})</p>'
        f'<div class="mt__pie"><span class="mt__ir">Leer nota →</span></div>'
        "</div></a></li>"
    )


# ---------------------------------------------------------------------------
# Páginas
# ---------------------------------------------------------------------------
def pagina_inicio():
    pre = ""
    tarjetas = "".join(tarjeta_proyecto(p, pre) for p in PROYECTOS)
    n_videos = sum(1 for p in LISTOS if p.get("video"))
    n_fichas = sum(len(p["fichas"]) for p in LISTOS)
    n_notas = sum(1 for p in LISTOS if p.get("nota"))
    if SITIO.get("borrador"):
        filas = [
            (len(LISTOS), 8, "proyectos de campo"), (n_videos, 8, "videos explicativos"),
            (n_fichas, 24, "fichas (especies y ecosistemas)"), (n_notas, 8, "notas científicas"),
        ]
        items = "".join(f"<li><b>{a}<small>/{b}</small></b><span>{t}</span></li>" for a, b, t in filas)
        titulo_inv = "Avance de la caja"
    else:
        items = "".join(f"<li><b>{a}</b><span>{t}</span></li>" for a, t in [
            (8, "proyectos de campo"), (8, "videos explicativos"), (16, "fichas de especies"),
            (8, "fichas de ecosistemas"), (8, "notas científicas")])
        titulo_inv = "Contenido de la caja"
    cuerpo = f"""
<section class="portada"><div class="envoltura portada__fila">
  <div class="portada__texto">
    <p class="antetitulo">{esc(SITIO["subtitulo"])} · {esc(SITIO["periodo"])}</p>
    <h1>{esc(SITIO["nombre"])}</h1>
    <p class="portada__bajada">{esc(SITIO["bajada"])}</p>
    <div class="portada__acciones">
      <a class="boton" href="#proyectos">Ver los proyectos</a>
      <a class="boton boton--sec" href="fichas/index.html">Buscar una especie</a>
    </div>
  </div>
  <aside class="inventario" aria-label="{titulo_inv}">
    <p class="inventario__titulo">{titulo_inv}</p>
    <ul>{items}</ul>
  </aside>
</div></section>

<section class="seccion" id="proyectos"><div class="envoltura">
  <div class="seccion__cabeza">
    <h2>Proyectos de campo</h2>
    <p>Cada proyecto reúne su video, sus fichas y su nota científica.</p>
  </div>
  <ul class="rejilla-proyectos">{tarjetas}</ul>
</div></section>

<section class="seccion seccion--suave"><div class="envoltura">
  <div class="seccion__cabeza"><h2>Cómo usar la caja</h2></div>
  <div class="usos">
    <div><h3>Para conocer un ecosistema</h3><p>Entra a un proyecto, mira el video y luego lee la ficha del ecosistema y las de sus especies.</p></div>
    <div><h3>Para buscar una especie</h3><p>En <a href="fichas/index.html">Fichas</a> están todas las especies y ecosistemas, sin importar el proyecto.</p></div>
    <div><h3>Para tu visita a Yurumí</h3><p>Cada ficha trae una actividad en «Qué puedes hacer» para hacer durante la caminata.</p></div>
  </div>
</div></section>
"""
    return documento("", cuerpo, pre, "proyectos", es_inicio=True)


def bloque_video(p):
    v = p.get("video")
    if not v:
        return (
            '<div class="video video--vacio video--vertical"><span class="video__play video__play--apagado" aria-hidden="true"></span>'
            '<span class="video__texto">Video en preparación</span></div>'
        )
    vid = esc(v["id"])
    clase = "video--vertical" if v.get("short") else ""
    if not VISTA_PREVIA:
        return (
            f'<div class="video {clase}"><iframe src="https://www.youtube-nocookie.com/embed/{vid}" '
            f'title="Video: {esc(p["titulo"])}" loading="lazy" '
            'allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>'
        )
    url = f"https://www.youtube.com/shorts/{vid}" if v.get("short") else f"https://www.youtube.com/watch?v={vid}"
    return (
        f'<a class="video video--vacio {clase}" href="{url}" target="_blank" rel="noopener">'
        '<span class="video__play" aria-hidden="true"></span>'
        '<span class="video__texto">Ver el video en YouTube<small>En el sitio final se reproduce aquí</small></span></a>'
    )


def pagina_proyecto(p):
    pre = "../"
    fichas = [F_POR_SLUG[s] for s in p["fichas"]]
    eco = [f for f in fichas if f["tipo"] == "ecosistema"]
    esp = [f for f in fichas if f["tipo"] == "especie"]
    materiales = "".join(tarjeta_ficha(f, pre, False) for f in eco)
    if not eco:
        materiales += tarjeta_pendiente("Ficha de ecosistema", "Aún no está en la carpeta")
    materiales += "".join(tarjeta_ficha(f, pre, False) for f in esp)
    for _ in range(2 - len(esp)):
        materiales += tarjeta_pendiente("Ficha de especie", "Aún no está en la carpeta")
    if p.get("nota"):
        materiales += tarjeta_nota(N_POR_SLUG[p["nota"]], pre, False)
    else:
        materiales += tarjeta_pendiente("Nota científica", "Aún no está en la carpeta")

    sub = f'<p class="pagina__bajada">{esc(p["subtitulo"])}</p>' if p.get("subtitulo") else ""
    campo = lista_def([
        ("Lugar", esc(SITIO["lugar"])), ("Ecosistema", esc(p["ecosistema"])),
        ("Video", "Disponible" if p.get("video") else "Pendiente"),
        ("Nota científica", "Disponible" if p.get("nota") else "Pendiente"),
    ], "datos datos--campo")
    cuerpo = f"""
<div class="envoltura pagina">
  {migas(pre, ("Proyectos", pre + "index.html#proyectos"), (p["codigo"], None))}
  <header class="pagina__cabeza">
    <p class="antetitulo">Proyecto de campo {p["codigo"]}</p>
    <h1>{esc(p["titulo"])}</h1>
    {sub}
    {campo}
  </header>
  <div class="proyecto">
    {bloque_video(p)}
    <div class="proyecto__texto">
      {foto(pre, p["foto"], p["foto_texto"], p["foto_texto"], "foto--ancha")}
      <section class="prosa">
        <h2>Resumen</h2>
        <p class="texto-pendiente">El resumen del proyecto se agregará cuando el equipo lo envíe.</p>
      </section>
    </div>
  </div>
  <section class="seccion seccion--interna">
    <div class="seccion__cabeza"><h2>Materiales del proyecto</h2>
      <p>Una ficha del ecosistema, dos fichas de especies y la nota científica con los resultados.</p></div>
    <ul class="rejilla-materiales">{materiales}</ul>
  </section>
  <p class="equipo"><span>Créditos</span> {esc(SITIO["creditos"])} · {esc(SITIO["periodo"])}</p>
</div>
"""
    return documento(f'{p["codigo"]} {p["titulo"]}', cuerpo, pre, "proyectos")


def pagina_ficha(f):
    pre = "../"
    proyectos = PROYECTOS_DE_FICHA[f["slug"]]
    enlaces_proy = "".join(
        f'<li><a href="{pre}proyectos/{p["id"]}.html"><span>{p["codigo"]}</span> {esc(p["titulo"])}</a></li>'
        for p in proyectos
    )
    cifra = f'<p class="dato-clave__cifra">{esc(f["cifra"])}</p>' if f.get("cifra") else ""
    estado = ""
    if f.get("estado"):
        titulo_estado = "Estado de conservación" if f["tipo"] == "especie" else "Presiones"
        estado = f'<div class="nota-lateral"><p class="etiqueta__titulo">{titulo_estado}</p><p>{esc(f["estado"])}</p></div>'
    cuerpo = f"""
<div class="envoltura pagina">
  {migas(pre, ("Fichas", pre + "fichas/index.html"), (f["organismo"], None))}
  <div class="ficha">
    <header class="ficha__cabeza">
      <p class="antetitulo">{tipo_ficha(f)} · {esc(SITIO["nombre"])}</p>
      <h1>{esc(f["titulo"])}</h1>
      <p class="ficha__cient">{nombre_organismo(f)}</p>
    </header>
    <aside class="ficha__lateral">
      <div class="etiqueta">
        <div class="etiqueta__bloque">
          <p class="etiqueta__titulo">Ficha original</p>
          <a class="ficha-original" href="{pre}recursos/pdf/{f["slug"]}.pdf" target="_blank" rel="noopener">
            <img src="{pre}recursos/fichas/{f["img"]}.jpg" alt="Ficha original en PDF: {esc(f["titulo"])}" loading="lazy"></a>
          <a class="boton boton--sec boton--bloque" href="{pre}recursos/pdf/{f["slug"]}.pdf" target="_blank" rel="noopener">Abrir PDF</a>
        </div>
        <div class="etiqueta__bloque">
          <p class="etiqueta__titulo">Aparece en</p>
          <ul class="lista-proyectos">{enlaces_proy}</ul>
        </div>
      </div>
    </aside>
    <article class="ficha__texto">
      {foto(pre, f["img"], f["leyenda"], f["leyenda"], "foto--ancha")}
      <div class="prosa prosa--serif">
        <p class="etiqueta__titulo">La pregunta</p>
        <h2 class="pregunta">{esc(f["pregunta"])}</h2>
        <p>{f["respuesta"]}</p>
      </div>
      <div class="dato-clave"><p class="dato-clave__titulo">Un dato clave</p>{cifra}<p>{esc(f["dato"])}</p></div>
      {estado}
      <div class="hacer"><p class="etiqueta__titulo">Qué puedes hacer</p><p>{esc(f["hacer"])}</p></div>
    </article>
  </div>
</div>
"""
    return documento(f["titulo"], cuerpo, pre, "fichas")


def pagina_indice_fichas():
    pre = "../"
    ordenadas = sorted(FICHAS, key=lambda f: (f["tipo"] != "ecosistema", min(p["codigo"] for p in PROYECTOS_DE_FICHA[f["slug"]])))
    tarjetas = "".join(tarjeta_ficha(f, pre) for f in ordenadas)
    n_esp = sum(1 for f in FICHAS if f["tipo"] == "especie")
    n_eco = len(FICHAS) - n_esp
    cuerpo = f"""
<div class="envoltura pagina">
  {migas(pre, ("Fichas", None))}
  <header class="pagina__cabeza">
    <h1>Fichas</h1>
    <p class="pagina__bajada">Todas las especies y ecosistemas de {esc(SITIO["nombre"])}. Cada ficha indica en qué proyecto se estudió y trae su versión original en PDF.</p>
  </header>
  <div class="filtros" role="group" aria-label="Filtrar fichas">
    <button type="button" class="filtro" data-filtro="todas" aria-pressed="true">Todas <span>{len(FICHAS)}</span></button>
    <button type="button" class="filtro" data-filtro="especie" aria-pressed="false">Especies <span>{n_esp}</span></button>
    <button type="button" class="filtro" data-filtro="ecosistema" aria-pressed="false">Ecosistemas <span>{n_eco}</span></button>
  </div>
  <ul class="rejilla-materiales" id="lista-fichas">{tarjetas}</ul>
  <p class="aviso-vacio">Las fichas que faltan aparecerán a medida que se completen los proyectos.</p>
</div>
"""
    return documento("Fichas", cuerpo, pre, "fichas")


def pagina_indice_notas():
    pre = "../"
    if NOTAS:
        contenido = f'<ul class="rejilla-materiales rejilla-materiales--notas">{"".join(tarjeta_nota(n, pre) for n in NOTAS)}</ul>'
    else:
        contenido = (
            '<div class="vacio"><p class="vacio__titulo">Todavía no hay notas publicadas</p>'
            "<p>Cada proyecto tendrá su nota científica con los resultados del trabajo de campo y su referencia lista para citar. "
            "Aparecerán aquí a medida que los equipos las entreguen.</p></div>"
        )
    cuerpo = f"""
<div class="envoltura pagina">
  {migas(pre, ("Notas científicas", None))}
  <header class="pagina__cabeza">
    <h1>Notas científicas</h1>
    <p class="pagina__bajada">Los resultados de cada proyecto de campo, escritos en formato de nota corta.</p>
  </header>
  {contenido}
</div>
"""
    return documento("Notas científicas", cuerpo, pre, "notas")


def pagina_acerca():
    pre = ""
    cita = f'{SITIO["creditos"]} ({SITIO["periodo"][:4]}). {SITIO["nombre"]}: {SITIO["subtitulo"].lower()}. {SITIO["lugar"]}.'
    cuerpo = f"""
<div class="envoltura pagina">
  {migas(pre, ("Acerca de", None))}
  <header class="pagina__cabeza"><h1>Acerca de {esc(SITIO["nombre"])}</h1></header>
  <div class="prosa acerca">
    <p class="entradilla">{esc(SITIO["nombre"])} es una caja de herramientas de gestión ambiental construida a partir de proyectos de campo en la Reserva Natural de la Sociedad Civil Yurumí, en Puerto López (Meta).</p>
    <h2>Para qué sirve</h2>
    <p>Está pensada para visitantes de la reserva, docentes, estudiantes, gestores ambientales y comunidades que quieran conocer sus ecosistemas, replicar un monitoreo sencillo o apoyar decisiones de manejo con datos de campo.</p>
    <h2>Quién la hizo</h2>
    <p>{esc(SITIO["creditos"])}, periodo {esc(SITIO["periodo"])}. Los créditos de las fotografías aparecen en cada ficha.</p>
    <h2 id="licencia">Licencia y cómo citar</h2>
    <p>Todo el contenido se publica bajo la licencia Creative Commons Atribución 4.0 Internacional ({esc(SITIO["licencia"])}). Puedes copiarlo, adaptarlo y compartirlo, siempre que cites la fuente.</p>
    <div class="cita">
      <p class="etiqueta__titulo">Cómo citar la caja completa</p>
      <p class="cita__texto" id="cita-caja">{esc(cita)}</p>
      <div class="cita__acciones"><button type="button" class="boton boton--sec" data-copiar="cita-caja">Copiar referencia</button></div>
    </div>
  </div>
</div>
"""
    return documento("Acerca de", cuerpo, pre, "acerca")


# ---------------------------------------------------------------------------
def escribir(ruta, texto):
    destino = SALIDA / ruta
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(texto, encoding="utf-8")


def main():
    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    SALIDA.mkdir()
    shutil.copy(BASE / "estilos.css", SALIDA / "estilos.css")
    shutil.copy(BASE / "sitio.js", SALIDA / "sitio.js")
    shutil.copytree(RECURSOS, SALIDA / "recursos")
    escribir("index.html", pagina_inicio())
    escribir("acerca.html", pagina_acerca())
    escribir("fichas/index.html", pagina_indice_fichas())
    escribir("notas/index.html", pagina_indice_notas())
    for p in LISTOS:
        escribir(f"proyectos/{p['id']}.html", pagina_proyecto(p))
    for f in FICHAS:
        escribir(f"fichas/{f['slug']}.html", pagina_ficha(f))
    archivos = sorted(str(x.relative_to(SALIDA)) for x in SALIDA.rglob("*") if x.is_file())
    print(f"Sitio generado en {SALIDA} ({len(archivos)} archivos)")


if __name__ == "__main__":
    main()
