# Interfaz de la herramienta

Al hacer doble clic en la herramienta **BSA2** dentro del toolbox, ArcGIS Pro abre el diálogo de parámetros. Esta página describe cada parámetro, su tipo de dato, si es obligatorio u opcional, y los valores de ejemplo del caso de Costa Rica.

## Diagrama de parámetros

```
BSA2 ─── Exposición ──── Red vial                    (0) [obligatorio]
         │               Puentes                     (1) [opcional]
         │               Túneles                     (2) [opcional]
         │               Drenajes                    (3) [opcional]
         │
         ├── Amenaza ─── Inundación fluvial (varios Tr) (4) [obligatorio*]
         │               Inundación pluvial/costera    (5) [obligatorio*]
         │               Tsunami                       (6) [obligatorio*]
         │               Sismo                         (7) [obligatorio*]
         │               Licuefacción                  (8) [opcional]
         │               Polígono de cambio climático  (9) [opcional]
         │
         ├── Vulnerabilidad ── Base de datos FVU      (10) [obligatorio]
         │
         ├── Operaciones ──── Base de costos operativos (11) [opcional†]
         │                    PIB per cápita por día    (12) [opcional†]
         │
         └── Segmentación ─── Longitud de segmento (m) (13) [obligatorio]
```

\* Al menos **uno** de los rásters de amenaza (parámetros 4–7) debe estar provisto.  
† Los parámetros 11 y 12 deben proveerse juntos o ninguno; de lo contrario la herramienta devuelve error.

## Parámetros de exposición

### (0) Red vial — `roads_path` *(obligatorio)*

Capa vectorial de polilíneas que representa la red de carreteras a analizar. Es el único componente de exposición estrictamente obligatorio.

| Atributo requerido | Tipo | Descripción |
|--------------------|------|-------------|
| `ID_TRAMO` | Long/String | Identificador único del tramo vial. |
| `vul_f` | String | Código de taxonomía de vulnerabilidad para amenazas de inundación (ej. `H_TRNP`). |
| `vul_eq` | String | Código de taxonomía de vulnerabilidad para sismo. |
| `rep_cost_k` | Double | Costo de reposición del tramo en **miles de USD por metro**. |
| `Longitud` | Double | Longitud del segmento en metros. |
| `T9`–`T15` | Double | Tránsito Promedio Diario Anual (TPDA) por tipo de vehículo. |

### (1) Puentes — `bridge_path` *(opcional)*

Capa de puntos con la localización de puentes. Si se provee, la herramienta calcula DAE y PAE para puentes de forma independiente y los agrega al tramo vial correspondiente mediante el campo `ID_TRAMO`.

| Atributo requerido | Tipo | Descripción |
|--------------------|------|-------------|
| `ID_TRAMO` | Long/String | Relaciona el puente con su tramo vial. |
| `vul_f` | String | Taxonomía de vulnerabilidad para inundación. |
| `vul_eq` | String | Taxonomía de vulnerabilidad para sismo. |
| `rep_cost` | Double | Costo de reposición del puente en USD. |

### (2) Túneles — `tunnel_path` *(opcional)*

Capa de puntos con túneles. Misma estructura de atributos que puentes.

### (3) Drenajes — `draina_path` *(opcional)*

Capa de puntos con elementos de drenaje (alcantarillas, cajas, etc.). Misma estructura de atributos que puentes.

## Parámetros de amenaza

Cada amenaza acepta **múltiples rásters** (uno por período de retorno). En el diálogo de ArcGIS Pro se pueden seleccionar varios archivos a la vez. La herramienta extrae automáticamente el valor de Tr del nombre del archivo.

### (4) Inundación fluvial — `fl_rive_raw`

Rásters GeoTIFF con tirante hídrico (en metros) para cada Tr de inundación fluvial.

**Ejemplo (Costa Rica):** `ri_h_CR_10.tif; ri_h_CR_20.tif; ri_h_CR_50.tif; ri_h_CR_75.tif; ri_h_CR_100.tif; ri_h_CR_200.tif; ri_h_CR_500.tif`

### (5) Inundación pluvial/costera — `fl_coas_raw`

Rásters GeoTIFF de inundación pluvial o costera, también en metros.

**Ejemplo (Costa Rica):** `c_h_CR_1.tif; c_h_CR_2.tif; c_h_CR_5.tif; c_h_CR_10.tif; c_h_CR_25.tif; c_h_CR_50.tif; c_h_CR_100.tif; c_h_CR_250.tif; c_h_CR_500.tif; c_h_CR_1000.tif`

