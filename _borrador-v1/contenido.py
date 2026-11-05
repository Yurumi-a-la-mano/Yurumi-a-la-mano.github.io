# -*- coding: utf-8 -*-
"""
Contenido de Yurumí a la mano.

Todo lo que aparece en el sitio sale de este archivo. Las fichas se transcriben
desde los PDF del curso (carpeta "Yurimi a la mano"); los PDF originales, las
fotos y la imagen de cada ficha están en ./recursos.
"""

SITIO = {
    "nombre": "Yurumí a la mano",
    "subtitulo": "Caja de herramientas de gestión ambiental",
    "bajada": (
        "Ocho proyectos de campo en la Reserva Natural de la Sociedad Civil Yurumí, "
        "en Puerto López (Meta), para conocer, medir y cuidar sus ecosistemas. "
        "Cada proyecto trae un video, fichas de sus especies y su ecosistema, y una nota científica."
    ),
    "lugar": "RNSC Yurumí, Puerto López (Meta)",
    "creditos": "Grupo de gestión ambiental, ecosistemas terrestres y biología tropical",
    "periodo": "2026-2",
    "licencia": "CC BY 4.0",
    "borrador": True,
}

# ---------------------------------------------------------------------------
# PROYECTOS
# estado: "listo" | "preparacion"
# video: id de YouTube (None si aún no hay); "short": True para videos verticales
# ---------------------------------------------------------------------------
PROYECTOS = [
    {
        "id": "p01", "codigo": "P-01", "estado": "listo",
        "titulo": "El hogar descompuesto de las termitas",
        "subtitulo": None,
        "ecosistema": "Bosque de galería",
        "foto": "02", "foto_texto": "Termita soldado de Nasutitermes corniger (Foto: Alison Pesillo)",
        "video": None,
        "fichas": ["termitas-bosque-galeria", "termitas-nasutitermes-nasus", "termitas-nasutitermes-troncos"],
        "nota": None,
    },
    {
        "id": "p02", "codigo": "P-02", "estado": "listo",
        "titulo": "Entre certezas",
        "subtitulo": "Líquenes y musgos en los árboles",
        "ecosistema": "Bosque de galería",
        "foto": "05", "foto_texto": "Octoblepharum sp. sobre corteza (Valdiri, 2026)",
        "video": {"id": "yuT1f7jNXw8", "short": True},
        "fichas": ["platanillo-bosque-galeria", "epifitos-octoblepharum"],
        "nota": None,
    },
    {
        "id": "p03", "codigo": "P-03", "estado": "listo",
        "titulo": "Entre pétalos y zumbidos",
        "subtitulo": None,
        "ecosistema": "Pastizal",
        "foto": "08", "foto_texto": "Desmocelis villosa en los pastizales de Yurumí (Foto: Alison Pesillo)",
        "video": {"id": "8t-rkZv2ihU", "short": True},
        "fichas": ["petalos-pastizal", "petalos-trigona-spinipes", "petalos-desmocelis-villosa"],
        "nota": None,
    },
    {
        "id": "p04", "codigo": "P-04", "estado": "listo",
        "titulo": "Guardianas de la orilla",
        "subtitulo": (
            "Variación morfológica, sexual y ecológica de Lycosidae como herramienta de apoyo "
            "a la gestión del recurso hídrico en la RNSC Yurumí, Puerto López, Meta"
        ),
        "ecosistema": "Bosque de galería",
        "foto": "10", "foto_texto": "Cuidado maternal en arañas de la familia Lycosidae",
        "video": {"id": "DbKizPdt6FE", "short": True},
        "fichas": ["bosque-galeria-arcoiris", "aranas-lycosidae"],
        "nota": None,
    },
    {
        "id": "p05", "codigo": "P-05", "estado": "listo",
        "titulo": "Hojas bajo la lupa",
        "subtitulo": (
            "Relación entre rasgos funcionales y herbivoría para identificar especies vegetales "
            "potencialmente resistentes al daño foliar en la RNSC Yurumí, Puerto López, Meta"
        ),
        "ecosistema": "Bosque de galería",
        "foto": "11", "foto_texto": "Oruga de la familia Geometridae alimentándose de una hoja",
        "video": None,
        "fichas": ["bosque-galeria-arcoiris", "hojas-geometridae"],
        "nota": None,
    },
    {
        "id": "p06", "codigo": "P-06", "estado": "listo",
        "titulo": "Un recurso entre parches",
        "subtitulo": "Distribución del platanillo y su importancia potencial para los monos maiceros",
        "ecosistema": "Bosque de galería",
        "foto": "12", "foto_texto": "Sapajus apella alimentándose de platanillo (Pulido, 2026)",
        "video": None,
        "fichas": ["platanillo-bosque-galeria", "platanillo-sapajus-apella", "platanillo-phenakospermum"],
        "nota": None,
    },
    {
        "id": "p07", "codigo": "P-07", "estado": "listo",
        "titulo": "La hoja que nadie se comió",
        "subtitulo": None,
        "ecosistema": None,
        "foto": None, "foto_texto": None,
        "video": {"id": "oWcEV79uiY4", "short": True},
        "fichas": [],
        "nota": None,
    },
    {
        "id": "p08", "codigo": "P-08", "estado": "listo",
        "titulo": "Todo empieza con una hoja",
        "subtitulo": "¿Quién se come a quién bajo el agua?",
        "ecosistema": None,
        "foto": None, "foto_texto": None,
        "video": {"id": "9RMvCWEwPJY", "short": True},
        "fichas": [],
        "nota": None,
    },
]

