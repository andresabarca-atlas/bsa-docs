# Resultados

## Capas de salida

| Patrón | Contenido |
|---|---|
| `roads_results_<fecha_hora>` | Carreteras con daño, DAE, PAE, DAE de activos asociados y prioridad. |
| `bridges_results_<fecha_hora>` | Puentes con daño, DAE, PAE y prioridad. |
| `tunnels_results_<fecha_hora>` | Túneles con daño, DAE, PAE y prioridad. |
| `drainage_results_<fecha_hora>` | Drenajes con daño, DAE, PAE y prioridad. |

## Campos principales

| Campo | Significado |
|---|---|
| `damage_{amenaza}_{TR}` | Daño monetario del escenario. |
| `loss_{amenaza}_{TR}` | Pérdida operacional del escenario. |
| `DAE_{amenaza}` | Daño anual esperado de una amenaza. |
| `DAE` | Suma de DAE de la geometría. |
| `DAE_bridge`, `DAE_tunnel`, `DAE_drainage` | DAE puntual agregado al tramo. |
| `DAE_total` | DAE de la carretera y sus activos asociados. |
| `PAE_{amenaza}` | Pérdida anual esperada de una amenaza. |
| `PAE_total` | Suma de PAE por amenaza. |
| `Priority` | En carreteras, `DAE_total + PAE_total`. |

La versión actual no crea un campo PML. Los daños o pérdidas de un TR específico son resultados por escenario, no PML calculada.

## Cambio de frecuencia climática

Cuando se carga `Climate layer`, se crean campos como `TP_TR_MODS_{escenario}`, `DAE_river_mod_{escenario}`, `DAE_coast_mod_{escenario}`, `PAE_river_mod_{escenario}`, `PAE_coast_mod_{escenario}`, `DAE_total_mod_{escenario}`, `PAE_total_mod_{escenario}` y `Priority_mod_{escenario}`.

Estos campos reutilizan los daños y tiempos de las mallas históricas y cambian su frecuencia; no representan nuevas intensidades.

## Validación

Ordene y simbolice valores sólo después de verificar moneda, año base, nulos, rangos y suma de campos. Una prioridad alta indica mayores consecuencias económicas anuales esperadas, no una orden automática de inversión.

