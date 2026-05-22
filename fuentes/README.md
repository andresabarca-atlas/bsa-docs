# Fuentes base — Documentación BSA 2.0

Esta carpeta contiene el material original que sirve de insumo para construir el sitio
de documentación del proyecto **Blue Spot Analysis 2.0 (BSA 2.0)** del BID.
No se publica en el sitio web; es material de referencia para la redacción.

## Contenido y organización

| Carpeta | Archivo | Qué es | Alimenta principalmente |
|---|---|---|---|
| `01_metodologia/` | `BSA 2.0 Concept Report.md` | Informe conceptual preliminar (V0.1, jul. 2025). Documento extenso. **Solo las líneas 1–1027 son texto; de la 1028 en adelante son imágenes en base64.** | Sección **Metodología** y **Glosario** |
| `02_presentaciones/` | `Ppt_BSA_Ejecutiva_15042026_v3_ENG.pdf` | Deck ejecutivo corto (10 láminas, inglés). | **Inicio**, visión general |
| `02_presentaciones/` | `Presentación_BSA2_23022026_V3.pdf` | Deck extenso orientado a usuario (17 láminas, español). | **Getting Started**, **Guía de Usuario**, **Dashboard** |
| `03_datos_entrada/` | `IDB_InputData_BSA_V1_25022026 1.xlsx` | Ficha de datos de entrada: 22 hojas con capas obligatorias/opcionales, atributos y formatos. | **Guía de Usuario → Inputs** |
| `04_codigo/` | `BSA2_CostaRica.zip` + carpeta extraída | Última versión del código y resultados del caso Costa Rica. | **Getting Started**, **Guía de Usuario** |
| `_guia/` | `Document_Guide.txt` | Guía original de Andrés sobre qué hacer con cada documento. | Referencia de trabajo |
| `_guia/` | `Proposed Documentation Structure.txt` | Estructura propuesta inicial del sitio. | Referencia de trabajo |
| `_guia/` | `Mapa_Actores_BSA2.md` | Equipo completo del proyecto (mapa de actores). | Sección **Inicio → Créditos** |
| `_guia/` | `License_Snippet_README.md` | Fragmento de licencia del BID para el `README.md`. | `README.md` del repositorio |

> El archivo `LICENSE.md` (licencia AM-331-A3 del BID) está en la **raíz** del
> repositorio, no dentro de `fuentes/`.

## Archivos clave dentro de `04_codigo/BSA2_CostaRica/`

- `BSA2.py` — **código central del cálculo** (~56 KB, Python). Fuente de verdad de la lógica.
- `BSA2.atbx` — toolbox de ArcGIS Pro que expone la herramienta `BSA2`.
- `CostaRica.aprx` — proyecto de ArcGIS Pro del caso Costa Rica.
- `BSA2.gdb/` — geodatabase de archivos (datos y resultados de Costa Rica). **Binario, no leer.**
- `FVU_BSA_V3.csv` — base de datos de funciones de vulnerabilidad (ejemplo de input).
- `OCO_BSA_CR_V1.csv` — base de datos de costos de operación (ejemplo de input).
- `Loc/run_config_*.loc` — archivo de configuración de una corrida.

> Nota: la carpeta `BSA2_CostaRica/` fue extraída del zip para que Claude Code pueda
> leer `BSA2.py` directamente. Conviene incluirla en `.gitignore` (ver el plan).
