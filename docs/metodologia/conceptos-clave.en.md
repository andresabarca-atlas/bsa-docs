# Key Concepts

This page is the conceptual reference for the site. The terms and metrics used throughout the BSA 2.0 methodology are defined here. Familiarity with these definitions is essential for correctly interpreting results and documentation.

---

## The four components of risk

### Hazard

Latent danger that a physical event of natural origin — or accidentally induced by human action — occurs with sufficient severity to cause damage and losses to infrastructure, assets, livelihoods, or environmental services.

In BSA 2.0, hazard is represented through **raster grids** containing intensity values associated with different return periods. Intensity measures vary by hazard type:

| Hazard | Intensity measure | Symbol |
|---|---|---|
| Fluvial / pluvial / coastal flooding | Water depth | TH |
| Fluvial / pluvial / coastal flooding | Mean flow velocity | V |
| Earthquake | Peak Ground Acceleration | PGA |
| Landslide *(future phase)* | Deposit depth / movement velocity | LD |
| Hurricane *(future phase)* | Maximum wind speed | WS |

### Exposure

The presence of people, services, assets, and infrastructure that, due to their location, can be affected by the manifestation of a hazard. In BSA 2.0, exposure is modeled as a georeferenced inventory of the road network, called the **exposure model**.

Each exposed element (EE) is a representative point of a road segment, with attributes including its physical value (**VFi**) and its transit economic value (**VFt**).

### Vulnerability

Susceptibility or physical fragility of infrastructure to be affected by a hazard event. It is expressed through **vulnerability functions** that relate event intensity to the **Mean Damage Ratio (MDR)**, expressed as a fraction of the physical value of the asset (between 0 and 1).

Unlike fragility functions — which estimate the *probability* of reaching a damage state —, the vulnerability functions of BSA 2.0 directly produce the expected economic damage.

### Criticality

A measure of the relative importance of a road segment within the network, based on its functional role and the impact its interruption would have on connectivity, accessibility, and transit. It is determined through a **multi-criteria analysis** that considers functionality, redundancy, accessibility, strategic value, and disruption under extreme events.

---

## Return period (Tr)

The return period (or recurrence interval) measures the *average time* — in years — between independent events that equal or exceed a given intensity level. It is equivalent to the inverse of the **annual exceedance rate**:

$$
T_r = \frac{1}{\lambda}
$$

where $\lambda$ is the annual exceedance rate. For example, an event with $T_r = 100$ years has an annual probability of occurrence of 1%.

BSA 2.0 typically uses return periods of 10, 50, 100, 200, and 500 years to construct the loss exceedance curve.

---

## Risk metrics: the fundamental distinction between damage and loss

!!! danger "Critical distinction"
    In BSA 2.0, **damage** and **loss** are distinct concepts and must not be used as synonyms.

### EAD — Expected Annual Damage *(DAE in Spanish)*

The **Expected Annual Damage** quantifies the economic impact from **direct physical damage** to road infrastructure. It is the average annualized cost of repairing or replacing assets damaged by natural events.

$$
\text{EAD} = \int_0^\infty D(p) \, d\lambda(p)
$$

where $D(p)$ is the damage associated with an event of magnitude $p$ and $d\lambda(p)$ is the differential of the exceedance rate.

In the discrete practice of BSA 2.0, it is approximated via the trapezoidal integral between return period levels:

$$
\text{EAD} \approx \sum_{i=1}^{n-1} \frac{D_i + D_{i+1}}{2} \cdot (\lambda_i - \lambda_{i+1})
$$

### EAL — Expected Annual Loss *(PAE in Spanish)*

The **Expected Annual Loss** quantifies the economic impact from **functional traffic disruption**: the annualized cost of interruption of road service (travel time losses, detours, logistics costs, etc.) caused by natural events affecting the operability of the network.

The formula is analogous to that of EAD, but using functional loss $L(p)$ instead of physical damage.

### PML — Probable Maximum Loss

The **Probable Maximum Loss** is the damage or loss expected for a **reference design event**, typically at $T_r = 500$ years. It represents the plausible worst-case scenario for contingency planning and insurance purposes.

### LEC — Loss Exceedance Curve

The **Loss Exceedance Curve** graphically represents the relationship between the magnitude of loss and its annual exceedance frequency. Integrating the area under this curve is equivalent to calculating the EAL.

---

## Other key acronyms and terms

| Acronym | Full term | Brief definition |
|---|---|---|
| EE | Exposed Element | Road segment discretized as a point in the exposure model |
| VF / FVU | Vulnerability Function | Relationship between hazard intensity and expected damage (MDR) |
| MDR / RMD | Mean Damage Ratio | Fraction of the asset's physical value expected to be lost; between 0 and 1 |
| MDRi / DMVi | Road Mean Damage – Infrastructure | Expected physical damage to an EE for a hazard event |
| MDRt / PMVt | Road Mean Loss – Transit | Expected functional loss of an EE for a hazard event |
| VFi | Physical Value of Infrastructure | Replacement cost of the exposed road segment |
| VFt | Economic Transit Value | Economic value of transit through the EE (vehicles, cargo, time) |
| BSA | Blue Spot Analysis | Tool for identifying and prioritizing critical risk points in road networks |
| Tr | Return Period | Mean time between events that equal or exceed a given intensity |
| TH | Water Depth (Tirante Hídrico) | Depth of the water layer during flooding |
| PGA | Peak Ground Acceleration | Peak ground acceleration during a seismic event |
| LEC / CEP | Loss Exceedance Curve | Relationship between loss magnitude and exceedance frequency |

---

*See the [full Glossary](../glosario/index.md) for additional definitions. For the computational structure of this data, see [Data structure](estructura-datos.md).*
