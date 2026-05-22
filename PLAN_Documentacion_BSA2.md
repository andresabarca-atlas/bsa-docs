# Plan de documentación — Sitio web BSA 2.0

**Proyecto:** Blue Spot Analysis 2.0 (BSA 2.0) — Banco Interamericano de Desarrollo (BID)
**Objetivo:** Consolidar la información dispersa del proyecto en un sitio de documentación
estructurado, bilingüe y público, construido con MkDocs + Material for MkDocs y
desplegado en GitHub Pages.
**Fecha:** Mayo 2026 · **Preparado para:** Andrés Abarca

---

## 1. Cómo usar este plan

Este documento es el plano de la documentación. Define **qué** se va a construir y
**cómo se organiza**. El archivo complementario `PROMPT_Claude_Code.md` contiene el
prompt operativo, dividido en fases, que se pega en Claude Code (VS Code) para
**construir** el sitio.

Flujo recomendado:

1. Revisá este plan y aprobá (o ajustá) la estructura del sitio de la sección 4.
2. Completá los datos pendientes de la sección 9 (créditos, licencia, contacto, repo).
3. Ejecutá el prompt de `PROMPT_Claude_Code.md`, fase por fase, en Claude Code.

---

## 2. Decisiones de partida (ya confirmadas)

| Decisión | Definición | Implicación |
|---|---|---|
| Idioma | **Bilingüe español + inglés** | Se usa el plugin `mkdocs-static-i18n`. El español es idioma base; el inglés es traducción. |
| Alcance | **Metodología + uso** | El sitio cubre Metodología, Getting Started, Guía de Usuario, Dashboard y Glosario. **No** incluye una referencia técnica del código (API del toolbox) para desarrolladores. |
| Repositorio | **Aún no existe** | El plan incluye la creación del repo y la configuración de GitHub Pages desde cero. |
| Dashboard | Los 3 dashboards (RD, CR, ES) son equivalentes | La documentación describe uno (República Dominicana) como referencia y enlaza los otros dos. |
| Generador | **MkDocs + Material for MkDocs** | Sin React, Docusaurus ni Node.js. Stack 100 % Python. |

---

## 3. Entendimiento del proyecto (resumen de la revisión de fuentes)

El BSA 2.0 es **una metodología, una herramienta de escritorio (toolbox de ArcGIS Pro
escrito en Python) y un dashboard de resultados en línea**. Sirve para **priorizar
inversiones en infraestructura de transporte** a partir de un análisis simplificado de
riesgo ante amenazas naturales, a escala nacional/regional.

El análisis se organiza en **cuatro componentes** que se combinan para estimar el riesgo:

- **Amenaza** — qué puede ocurrir, con qué intensidad y frecuencia (mapas ráster por período de retorno).
- **Exposición** — qué activos hay, dónde están y cuánto valen (inventario georreferenciado).
- **Vulnerabilidad** — cómo responde cada activo a cada amenaza (funciones de daño).
- **Criticidad** — qué pasa si un tramo falla o se interrumpe (rutas alternas y costos de interrupción).

**Salidas principales:** mapas de daños, mapas de pérdidas, curvas de excedencia de
pérdidas, y rankings de priorización de activos. Implementado en 3 países: República
Dominicana (referencia de desarrollo), Costa Rica y El Salvador.

**Audiencia doble:** usuarios técnicos (especialistas en riesgo, unidades SIG,
consultores) y usuarios estratégicos (ministerios de transporte, planificación y
finanzas, sistemas de gestión de riesgo, especialistas del BID).

### 3.1. Nota de terminología — punto a unificar en todo el sitio

Hay una **inconsistencia entre el Concept Report (documento temprano) y el material
reciente** (presentaciones, dashboard y código). El sitio debe usar la terminología
reciente de forma consistente:

| Concepto | Sigla ES | Sigla EN | Significado |
|---|---|---|---|
| Daño Anual Esperado | **DAE** | **EAD** (Expected Annual Damage) | Daño físico directo a la infraestructura |
| Pérdida Anual Esperada | **PAE** | **EAL** (Expected Annual Loss) | Pérdida económica por interrupción del servicio/tránsito |
| Pérdida Máxima Probable | **PML** | PML | Pérdida asociada a un evento de diseño (p. ej. Tr=500) |

