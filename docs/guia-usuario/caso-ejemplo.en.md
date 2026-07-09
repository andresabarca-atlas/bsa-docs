# Case Study — Costa Rica

This page describes the application of BSA 2.0 to the Costa Rica reference case, included in the `fuentes/04_codigo/BSA2_CostaRica/` folder. This case serves as a reference for validating the installation, understanding the workflow, and calibrating expectations about the results.

!!! note "Purpose of the case study"
    The Costa Rica case is a reference dataset that illustrates the complete operation of the toolbox. It does not represent an official analysis of the country; its function is pedagogical and technical validation.

## Components of the case study

The `BSA2_CostaRica/` directory contains the following files:

| File | Description |
|------|-------------|
| `CostaRica.aprx` | ArcGIS Pro project with all input and result layers already referenced. |
| `BSA2.atbx` | Toolbox with the BSA2 tool ready to run. |
| `BSA2.py` | Toolbox script (do not modify). |
| `FVU_BSA_V3.csv` | Vulnerability functions database (physical and transit). |
| `OCO_BSA_CR_V1.csv` | Operating costs database by vehicle type for Costa Rica. |
| `BSA2.gdb/` | Geodatabase with input exposure layers and results from the last run. |
| `Loc/run_config_20260413_172736.loc` | Traceability file from the reference run. |

## Inputs used

### Exposure layers (within `BSA2.gdb`)

| Layer | Type | Description |
|-------|------|-------------|
| `crc_RVN_WGS84` | Polylines | Costa Rica national road network in WGS84 datum. |
| `crc_rvn_puentes2` | Points | Bridge inventory on main corridors. |
| `cr_tuneles_rvn_WGS84` | Points | Tunnel inventory of the national road network. |
| `crc_rvn_drenaje2` | Points | Drainage elements in the road network. |

### Hazard grids used

The reference run used the following rasters (listed in the `.loc` file):

**Fluvial flooding (7 return periods):**

| File | Tr (years) |
|------|-----------|
| `ri_h_CR_10.tif` | 10 |
| `ri_h_CR_20.tif` | 20 |
| `ri_h_CR_50.tif` | 50 |
| `ri_h_CR_75.tif` | 75 |
| `ri_h_CR_100.tif` | 100 |
| `ri_h_CR_200.tif` | 200 |
| `ri_h_CR_500.tif` | 500 |

**Coastal/pluvial flooding (10 return periods):**

| File | Tr (years) |
|------|-----------|
| `c_h_CR_1.tif` | 1 |
| `c_h_CR_2.tif` | 2 |
| `c_h_CR_5.tif` | 5 |
| `c_h_CR_10.tif` | 10 |
| `c_h_CR_25.tif` | 25 |
| `c_h_CR_50.tif` | 50 |
| `c_h_CR_100.tif` | 100 |
| `c_h_CR_250.tif` | 250 |
| `c_h_CR_500.tif` | 500 |
| `c_h_CR_1000.tif` | 1,000 |

**Earthquake (5 return periods — PGA):**

| File | Tr (years) |
|------|-----------|
| `EQ_CR_PGA_100.tif` | 100 |
| `EQ_CR_PGA_225.tif` | 225 |
| `EQ_CR_PGA_475.tif` | 475 |
| `EQ_CR_PGA_2475.tif` | 2,475 |
| `EQ_CR_PGA_4975.tif` | 4,975 |

Tsunami and liquefaction were not available for this run.

### Economic parameters

| Parameter | Value |
|-----------|-------|
| GDP per capita per day | USD 45,249.62 |
| Segment length | 30 meters |

## Type of results obtained

The run generated four result layers in `BSA2.gdb`:

- **`roads_results_20260413_172736`** — road segments with EAD fields by hazard (fluvial, coastal, seismic), total EAD, EAL by hazard, total EAL, and Priority.
- **`bridges_results_20260413_172736`** — bridges with their own EAD, EAL, and Priority metrics.
- **`tunnels_results_20260413_172736`** — tunnels with individual metrics.
- **`drainage_results_20260413_172736`** — drainage elements with individual metrics.

In the road layer, the `DAE_bridge`, `DAE_tunnel`, and `DAE_drainage` fields contain the damage of components associated with the `ID_TRAMO`, allowing visualization of total corridor risk.

## How to reproduce the analysis

1. Open `CostaRica.aprx` in ArcGIS Pro.
2. In the Catalog panel, locate `BSA2.atbx` and open the **BSA2** tool.
3. Load the parameters according to the example configuration table in [Configuring a run](configuracion-corrida.md#ejemplo-de-configuracion-costa-rica).
4. Click **Run** and wait for completion.
5. Compare the results with the fields of the existing `roads_results_*` layer in the geodatabase to validate reproducibility.

!!! tip "Quick validation"
    Filter the result layer by segments with the highest `Priority` and compare them geographically with historical road damage records for the country. A spatial coincidence between high-Priority segments and historically affected areas is an indicator of model consistency.
