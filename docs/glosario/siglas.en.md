# Acronym Dictionary

Acronyms and abbreviations used in the BSA 2.0 methodology, tool, and documentation. Listed alphabetically.

*Primary source: Table 4.1 of BSA 2.0 Concept Report. EAD and EAL are added to align with the project's terminology rules.*

---

| Acronym | Full name | Technical description |
|---------|-----------|----------------------|
| **BSA** | Blue Spot Analysis | Tool for identifying, prioritizing, and recommending solutions for critical risk points (*Blue Spots*) from natural hazards in road infrastructure networks. |
| **EAD** | Expected Annual Damage | Average annual monetary value of direct physical damage to road infrastructure, integrated across all evaluated return periods. Equivalent to *Daño Anual Esperado* (DAE) in Spanish. Measures physical impact on the road, not loss from service interruption. |
| **EAL** | Expected Annual Loss | Average annual monetary value of functional and economic losses from traffic or road service interruption, integrated across all evaluated return periods. Equivalent to *Pérdida Anual Esperada* (PAE) in Spanish. Measures loss from service interruption, not direct physical damage. |
| **EE** | Exposed Element (*Elemento Expuesto*) | Discretized road segment (represented as a point or line in a shapefile) on which impacts per event are calculated. |
| **LEC** | Loss Exceedance Curve (*Curva de Excedencia de Pérdidas* — CEP) | Graphical representation of the relationship between probability of occurrence and loss magnitude. The area under the curve equals the EAL. |
| **MDR** | Mean Damage Ratio (*Relación Media de Daño* — RMD) | Expected value of physical damage for a road segment given an event, according to its type and structural condition. |
| **MDRi / DMVi** | Road Mean Damage – Infrastructure | Expected physical damage for a road segment given a hazard event, according to its type and structural condition. |
| **MDRt / PMVt** | Road Mean Loss – Transit | Expected functional or economic loss from traffic disruption given a hazard event. |
| **PML** | Probable Maximum Loss (*Pérdida Máxima Probable*) | Estimated loss for a specific design event (e.g., Tr = 500 years). Represents the extreme reference scenario for sizing reserves or high-standard structural measures. |
| **VF / FVU** | Vulnerability Function (*Función de Vulnerabilidad*) | Functional relationship between hazard intensity (TH, V) and the expected degree of damage for a road asset type. |
| **VF-traffic / FVU tráfico** | Transit Vulnerability Function | Function that models the event's impact on operability or economic transit value of the affected segment. |
| **TH** | Water Depth (*Tirante Hídrico*) | Depth of the water sheet during a flood event, expressed in meters. Intensity parameter in vulnerability functions. |
| **Tr** | Return Period (*Período de Retorno*) | Statistical frequency with which an event's magnitude is expected to be equaled or exceeded. Expressed in years (e.g., Tr = 100 years means an annual exceedance frequency of 1%). |
| **V** | Velocity (*Velocidad*) | Velocity of surface flow during a flood event, in meters per second. Complementary parameter to TH in vulnerability functions. |
| **VFi** | Physical Infrastructure Value (*Valor Físico de la Infraestructura*) | Estimated replacement cost of the exposed road segment, by typology and length. Basis for EAD calculation. |
| **VFt** | Economic Transit Value (*Valor Económico del Tránsito*) | Economic value associated with transit per road segment (vehicles, cargo, travel time). Basis for EAL calculation. |
| **Crit. Module / Mód. Criticidad** | Functional Transit Criticality Module | BSA 2.0 tool module that estimates the functional impact of a road segment's disruption on the network and transit. |
| **Exp. Module / Mód. Exposición** | Exposure Module | Georeferenced database characterizing all exposed elements susceptible to damage or loss. |
| **Vuln. Module / Mód. Vuln. Física** | Physical Vulnerability Module | Tool module containing the set of vulnerability functions corresponding to each identified road segment and transit typology in the exposure model. |

---

!!! tip "EAD vs. EAL"
    In BSA 2.0 documentation, English terms (EAD, EAL) are the primary names and Spanish acronyms (DAE, PAE) are their equivalents. **EAD = DAE** (direct physical damage) and **EAL = PAE** (loss from service interruption). These two metrics must not be confused: they quantify distinct and complementary types of impact.
