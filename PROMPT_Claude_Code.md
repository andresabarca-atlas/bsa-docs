# Prompt para Claude Code — Sitio de documentación BSA 2.0

Este documento contiene los prompts, listos para copiar y pegar, que generan el sitio
de documentación del proyecto **Blue Spot Analysis 2.0** con **Claude Code en VS Code**.

---

## Cómo usar este documento

El sitio se construye en **6 fases**. Cada fase se ejecuta en una **conversación nueva
de Claude Code** para no agotar el límite de uso de una sesión de Claude Pro.

**Antes de empezar:**

1. Abrí la carpeta `BSA Documentation` en VS Code (es la carpeta de trabajo y será el
   repositorio de GitHub). Debe contener ya: `fuentes/`, `PLAN_Documentacion_BSA2.md`
   y este archivo.
2. Asegurate de tener instalado **Python 3.11+** y **git**.
3. Iniciá Claude Code en esa carpeta.

**Para cada fase:**

1. Abrí una conversación nueva en Claude Code (o usá `/clear` para limpiar el contexto).
2. Copiá el bloque de prompt de la fase (entre los marcadores `▼ COPIAR` y `▲ FIN`).
3. Pegalo y dejá que Claude Code trabaje. Hará *commits* a medida que avanza.
4. Cuando termine, revisá el resultado y pasá a la fase siguiente.

**Por qué funciona sin agotar el límite:** la Fase 0 crea un archivo `CLAUDE.md` que
Claude Code lee automáticamente en cada conversación dentro de esa carpeta. Así, las
fases 1 a 5 ya conocen el contexto del proyecto sin tener que repetirlo, y cada fase
lee solo las fuentes que necesita.

**Orden de las fases:**

| Fase | Contenido | Resultado |
|---|---|---|
| 0 | Andamiaje: repo, configuración, navegación, CI/CD | Sitio vacío que compila |
| 1 | Metodología (español) | Sección Metodología completa |
| 2 | Getting Started + Guía de Usuario (español) | 2 secciones completas |
| 3 | Inicio + Dashboard + Recursos + Glosario (español) | Sitio completo en español |
| 4 | Traducción al inglés | Sitio bilingüe |
| 5 | Revisión, build y despliegue | Sitio publicado en GitHub Pages |

---

# FASE 0 — Andamiaje del proyecto

> **▼ COPIAR DESDE AQUÍ ▼**

Sos un ingeniero de documentación. Vas a crear el andamiaje de un sitio de
documentación con **MkDocs + Material for MkDocs**, bilingüe (español base, inglés),
para el proyecto Blue Spot Analysis 2.0 (BSA 2.0) del BID. La carpeta de trabajo
actual será el repositorio de GitHub. **No uses React, Docusaurus ni Node.js.**

En esta fase **no escribas contenido todavía**: solo creá la estructura, la
configuración y páginas vacías con un encabezado provisional.

## Tarea 1 — Crear `CLAUDE.md` en la raíz

Creá un archivo `CLAUDE.md` con exactamente este contenido:

