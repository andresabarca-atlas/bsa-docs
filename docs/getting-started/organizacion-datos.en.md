# Data Organization

Before running BSA 2.0, it is recommended to organize all inputs in a predictable folder structure. This facilitates parameter assignment in the toolbox and allows the analysis to be reproduced in an orderly manner.

## Recommended folder structure

```
<Project>/
│
├── <Project>.aprx              ← ArcGIS Pro project
├── BSA2.atbx                   ← Tool toolbox
├── BSA2.py                     ← Toolbox script (do not modify)
│
├── Exposure/                   ← Exposure layers (asset inventories)
│   ├── roads.shp               ← Road network (polylines)
│   ├── bridges.shp             ← Bridges (points)
│   ├── tunnels.shp             ← Tunnels (points)
│   └── drainage.shp            ← Drainage / culverts (points)
│
├── Hazard/                     ← Hazard raster grids (GeoTIFF)
│   ├── ri_h_<country>_10.tif   ← Fluvial flooding, Tr = 10 years
│   ├── ri_h_<country>_25.tif
│   ├── ri_h_<country>_100.tif
│   ├── ri_h_<country>_500.tif
│   ├── c_h_<country>_10.tif    ← Pluvial/coastal flooding
│   ├── EQ_<country>_PGA_475.tif ← Earthquake (PGA)
│   ├── ts_<country>_500.tif    ← Tsunami
│   └── li_<country>.tif        ← Liquefaction (single raster)
│
├── Vulnerability/              ← Vulnerability databases
│   └── FVU_BSA_V3.csv          ← Vulnerability functions (physical damage + transit)
│
├── Operations/                 ← Operations and economics databases
│   ├── OCO_BSA_<country>_V1.csv ← Vehicle operating costs by taxonomy
│   └── GDP_capita_<country>.csv ← GDP per capita by territorial unit (optional)
│
└── BSA2.gdb/                   ← Results geodatabase (auto-generated)
    ├── roads_results_<stamp>
    ├── bridges_results_<stamp>
    ├── tunnels_results_<stamp>
    └── drainage_results_<stamp>
```

!!! note "Results geodatabase"
    The `BSA2.gdb` folder and its result layers are generated automatically when running the tool, in the same directory where `BSA2.py` is located. It does not need to be created manually.

## Notes on each data group

### Exposure layers

Vector layers representing the road infrastructure to be analyzed. They must be in shapefile format and projected in the same reference system as the hazard rasters.

- **Road network** (`roads.shp`): polylines. Each segment must have at least the fields `ID_TRAMO`, `vul_f`, `vul_eq`, and `rep_cost_k`. See [Input data](../guia-usuario/datos-entrada.md) for the full attribute description.
- **Bridges** (`bridges.shp`): points. Required to calculate EAD and EAL for bridges.
- **Tunnels** (`tunnels.shp`): points. Optional; if not provided, the tool skips it.
- **Drainage** (`drainage.shp`): points. Optional.

### Hazard grids

GeoTIFF rasters containing the phenomenon intensity for each return period (Tr). They must follow the naming convention established in the input data sheet (see [Input data → Hazard grids](../guia-usuario/datos-entrada.md#b-hazard-grids)). The tool extracts the Tr value directly from the file name.

### Vulnerability databases

The `FVU_BSA_V3.csv` file contains the vulnerability functions in text format. See [Input data → Vulnerability and recovery](../guia-usuario/datos-entrada.md) for the detailed format.

### Operations databases

The operating cost and GDP per capita files are needed for EAL calculation (functional losses from traffic disruption). If not provided, the tool will only calculate EAD (physical damage).

## Management tips

- Keep all rasters of the same hazard in the same subfolder to facilitate multiple selection in the toolbox.
- Avoid spaces in file and folder names.
- Use descriptive names that include the country and return period (e.g., `ri_h_CR_100.tif`), as required by the tool's naming convention.
- The `Loc/` folder (auto-generated alongside `BSA2.gdb/`) stores `.loc` files with the configuration of each executed run. Keep them as traceability records.
