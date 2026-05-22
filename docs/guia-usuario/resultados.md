# Resultados

Al finalizar la ejecución del toolbox BSA2, la herramienta genera una geodatabase de archivo (`BSA2.gdb`) con una capa de resultados por cada componente de exposición provisto. Esta página describe los productos de salida y cómo interpretarlos para la priorización de inversiones.

## Capas de salida

| Capa | Contenido |
|------|-----------|
| `roads_results_<timestamp>` | Red vial con DAE, PAE y Priority por tramo. Incluye los DAE de componentes (puentes, túneles, drenajes) agregados al tramo correspondiente. |
| `bridges_results_<timestamp>` | Puentes con DAE, PAE y Priority individuales. |
| `tunnels_results_<timestamp>` | Túneles con DAE, PAE y Priority individuales. |
| `drainage_results_<timestamp>` | Elementos de drenaje con DAE, PAE y Priority. |

El `<timestamp>` corresponde a la fecha y hora de ejecución en formato `YYYYMMDD_HHMMSS` (p. ej. `roads_results_20260413_172736`). Esto permite mantener el historial de múltiples corridas sin sobreescribir resultados anteriores.

## Métricas de salida por tramo

### DAE — Daño Anual Esperado

El **DAE** (*Expected Annual Damage*, EAD) representa el **daño físico directo** anualizado sobre la infraestructura, expresado en USD por año. Es la integral de la curva de excedencia de daños:

$$
\text{DAE} = \int_0^1 D(p) \, dp \approx \sum_{i} D_i \cdot \Delta p_i
$$

donde $D_i$ es el daño estimado para el período de retorno $Tr_i$ y $\Delta p_i$ es la diferencia de probabilidades anuales de excedencia entre Trs consecutivos.

| Campo | Descripción |
|-------|-------------|
| `DAE` | DAE total de la vía (solo infraestructura vial, sin componentes) |
| `DAE_{amenaza}` | DAE desagregado por amenaza (p. ej. `DAE_river`, `DAE_earthquake`) |
| `DAE_bridge` | DAE de los puentes del tramo, agregado al nivel de `ID_TRAMO` |
| `DAE_tunnel` | DAE de los túneles del tramo |
| `DAE_drainage` | DAE de los drenajes del tramo |
| `DAE_total` | DAE combinado: vía + puentes + túneles + drenajes |

### PAE — Pérdida Anual Esperada

La **PAE** (*Expected Annual Loss*, EAL) representa la **pérdida económica funcional** anualizada debida a la interrupción del tránsito, expresada en USD por año. Se calcula multiplicando el nivel de interrupción funcional (derivado de la curva-T de vulnerabilidad) por el valor económico diario del tránsito (`DLT`) y anualizado de forma similar al DAE.

| Campo | Descripción |
|-------|-------------|
| `PAE_total` | PAE total por el tramo (suma de todas las amenazas) |
| `PAE_{amenaza}` | PAE desagregado por amenaza |

!!! note "Distinción DAE vs PAE"
    El **DAE** mide el costo de reparar la infraestructura dañada. El **PAE** mide las pérdidas económicas por la interrupción del flujo vehicular mientras la vía está fuera de servicio. Ambas métricas son complementarias y necesarias para una evaluación de riesgo completa.

### PML — Pérdida Máxima Probable

La **PML** (*Probable Maximum Loss*) corresponde al daño o pérdida esperados para un **evento de diseño específico** (generalmente Tr = 500 años). Se obtiene leyendo el valor del campo `damage_{amenaza}_500` o `loss_{amenaza}_500` de la capa de resultados.

### Priority — Índice de Priorización

El campo `Priority` es el indicador sintético de riesgo usado para el ranking:

$$
\text{Priority} = \text{DAE\_total} + \text{PAE\_total}
$$

Un valor mayor de `Priority` indica mayor riesgo combinado (daño físico + pérdida funcional) y mayor urgencia de intervención.

!!! tip "Uso en priorización"
    Para generar el mapa de priorización, simbolice la capa `roads_results_*` usando el campo `Priority` como valor de simbología (p. ej. simbología graduada por grosor de línea o escala de colores). Los tramos con mayor `Priority` son los candidatos prioritarios para intervención.

## Campos intermedios

Además de los campos agregados, las capas de resultados incluyen los campos de daño y pérdida por evento, útiles para análisis avanzados:

| Campo | Descripción |
|-------|-------------|
| `damage_{amenaza}_{Tr}` | Daño estimado (USD) para la amenaza y el Tr específico |
| `loss_{amenaza}_{Tr}` | Pérdida funcional (USD) para la amenaza y el Tr específico |

Estos campos permiten construir manualmente la curva de excedencia de pérdidas (CEP) para cualquier tramo individual.

## Campos de cambio climático (si aplica)

Si se proveyó el polígono de modificación climática (parámetro 9), la capa incluye campos adicionales por escenario:

| Campo | Descripción |
|-------|-------------|
| `DAE_river_mod_{scen}` | DAE de inundación fluvial con Trs modificados por el escenario `scen` |
| `DAE_coast_mod_{scen}` | DAE de inundación costera modificado |
| `PAE_river_mod_{scen}` | PAE de inundación fluvial modificada |
| `PAE_coast_mod_{scen}` | PAE de inundación costera modificada |
| `DAE_mod_{scen}` | DAE total bajo el escenario climático |
| `PAE_total_mod_{scen}` | PAE total bajo el escenario climático |
| `Priority_mod_{scen}` | Priority bajo el escenario climático |
| `TP_TR_MODS_{scen}` | Texto con el mapeo TP→TR aplicado (p. ej. `TP25_TR10; TP100_TR50`) |

## Interpretación para la toma de decisiones

Los resultados del BSA 2.0 permiten:

1. **Identificar tramos críticos:** Ordenar la red vial por `Priority` de mayor a menor identifica los segmentos con mayor riesgo combinado.

2. **Desagregar por amenaza:** Los campos `DAE_{amenaza}` y `PAE_{amenaza}` permiten identificar cuál amenaza domina el riesgo en cada zona, informando el tipo de medida de mitigación más apropiada.

3. **Cuantificar beneficios de intervención:** Si se aplican medidas de reducción de riesgo, una segunda corrida con parámetros de vulnerabilidad reducidos permite estimar la reducción en DAE y PAE.

4. **Comparar escenarios climáticos:** Los campos `_mod_{scen}` permiten comparar el riesgo actual con el proyectado bajo diferentes escenarios de cambio climático.

5. **Alimentar el dashboard:** Las métricas de salida se cargan al dashboard del BID, donde se visualizan de forma interactiva a nivel nacional y regional.

## Archivo .loc de trazabilidad

Junto con los resultados, la herramienta guarda un archivo de configuración en `Loc/run_config_<timestamp>.loc` con los parámetros exactos usados en esa corrida. Este archivo permite reproducir el análisis o auditar la configuración en caso de revisión posterior.

Ejemplo de contenido de un archivo `.loc`:

```
roads_path=crc_RVN_WGS84
bridge_path=crc_rvn_puentes2
fl_rive_raw=ri_h_CR_10.tif;ri_h_CR_100.tif;...
earthqu_raw=EQ_CR_PGA_100.tif;EQ_CR_PGA_475.tif;...
vulner_data=C:\...\FVU_BSA_V3.csv
gdppca_doub=45249.62
road_segme=30
```