```markdown
# CLAUDE.md — Proyecto de documentación BSA 2.0

## Qué se está construyendo
Sitio de documentación del proyecto Blue Spot Analysis 2.0 (BSA 2.0) del Banco
Interamericano de Desarrollo, con MkDocs + Material for MkDocs, bilingüe (español
base, inglés traducción), desplegado en GitHub Pages. No usar React, Docusaurus ni Node.

## Qué es el BSA 2.0
Es a la vez una metodología, una herramienta de escritorio (toolbox de ArcGIS Pro
escrito en Python) y un dashboard de resultados en línea. Sirve para priorizar
inversiones en infraestructura de transporte a partir de un análisis simplificado de
riesgo ante amenazas naturales, a escala nacional/regional. El análisis combina cuatro
componentes —Amenaza, Exposición, Vulnerabilidad y Criticidad— para estimar el riesgo
y generar mapas de daños, mapas de pérdidas, curvas de excedencia y rankings de
priorización de activos. Está implementado en República Dominicana (referencia),
Costa Rica y El Salvador. La audiencia es doble: usuarios técnicos (especialistas en
riesgo, unidades SIG, consultores) y usuarios estratégicos (ministerios y tomadores
de decisión).

## Datos del proyecto
- Repositorio GitHub: cuenta personal `andresabarca-atlas`, repositorio `bsa-docs`
  (nuevo). A futuro se transferirá a un repositorio del BID.
- site_url: https://andresabarca-atlas.github.io/bsa-docs/
- Contacto público del proyecto: María Alejandra Escovar — MARIAESC@IADB.ORG
- Marca: usar el branding institucional del BID (logo y paleta de color del BID).
- Licencia: BID, licencia AM-331-A3. El repositorio incluye un archivo `LICENSE.md` y
  un fragmento de licencia ("license snippet") que va en el `README.md`. Usá esos
  archivos tal como los provea el cliente; no inventes el texto de la licencia.
- Descargables: el proyecto NO se libera al público por ahora. No incluir archivos
  descargables en el sitio; solo dejar espacios marcados con
  `<!-- COMPLETAR: enlace de descarga (a futuro) -->` para agregarlos más adelante.

## Reglas de terminología (OBLIGATORIO)
- DAE = Daño Anual Esperado = EAD (Expected Annual Damage): daño físico directo a la
  infraestructura.
- PAE = Pérdida Anual Esperada = EAL (Expected Annual Loss): pérdida económica por
  interrupción del servicio o del tránsito.
- PML = Pérdida Máxima Probable: pérdida asociada a un evento de diseño (p. ej. Tr=500).
- Distinguir SIEMPRE "daño" (físico) de "pérdida" (funcional/económica por
  interrupción). El Concept Report temprano usa "PAE" como métrica única; en el sitio
  hay que separar DAE de PAE como lo hacen el dashboard y el código.
- Amenazas implementadas en la versión actual: inundación fluvial, inundación
  pluvial/costera, sismo, tsunami y licuefacción. Deslizamientos y huracanes se
  mencionan solo como amenazas previstas para fases futuras, no como implementadas.

## Reglas de bilingüismo
- Idioma base español: archivos `docs/.../pagina.md`.
- Idioma inglés: archivos `docs/.../pagina.en.md`.
- NO crear los archivos `.en.md` hasta la Fase 4. Las fases 1 a 3 escriben solo español.

## Ubicación de las fuentes (carpeta `fuentes/`, NO publicar)
- `fuentes/01_metodologia/BSA 2.0 Concept Report.md` — informe conceptual.
  IMPORTANTE: pesa 1,3 MB. SOLO las líneas 1 a 1027 son texto. De la línea 1028 en
  adelante son imágenes en base64; nunca leas ese rango como texto.
- `fuentes/02_presentaciones/Ppt_BSA_Ejecutiva_15042026_v3_ENG.pdf` — deck ejecutivo
  corto en inglés (10 láminas).
- `fuentes/02_presentaciones/Presentación_BSA2_23022026_V3.pdf` — deck extenso en
  español (17 láminas).
- `fuentes/03_datos_entrada/IDB_InputData_BSA_V1_25022026 1.xlsx` — ficha de datos de
  entrada, 22 hojas. Leelo con un script de Python + openpyxl, nunca como texto plano.
- `fuentes/04_codigo/BSA2_CostaRica/` — código. Archivo clave: `BSA2.py`. NO leas
  `BSA2.gdb/` (geodatabase binaria).

## Mapa fuente → sección del sitio
- Inicio: deck ejecutivo láminas 1-5; Concept Report cap. 1-2; créditos del equipo en `fuentes/_guia/Mapa_Actores_BSA2.md`.
- Metodología/antecedentes: Concept Report líneas 149-237.
- Metodología/propósito-alcances: Concept Report líneas 167-236.
- Metodología/conceptos-clave: Concept Report glosario líneas 116-145; deck ejecutivo lám. 4-5.
- Metodología/arquitectura: Concept Report líneas 240-341.
- Metodología/modulo-amenaza: Concept Report líneas 465-519; xlsx hoja Hazard.
- Metodología/modulo-exposicion: Concept Report líneas 520-575.
- Metodología/modulo-vulnerabilidad: Concept Report líneas 600-657.
- Metodología/modulo-criticidad: Concept Report líneas 576-599.
- Metodología/calculo-riesgo: Concept Report líneas 658-737.
- Metodología/estructura-datos: Concept Report líneas 343-464.
- Getting Started: deck extenso láminas 8, 12-13, 15-17; BSA2.py; BSA2.atbx.
- Guía de Usuario/flujo: deck extenso láminas 6-7; BSA2.py.
- Guía de Usuario/datos-entrada: xlsx (22 hojas); deck extenso láminas 9-11.
- Guía de Usuario/resultados: Concept Report líneas 334-341; deck extenso lám. 7.
- Guía de Usuario/caso-ejemplo: carpeta fuentes/04_codigo/BSA2_CostaRica/.
- Dashboard: ver la descripción detallada en el prompt de la Fase 3 (basada en la exploración en vivo del dashboard de RD); deck extenso lámina 14 y deck ejecutivo lámina 8 como apoyo.
- Recursos/referencias: Concept Report líneas 954 en adelante.
- Glosario: Concept Report líneas 116-145 (conceptos) y 349-371 (siglas).

## Reglas de eficiencia (para no agotar el límite de uso)
- Leé SOLO el rango de líneas necesario de cada fuente (usá offset/limit).
- No leas archivos binarios (.gdb, imágenes base64).
- Hacé `git commit` después de cada página o subsección terminada.
- No reescribas páginas ya finalizadas.

## Convenciones de redacción
- Tono técnico pero accesible; recordá las dos audiencias.
- Usá admonitions de Material (note, tip, warning) para destacar ideas.
- Fórmulas con sintaxis `$...$` y `$$...$$` (extensión arithmatex).
- Diagramas de flujo con Mermaid cuando aporten claridad.
- Imágenes en `docs/assets/`.
- Citá la fuente de figuras y datos.
- Respetá los derechos de autor: no copies bloques largos textuales de los PDF ni del
  Concept Report; redactá con palabras propias y resumí.

## Estructura de navegación
Inicio · Metodología (antecedentes, propósito-alcances, conceptos-clave, arquitectura,
módulo de amenaza, módulo de exposición, módulo de vulnerabilidad, módulo de
criticidad, cálculo de riesgo, estructura de datos) · Primeros pasos (requisitos,
instalación, organización de datos, interfaz) · Guía de Usuario (flujo de trabajo,
datos de entrada, configuración de una corrida, resultados, caso de ejemplo) ·
Dashboard (descripción general, exploración de métricas, resultados por país) ·
Recursos (descargas, referencias, FAQ) · Glosario (conceptos, siglas).

## Imágenes
- Las figuras del Concept Report están como imágenes base64 al final del archivo, con
  definiciones del tipo `[imageN]: data:image/...;base64,...`. Extraelas con un script
  de Python y guardalas en `docs/assets/metodologia/`.
- Para figuras de los PDF, podés usar `pdftoppm` o `pdfimages` (poppler-utils). Si no
  es viable, dejá un placeholder marcado como `<!-- FALTA IMAGEN: ... -->`.

## No tocar
No modifiques `fuentes/`, `PLAN_Documentacion_BSA2.md` ni `PROMPT_Claude_Code.md`.
```

