# Yurumí a la mano

Caja de herramientas de gestión ambiental con los proyectos de campo de la RNSC Yurumí (Puerto López, Meta).
Grupo de gestión ambiental, ecosistemas terrestres y biología tropical · 2026-2.

Sitio publicado: https://yurumi-a-la-mano.github.io

## Cómo está organizado

- La raíz del repositorio es el sitio publicado (páginas HTML, `estilos.css`, `sitio.js`).
- `recursos/`: fotos, imágenes de las fichas y PDF originales.
- `_fuente/`: el generador del sitio. Todo el contenido está en `_fuente/contenido.py`; las páginas se vuelven a crear con `python3 build.py` y se copian a la raíz. GitHub Pages no publica esta carpeta.

Contenido bajo licencia CC BY 4.0.
