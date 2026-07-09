# Tool Interface

When double-clicking on the **BSA2** tool within the toolbox, ArcGIS Pro opens the parameters dialog. This page describes each parameter, its data type, whether it is required or optional, and example values from the Costa Rica case.

## Parameters diagram

```
BSA2 ─── Exposure ──── Road network                (0) [required]
         │              Bridges                     (1) [optional]
         │              Tunnels                     (2) [optional]
         │              Drainage                    (3) [optional]
         │
         ├── Hazard ─── Fluvial flooding (multiple Tr) (4) [required*]
         │              Pluvial/coastal flooding        (5) [required*]
         │              Tsunami                         (6) [required*]
         │              Earthquake                      (7) [required*]
         │              Liquefaction                    (8) [optional]
         │              Climate change polygon          (9) [optional]
         │
         ├── Vulnerability ── VF database           (10) [required]
         │
         ├── Operations ──── Operating costs database (11) [optional†]
         │                   GDP per capita per day    (12) [optional†]
         │
         └── Segmentation ─── Segment length (m)    (13) [required]
```

\* At least **one** hazard raster (parameters 4–7) must be provided.  
† Parameters 11 and 12 must be provided together or neither; otherwise the tool returns an error.

## Exposure parameters

### (0) Road network — `roads_path` *(required)*

Polyline vector layer representing the road network to analyze. It is the only strictly required exposure component.

| Required attribute | Type | Description |
|--------------------|------|-------------|
| `ID_TRAMO` | Long/String | Unique identifier of the road segment. |
| `vul_f` | String | Vulnerability taxonomy code for flood hazards (e.g., `H_TRNP`). |
| `vul_eq` | String | Vulnerability taxonomy code for earthquake. |
| `rep_cost_k` | Double | Segment replacement cost in **thousands of USD per meter**. |
| `Longitud` | Double | Segment length in meters. |
| `T9`–`T15` | Double | Annual Average Daily Traffic (AADT) by vehicle type. |

### (1) Bridges — `bridge_path` *(optional)*

Point layer with bridge locations. If provided, the tool calculates EAD and EAL for bridges independently and aggregates them to the corresponding road segment via the `ID_TRAMO` field.

| Required attribute | Type | Description |
|--------------------|------|-------------|
| `ID_TRAMO` | Long/String | Links the bridge to its road segment. |
| `vul_f` | String | Vulnerability taxonomy for flooding. |
| `vul_eq` | String | Vulnerability taxonomy for earthquake. |
| `rep_cost` | Double | Bridge replacement cost in USD. |

### (2) Tunnels — `tunnel_path` *(optional)*

Point layer with tunnels. Same attribute structure as bridges.

### (3) Drainage — `draina_path` *(optional)*

Point layer with drainage elements (culverts, box culverts, etc.). Same attribute structure as bridges.

## Hazard parameters

Each hazard accepts **multiple rasters** (one per return period). In the ArcGIS Pro dialog, multiple files can be selected at once. The tool automatically extracts the Tr value from the file name.

### (4) Fluvial flooding — `fl_rive_raw`

GeoTIFF rasters with water depth (in meters) for each fluvial flooding Tr.

**Example (Costa Rica):** `ri_h_CR_10.tif; ri_h_CR_20.tif; ri_h_CR_50.tif; ri_h_CR_75.tif; ri_h_CR_100.tif; ri_h_CR_200.tif; ri_h_CR_500.tif`

### (5) Pluvial/coastal flooding — `fl_coas_raw`

GeoTIFF rasters for pluvial or coastal flooding, also in meters.

**Example (Costa Rica):** `c_h_CR_1.tif; c_h_CR_2.tif; c_h_CR_5.tif; c_h_CR_10.tif; c_h_CR_25.tif; c_h_CR_50.tif; c_h_CR_100.tif; c_h_CR_250.tif; c_h_CR_500.tif; c_h_CR_1000.tif`

### (6) Tsunami — `ts_coas_raw`

Rasters with wave height (in meters) by Tr.

### (7) Earthquake — `earthqu_raw`

Rasters with Peak Ground Acceleration (PGA) for each Tr.

**Example (Costa Rica):** `EQ_CR_PGA_100.tif; EQ_CR_PGA_225.tif; EQ_CR_PGA_475.tif; EQ_CR_PGA_2475.tif; EQ_CR_PGA_4975.tif`

### (8) Liquefaction — `liquefa_raw` *(optional)*

A single raster with liquefaction susceptibility values (scale 1–4). Used only when there is seismic hazard; modifies the vulnerability function applied to each element.

### (9) Climate change polygon — `mod_tp_poly` *(optional)*

Vector polygon with `TP###S#M` fields containing return periods modified by climate scenario (e.g., RCP 8.5 for 2080). The tool calculates additional EAD and EAL versions under each scenario.

## Vulnerability parameters

### (10) VF database — `vulner_data` *(required)*

CSV file (`FVU_BSA_V3.csv`) with the physical (damage) and transit (interruption time) vulnerability functions for each infrastructure taxonomy and hazard type. The format of each line is:

```
taxonomy,[intensities],[percentage_values]
```

**Example:** `FL_RMD_H_TRNP,[0,0.2,0.5,1.5,50],[0,1,2,20,20]`

## Operations and economics parameters

### (11) Operating costs database — `operat_data` *(optional)*

CSV with operating costs and average occupancy by vehicle taxonomy (T9–T15). Required for EAL calculation.

| Field | Description |
|-------|-------------|
| `taxonomy` | Vehicle type: T9 (pick-up), T10 (car), T11 (bus), T12 (light truck), T13 (medium truck), T14 (heavy truck), T15 (articulated truck). |
| `COV` | Vehicle operating cost (USD/km). |
| `OCU` | Average occupants per vehicle (persons). |

### (12) GDP per capita per day — `gdppca_doub` *(optional)*

Scalar value of the country's daily GDP per capita, expressed in USD. Used to value travel time lost by users during road service interruption.

**Example (Costa Rica):** `45249.62`

!!! tip "Calculating GDP per capita per day"
    If only the annual GDP per capita is available, divide it by 365 to get the daily value (e.g., USD 16,500/year ÷ 365 ≈ USD 45.2/day). Confirm the unit with the project team before entering the value.

## Segmentation parameters

### (13) Segment length — `road_segme` *(required)*

Length in meters of the sampling points the tool generates along the road network. Defines the spatial resolution of the analysis.

| Value | Effect |
|-------|--------|
| **10–30 m** | High resolution; longer processing time. Recommended for critical corridors. |
| **50 m** | Standard resolution for national analyses. |
| **100 m** | Low resolution; fast processing. For testing or very extensive networks only. |

**Example (Costa Rica):** `30`

!!! warning "Resolution vs. computation time"
    For national networks with thousands of kilometers, a 10 m segmentation may require several hours of processing. It is recommended to start with 50 m and adjust based on available resources.

## Output parameters

The tool automatically writes results to the `BSA2.gdb` geodatabase, located in the script directory:

| Output | Content |
|--------|---------|
| `roads_results_<timestamp>` | Road network with EAD, EAL, and Priority fields per segment. |
| `bridges_results_<timestamp>` | Bridges with individual EAD, EAL, and Priority. |
| `tunnels_results_<timestamp>` | Tunnels with individual EAD, EAL, and Priority. |
| `drainage_results_<timestamp>` | Drainage elements with EAD, EAL, and Priority. |

Results are automatically added to the active ArcGIS Pro map upon completion.