## Tarea 2 — `requirements.txt`

```
mkdocs-material
mkdocs-static-i18n
```

## Tarea 3 — `mkdocs.yml`

Creá `mkdocs.yml` con esta configuración. Dejá `site_url` con el valor de ejemplo y un
comentario para ajustarlo más adelante.

```yaml
site_name: Blue Spot Analysis 2.0
site_description: Documentación de la metodología, la herramienta y el dashboard del BSA 2.0
site_url: https://andresabarca-atlas.github.io/bsa-docs/
docs_dir: docs

theme:
  name: material
  language: es
  palette:
    - scheme: default
      primary: blue
      accent: light blue
      toggle:
        icon: material/weather-night
        name: Modo oscuro
    - scheme: slate
      primary: blue
      accent: light blue
      toggle:
        icon: material/weather-sunny
        name: Modo claro
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.indexes
    - navigation.top
    - navigation.footer
    - toc.follow
    - search.suggest
    - search.highlight
    - content.code.copy
  logo: assets/logo-bid.png      # logo del BID (ver Tarea 4)
  favicon: assets/favicon.png

plugins:
  - search:
      lang:
        - es
        - en
  - i18n:
      docs_structure: suffix
      languages:
        - locale: es
          default: true
          name: Español
          build: true
        - locale: en
          name: English
          build: true

markdown_extensions:
  - admonition
  - attr_list
  - md_in_html
  - footnotes
  - tables
  - toc:
      permalink: true
  - pymdownx.details
  - pymdownx.highlight
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.arithmatex:
      generic: true

extra_javascript:
  - javascripts/mathjax.js
  - https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js

extra_css:
  - stylesheets/extra.css

nav:
  - Inicio: index.md
  - Metodología:
      - metodologia/index.md
      - Introducción y antecedentes: metodologia/antecedentes.md
      - Propósito, alcances y limitaciones: metodologia/proposito-alcances.md
      - Conceptos clave: metodologia/conceptos-clave.md
      - Lógica funcional y arquitectura: metodologia/arquitectura.md
      - Módulo de Amenaza: metodologia/modulo-amenaza.md
      - Módulo de Exposición: metodologia/modulo-exposicion.md
      - Módulo de Vulnerabilidad: metodologia/modulo-vulnerabilidad.md
      - Módulo de Criticidad: metodologia/modulo-criticidad.md
      - Cálculo de Riesgo: metodologia/calculo-riesgo.md
      - Estructura de datos: metodologia/estructura-datos.md
  - Primeros pasos:
      - getting-started/index.md
      - Requisitos: getting-started/requisitos.md
      - Instalación: getting-started/instalacion.md
      - Organización de datos: getting-started/organizacion-datos.md
      - Interfaz de la herramienta: getting-started/interfaz.md
  - Guía de Usuario:
      - guia-usuario/index.md
      - Flujo de trabajo: guia-usuario/flujo-trabajo.md
      - Datos de entrada: guia-usuario/datos-entrada.md
      - Configuración de una corrida: guia-usuario/configuracion-corrida.md
      - Resultados: guia-usuario/resultados.md
      - Caso de ejemplo: guia-usuario/caso-ejemplo.md
  - Dashboard:
      - dashboard/index.md
      - Exploración de métricas: dashboard/exploracion-metricas.md
      - Resultados por país: dashboard/resultados-paises.md
  - Recursos:
      - recursos/index.md
      - Referencias: recursos/referencias.md
      - Preguntas frecuentes: recursos/faq.md
  - Glosario:
      - glosario/index.md
      - Diccionario de siglas: glosario/siglas.md
```