### (6) Tsunami — `ts_coas_raw`

Rásters con altura de ola (en metros) por Tr.

### (7) Sismo — `earthqu_raw`

Rásters con Aceleración Pico del Suelo (PGA) para cada Tr.

**Ejemplo (Costa Rica):** `EQ_CR_PGA_100.tif; EQ_CR_PGA_225.tif; EQ_CR_PGA_475.tif; EQ_CR_PGA_2475.tif; EQ_CR_PGA_4975.tif`

### (8) Licuefacción — `liquefa_raw` *(opcional)*

Un único ráster con valores de susceptibilidad a la licuefacción (escala 1–4). Se usa solo cuando hay amenaza sísmica; modifica la función de vulnerabilidad aplicada a cada elemento.

### (9) Polígono de cambio climático — `mod_tp_poly` *(opcional)*

Polígono vectorial con campos `TP###S#M` que contienen los períodos de retorno modificados por escenario climático (p. ej. RCP 8.5 para 2080). La herramienta calcula versiones adicionales de DAE y PAE bajo cada escenario.

## Parámetros de vulnerabilidad

### (10) Base de datos FVU — `vulner_data` *(obligatorio)*

Archivo CSV (`FVU_BSA_V3.csv`) con las funciones de vulnerabilidad física (daño) y de tránsito (tiempo de interrupción). El formato de cada línea es:

```
taxonomy,[intensidades],[valores_porcentaje]
```

**Ejemplo:** `FL_RMD_H_TRNP,[0,0.2,0.5,1.5,50],[0,1,2,20,20]`

## Parámetros de operaciones y economía

### (11) Base de costos operativos — `operat_data` *(opcional)*

CSV con los costos operativos y la ocupación promedio por taxonomía de vehículo (T9–T15). Necesario para el cálculo de PAE.

| Campo | Descripción |
|-------|-------------|
| `taxonomy` | Tipo de vehículo: T9 (pick-up), T10 (automóvil), T11 (bus), T12 (camión ligero), T13 (camión mediano), T14 (camión pesado), T15 (camión articulado). |
| `COV` | Costo de operación vehicular (USD/km). |
| `OCU` | Ocupantes promedio por vehículo (personas). |

### (12) PIB per cápita por día — `gdppca_doub` *(opcional)*

Valor escalar del Producto Interno Bruto per cápita diario del país, expresado en USD. Se usa para valorar el tiempo de viaje perdido por usuarios durante la interrupción del servicio vial.

**Ejemplo (Costa Rica):** `45249.62`

!!! tip "Cálculo del PIB per cápita por día"
    Si solo se dispone del PIB per cápita anual, divídalo entre 365 para obtener el valor diario (p. ej., USD 16,500/año ÷ 365 ≈ USD 45.2/día). Confirme la unidad con el equipo de proyecto antes de ingresar el valor.

## Parámetros de segmentación

### (13) Longitud de segmento — `road_segme` *(obligatorio)*

Longitud en metros de los puntos de muestreo que la herramienta genera a lo largo de la red vial. Define la resolución espacial del análisis.

| Valor | Efecto |
|-------|--------|
| **10–30 m** | Alta resolución; mayor tiempo de procesamiento. Recomendado para corredores críticos. |
| **50 m** | Resolución estándar para análisis nacionales. |
| **100 m** | Baja resolución; procesamiento rápido. Solo para pruebas o redes muy extensas. |

**Ejemplo (Costa Rica):** `30`

!!! warning "Resolución vs. tiempo de cómputo"
    Para redes nacionales con miles de kilómetros, una segmentación de 10 m puede requerir varias horas de procesamiento. Se recomienda comenzar con 50 m y ajustar según los recursos disponibles.

## Parámetros de salida

La herramienta escribe automáticamente los resultados en la geodatabase `BSA2.gdb`, ubicada en el directorio del script:

| Salida | Contenido |
|--------|-----------|
| `roads_results_<timestamp>` | Red vial con campos DAE, PAE y Priority por tramo. |
| `bridges_results_<timestamp>` | Puentes con DAE, PAE y Priority individuales. |
| `tunnels_results_<timestamp>` | Túneles con DAE, PAE y Priority individuales. |
| `drainage_results_<timestamp>` | Elementos de drenaje con DAE, PAE y Priority. |

Los resultados se añaden automáticamente al mapa activo de ArcGIS Pro al finalizar la ejecución.