El Concept Report usa "PAE" como métrica integrada única; el sitio debe **distinguir
DAE (daño) de PAE (pérdida)**, como lo hacen el dashboard y el código. Esta decisión se
inserta explícitamente en el prompt de Claude Code.

### 3.2. Amenazas que la herramienta soporta actualmente

Según los parámetros del toolbox y la ficha de datos de entrada, la versión actual
trabaja con: **inundación fluvial (riverine), inundación pluvial/costera, sismo,
tsunami y licuefacción**. El Concept Report menciona además, a nivel conceptual,
deslizamientos y huracanes como amenazas de fases futuras: el sitio debe diferenciar
lo **implementado** de lo **previsto**.

---

## 4. Estructura propuesta del sitio

La estructura de abajo parte de la propuesta original (`Proposed Documentation
Structure.txt`) y la refina. Los **ajustes están justificados en la sección 4.1**.

```
Inicio
 └─ Presentación del proyecto · ¿Qué preguntas responde? · A quién va dirigido
    Cómo navegar la documentación · Créditos, equipo, licencia y contacto

Metodología
 ├─ Introducción y antecedentes (origen y evolución del BSA)
 ├─ Propósito, alcances y limitaciones
 ├─ Conceptos clave (amenaza/exposición/vulnerabilidad/criticidad/riesgo; daños vs pérdidas)
 ├─ Lógica funcional y arquitectura por módulos
 ├─ Módulo de Amenaza
 ├─ Módulo de Exposición
 ├─ Módulo de Vulnerabilidad
 ├─ Módulo de Criticidad
 ├─ Cálculo de Riesgo (DAE, PAE, curvas de excedencia, PML)
 └─ Estructura de datos

Primeros pasos (Getting Started)
 ├─ Requisitos del sistema y conocimientos previos
 ├─ Instalación (ArcGIS Pro · toolbox .atbx · entorno Python)
 ├─ Organización de datos y carpetas de trabajo
 └─ Interfaz de la herramienta (parámetros del toolbox BSA2)

Guía de Usuario
 ├─ Flujo de trabajo paso a paso
 ├─ Datos de entrada (inputs: capas, atributos, formatos)
 ├─ Configuración de una corrida
 ├─ Resultados (outputs) e interpretación
 └─ Caso de ejemplo (Costa Rica)

Dashboard
 ├─ Descripción general
 ├─ Exploración de métricas (DAE/PAE, curvas de excedencia, priorización)
 └─ Resultados disponibles por país (RD · CR · El Salvador)

Recursos
 ├─ Descargas (ficha de datos de entrada · toolbox · plantillas)
 ├─ Referencias bibliográficas
 └─ Preguntas frecuentes (FAQ)

Glosario
 ├─ Glosario de conceptos
 └─ Diccionario de siglas
```

### 4.1. Ajustes respecto a la propuesta original y por qué

- **"Inicio" ampliado.** Se añade "¿Qué preguntas responde?" y "A quién va dirigido"
  porque el sitio tiene dos audiencias muy distintas y conviene orientarlas desde la
  portada.
- **Nueva página "Conceptos clave" en Metodología.** Centraliza definiciones
  transversales (incluida la distinción daños vs pérdidas, que es un concepto central
  del BSA y aparece destacado en el deck ejecutivo). Evita repetir definiciones en
  cada módulo.
- **"Estructura de datos" se mantiene dentro de Metodología.** El Concept Report la
  describe en detalle (modelo entidad-relación); es conceptual, no operativa.
- **"Organización de datos y carpetas" en Getting Started.** Necesaria antes de correr
  el toolbox; estaba implícita pero no listada.
- **Nueva sección "Recursos".** El deck ejecutivo invita a "descargar la ficha de
  datos de entrada"; conviene un lugar único para descargas, referencias y FAQ. Las
  referencias bibliográficas del Concept Report (sección 8) son valiosas y no tenían
  hogar en la estructura original.
- **"Caso de ejemplo" en la Guía de Usuario.** El código entregado es precisamente el
  caso Costa Rica; documentar una corrida real ancla la teoría en la práctica.
- **El "Diccionario de siglas" (Tabla 4.1 del Concept Report) entra al Glosario**
  junto con el glosario de conceptos.

### 4.2. Posible adición a evaluar