## Tarea 4 — Archivos de soporte

- `docs/javascripts/mathjax.js` con la configuración estándar de MathJax para
  arithmatex (inicialización de `tex`, `options` y reacción a `document$`).
- `docs/stylesheets/extra.css` con los ajustes de marca del BID (la paleta ya está en
  `mkdocs.yml`; acá afiná detalles de color institucional) y reglas mínimas para
  leyendas de figuras.
- `.gitignore` que excluya: `site/`, `.cache/`, `__pycache__/`, `*.pyc`, entornos
  virtuales, y `fuentes/04_codigo/BSA2_CostaRica/` (geodatabase pesada). Mantené el
  resto de `fuentes/` versionado como referencia.
- **Marca del BID.** El logo del BID aparece en todas las láminas de los PDF de
  `fuentes/02_presentaciones/`. Extraé el logo del BID y úsalo como
  `docs/assets/logo-bid.png`; generá también un `docs/assets/favicon.png`. Si no
  lográs una extracción de buena calidad, creá un placeholder y dejá el comentario
  `<!-- COMPLETAR: logo del BID en alta resolución -->`.
- **`LICENSE.md`.** En la raíz del repositorio ya existe un archivo `LICENSE.md` con la
  licencia AM-331-A3 del BID. Conservalo tal cual, no lo modifiques.
- `README.md` del repositorio: explicá brevemente qué es el sitio y cómo construirlo
  localmente (`pip install -r requirements.txt`, `mkdocs serve`). Al final del
  `README.md` incluí el fragmento de licencia del BID: copialo del archivo
  `fuentes/_guia/License_Snippet_README.md` (sección "Licencia" con el copyright
  AM-331-A3 y la limitación de responsabilidades).

## Tarea 5 — Workflow de CI/CD

Creá `.github/workflows/ci.yml` con el flujo oficial de Material for MkDocs para
publicar en GitHub Pages mediante la rama `gh-pages`:

```yaml
name: ci
on:
  push:
    branches:
      - main
permissions:
  contents: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Configurar credenciales de Git
        run: |
          git config user.name github-actions[bot]
          git config user.email 41898282+github-actions[bot]@users.noreply.github.com
      - uses: actions/setup-python@v5
        with:
          python-version: 3.x
      - run: echo "cache_id=$(date --utc '+%V')" >> $GITHUB_ENV
      - uses: actions/cache@v4
        with:
          key: mkdocs-material-${{ env.cache_id }}
          path: .cache
          restore-keys: |
            mkdocs-material-
      - run: pip install -r requirements.txt
      - run: mkdocs gh-deploy --force
```

## Tarea 6 — Páginas vacías

Creá todos los archivos `.md` listados en la `nav` (solo en español, sin `.en.md`).
Cada uno con un encabezado H1 y la nota `> Página en construcción.`. Las páginas
`index.md` de cada sección serán la portada de esa sección (gracias a
`navigation.indexes`).

## Tarea 7 — Verificar y versionar

1. `pip install -r requirements.txt`
2. `mkdocs build --strict` y corregí cualquier error de configuración hasta que
   compile limpio.
3. `git init` (si hace falta), primer commit con todo el andamiaje.
4. Mostrame un resumen de lo creado y confirmá que `mkdocs build` pasa sin errores.

> **▲ FIN DEL PROMPT FASE 0 ▲**

---

# FASE 1 — Metodología (español)

> **▼ COPIAR DESDE AQUÍ ▼**

Continuá con el sitio de documentación del BSA 2.0. Leé `CLAUDE.md` antes de empezar;
contiene las reglas del proyecto, el mapa de fuentes y las reglas de eficiencia.

En esta fase escribís el contenido **en español** de la sección **Metodología**.
Trabajá página por página, en este orden, y hacé `git commit` después de cada una.

**Antes de la primera página:** extraé las figuras del Concept Report. Las imágenes
están en base64 al final de `fuentes/01_metodologia/BSA 2.0 Concept Report.md`
(definiciones `[imageN]: data:image/...;base64,...`). Escribí un script de Python que
las decodifique y las guarde en `docs/assets/metodologia/imageN.png`. Usalas luego en
las páginas correspondientes con su leyenda y la cita de fuente.

