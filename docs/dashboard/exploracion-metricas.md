# Exploración de métricas

Esta página explica cómo leer e interpretar cada componente del dashboard para priorizar inversiones en infraestructura de transporte.

---

## Pestaña General View

La pestaña **General View** integra cuatro zonas funcionales en una sola pantalla. A continuación se describe cada una.

### Indicadores superiores

<!-- FALTA CAPTURA: barra de indicadores superiores con Length Assessed, EAD Total y EAL Total -->

La barra horizontal en la parte superior de la pantalla muestra tres métricas globales de la red evaluada:

| Indicador | Nombre en español | Descripción |
|-----------|-------------------|-------------|
| **Length Assessed** | Longitud evaluada | Extensión total (km) de la red vial incluida en el análisis |
| **EAD Total** | DAE Total — Daño Anual Esperado | Valor monetario promedio anual de los daños físicos directos a la infraestructura, integrado sobre todos los períodos de retorno y amenazas evaluadas |
| **EAL Total** | PAE Total — Pérdida Anual Esperada | Valor monetario promedio anual de las pérdidas económicas por interrupción del tránsito y del servicio vial |

!!! tip "DAE vs. PAE"
    El **DAE** (Daño Anual Esperado / EAD) cuantifica el impacto físico directo sobre la vía —el costo de reparar o reponer la infraestructura dañada—. El **PAE** (Pérdida Anual Esperada / EAL) cuantifica las pérdidas funcionales y económicas por la interrupción del servicio de transporte. Ambas métricas son complementarias y deben leerse en conjunto.

---

### Panel "Prioritized Assets" (izquierda)

<!-- FALTA CAPTURA: panel de activos priorizados con sub-pestañas Roads, Drainage, Tunnels, Bridges -->

El panel izquierdo presenta el **ranking de activos priorizados** según su nivel de riesgo. Se organiza en cuatro sub-pestañas por tipo de activo:

- **Roads** — Segmentos de carretera
- **Drainage** — Infraestructura de drenaje
- **Tunnels** — Túneles
- **Bridges** — Puentes

Cada elemento de la lista muestra:

- **Código de ruta** — identificador del tramo según la red vial nacional.
- **Nombre** — denominación del tramo o activo.
- **Valor económico** — indicador de riesgo monetario (DAE o PAE según configuración) que fundamenta la posición en el ranking.

!!! note "¿Cómo se prioriza?"
    El ranking integra daño físico (DAE), pérdida funcional (PAE) y la criticidad de cada activo en la red. Un tramo con alto volumen de tránsito que conecta zonas aisladas tenderá a aparecer más arriba en la lista aunque su daño físico sea moderado.

---

### Mapa interactivo (centro)

<!-- FALTA CAPTURA: mapa interactivo con activos priorizados y simbología graduada -->

El mapa central georreferencia los activos priorizados sobre el territorio. Funciones disponibles:

| Herramienta | Función |
|-------------|---------|
| **Zoom** | Acercar / alejar la vista |
| **Capas** | Activar o desactivar capas temáticas |
| **Mapa base** | Alternar entre imágenes satelitales, topografía u otros fondos |
| **Leyenda** | Consultar la clasificación cromática del nivel de riesgo |
| **Búsqueda** | Localizar un tramo o activo por nombre o código |

La **simbología graduada** asigna colores y tamaños distintos a los activos según su categoría de riesgo. Los activos con mayor DAE o PAE aparecen resaltados. Al hacer clic sobre un activo en el mapa, se despliega una ficha con sus atributos detallados.

---

### Panel "Comparison of EAL vs. EAD" (derecha)

<!-- FALTA CAPTURA: panel derecho con gráfico de anillo por amenaza y resultados de túneles -->

El panel derecho presenta comparaciones gráficas entre los distintos componentes del riesgo. Incluye:

#### Gráfico "Total Expected Annual Loss by Hazard"

Gráfico de anillo que desglosa el **PAE total** (EAL) por tipo de amenaza. Las amenazas representadas son:

- Inundación fluvial
- Inundación costera / pluvial
- Tsunami
- Sismo

El área de cada segmento es proporcional a la contribución de esa amenaza al PAE total. Este gráfico responde a la pregunta: *¿qué amenaza domina el riesgo en esta red vial?*

#### Resultados de túneles ("Tunnels results")

Sección específica para los resultados de túneles, con su leyenda de DAE. Los túneles tienen particularidades de vulnerabilidad y criticidad que justifican su visualización separada.

---

### Tabla "Top 5 Highest-Criticality Segments" (inferior)

<!-- FALTA CAPTURA: tabla inferior con los 5 segmentos de mayor criticidad -->

La tabla en la parte inferior de la pantalla lista los **cinco segmentos con mayor criticidad** de toda la red evaluada, con las siguientes columnas:

| Columna | Descripción |
|---------|-------------|
| **TRAMO_ATT** | Código identificador del tramo vial |
| **LONGITUD** | Longitud del segmento (km o m) |
| **LAYER** | Tipo de activo (carretera, túnel, puente, etc.) |
| **NOMBRE_ATT** | Nombre descriptivo del tramo o ruta |
| **RD_Tipo** | Tipo de vía según la clasificación nacional |
| **DAE_total** | Daño Anual Esperado acumulado del tramo |
| **PAE_total** | Pérdida Anual Esperada acumulada del tramo |

Esta tabla es un insumo directo para la planificación de intervenciones: los segmentos que aparecen aquí son los candidatos prioritarios para estudios de detalle y diseño de medidas de mitigación.

---

## Pestaña Loss Curves

<!-- FALTA CAPTURA: pestaña Loss Curves con curva de excedencia de pérdidas -->

La pestaña **Loss Curves** muestra las **curvas de excedencia de pérdidas (CEP)** del portafolio evaluado. Una CEP relaciona el monto de las pérdidas con la frecuencia anual con que se espera superar ese monto.

### Cómo leer una curva de excedencia

```
Frecuencia anual
de excedencia
    |
1/10│ ·
    │   ·
1/100│     ·
    │        ·
1/500│           ·
    └────────────────────
              Pérdidas ($)
```

- **Eje horizontal (X):** magnitud de las pérdidas, expresada en la moneda local.
- **Eje vertical (Y):** frecuencia anual de excedencia (inverso del período de retorno). Una frecuencia de 1/100 corresponde a un evento con período de retorno de 100 años.
- **Lectura:** un punto de la curva indica que, en promedio, la pérdida asociada a ese punto será *igualada o superada* con la frecuencia indicada en el eje Y.

### Uso para priorización de inversiones

| Indicador | Cómo usarlo |
|-----------|-------------|
| **Área bajo la curva** | Equivale al PAE (Pérdida Anual Esperada). A mayor área, mayor riesgo promedio anual. |
| **Pendiente de la curva** | Una curva con pendiente pronunciada indica que un aumento pequeño en el período de retorno produce pérdidas mucho mayores. |
| **PML (Pérdida Máxima Probable)** | Punto en la curva correspondiente al evento de diseño (p. ej. Tr = 500 años). Define el escenario extremo para el dimensionamiento de reservas o medidas de protección. |

!!! warning "Limitación de escala"
    Las CEP del dashboard representan el riesgo **agregado de toda la red** evaluada. Para análisis a nivel de tramo individual, consulte los archivos de resultados generados por la herramienta BSA 2.0 (ver [Resultados](../guia-usuario/resultados.md)).