- **Sección "Casos de estudio".** El Concept Report (sección 6) documenta aplicaciones
  reales en República Dominicana (programa de puentes DR-L1166, caminos vecinales
  DR-L1151, Puerto de Manzanillo, estimación post-huracán Fiona). Hoy se propone
  integrarlas en "Dashboard → Resultados por país". Si se quiere darles más peso como
  evidencia de impacto, pueden convertirse en una sección propia. **Decisión tuya.**

---

## 5. Mapa de fuentes → secciones del sitio

Indica a Claude Code de dónde sacar el contenido de cada parte (evita que lea todo).

| Sección del sitio | Fuente principal | Fuente secundaria |
|---|---|---|
| Inicio | Deck ejecutivo (PDF, láminas 1–5) | Concept Report, cap. 1–2 |
| Metodología → Introducción y antecedentes | Concept Report, cap. 1 y 3 (líneas 149–237) | Deck ejecutivo lám. 3 |
| Metodología → Propósito, alcances, limitaciones | Concept Report, cap. 2 y 3.3 (líneas 167–236) | Deck extenso lám. 2–4 |
| Metodología → Conceptos clave | Concept Report, Glosario (líneas 116–145) | Deck ejecutivo lám. 4–5 |
| Metodología → Lógica funcional y arquitectura | Concept Report, 4.1–4.3 (líneas 240–341) | Deck extenso lám. 6–7 |
| Metodología → Módulo de Amenaza | Concept Report, 4.6 (líneas 465–519) | Ficha de inputs, hoja `Hazard` |
| Metodología → Módulo de Exposición | Concept Report, 4.7 (líneas 520–575) | Ficha de inputs, hojas de exposición |
| Metodología → Módulo de Vulnerabilidad | Concept Report, 4.9 (líneas 600–657) | Ficha de inputs, hoja `Funciones_Dano` |
| Metodología → Módulo de Criticidad | Concept Report, 4.8 (líneas 576–599) | Ficha de inputs, hojas de tránsito/logística |
| Metodología → Cálculo de Riesgo | Concept Report, 4.10 (líneas 658–737) | Deck ejecutivo lám. 6 |
| Metodología → Estructura de datos | Concept Report, 4.4–4.5 (líneas 343–464) | — |
| Getting Started | Deck extenso, lám. 8, 12–13, 15–17 | `BSA2.py`, `BSA2.atbx` |
| Guía de Usuario → Flujo de trabajo | Deck extenso, lám. 6–7 | `BSA2.py` |
| Guía de Usuario → Datos de entrada | **Ficha de inputs (xlsx), 22 hojas** | Deck extenso, lám. 9–11 |
| Guía de Usuario → Resultados | Concept Report, 4.3-D (líneas 334–341) | Deck extenso, lám. 7 |
| Guía de Usuario → Caso de ejemplo | `04_codigo/BSA2_CostaRica/` | — |
| Dashboard | Deck extenso lám. 14 · Deck ejecutivo lám. 8 | Dashboards en vivo (capturas) |
| Recursos → Referencias | Concept Report, cap. 8 (líneas 954+) | — |
| Glosario | Concept Report, Glosario + Tabla 4.1 (líneas 116–145 y 349–371) | — |

**URLs de los dashboards:**

- República Dominicana — https://experience.arcgis.com/experience/f9ef8a09343e49b8828d590fbc82bae0
- Costa Rica — https://experience.arcgis.com/experience/e1c2ebe138554254b29f5f0ea74f2302
- El Salvador — https://experience.arcgis.com/experience/a9258d5c9ffe4cd0aa6b5fdef675c659

---

## 6. Arquitectura técnica

### 6.1. Stack

- **MkDocs** — generador de sitios estáticos.
- **Material for MkDocs** — tema.
- **mkdocs-static-i18n** — plugin de bilingüismo (ES base, EN traducción).
- **Python 3.11+** y `pip` para instalar dependencias.
- **GitHub Actions** — build y publicación automática en GitHub Pages.

### 6.2. Plugins y extensiones recomendados

| Componente | Para qué |
|---|---|
| `search` (nativo) | Búsqueda; configurada para español + inglés |
| `mkdocs-static-i18n` | Cambio de idioma ES/EN |
| Extensión `pymdownx.superfences` | Diagramas Mermaid (flujos de la metodología) |
| Extensión `pymdownx.arithmatex` + MathJS/KaTeX | Fórmulas (curva de excedencia, riesgo) |
| `pymdownx.tabbed`, `admonition`, `pymdownx.details` | Notas, advertencias, pestañas |
| `attr_list`, `md_in_html` | Imágenes con leyenda y diseño de la portada |
| Característica de Material `content.code.copy` | Botón de copiar en bloques de código |

