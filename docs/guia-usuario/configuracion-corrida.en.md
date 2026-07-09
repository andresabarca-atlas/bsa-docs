# Configuring a Run

This page explains how to correctly assign each BSA2 toolbox parameter, choose segment length, and define economic parameters before running the analysis. For the technical description of each parameter, see [Tool interface](../getting-started/interfaz.md).

## Open the toolbox

1. In the **Catalog** panel of ArcGIS Pro, expand the **Toolboxes** section.
2. Double-click on the **BSA2** tool within `BSA2.atbx`.
3. The toolbox parameter panel will open.

## Assigning exposure layers

For each exposure parameter, click the folder icon of the parameter and navigate to the corresponding layer:

| Parameter | What to select |
|-----------|---------------|
| Road network | Polyline shapefile with complete `ID_TRAMO`, `vul_f`, `vul_eq`, and `rep_cost_k` attributes. |
| Bridges | Point shapefile. Leave empty if no bridge inventory is available. |
| Tunnels | Point shapefile. Optional. |
| Drainage | Point shapefile. Optional. |

!!! warning "Incomplete attributes"
    If the road network layer does not have the `vul_f`, `vul_eq`, or `rep_cost_k` fields, the tool will not be able to calculate damages or losses. Verify that attributes are complete **before** running.

## Assigning hazard rasters

Hazard parameters accept **multiple rasters** via multiple selection. In the file selection dialog:

1. Navigate to the `Hazard/` folder.
2. Select all rasters corresponding to the hazard type (hold `Ctrl` for multiple selection).
3. Click **OK**.

**Assignment order:**

- Parameter 4 → all fluvial flooding rasters (`ri_h_*`)
- Parameter 5 → all pluvial/coastal flooding rasters (`pl_h_*` or `c_h_*`)
- Parameter 6 → tsunami rasters (`ts_*`); leave empty if not applicable
- Parameter 7 → earthquake rasters (`eq_*`); leave empty if not applicable
- Parameter 8 → liquefaction raster (`li_*`, single file); leave empty if not applicable

!!! tip "Mixed hazards"
    It is not necessary to have data for all hazards. It is sufficient to provide at least one raster in any of parameters 4–7. The tool will only process the hazards that receive data.

## Assigning databases

| Parameter | File |
|-----------|------|
| VF database (10) | `FVU_BSA_Vx.csv` — located in the `Vulnerability/` folder |
| Operating costs (11) | `OCO_BSA_{country}.csv` — located in `Operations/`; leave empty if EAL is not needed |
| GDP per capita/day (12) | Numeric value; leave blank if parameter 11 is not provided |

## Defining segment length

Enter an integer value in meters in the **Segment length (13)** parameter. Consider:

- **30 m** — Recommended for priority corridors or high-resolution studies.
- **50 m** — Adequate balance for standard national analyses.
- **100 m** — Only for quick testing or networks larger than 20,000 km.

To run an initial test before the final analysis, start with 100 m to verify data is correctly configured; then run the final version with the desired resolution.

## Climate change polygon (optional)

If you have a vector polygon with `TP###S#M` fields (return periods modified by climate scenario), assign it to parameter 9. The tool will calculate additional EAD and EAL versions for each scenario (e.g., RCP 4.5, RCP 8.5).

If this polygon is not available, leave the parameter empty. The analysis will run only with historical data.

## Pre-run verification

Before clicking **Run**, review the following checklist:

- [ ] Road network with complete `ID_TRAMO`, `vul_f`, `vul_eq`, and `rep_cost_k`.
- [ ] At least one set of hazard rasters assigned.
- [ ] The VF file is assigned to parameter 10.
- [ ] If parameter 11 (operating costs) is assigned, parameter 12 (GDP per capita/day) is also complete.
- [ ] Segment length is defined.
- [ ] All files are in the same CRS.

## Execution and monitoring

Click **Run**. Progress is displayed in the bottom bar of the geoprocessing panel. Progress messages include:

- Confirmation of vulnerability database read.
- Progress by hazard and return period.
- Warning messages if any raster does not have a parseable Tr in its name.
- Final message `✅ Computation complete.` upon completion.

Upon completion, result layers are automatically added to the active map and the run configuration is saved in `Loc/run_config_<timestamp>.loc`.

## Configuration example — Costa Rica

The following table shows the configuration used for the Costa Rica reference case (see [Case study](caso-ejemplo.md)):

| Parameter | Value |
|-----------|-------|
| Road network | `crc_RVN_WGS84` |
| Bridges | `crc_rvn_puentes2` |
| Tunnels | `cr_tuneles_rvn_WGS84` |
| Drainage | `crc_rvn_drenaje2` |
| Fluvial flooding | 7 rasters: `ri_h_CR_{10,20,50,75,100,200,500}.tif` |
| Coastal flooding | 10 rasters: `c_h_CR_{1,2,5,10,25,50,100,250,500,1000}.tif` |
| Tsunami | *(not available for CR)* |
| Earthquake | 5 rasters: `EQ_CR_PGA_{100,225,475,2475,4975}.tif` |
| Liquefaction | *(not available for CR)* |
| VF | `FVU_BSA_V3.csv` |
| Operating costs | `OCO_BSA_CR_V1.csv` |
| GDP per capita/day | `45249.62` |
| Segment length | `30` meters |
