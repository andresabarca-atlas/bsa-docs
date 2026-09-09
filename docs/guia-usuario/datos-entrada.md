# Datos de entrada

El BSA 2.0 requiere cuatro grupos de insumos: **(a) inventarios de activos / exposición**, **(b) mallas de amenaza**, **(c) vulnerabilidad y recuperación**, y **(d) criticidad y costos de operación**. Esta página describe cada conjunto con su descripción, formato, obligatoriedad y atributos principales.

---

## a) Inventarios de activos — Exposición

Estas capas representan la infraestructura vial susceptible de ser afectada por amenazas naturales. Todas deben estar en formato **shapefile** y proyectadas en el mismo SRC que los rásters de amenaza.

### Red vial (carreteras)

| Campo | Descripción | Tipo | Obligatorio |
|-------|-------------|------|-------------|
| `ID_TRAMO` | Identificador único del tramo | Long / String | Sí |
| `Nombre` | Nombre de la carretera o ruta | String | No |
| `Longitud` | Longitud del tramo en metros | Double | Sí |
| `Jerarquía` | Nivel de la vía (1 = primaria, 2 = secundaria, 3 = terciaria) | String | No |
| `ID_País` | Código del país (p. ej. CR, DO, SV) | String | No |
| `vul_f` | Código de taxonomía de vulnerabilidad para inundación | String | Sí |
| `vul_eq` | Código de taxonomía de vulnerabilidad para sismo | String | Sí (si hay amenaza sísmica) |
| `rep_cost_k` | Costo de reposición en miles de USD/metro de carretera | Double | Sí |
| `T9`–`T15` | TPDA por tipo de vehículo (pick-up, automóvil, bus, camiones) | Double | Sí (para PAE) |

- **Formato:** Shapefile de polilíneas (`.shp`)
- **Fuente:** Ministerios de Obras Públicas / Transporte; fuentes secundarias
- **Obligatoriedad:** Capa base; siempre requerida

### Puentes

| Campo | Descripción | Tipo |
|-------|-------------|------|
| `ID_TRAMO` | Relaciona el puente con su tramo vial | Long / String |
| `Nombre` | Nombre del puente | String |
| `País` | País de ubicación | String |
| `Puente` | Tipología estructural (vigas, armadura, etc.) | String |
| `Estado` | Condición de la infraestructura (Bueno / Regular / Malo) | String |
| `Año` | Año de construcción | Double |
| `vul_f` | Taxonomía de vulnerabilidad para inundación | String |
| `vul_eq` | Taxonomía de vulnerabilidad para sismo | String |
| `rep_cost` | Costo de reposición del puente en USD | Double |

- **Formato:** Shapefile de puntos (`.shp`)
- **Fuente:** Ministerios de Obras Públicas / Transporte; inventarios de campo
- **Obligatoriedad:** Opcional; si se provee, la herramienta calcula DAE y PAE por puente de forma independiente

### Túneles

Misma estructura de atributos que los puentes. El campo `rep_cost` corresponde al costo de reposición del túnel.

- **Formato:** Shapefile de puntos
- **Obligatoriedad:** Opcional

### Drenajes (alcantarillas y elementos de drenaje)

| Campo | Descripción | Tipo |
|-------|-------------|------|
| `ID_TRAMO` | Tramo vial al que pertenece el elemento | Long / String |
| `Drenaje` | Tipología (alcantarilla tubular, cajón, badén, cuneta, etc.) | String |
| `Estado` | Condición estructural | String |
| `Año` | Año de construcción | Double |
| `vul_f` | Taxonomía de vulnerabilidad para inundación | String |
| `rep_cost` | Costo de reposición en USD | Double |

- **Formato:** Shapefile de puntos
- **Obligatoriedad:** Opcional

---

## b) Mallas de amenaza

Las mallas de amenaza son **rásters GeoTIFF** que contienen, para cada celda, la intensidad del fenómeno asociada a un evento de diseño con un período de retorno (Tr) específico.

### Tipos de amenaza y medidas de intensidad

| Amenaza | ID | Medida de intensidad | Unidad |
|---------|----|---------------------|--------|
| Inundación fluvial | `ri` | Tirante hídrico (profundidad de agua) | metros |
| Inundación pluvial / costera | `pl` / `c` | Tirante hídrico | metros |
| Tsunami | `ts` | Altura de ola / tirante hídrico | metros |
| Sismo | `eq` | Aceleración Pico del Suelo (PGA) | g o gales |
| Licuefacción | `li` | Susceptibilidad (escala 1–4) | adimensional |