### 6.3. Estrategia de bilingüismo

- Idioma base: **español** → archivos `*.md` (sin sufijo).
- Idioma alterno: **inglés** → archivos `*.en.md` (sufijo `.en`).
- `mkdocs-static-i18n` en modo `suffix` genera el sitio en `/` (español) y `/en/`
  (inglés) con un selector de idioma en la cabecera.
- **Ventaja para el flujo por fases:** las fases 1–3 escriben solo el contenido en
  español; la fase 4 crea las traducciones `.en.md`. Así el inglés no se mezcla con la
  redacción del contenido base.

### 6.4. Estructura del repositorio

```
bsa-docs/                          (repositorio de GitHub)
├─ .github/workflows/ci.yml        Workflow de build + deploy a GitHub Pages
├─ docs/
│  ├─ index.md  /  index.en.md     Inicio
│  ├─ metodologia/                 (una página .md + .en.md por subsección)
│  ├─ getting-started/
│  ├─ guia-usuario/
│  ├─ dashboard/
│  ├─ recursos/
│  ├─ glosario/
│  ├─ assets/                      Imágenes, diagramas, logos
│  └─ stylesheets/extra.css        Ajustes de marca (colores BID)
├─ fuentes/                        Material base (NO se publica)
├─ mkdocs.yml                      Configuración del sitio
├─ requirements.txt                Dependencias de Python
├─ .gitignore
├─ LICENSE.md                      Licencia AM-331-A3 del BID
└─ README.md                       Cómo construir el sitio + snippet de licencia
```

> El `.gitignore` debe excluir `fuentes/04_codigo/BSA2_CostaRica/` (geodatabase
> binaria pesada) y `site/`. Se puede conservar `fuentes/` en el repo como referencia
> o excluirla por completo; la recomendación es excluir al menos los binarios pesados.

### 6.5. Despliegue en GitHub Pages

1. Crear el repositorio `bsa-docs` en la cuenta personal `andresabarca-atlas` (vacío,
   sin README).
2. Subir el proyecto generado por Claude Code a la rama `main`.
3. El workflow `ci.yml` se ejecuta en cada *push* a `main`, construye el sitio y lo
   publica con `mkdocs gh-deploy` en la rama `gh-pages`.
4. Tras la primera corrida del workflow, en **Settings → Pages** fijar la fuente en la
   rama **`gh-pages`**.
5. El sitio queda publicado en `https://andresabarca-atlas.github.io/bsa-docs/`.

> A futuro, cuando el equipo valide la documentación, el repositorio se transferirá a
> una organización del BID; en ese momento habrá que actualizar `site_url`.

---

## 7. Estrategia para no exceder los límites de uso de Claude Pro

El sitio es grande (≈25–30 páginas × 2 idiomas). Generar todo en una sola sesión
agotaría el límite de uso. El prompt de Claude Code está dividido en **6 fases
independientes**; cada fase se corre en **una conversación nueva** de Claude Code:

| Fase | Qué hace | Por qué se aísla |
|---|---|---|
| 0 | Andamiaje: repo, `mkdocs.yml`, tema, i18n, navegación, workflow CI, páginas vacías | Trabajo de configuración, bajo consumo |
| 1 | Contenido en español de **Metodología** (la sección más extensa) | Es el grueso del contenido |
| 2 | Contenido en español de **Getting Started + Guía de Usuario** | Depende de fuentes distintas (código, xlsx) |
| 3 | Contenido en español de **Inicio + Dashboard + Recursos + Glosario** | Secciones más cortas, agrupables |
| 4 | **Traducción al inglés** de todo el sitio (`*.en.md`) | Tarea mecánica y voluminosa, mejor aislada |
| 5 | Revisión, build local, ajustes finales y despliegue | Cierre y QA |

Reglas de eficiencia incluidas en el prompt para que Claude Code no malgaste contexto:

- Leer **solo** el rango de líneas indicado de cada fuente (el Concept Report pesa
  1,3 MB; solo las líneas 1–1027 son texto, el resto son imágenes en base64).
- No leer la geodatabase `BSA2.gdb` (binaria).
- Hacer *commit* después de cada subsección, para no perder trabajo.
- Usar `/clear` o una conversación nueva entre fases.
- Extraer figuras del Concept Report y los PDF como imágenes a `docs/assets/`.