Páginas a escribir (recordá: leé solo el rango de líneas indicado en el mapa de
fuentes del `CLAUDE.md`):

1. **`metodologia/index.md`** — Portada de la sección. Resumen de qué es la
   metodología BSA 2.0, los cuatro componentes (amenaza, exposición, vulnerabilidad,
   criticidad) y cómo se combinan para estimar el riesgo. Incluí un diagrama Mermaid
   del flujo general y enlaces a las subpáginas.

2. **`metodologia/antecedentes.md`** — Origen del Blue Spot Analysis (Danish Road
   Directorate, proyecto SWAMP), su adopción por el BID y la evolución hacia el BSA
   2.0. Evolución conceptual de la evaluación de riesgo por inundación.

3. **`metodologia/proposito-alcances.md`** — Propósito de la herramienta, preguntas
   que responde, escalas de aplicación (regional, nacional, corredor, tramo),
   alcances y limitaciones (enfoque probabilista simplificado, no propagación de
   incertidumbre en versiones iniciales).

4. **`metodologia/conceptos-clave.md`** — Definiciones transversales: amenaza,
   exposición, vulnerabilidad, criticidad, riesgo; período de retorno; **la distinción
   central entre daños (DAE) y pérdidas (PAE)**; medidas de intensidad (TH, V, PGA,
   etc.). Esta página es la referencia conceptual del resto del sitio.

5. **`metodologia/arquitectura.md`** — Lógica funcional por módulos y flujo general de
   cálculo (rutas de daño físico y de pérdida por disrupción del tránsito, agregación
   por período de retorno). Incluí el diagrama de flujo de la herramienta.

6. **`metodologia/modulo-amenaza.md`** — Tipos de amenaza implementados (inundación
   fluvial, pluvial/costera, sismo, tsunami, licuefacción), mallas ráster por período
   de retorno, escalas temporales y espaciales, escenarios de cambio climático.
   Mencioná deslizamientos y huracanes solo como amenazas previstas a futuro.

7. **`metodologia/modulo-exposicion.md`** — Tipos de infraestructura analizada (vías,
   puentes, túneles, drenajes), métodos de caracterización, segmentación y valoración
   económica, atributos de la base de datos de exposición.

8. **`metodologia/modulo-vulnerabilidad.md`** — Funciones de vulnerabilidad (relación
   intensidad–daño medio), diferencia con funciones de fragilidad, niveles de análisis
   cualitativo vs. cuantitativo, librería modular de funciones.

9. **`metodologia/modulo-criticidad.md`** — Criticidad de la red vial, enfoque
   multicriterio (funcionalidad, redundancia, accesibilidad, valor estratégico,
   disrupción), relación con el costo de interrupción del tránsito.

10. **`metodologia/calculo-riesgo.md`** — Modelo de riesgo, estimación probabilista
    simplificada, cálculo de DAE y PAE, curva de excedencia de pérdidas y PML.
    Renderizá las fórmulas con arithmatex.

11. **`metodologia/estructura-datos.md`** — Modelo de datos de la herramienta: tablas
    principales, campos y relaciones (elemento expuesto, vulnerabilidad, criticidad,
    realizaciones, uso).

Al terminar, ejecutá `mkdocs build --strict`, corregí errores y mostrame un resumen.

> **▲ FIN DEL PROMPT FASE 1 ▲**

---

# FASE 2 — Primeros pasos y Guía de Usuario (español)

> **▼ COPIAR DESDE AQUÍ ▼**

Continuá con el sitio de documentación del BSA 2.0. Leé `CLAUDE.md` antes de empezar.

En esta fase escribís el contenido **en español** de las secciones **Primeros pasos**
y **Guía de Usuario**. Trabajá página por página y hacé `git commit` después de cada
una.

Para la página de datos de entrada vas a necesitar el contenido del Excel
`fuentes/03_datos_entrada/IDB_InputData_BSA_V1_25022026 1.xlsx`. Leelo con un script
de Python + openpyxl (instalá openpyxl si hace falta) y recorré las 22 hojas: una
hoja resumen (`Capas_Resumen`), hojas de capas de exposición, hojas de bases de datos
de vulnerabilidad y operación, y la hoja `Hazard`.

### Sección Primeros pasos

1. **`getting-started/index.md`** — Portada: qué se necesita para poner en marcha el
   BSA 2.0 y las fases de acceso (Alfa interno, Beta distribución controlada, versión
   estable). Enlaces a las subpáginas.

2. **`getting-started/requisitos.md`** — Requisitos del sistema (tabla: SO, ArcGIS Pro
   3.2.x, extensión Spatial Analyst, entorno Python `arcgispro-py3`, RAM, CPU,
   almacenamiento) y conocimientos previos recomendados (teóricos y prácticos).