!!! note "Amenazas futuras"
    Los deslizamientos y huracanes están previstos para fases futuras del BSA 2.0, pero no están implementados en la versión actual.

### Convención de nombres de los rásters

La herramienta **extrae automáticamente el período de retorno (Tr) del nombre del archivo**. Es fundamental seguir la siguiente convención:

**Inundación histórica:**
```
{amenaza}_{h}_{país}_{Tr}.tif
```

**Inundación con cambio climático:**
```
{amenaza}_{cc}_{escenario}_{año}_{país}_{Tr}.tif
```

**Sismo:**
```
eq_{país}_{medida_intensidad}_{Tr}.tif
```

**Tsunami:**
```
ts_{país}_{Tr}.tif
```

**Licuefacción** (un único ráster, sin Tr):
```
li_{país}.tif
```

#### Códigos de identificación

| Componente | Código | Opciones |
|-----------|--------|---------|
| Amenaza | `{amenaza}` | `pl` (pluvial), `ri` (fluvial), `ts` (tsunami), `eq` (sismo), `li` (licuefacción) |
| Horizonte temporal | `{h}` / `{cc}` | `h` (histórico), `cc` (cambio climático) |
| Escenario climático | `{escenario}` | `rcp26`, `rcp45`, `rcp60`, `rcp85` |
| Año de proyección | `{año}` | p. ej. `2050`, `2080` |
| País | `{país}` | `AR`, `CR`, `DO`, `SV`, `GT`, `HN`, `MX`, `NI`, `PA`, etc. |
| Medida de intensidad (sismo) | `{medida}` | `PGA`, `SAT03`, `SAT06`, etc. |
| Período de retorno | `{Tr}` | Cualquier entero: `10`, `25`, `50`, `100`, `500`, `1000`, etc. |

#### Ejemplos de nombres válidos

| Archivo | Interpretación |
|---------|---------------|
| `ri_h_CR_100.tif` | Inundación fluvial, histórico, Costa Rica, Tr = 100 años |
| `pl_cc_rcp85_2080_DO_25.tif` | Inundación pluvial, cambio climático RCP8.5 año 2080, Rep. Dom., Tr = 25 años |
| `eq_CR_PGA_475.tif` | Sismo, Costa Rica, PGA, Tr = 475 años |
| `ts_DO_1500.tif` | Tsunami, Rep. Dom., Tr = 1500 años |
| `li_CR.tif` | Licuefacción, Costa Rica (sin Tr) |

- **Formato:** GeoTIFF (`.tif`)
- **Fuente:** Fuentes oficiales nacionales, plataformas multilaterales (p. ej. AIGHF, GloFAS, USGS ShakeMap)
- **Obligatoriedad:** Al menos un ráster de amenaza es obligatorio; los demás son opcionales según las amenazas presentes en el país

---

## c) Vulnerabilidad y recuperación

### Funciones de vulnerabilidad (FVU)

El archivo CSV de funciones de vulnerabilidad (`FVU_BSA_Vx.csv`) contiene las curvas de daño físico (RMD) y las curvas de tiempo de interrupción (T) para cada taxonomía de infraestructura y tipo de amenaza.

**Formato de cada línea:**
```
taxonomy,[intensidades],[valores_porcentaje]
```

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| `taxonomy` | Clave compuesta que identifica amenaza, tipo de curva, horizonte y tipología de infraestructura | `FL_RMD_H_TRNP` |
| `[intensidades]` | Lista de valores de intensidad (tirante en metros, PGA en g, etc.) | `[0,0.2,0.5,1.5,50]` |
| `[valores_porcentaje]` | Porcentaje medio de daño o tiempo de interrupción (horas ÷ 24) | `[0,1,2,20,20]` |

#### Estructura de la clave de taxonomía

La clave sigue el patrón `{amenaza}_{tipo_curva}_{horizonte}_{tipología}`:

| Prefijo | Significado |
|---------|------------|
| `FL_RMD_` | Inundación (Flood), curva de Daño Medio (Repair Mean Damage) |
| `FL_T_` | Inundación, curva de Tiempo de interrupción (Transit) |
| `EQ_RMD_LQ{n}_` | Sismo con licuefacción zona `n` (1–4), daño medio |
| `EQ_T_LQ{n}_` | Sismo con licuefacción zona `n`, tiempo de interrupción |

La parte final de la clave identifica la tipología de infraestructura (p. ej. `H_TRNP` = histórico, troncal pavimentada; `H_REGP` = histórico, regional pavimentada).

- **Formato:** CSV (`.csv`), codificación UTF-8
- **Fuente:** Literatura especializada, modelos analíticos, criterio experto, talleres técnicos
- **Obligatoriedad:** Siempre obligatorio