---

## 8. Cobertura de la estructura propuesta original

Verificación de que nada de la propuesta original se perdió:

| Propuesta original | Dónde quedó |
|---|---|
| Inicio (intro, índice, desarrolladores/licencia/contacto) | Sección **Inicio** (ampliada) |
| Metodología (todos los módulos) | Sección **Metodología** (con "Conceptos clave" añadido) |
| Getting Started (requisitos, ArcGIS, correr cálculos) | Sección **Primeros pasos** |
| Guía de Usuario (workflow, inputs, outputs) | Sección **Guía de Usuario** (con caso de ejemplo) |
| Dashboard (overview, métricas, países) | Sección **Dashboard** |
| Glosario | Sección **Glosario** (con diccionario de siglas) |

---

## 9. Definiciones del cliente (resueltas)

Estas definiciones ya están confirmadas e incorporadas en el prompt de Claude Code.

1. **Repositorio:** cuenta personal de GitHub `andresabarca-atlas`, repositorio nuevo
   `bsa-docs`. A futuro se transferirá a un repositorio del BID.
   `site_url = https://andresabarca-atlas.github.io/bsa-docs/`.
2. **Créditos / equipo:** definidos en `fuentes/_guia/Mapa_Actores_BSA2.md` (mapa de
   actores completo, ~20 personas en 3 niveles y 4 bloques de ejecución). Claude Code
   construye la sección de créditos a partir de ese archivo.
3. **Licencia:** licencia AM-331-A3 del BID. El archivo `LICENSE.md` ya está en la raíz
   del repositorio; el fragmento para el `README.md` está en
   `fuentes/_guia/License_Snippet_README.md`.
4. **Contacto:** María Alejandra Escovar — MARIAESC@IADB.ORG.
5. **Marca:** branding institucional del BID. El logo se extrae de los PDF de
   presentaciones (aparece en todas las láminas).
6. **Descargas:** el proyecto NO se libera al público por ahora; el sitio no incluye
   archivos descargables. La página de Recursos queda preparada con espacios marcados
   para agregar descargas en el futuro.
7. **Dashboard:** la estructura se documentó por exploración en vivo (ver sección 10).
   Las capturas de pantalla las aporta el cliente en `docs/assets/dashboard/`.

> Único pendiente operativo: colocar las capturas del dashboard en
> `docs/assets/dashboard/` antes (o después) de la Fase 3.

---

## 10. Nota sobre el dashboard

La exploración en vivo del dashboard de República Dominicana se completó. La estructura
observada es la siguiente y ya está reflejada en el prompt de la Fase 3:

- **Dos pestañas:** *General View* y *Loss Curves*.
- *General View* — indicadores superiores (Length Assessed, EAD Total, EAL Total);
  panel izquierdo "Prioritized Assets" con sub-pestañas Roads, Drainage, Tunnels y
  Bridges (lista jerarquizada de 431 activos); mapa interactivo central con símbolos
  graduados; panel derecho "Comparison of EAL vs. EAD" con gráficos —incluido "Total
  Expected Annual Loss by Hazard"— y "Tunnels results"; tabla inferior "Top 5
  Highest-Criticality Segments" (columnas TRAMO_ATT, LONGITUD, LAYER, NOMBRE_ATT,
  RD_Tipo, DAE_total, PAE_total).
- *Loss Curves* — visualización de las curvas de excedencia de pérdidas.
- Los valores se muestran en moneda local (DOP en el caso de RD).

> Nota: el dashboard de ArcGIS Experience es muy pesado y dejó de responder durante la
> exploración tras cargar la vista *General View*. La pestaña *Loss Curves* se
> documenta a partir del material de las presentaciones. Si hace falta, se puede
> repetir la exploración para capturarla en detalle.

Capturas de pantalla en alta resolución (opcionales) pueden colocarse en
`docs/assets/dashboard/` para ilustrar la sección; el prompt ya contempla usarlas.

---

## 11. Próximos pasos

1. Revisar y aprobar la estructura (sección 4).
2. Responder los pendientes de la sección 9.
3. Abrir `PROMPT_Claude_Code.md` y ejecutar la Fase 0 en Claude Code.
4. Continuar fase por fase, en conversaciones nuevas, hasta el despliegue.
