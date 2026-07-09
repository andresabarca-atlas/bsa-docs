# Metrics Exploration

This page explains how to read and interpret each component of the dashboard to prioritize investments in transport infrastructure.

---

## General View tab

The **General View** tab integrates four functional zones in a single screen. Each is described below.

### Top indicators

<!-- FALTA CAPTURA: barra de indicadores superiores con Length Assessed, EAD Total y EAL Total -->

The horizontal bar at the top of the screen shows three global metrics of the evaluated network:

| Indicator | Spanish name | Description |
|-----------|-------------|-------------|
| **Length Assessed** | Longitud evaluada | Total length (km) of the road network included in the analysis |
| **EAD Total** | DAE Total — Daño Anual Esperado | Average annual monetary value of direct physical damage to infrastructure, integrated across all evaluated return periods and hazards |
| **EAL Total** | PAE Total — Pérdida Anual Esperada | Average annual monetary value of economic losses from traffic and road service interruption |

!!! tip "EAD vs. EAL"
    **EAD** (Expected Annual Damage / *DAE*) quantifies the direct physical impact on the road — the cost of repairing or replacing damaged infrastructure —. **EAL** (Expected Annual Loss / *PAE*) quantifies the functional and economic losses from the interruption of transport service. Both metrics are complementary and should be read together.

---

### "Prioritized Assets" panel (left)

<!-- FALTA CAPTURA: panel de activos priorizados con sub-pestañas Roads, Drainage, Tunnels, Bridges -->

The left panel presents the **ranking of prioritized assets** according to their risk level. It is organized into four sub-tabs by asset type:

- **Roads** — Road segments
- **Drainage** — Drainage infrastructure
- **Tunnels** — Tunnels
- **Bridges** — Bridges

Each list item shows:

- **Route code** — segment identifier according to the national road network.
- **Name** — designation of the segment or asset.
- **Economic value** — monetary risk indicator (EAD or EAL depending on configuration) that justifies its ranking position.

!!! note "How is prioritization done?"
    The ranking integrates physical damage (EAD), functional loss (EAL), and the criticality of each asset in the network. A segment with high traffic volume connecting isolated areas will tend to appear higher in the list even if its physical damage is moderate.

---

### Interactive map (center)

<!-- FALTA CAPTURA: mapa interactivo con activos priorizados y simbología graduada -->

The central map georeferenced the prioritized assets over the territory. Available tools:

| Tool | Function |
|------|----------|
| **Zoom** | Zoom in / out |
| **Layers** | Activate or deactivate thematic layers |
| **Basemap** | Toggle between satellite imagery, topography, or other backgrounds |
| **Legend** | Consult the color classification by risk level |
| **Search** | Locate a segment or asset by name or code |

The **graduated symbology** assigns different colors and sizes to assets according to their risk category. Assets with the highest EAD or EAL appear highlighted. Clicking on an asset in the map displays a detail card with its attributes.

---

### "Comparison of EAL vs. EAD" panel (right)

<!-- FALTA CAPTURA: panel derecho con gráfico de anillo por amenaza y resultados de túneles -->

The right panel presents graphic comparisons between the different risk components. It includes:

#### Chart "Total Expected Annual Loss by Hazard"

Ring chart that breaks down the **total EAL** by hazard type. The hazards represented are:

- Fluvial flooding
- Coastal / pluvial flooding
- Tsunami
- Earthquake

The area of each segment is proportional to that hazard's contribution to the total EAL. This chart answers the question: *Which hazard dominates risk in this road network?*

#### Tunnel results ("Tunnels results")

Specific section for tunnel results, with their EAD legend. Tunnels have particular vulnerability and criticality characteristics that justify their separate visualization.

---

### "Top 5 Highest-Criticality Segments" table (bottom)

<!-- FALTA CAPTURA: tabla inferior con los 5 segmentos de mayor criticidad -->

The table at the bottom of the screen lists the **five segments with the highest criticality** of the entire evaluated network, with the following columns:

| Column | Description |
|--------|-------------|
| **TRAMO_ATT** | Road segment identifier code |
| **LONGITUD** | Segment length (km or m) |
| **LAYER** | Asset type (road, tunnel, bridge, etc.) |
| **NOMBRE_ATT** | Descriptive name of the segment or route |
| **RD_Tipo** | Road type according to national classification |
| **DAE_total** | Accumulated Expected Annual Damage of the segment |
| **PAE_total** | Accumulated Expected Annual Loss of the segment |

This table is a direct input for intervention planning: the segments that appear here are the priority candidates for detailed studies and mitigation measure design.

---

## Loss Curves tab

<!-- FALTA CAPTURA: pestaña Loss Curves con curva de excedencia de pérdidas -->

The **Loss Curves** tab shows the **Loss Exceedance Curves (LEC)** of the evaluated portfolio. A LEC relates the amount of losses to the annual frequency with which it is expected to exceed that amount.

### How to read an exceedance curve

```
Annual exceedance
frequency
    |
1/10│ ·
    │   ·
1/100│     ·
    │        ·
1/500│           ·
    └────────────────────
              Losses ($)
```

- **Horizontal axis (X):** magnitude of losses, expressed in local currency.
- **Vertical axis (Y):** annual exceedance frequency (inverse of return period). A frequency of 1/100 corresponds to an event with a return period of 100 years.
- **Reading:** a point on the curve indicates that, on average, the loss associated with that point will be *equaled or exceeded* with the frequency indicated on the Y axis.

### Use for investment prioritization

| Indicator | How to use it |
|-----------|--------------|
| **Area under the curve** | Equivalent to EAL (Expected Annual Loss). The larger the area, the higher the average annual risk. |
| **Slope of the curve** | A curve with a steep slope indicates that a small increase in return period produces much higher losses. |
| **PML (Probable Maximum Loss)** | Point on the curve corresponding to the design event (e.g., Tr = 500 years). Defines the extreme scenario for sizing reserves or protection measures. |

!!! warning "Scale limitation"
    The LECs on the dashboard represent the risk **aggregated across the entire evaluated network**. For analysis at the individual segment level, consult the result files generated by the BSA 2.0 tool (see [Results](../guia-usuario/resultados.md)).