# ---------------------------------------------------------------------------
# FICHAS
# tipo: "especie" | "ecosistema"
# organismo: nombre del organismo o ecosistema; cientifico: True si va en cursiva
# cifra: número destacado del "dato clave" (opcional)
# img: número de la foto y de la imagen de la ficha en ./recursos
# ---------------------------------------------------------------------------
FICHAS = [
    {
        "slug": "termitas-bosque-galeria", "tipo": "ecosistema", "img": "01",
        "titulo": "El refugio de la biodiversidad",
        "organismo": "Bosque de galería", "cientifico": False,
        "leyenda": "Bosque de galería, RNSC Yurumí. Foto: Mariana Soto",
        "pregunta": "¿Por qué las plantas en este bosque son tan abundantes?",
        "respuesta": "Este bosque solo podrás encontrarlo cerca de ríos y lagos, lo que favorece suelos más fértiles. ¡Viven cerca del supermercado más grande del mundo!",
        "dato": "El bosque de galería conecta hábitats, abarca una gran cantidad de especies y protege las fuentes de agua.",
        "hacer": "No dañes las plantas ni contamines el agua: es el hogar de muchos seres vivos que quieren seguir viviendo allí.",
    },
    {
        "slug": "termitas-nasutitermes-nasus", "tipo": "especie", "img": "02",
        "titulo": "Hasta el ser más diminuto es extraordinariamente complejo",
        "organismo": "Nasutitermes corniger", "cientifico": True, "comun": "Termita",
        "leyenda": "Nasutitermes corniger, RNSC Yurumí. Foto: Alison Pesillo",
        "pregunta": "¿Para qué sirve el “pico” de la termita?",
        "respuesta": "El “pico” de la termita se llama nasus; le sirve para defenderse ante una amenaza, pues expulsa una sustancia corrosiva para sus enemigos. Si llevas un gas pimienta para defenderte en las calles, ¡estás imitando a una termita!",
        "dato": "El nasus está presente solo en las termitas soldado, que deben defender la colonia de las hormigas.",
        "hacer": "La sustancia que producen para defenderse no es dañina para el ser humano. ¡No te asustes ni la mates! No te puede hacer ningún daño.",
    },
    {
        "slug": "termitas-nasutitermes-troncos", "tipo": "especie", "img": "03",
        "titulo": "Termitas en su hogar: troncos en estado de descomposición",
        "organismo": "Nasutitermes corniger", "cientifico": True, "comun": "Termita",
        "leyenda": "Nasutitermes corniger, RNSC Yurumí. Foto: Alison Pesillo",
        "pregunta": "¿Por qué las termitas viven sobre troncos medianamente descompuestos?",
        "respuesta": "Dentro de estos troncos encuentran alimento, refugio y las condiciones que necesitan para sobrevivir. Para ellas es como la casa a la que llegan tras un largo día de trabajo, donde encuentran a su familia y todas las comodidades de un hogar.",
        "dato": "Al alimentarse de estos troncos devuelven sus nutrientes al suelo, donde pueden ser usados por otros organismos.",
        "hacer": "Si ves un árbol en descomposición, ¡no lo destruyas! Las termitas y el ecosistema te lo agradecerán.",
    },
    {
        "slug": "platanillo-bosque-galeria", "tipo": "ecosistema", "img": "04",
        "titulo": "Bosque de galería: trama de vida",
        "organismo": "Bosque de galería", "cientifico": False,
        "leyenda": "Mosaico de bosque de galería (Vega, 2026)",
        "pregunta": "¿Qué papel cumple el bosque de galería en la RNSC Yurumí?",
        "respuesta": "Son franjas de vegetación que crecen a lo largo de los ríos. En Yurumí acompañan el río Yucao, en Puerto López, Meta; protegen el cauce y ayudan a regular el caudal y la disponibilidad de agua. Unos son inundables y otros no, y conviven con sabanas, morichales y serranía.",
        "cifra": "216 ha",
        "dato": "de mata de monte y bosques de galería: el 27 % de las 800 ha de la reserva.",
        "hacer": "Anota durante tu caminata qué tan cerca del río está el bosque y cuántos niveles de vegetación distingues.",
    },
    {
        "slug": "epifitos-octoblepharum", "tipo": "especie", "img": "05",
        "titulo": "El musgo que le huye al río",
        "organismo": "Octoblepharum sp.", "cientifico": True, "comun": "Musgo",
        "leyenda": "Octoblepharum sp. sobre corteza (Valdiri, 2026)",
        "pregunta": "¿Por qué este musgo blanquecino abunda más lejos del agua?",
        "respuesta": "Este musgo crece erguido, en cojines compactos, como una esponja que se cierra sobre sí misma para no perder agua. Por eso resiste mejor la sequedad de los troncos alejados del río, donde los musgos de manto no aguantan tanto.",
        "cifra": "P = 0,036",
        "dato": "Encontramos que su cobertura aumenta mientras más lejos está del cuerpo de agua (no es azar).",
        "hacer": "Compara dos troncos, uno cerca y otro lejos del caño: si ves más de este musgo blanquecino en el más alejado, acabas de confirmar nuestro hallazgo.",
    },
    {
        "slug": "petalos-pastizal", "tipo": "ecosistema", "img": "06",
        "titulo": "¡El pasto esconde todo un mundo!",
        "organismo": "Pastizal", "cientifico": False,
        "leyenda": "Pastizales de la RNSC Yurumí. Foto: Alison Pesillo",
        "pregunta": "¿De verdad puede pasar tanto en un lugar que parece tener solamente pasto?",
        "respuesta": "En el pastizal crecen plantas de distintas formas y tamaños que sirven de alimento y refugio para muchos animales. Es como un edificio lleno de vecinos: las plantas, los insectos y otros seres vivos comparten el espacio y dependen unos de otros de distintas maneras. En nuestro estudio encontramos que dos plantas del mismo pastizal recibían cantidades diferentes de visitas.",
        "dato": "Este ecosistema ofrece alimento, refugio y lugares para vivir a muchos animales pequeños.",
        "estado": "Pastizales bajo presión por la expansión agropecuaria y la transformación del suelo.",
        "hacer": "Camina por los senderos, evita pisar las flores y no dejes basura. ¡Hasta el rincón más pequeño del pastizal puede ser importante para la vida!",
    },
    {
        "slug": "petalos-trigona-spinipes", "tipo": "especie", "img": "07",
        "titulo": "Una pequeña visitante muy trabajadora",
        "organismo": "Trigona spinipes", "cientifico": True, "comun": "Abeja",
        "leyenda": "Trigona spinipes en los pastizales de la RNSC Yurumí. Foto: Alison Pesillo",
        "pregunta": "¿Qué hace una abeja cuando se posa sobre una flor?",
        "respuesta": "Puede estar buscando alimento y, mientras se mueve entre las flores, puede llevar un polvito dorado llamado polen de una a otra. ¡Es como una repartidora que visita distintas casas y lleva un pequeño paquete que ayuda a las plantas a formar semillas! En las observaciones, <em>Trigona spinipes</em> visitó con mayor frecuencia <em>Desmocelis villosa</em> que <em>Hyptis conferta</em>.",
        "dato": "Estas abejas viven en colonias y pueden defender juntas su nido cuando detectan algún peligro.",
        "estado": "Sin categoría confirmada en la UICN. Sin categoría nacional confirmada.",
        "hacer": "Si encuentras una abeja sobre una flor, obsérvala sin tocarla. ¡Los insectos también necesitan lugares tranquilos para alimentarse!",
    },
    {
        "slug": "petalos-desmocelis-villosa", "tipo": "especie", "img": "08",
        "titulo": "Una flor que destaca entre las demás",
        "organismo": "Desmocelis villosa", "cientifico": True, "comun": "Planta con flor",
        "leyenda": "Desmocelis villosa en los pastizales de la RNSC Yurumí. Foto: Alison Pesillo",
        "pregunta": "Si hay más flores de un tipo que de otro, ¿significa que serán las favoritas de los insectos?",
        "respuesta": "<em>Desmocelis villosa</em> tiene pequeñas flores rosadas o moradas que resaltan entre la vegetación del pastizal. Sus flores pueden ofrecer alimento a los insectos, ¡como una pequeña tienda de comida en medio de un vecindario! En nuestro estudio recibió más visitas de abejas que <em>Hyptis conferta</em>, aunque había menos plantas de su tipo.",
        "dato": "La forma de sus flores y el alimento que ofrecen podrían hacerlas más atractivas para las abejas que otras plantas.",
        "estado": "Sin categoría confirmada en la UICN. Sin categoría nacional confirmada.",
        "hacer": "Observa las flores pequeñas que crecen entre el pasto. ¡No las arranques! Pueden ser una fuente de alimento para los insectos.",
    },
    {
        "slug": "bosque-galeria-arcoiris", "tipo": "ecosistema", "img": "09",
        "titulo": "El paraíso al final del arcoíris",
        "organismo": "Bosque de galería", "cientifico": False,
        "leyenda": "Bosque de galería visto desde la sabana, con un arcoíris en el cielo. RNSC Yurumí",
        "pregunta": "¿Qué hay al final del arcoíris?",
        "respuesta": "Un bosque de galería: un tipo de bosque que crece a lo largo de ríos, quebradas y otros cuerpos de agua, formando una franja de vegetación que contrasta con la vegetación que lo rodea.",
        "dato": "El IDEAM identifica en la Orinoquía al bosque de galería inundable basal como uno de los ecosistemas regionales.",
        "hacer": "Recorrerlo con botas pantaneras, hidratación y la mejor actitud.",
    },
    {
        "slug": "aranas-lycosidae", "tipo": "especie", "img": "10",
        "titulo": "El peso de una nueva generación",
        "organismo": "Lycosidae", "cientifico": False, "comun": "Araña lobo",
        "leyenda": "Cuidado maternal en arañas de la familia Lycosidae, RNSC Yurumí",
        "pregunta": "¿Cuántas crías puede cargar a la vez?",
        "respuesta": "Las arañas lobo pueden cargar aproximadamente entre 40 y más de 100 crías sobre el abdomen, aunque la cantidad varía según la especie y el tamaño de la hembra. En algunas especies se han registrado cifras cercanas a las 300.",
        "dato": "En las Lycosidae la madre no se limita a proteger los huevos: las crías recién nacidas suben a su abdomen y permanecen allí durante varios días.",
        "hacer": "¡No tener miedo! No están allí para lastimarte.",
    },
    {
        "slug": "hojas-geometridae", "tipo": "especie", "img": "11",
        "titulo": "Hojas bajo la lupa",
        "organismo": "Geometridae", "cientifico": False, "comun": "Oruga medidora",
        "leyenda": "Oruga de la familia Geometridae alimentándose de una hoja",
        "pregunta": "¿Plaga o supervivencia?",
        "respuesta": "Aunque algunas especies pueden convertirse en plagas cuando sus poblaciones aumentan y causan daños importantes a los cultivos, la mayoría forma parte de las interacciones naturales entre plantas y herbívoros.",
        "dato": "El nombre de esta oruga viene de su forma de moverse, parecida a cuando se mide a palmos: con la mano abierta y luego juntando el meñique con el pulgar.",
        "hacer": "¡Meditar sobre cómo la metamorfosis permite el paso de esta pequeña oruga a una polilla!",
    },
    {
        "slug": "platanillo-sapajus-apella", "tipo": "especie", "img": "12",
        "titulo": "El platanillo como recurso alimenticio",
        "organismo": "Sapajus apella", "cientifico": True, "comun": "Mono maicero",
        "leyenda": "Sapajus apella alimentándose de platanillo (Pulido, 2026)",
        "pregunta": "¿Qué comen los maiceros cuando no hay frutas?",
        "respuesta": "No dependen de un solo alimento: aprovechan lo que encuentran cuando escasea la comida, como la base de la hoja (pecíolo) del platanillo.",
        "cifra": "3,4 kg",
        "dato": "de restos de alimento a lo largo de los parches de platanillo: así supimos que los maiceros lo usan.",
        "hacer": "Observa a los maiceros con binoculares desde una distancia prudente y anota en tu ficha de registro qué comen.",
    },
    {
        "slug": "platanillo-phenakospermum", "tipo": "especie", "img": "13",
        "titulo": "El platanillo como recurso alimenticio",
        "organismo": "Phenakospermum guyannense", "cientifico": True, "comun": "Platanillo",
        "leyenda": "Phenakospermum guyannense en bosque de galería (Jiménez, 2026)",
        "pregunta": "¿Cómo cambia la oferta de platanillo entre parches?",
        "respuesta": "Las plantas adultas suelen tener más hojas que las jóvenes. Es como una despensa en la que algunas plantas guardan más alimento disponible, mientras las jóvenes crecen y renuevan el follaje.",
        "cifra": "41",
        "dato": "platanillos distribuidos en 7 parches.",
        "hacer": "Anota durante tu caminata cuántos platanillos ves, si están agrupados, su edad (maduros o juveniles) y si hay restos de platanillo en el suelo.",
    },
]

# ---------------------------------------------------------------------------
# NOTAS CIENTÍFICAS (aún no hay ninguna en la carpeta)
# ---------------------------------------------------------------------------
NOTAS = []

# Punto de enfoque de las fotos que se recortan mal (posición horizontal y vertical)
FOCO_FOTOS = {"10": "50% 78%"}