### Tiempos de rehabilitación

Base de datos con los tiempos estimados de rehabilitación por tipología de infraestructura y nivel de intensidad de amenaza. Se usa para escalar las pérdidas funcionales.

| Campo | Descripción | Tipo |
|-------|-------------|------|
| `Tipo` | Código único de tipología de infraestructura | String |
| `Pais` | País sin tilde ortográfica | String |
| `Int_inunda` | Medidas de intensidad de inundación (m) | Double |
| `Int_sismo` | Medidas de intensidad sísmica (gales) | Double |
| `T_int_inunda` | Tiempos de interrupción para inundación (horas) | Double |
| `T_int_sismo` | Tiempos de interrupción para sismo (horas) | Double |

- **Formato:** Tabla incluida en el archivo Excel de la ficha de datos de entrada (`IDB_InputData_BSA.xlsx`, hoja `Tiempo_rehab`)
- **Obligatoriedad:** Requerido para el cálculo de PAE

---

## d) Criticidad y costos de operación

### Costos operativos por tipo de vehículo

Archivo CSV (`OCO_BSA_{país}.csv`) con los parámetros de operación vehicular por taxonomía, usados para valorar las pérdidas funcionales.

| Campo | Descripción | Tipo |
|-------|-------------|------|
| `taxonomy` | Tipo de vehículo: T9, T10, T11, T12, T13, T14, T15 | String |
| `COV` | Costo de operación vehicular (USD/km por vehículo) | Double |
| `OCU` | Ocupantes promedio por vehículo (personas) | Double |

#### Taxonomías de vehículos

| Código | Tipo |
|--------|------|
| T9 | Pick-up |
| T10 | Automóvil |
| T11 | Autobús |
| T12 | Camión ligero |
| T13 | Camión mediano |
| T14 | Camión pesado |
| T15 | Camión articulado |

- **Formato:** CSV (`.csv`)
- **Fuente:** Ministerio de Hacienda o banca multilateral del país
- **Obligatoriedad:** Obligatorio si se quiere calcular PAE (debe acompañarse del PIB per cápita por día)

### PIB per cápita por día

Valor escalar en USD utilizado para valorar el tiempo de viaje perdido por los usuarios durante una interrupción vial.

| Campo | Descripción | Tipo |
|-------|-------------|------|
| `Id` | Identificador de la unidad administrativa de segundo nivel | String |
| `Pais` | País | String |
| `GDP_Cap` | PIB per cápita anual por unidad territorial (USD) | Double |

!!! tip "Cálculo del valor diario"
    La herramienta recibe el valor ya convertido a **por día**. Divida el PIB per cápita anual entre 365 antes de ingresarlo.

- **Formato:** Valor escalar (ingresado directamente en el parámetro 12 del toolbox)
- **Fuente:** Bancos centrales, Banco Mundial, CEPAL
- **Obligatoriedad:** Obligatorio si se provee la base de costos operativos (parámetro 11)

---

## Resumen de capas por componente

| Componente | Capa | Importancia |
|-----------|------|-------------|
| Exposición | Red vial (polilíneas) | Core — obligatoria |
| Exposición | Puentes (puntos) | Core — recomendada |
| Exposición | Drenajes (puntos) | Core — recomendada |
| Exposición | Nombre de corredores | Core |
| Exposición | Estado de calzada | Core |
| Exposición | Fallas de pavimento | Core |
| Exposición | Nivel de servicio | Core |
| Exposición | TPDA (tránsito) | Core — obligatorio para PAE |
| Exposición | Pasos fronterizos | Referencia |
| Exposición | Puertos | Referencia |
| Exposición | Aeropuertos | Referencia |
| Exposición | Nodos de producción/exportación | Referencia |
| Exposición | Cadenas logísticas | Referencia |
| Vulnerabilidad | Funciones de daño (FVU CSV) | Core — obligatoria |
| Vulnerabilidad | Tiempos de rehabilitación | Core — obligatoria |
| Operaciones | PIB per cápita | Core — para PAE |
| Operaciones | Costos operativos (OCO CSV) | Core — para PAE |
| Amenaza | Inundación fluvial (rásters por Tr) | Core |
| Amenaza | Tsunami (rásters por Tr) | Core |
| Amenaza | Sismo (rásters por Tr) | Core |
| Amenaza | Inundación pluvial (rásters por Tr) | Core |
| Amenaza | Inundación fluvial — cambio climático | Referencia |
| Amenaza | Zonas climáticas CC | Referencia |
