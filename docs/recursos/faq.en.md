# Frequently Asked Questions

---

## About the tool and requirements

??? question "What software do I need to use BSA 2.0?"

    BSA 2.0 requires **ArcGIS Pro** (version 3.0 or higher) with an active license, as the tool is distributed as a native *toolbox* (`.atbx`) for that platform. Additionally, Python 3 must be available in the ArcGIS Pro environment (included by default). No other hydraulic modeling or additional GIS software is required to run the tool; hazard data must be prepared externally and loaded as inputs.

??? question "Does BSA 2.0 include the generation of flood maps?"

    No. BSA 2.0 is a **risk analysis and prioritization** tool, not a hydraulic modeling one. Flood maps (depth, velocity) for each return period must be obtained from prior hydrological and hydraulic studies and loaded as input data. The tool consumes them to calculate damage and loss on the exposed infrastructure.

---

## About input data

??? question "How should I organize the input data?"

    The tool requires a **geodatabase** with the georeferenced road network and a **parameter sheet** in Excel format (22 sheets). The geodatabase must include road segments as point or linear elements, with attributes for road type, length, and replacement value. Hazard maps must be in raster format and projected in the same coordinate system as the road network. See the [Data organization](../getting-started/organizacion-datos.md) section for the detailed structure.

??? question "What licenses are required for hazard data (flooding, earthquake, etc.)?"

    BSA 2.0 is neutral regarding the source of hazard data. Open-access data (OpenStreetMap, GEBCO, USGS, GloFAS, OpenQuake, etc.) or proprietary data from existing hydrological and hydraulic studies can be used. The project team has primarily worked with national and international open-access data, but the quality and scale of inputs directly impacts the precision of results.

---

## About the methodology and results

??? question "What is the difference between EAD and EAL?"

    They are two complementary metrics that quantify different types of impact:

    | Metric | Full name | What it measures |
    |--------|-----------|-----------------|
    | **EAD** (*DAE*) | Expected Annual Damage / *Daño Anual Esperado* | Direct physical damage to infrastructure: cost of repairing or replacing the damaged road |
    | **EAL** (*PAE*) | Expected Annual Loss / *Pérdida Anual Esperada* | Functional and economic loss from traffic or road service interruption |

    A segment may have low EAD (physical damage is small) but high EAL if it connects high-traffic areas or is the only available route in an emergency.

??? question "Which natural hazards does BSA 2.0 cover in its current version?"

    The current version of BSA 2.0 has implemented modules for:

    - Fluvial flooding
    - Pluvial / coastal flooding
    - Earthquake
    - Tsunami
    - Liquefaction

    The **landslides** and **hurricanes** modules are planned for future phases of the project and are not available in the current version.

??? question "At what scale does BSA 2.0 work?"

    BSA 2.0 is designed for analysis at **national or regional scale**. It is not oriented toward the design of individual works or site-specific analysis. Its purpose is to generate prioritization rankings that guide the distribution of investments across multiple assets of a complete road network.

??? question "What is the Probable Maximum Loss (PML) and how is it used?"

    The **PML** (Probable Maximum Loss) is the estimated loss associated with a specific design event, generally corresponding to a return period of 500 years. Unlike EAD and EAL (which are annual averages), PML represents an extreme scenario useful for sizing contingency funds, insurance, or high-standard structural measures.

---

## About application in new countries

??? question "How is BSA 2.0 applied to a new country?"

    Implementation in a new country follows these main steps:

    1. **Hazard data collection:** flood maps, seismic hazard curves, etc., for the required return periods (e.g., Tr = 10, 25, 50, 100, 200, 500 years).
    2. **Road inventory:** georeferenced road network database with typologies, lengths, and replacement costs.
    3. **Traffic parameters:** traffic volumes (AADT), travel time values, and cargo values.
    4. **Excel sheet configuration:** complete the 22 parameter sheets with local values.
    5. **Tool execution:** run the modules sequentially (hazard → exposure → vulnerability → criticality → risk).
    6. **Dashboard publication:** load results to ArcGIS Online and configure the dashboard.

    To access the detailed guide, contact the project team at [MARIAESC@IADB.ORG](mailto:MARIAESC@IADB.ORG).

??? question "Is BSA 2.0 free to use?"

    Not at this stage. The project is distributed under the **IDB AM-331-A3 license** and is not publicly available. Access to the tool and data is restricted to teams authorized by the Inter-American Development Bank. See the [License](../licencia.md) page for full terms.

---

## About the dashboard

??? question "Can I access the dashboard without an ArcGIS account?"

    The dashboards are published as ArcGIS Experience Builder applications. In most cases, they are publicly accessible from any browser without an account. However, some advanced editing or analysis functions may require an IDB institutional account on ArcGIS Online.

??? question "Do the dashboard values update automatically?"

    No. The dashboard reflects the results of the last BSA 2.0 model run loaded to ArcGIS Online. To update results (for example, when incorporating new hazard data or expanding the evaluated network), it is necessary to run the tool again and reload the results in the service.