3. **`getting-started/instalacion.md`** — Instalación de ArcGIS Pro, del toolbox
   `BSA2.atbx` y configuración del entorno Python. Pasos numerados.

4. **`getting-started/organizacion-datos.md`** — Cómo organizar carpetas y datos de
   trabajo antes de correr la herramienta (capas de exposición, mallas de amenaza,
   bases de datos de vulnerabilidad y operación, geodatabase de resultados).

5. **`getting-started/interfaz.md`** — La interfaz de la herramienta `BSA2`: describí
   los parámetros del toolbox (capas de exposición de vías, puentes, túneles y
   drenajes; capas de amenaza fluvial, costera, tsunami, sismo y licuefacción; base de
   datos de vulnerabilidad; base de datos de operaciones; PIB per cápita por día;
   longitud de segmento de análisis). Para conocer los parámetros exactos podés
   revisar `fuentes/04_codigo/BSA2_CostaRica/BSA2.atbx` y `BSA2.py`.

### Sección Guía de Usuario

6. **`guia-usuario/index.md`** — Portada: visión general del proceso de uso, del dato
   "bruto" al mapa de priorización.

7. **`guia-usuario/flujo-trabajo.md`** — Flujo paso a paso: preparar y estandarizar
   datos, calcular/insertar PIB per cápita, definir longitud de análisis por segmento,
   cálculo de DAE y PAE, priorización e interacción en el dashboard. Incluí un
   diagrama Mermaid.

8. **`guia-usuario/datos-entrada.md`** — **Página central de inputs.** A partir del
   Excel, documentá cada conjunto de datos de entrada agrupado en: (a) inventarios de
   activos / exposición, (b) mallas de amenaza, (c) vulnerabilidad y recuperación,
   (d) criticidad y costos de operación. Para cada capa indicá: descripción, si es
   obligatoria o de referencia, formato (shapefile polilínea/punto, ráster GeoTIFF,
   CSV) y atributos principales con su tipo. Usá tablas. Explicá la convención de
   nombres de los rásters de amenaza de la hoja `Hazard`
   (`{amenaza}_{horizonte}_{escenario}_{país}_{Tr}.tif`).

9. **`guia-usuario/configuracion-corrida.md`** — Cómo configurar una corrida:
   asignación de capas a parámetros, definición de la longitud de segmento, parámetros
   económicos. Podés apoyarte en `BSA2.py` y en el archivo de configuración
   `fuentes/04_codigo/BSA2_CostaRica/Loc/`.

10. **`guia-usuario/resultados.md`** — Productos de salida: archivo de resultados,
    mapas de daños, mapas de pérdidas, métricas DAE/PAE/PML y cómo interpretarlos para
    la priorización.

11. **`guia-usuario/caso-ejemplo.md`** — Caso de ejemplo con los datos de Costa Rica
    entregados en `fuentes/04_codigo/BSA2_CostaRica/`. Describí el proyecto
    (`CostaRica.aprx`), los insumos usados y el tipo de resultados obtenidos, sin
    volcar datos binarios.

Al terminar, ejecutá `mkdocs build --strict`, corregí errores y mostrame un resumen.

> **▲ FIN DEL PROMPT FASE 2 ▲**

---

# FASE 3 — Inicio, Dashboard, Recursos y Glosario (español)

> **▼ COPIAR DESDE AQUÍ ▼**

Continuá con el sitio de documentación del BSA 2.0. Leé `CLAUDE.md` antes de empezar.

En esta fase completás el contenido **en español** de las secciones restantes.
Trabajá página por página y hacé `git commit` después de cada una.

### Inicio

1. **`index.md`** — Portada del sitio. Presentación del BSA 2.0, qué preguntas
   responde, a quién va dirigido (usuarios técnicos y estratégicos), cómo navegar la
   documentación (tarjetas o enlaces a las secciones principales), un bloque de
   créditos del equipo y la información de contacto y licencia.

   - **Créditos / equipo:** construí esta sección a partir del archivo
     `fuentes/_guia/Mapa_Actores_BSA2.md`, que tiene el equipo completo del proyecto.
     Presentalo agrupado por nivel (liderazgo, dirección del producto, equipos de
     ejecución por bloque A/B/C/D). Como son ~20 personas, usá un formato compacto;
     podés poner los equipos de ejecución dentro de bloques desplegables
     (`pymdownx.details`) para no recargar la portada.
   - **Contacto:** punto de contacto del proyecto — María Alejandra Escovar,
     MARIAESC@IADB.ORG.
   - **Licencia:** indicá que el proyecto se distribuye bajo la licencia AM-331-A3 del
     BID y enlazá al archivo `LICENSE.md` del repositorio.
   - **Logo:** usá el logo del BID en la cabecera (`docs/assets/logo-bid.png`, creado
     en la Fase 0).

