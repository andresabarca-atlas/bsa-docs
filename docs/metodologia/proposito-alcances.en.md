# Purpose, Scope, and Limitations

## General purpose

The BSA 2.0 aims to provide a scalable and participatory methodological platform that enables regional institutions to:

- Make **more informed decisions** about critical points in a country's infrastructure.
- **Prioritize investments** and interventions in road networks exposed to natural hazards.
- Improve **national and territorial planning** for the maintenance and development of critical infrastructure.
- Dynamically manage the **asset inventory** of roads and bridges.

In operational terms, the platform facilitates the calculation of damage and losses in the national road network from natural hazards — with climate change influence —, the identification of the most critical segments on which to focus investments, and the evaluation of the most cost-effective intervention measures.

## Questions the tool answers

BSA 2.0 is designed to help answer four strategic questions:

!!! question "Where are the assets and what are their characteristics?"
    Maintain a complete and up-to-date inventory of the road network, including structural typology, economic value, and adaptation condition.

!!! question "Which elements are at greatest risk?"
    For the current inventory of assets and the country's catastrophic risk profile, identify which elements are most likely to be affected by natural phenomena.

!!! question "Where should I focus investment?"
    In a context of economic uncertainty, climate change, and natural hazards, identify the segments that deserve priority attention.

!!! question "What type of intervention to prioritize and at what cost?"
    Provide recommendations for structural and non-structural measure archetypes to reduce risk, with estimates of the required investment.

## Scales of application

A distinctive feature of BSA 2.0 is its **multi-scale design**. The generated metrics can inform decisions at four levels:

```mermaid
graph LR
    A["🌎 Regional\n(international entities)"] --> B["🇨🇷 National\n(government institutions)"]
    B --> C["🛣️ Road corridor\n(local governments)"]
    C --> D["📍 Specific segment\n(specific interventions)"]
```

Not all scales are addressed from the first iterations of the tool. The incorporation of more detailed analyses by corridor and segment will be enabled as data integration and functionalities advance.

## Methodological consideration: simplified probabilistic approach

BSA 2.0 adopts a **simplified probabilistic model**, suitable for contexts where hazard models deliver spatial grids (rasters) of intensity associated with discrete return periods — which is the most commonly available format in the region — rather than exhaustive catalogs of stochastically simulated events (*event-based* approaches).

Under this approach, the Loss Exceedance Curve (LEC) is not derived directly, but it is possible to estimate **EAD and EAL** through interpolation between discrete hazard levels, assuming functional continuity between them and applying intensity-calibrated damage functions. This approach is compatible with that used in the *Global Assessment Report on Disaster Risk Reduction 2015* (UNISDR), where EAL was calculated for more than 140 countries using hazard grids for return periods of 25, 50, 100, 200, 500, and 1,000 years.

## Recognized limitations

### No uncertainty propagation in vulnerability

In the initial versions of BSA 2.0, losses are estimated using the **expected value** of the vulnerability functions. These functions are subject to inherent variability:

- **Epistemic uncertainty**: limitation of historical data and calibration.
- **Aleatoric uncertainty**: natural dispersion of the asset's physical response.

Since this uncertainty is not explicitly propagated, the reported EAD and EAL values are **point estimates of the mean value**, not representations of the full spectrum of possible losses.

!!! warning "Use in financial design processes"
    Caution is recommended when using these values for insurance, financial design, or contingency planning that require extreme-value analysis. In such cases, a complete probabilistic analysis — for example through Monte Carlo simulations — would be necessary.

### Input data: variable availability and quality

The quality of BSA 2.0 results depends directly on the quality of input data: road inventories, hazard models, and vulnerability functions. In many countries of the region, this data has incomplete coverage or outdated chronology. The platform incorporates validation procedures and participatory updating to mitigate this limitation.

### Hazards outside current scope

The hazards of **landslides** and **hurricanes**, although contemplated in the BSA 2.0 design, are planned for future development phases. The currently implemented hazards are:

| Hazard | Status |
|---|---|
| Fluvial flooding | ✅ Implemented |
| Pluvial / coastal flooding | ✅ Implemented |
| Earthquake | ✅ Implemented |
| Tsunami | ✅ Implemented |
| Liquefaction | ✅ Implemented |
| Landslides | 🔜 Future phase |
| Hurricanes | 🔜 Future phase |

### Does not replace structural design studies

The simplified probabilistic approach of BSA 2.0 is suitable for **prioritization and strategic planning**, not for structural design of works or the assessment of complex indirect losses, which require more detailed dynamic models.

---

*See also: [Key concepts](conceptos-clave.md) for a precise definition of EAD, EAL, and PML metrics.*
