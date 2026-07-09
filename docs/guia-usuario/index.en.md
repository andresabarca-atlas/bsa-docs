# User Guide

This section describes how to use BSA 2.0 from start to finish: from the preparation and standardization of input data to the interpretation of risk maps and investment prioritization.

## The process in summary

BSA 2.0 transforms raw geospatial data into a ranking of road segments by their risk from natural hazards. The process can be summarized in four stages:

```
  Raw data                 Preparation                 Execution              Interpretation
       │                        │                           │                        │
  Road network   ──────►  Standardize layers  ──────►  BSA2 Toolbox  ──────►  EAD / EAL maps
  Hazard rasters           Complete attributes           (ArcGIS Pro)           Priority ranking
  Vulnerability            Calculate GDP/day                                    IDB Dashboard
  Costs                    Define segmentation
```

## Contents of this section

| Page | What you will find |
|------|--------------------|
| [Workflow](flujo-trabajo.md) | Step-by-step sequence from data collection to loading results to the dashboard. |
| [Input data](datos-entrada.md) | Full description of each input layer: format, attributes, requirements, and naming conventions. |
| [Configuring a run](configuracion-corrida.md) | How to assign parameters in the toolbox, choose segment length, and define economic parameters. |
| [Results](resultados.md) | Description of output layers, their fields, and how to interpret EAD, EAL, and Priority for prioritization. |
| [Case study — Costa Rica](caso-ejemplo.md) | Full example using the Costa Rica reference case data. |

!!! tip "Suggested starting point"
    If this is your first time using BSA 2.0, read [Workflow](flujo-trabajo.md) first to get a global view of the process, then review [Input data](datos-entrada.md) to validate that your inputs meet the required format.