### Dashboard

> La descripción de abajo se basa en la exploración en vivo del dashboard de
> República Dominicana (mayo 2026). El dashboard es una aplicación de ArcGIS
> Experience con dos pestañas: **General View** y **Loss Curves**.
>
> **Capturas de pantalla:** el cliente colocará capturas del dashboard en
> `docs/assets/dashboard/`. Usá las que encuentres allí para ilustrar estas páginas.
> Donde falte una captura, insertá un placeholder visible
> `<!-- FALTA CAPTURA: descripción de la vista -->` indicando qué vista se necesita.

2. **`dashboard/index.md`** — Descripción general. El dashboard es la interfaz en
   línea para visualizar e interpretar los resultados del BSA y facilitar el diálogo
   con tomadores de decisión. Describí sus dos pestañas: **General View** (activos
   priorizados, métricas y mapa) y **Loss Curves** (curvas de excedencia de
   pérdidas). Indicá que cada país tiene su propio dashboard y que los valores se
   muestran en la moneda local (p. ej. DOP en República Dominicana).

3. **`dashboard/exploracion-metricas.md`** — Cómo explorar las métricas en la pestaña
   *General View*:
   - **Indicadores superiores:** Length Assessed (longitud evaluada), Expected Annual
     Damage (EAD/DAE) Total y Expected Annual Loss (EAL/PAE) Total.
   - **Panel "Prioritized Assets"** (izquierda): lista jerarquizada de activos
     priorizados, con sub-pestañas por tipo de activo —Roads, Drainage, Tunnels,
     Bridges—; cada elemento muestra código de ruta, nombre y valor económico.
   - **Mapa interactivo** (centro): activos priorizados con símbolos graduados;
     herramientas de zoom, capas, mapa base, leyenda y búsqueda.
   - **Panel "Comparison of EAL vs. EAD"** (derecha): gráficos de comparación, entre
     ellos "Total Expected Annual Loss by Hazard" (anillo por amenaza: fluvial,
     costera, tsunami, sismo) y los resultados de túneles ("Tunnels results") con su
     leyenda de DAE.
   - **Tabla "Top 5 Highest-Criticality Segments"** (inferior): segmentos con las
     columnas TRAMO_ATT, LONGITUD, LAYER, NOMBRE_ATT, RD_Tipo, DAE_total y PAE_total.

   Y en la pestaña *Loss Curves*: la visualización de las curvas de excedencia de
   pérdidas. Explicá cómo se leen estos elementos para priorizar inversiones.

4. **`dashboard/resultados-paises.md`** — Resultados disponibles por país, con enlaces:
   - República Dominicana (referencia de desarrollo): https://experience.arcgis.com/experience/f9ef8a09343e49b8828d590fbc82bae0
   - Costa Rica (preliminar): https://experience.arcgis.com/experience/e1c2ebe138554254b29f5f0ea74f2302
   - El Salvador (preliminar): https://experience.arcgis.com/experience/a9258d5c9ffe4cd0aa6b5fdef675c659

   Si hay capturas de pantalla del dashboard en `docs/assets/dashboard/`, usalas. Si
   no, dejá placeholders `<!-- FALTA CAPTURA: ... -->` para insertarlas después.

### Recursos

5. **`recursos/index.md`** — Descargas. **Importante:** por ahora el proyecto NO se
   libera al público, así que esta página no debe ofrecer archivos descargables.
   Redactá una página breve que explique que los materiales descargables (ficha de
   datos de entrada, toolbox, plantillas) estarán disponibles en una etapa futura, y
   dejá la estructura preparada con espacios marcados
   `<!-- COMPLETAR: enlace de descarga (a futuro) -->` para cada material previsto.

6. **`recursos/referencias.md`** — Referencias bibliográficas, tomadas del capítulo de
   referencias del Concept Report (líneas 954 en adelante). Formato de lista.

7. **`recursos/faq.md`** — Preguntas frecuentes. Redactá entre 8 y 12 preguntas útiles
   a partir de todo el material (requisitos, licencias de datos, diferencia DAE/PAE,
   amenazas soportadas, escalas de análisis, cómo aplicar a un país nuevo, etc.).

### Glosario

8. **`glosario/index.md`** — Glosario de conceptos, a partir del glosario del Concept
   Report (líneas 116-145). Tabla concepto/definición, ordenada alfabéticamente.

9. **`glosario/siglas.md`** — Diccionario de siglas, a partir de la Tabla 4.1 del
   Concept Report (líneas 349-371). Tabla sigla/significado/descripción. Verificá que
   DAE, PAE, EAD y EAL estén incluidos y definidos según las reglas de terminología.

