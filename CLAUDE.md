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
