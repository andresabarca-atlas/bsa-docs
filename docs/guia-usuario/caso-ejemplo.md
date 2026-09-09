# Caso de ejemplo — Costa Rica

Esta página describe la aplicación del BSA 2.0 al caso de referencia de Costa Rica, incluido en la carpeta `fuentes/04_codigo/BSA2_CostaRica/`. Este caso sirve como referencia para validar la instalación, entender el flujo de trabajo y calibrar las expectativas sobre los resultados.

!!! note "Propósito del caso de ejemplo"
    El caso de Costa Rica es un conjunto de datos de referencia que ilustra el funcionamiento completo del toolbox. No representa un análisis oficial del país; su función es pedagógica y de validación técnica.

## Componentes del caso de ejemplo

El directorio `BSA2_CostaRica/` contiene los siguientes archivos:

| Archivo | Descripción |
|---------|-------------|
| `CostaRica.aprx` | Proyecto de ArcGIS Pro con todas las capas de insumos y resultados ya referenciadas. |
| `BSA2.atbx` | Toolbox con la herramienta BSA2 lista para ejecutar. |
| `BSA2.py` | Script del toolbox (no modificar). |
| `FVU_BSA_V3.csv` | Base de datos de funciones de vulnerabilidad (física y de tránsito). |
| `OCO_BSA_CR_V1.csv` | Base de datos de costos operativos por tipo de vehículo para Costa Rica. |
| `BSA2.gdb/` | Geodatabase con las capas de exposición de entrada y los resultados de la última corrida. |
| `Loc/run_config_20260413_172736.loc` | Archivo de trazabilidad de la corrida de referencia. |

## Insumos utilizados

### Capas de exposición (dentro de `BSA2.gdb`)

| Capa | Tipo | Descripción |
|------|------|-------------|
| `crc_RVN_WGS84` | Polilíneas | Red vial nacional de Costa Rica en datum WGS84. |
| `crc_rvn_puentes2` | Puntos | Inventario de puentes en corredores principales. |
| `cr_tuneles_rvn_WGS84` | Puntos | Inventario de túneles de la red vial nacional. |
| `crc_rvn_drenaje2` | Puntos | Elementos de drenaje en la red vial. |

### Mallas de amenaza utilizadas

La corrida de referencia usó los siguientes rásters (listados en el archivo `.loc`):

**Inundación fluvial (7 períodos de retorno):**

| Archivo | Tr (años) |
|---------|----------|
| `ri_h_CR_10.tif` | 10 |
| `ri_h_CR_20.tif` | 20 |
| `ri_h_CR_50.tif` | 50 |
| `ri_h_CR_75.tif` | 75 |
| `ri_h_CR_100.tif` | 100 |
| `ri_h_CR_200.tif` | 200 |
| `ri_h_CR_500.tif` | 500 |

**Inundación costera/pluvial (10 períodos de retorno):**

| Archivo | Tr (años) |
|---------|----------|
| `c_h_CR_1.tif` | 1 |
| `c_h_CR_2.tif` | 2 |
| `c_h_CR_5.tif` | 5 |
| `c_h_CR_10.tif` | 10 |
| `c_h_CR_25.tif` | 25 |
| `c_h_CR_50.tif` | 50 |
| `c_h_CR_100.tif` | 100 |
| `c_h_CR_250.tif` | 250 |
| `c_h_CR_500.tif` | 500 |
| `c_h_CR_1000.tif` | 1 000 |

**Sismo (5 períodos de retorno — PGA):**

| Archivo | Tr (años) |
|---------|----------|
| `EQ_CR_PGA_100.tif` | 100 |
| `EQ_CR_PGA_225.tif` | 225 |
| `EQ_CR_PGA_475.tif` | 475 |
| `EQ_CR_PGA_2475.tif` | 2 475 |
| `EQ_CR_PGA_4975.tif` | 4 975 |

Tsunami y licuefacción no estuvieron disponibles para esta corrida.

### Parámetros económicos

| Parámetro | Valor |
|-----------|-------|
| PIB per cápita por día | USD 45 249.62 |
| Longitud de segmento | 30 metros |

## Tipo de resultados obtenidos

La corrida generó cuatro capas de resultados en `BSA2.gdb`:

- **`roads_results_20260413_172736`** — tramos de vía con campos de DAE por amenaza (fluvial, costera, sísmica), DAE total, PAE por amenaza, PAE total y Priority.
- **`bridges_results_20260413_172736`** — puentes con sus propias métricas de DAE, PAE y Priority.
- **`tunnels_results_20260413_172736`** — túneles con métricas individuales.
- **`drainage_results_20260413_172736`** — drenajes con métricas individuales.

En la capa de vías, los campos `DAE_bridge`, `DAE_tunnel` y `DAE_drainage` contienen los daños de los componentes asociados al `ID_TRAMO`, permitiendo visualizar el riesgo total de corredor.

## Cómo reproducir el análisis

1. Abra `CostaRica.aprx` en ArcGIS Pro.
2. En el panel Catalog, localice `BSA2.atbx` y abra la herramienta **BSA2**.
3. Cargue los parámetros según el ejemplo de la tabla de configuración en [Configuración de una corrida](configuracion-corrida.md#ejemplo-de-configuracion-costa-rica).
4. Haga clic en **Run** y espere a que finalice.
5. Compare los resultados con los campos de la capa `roads_results_*` ya existente en la geodatabase para validar la reproducibilidad.

!!! tip "Validación rápida"
    Filtre la capa de resultados por los tramos con mayor `Priority` y compárelos geográficamente con los registros históricos de daños viales del país. Una coincidencia espacial entre tramos de alta Priority y zonas históricamente afectadas es un indicador de la coherencia del modelo.