Al terminar, ejecutá `mkdocs build --strict`, corregí errores, revisá que todo el
sitio en español esté completo y mostrame un resumen.

> **▲ FIN DEL PROMPT FASE 3 ▲**

---

# FASE 4 — Traducción al inglés

> **▼ COPIAR DESDE AQUÍ ▼**

Continuá con el sitio de documentación del BSA 2.0. Leé `CLAUDE.md` antes de empezar.

El sitio en español está completo. En esta fase creás la versión en inglés.

Para **cada** archivo `docs/**/pagina.md` creá su equivalente `docs/**/pagina.en.md`
con la traducción profesional al inglés del contenido. Reglas:

- Traducí también `index.md` → `index.en.md`.
- Mantené idéntica la estructura, los enlaces internos, las rutas de imágenes, los
  bloques de código, las fórmulas y los diagramas Mermaid.
- Respetá la terminología: DAE→EAD, PAE→EAL; podés conservar las siglas españolas
  entre paréntesis la primera vez que aparezcan.
- Traducí las leyendas de figuras y los textos de los admonitions.
- No traduzcas nombres propios, URLs ni el nombre del proyecto.
- Trabajá sección por sección y hacé `git commit` después de cada sección (Inicio,
  Metodología, Primeros pasos, Guía de Usuario, Dashboard, Recursos, Glosario).

Después de traducir, revisá `mkdocs.yml`: con el plugin `i18n` en modo `suffix`, el
selector de idioma debería funcionar automáticamente. Si los títulos de la navegación
necesitan traducirse, agregá `nav_translations` para el locale `en` en la
configuración del plugin.

Al terminar, ejecutá `mkdocs build --strict`, levantá `mkdocs serve`, verificá que el
selector ES/EN funcione y mostrame un resumen.

> **▲ FIN DEL PROMPT FASE 4 ▲**

---

# FASE 5 — Revisión y despliegue

> **▼ COPIAR DESDE AQUÍ ▼**

Continuá con el sitio de documentación del BSA 2.0. Leé `CLAUDE.md` antes de empezar.

El sitio bilingüe está completo. En esta fase hacés la revisión final y el despliegue.

### Revisión

1. Ejecutá `mkdocs build --strict` y corregí cualquier advertencia o error (enlaces
   rotos, referencias a imágenes inexistentes, etc.).
2. Revisá la consistencia de terminología en todo el sitio: DAE/PAE/EAD/EAL usados
   correctamente; "daño" vs "pérdida" bien distinguidos.
3. Buscá los placeholders pendientes (`<!-- COMPLETAR -->`, `<!-- FALTA -->`,
   `<!-- FALTA IMAGEN -->`, `<!-- FALTA CAPTURA -->`) y hacé una lista de todo lo que
   queda pendiente de completar con información del cliente.
4. Verificá que cada página en español tenga su `.en.md` correspondiente.
5. Levantá `mkdocs serve` y revisá visualmente la portada, la navegación por pestañas,
   la búsqueda y el selector de idioma.

### Despliegue en GitHub Pages

El repositorio se creará en la **cuenta personal de GitHub `andresabarca-atlas`**, con
el nombre **`bsa-docs`** (a futuro se transferirá a un repositorio del BID).

Guiame paso a paso (mostrame los comandos, pero recordá que la creación del repositorio
en GitHub y la conexión remota las hago yo):

1. Indicame cómo crear el repositorio `bsa-docs` en GitHub (vacío, sin README) en la
   cuenta `andresabarca-atlas`, y cómo conectar el remoto
   (`git remote add origin https://github.com/andresabarca-atlas/bsa-docs.git`).
2. Confirmá que `site_url` en `mkdocs.yml` es
   `https://andresabarca-atlas.github.io/bsa-docs/` (ya debería estarlo).
3. Indicame el `git push` inicial a la rama `main`.
4. Explicame que el workflow `ci.yml` se ejecutará solo y, tras su primera corrida,
   debo entrar a **Settings → Pages** y fijar la fuente en la rama `gh-pages`.
5. Confirmame la URL final: `https://andresabarca-atlas.github.io/bsa-docs/`.

Al terminar, mostrame un resumen del estado del sitio y la lista de placeholders
pendientes de la revisión.

> **▲ FIN DEL PROMPT FASE 5 ▲**

---

## Notas finales

- Si una fase queda a medias por el límite de uso, abrí una conversación nueva y
  pedile a Claude Code que continúe: como ya hay *commits* y `CLAUDE.md`, retomará sin
  perder contexto.
- Si querés enriquecer la sección Dashboard con capturas reales, guardalas en
  `docs/assets/dashboard/` antes de la Fase 3 (o volvé a correr esa página después).
- El plan completo, con la justificación de la estructura y los pendientes de
  información, está en `PLAN_Documentacion_BSA2.md`.
