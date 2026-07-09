# Results

Upon completion of the BSA2 toolbox run, the tool generates a file geodatabase (`BSA2.gdb`) with a result layer for each exposure component provided. This page describes the output products and how to interpret them for investment prioritization.

## Output layers

| Layer | Content |
|-------|---------|
| `roads_results_<timestamp>` | Road network with EAD, EAL, and Priority per segment. Includes EAD from components (bridges, tunnels, drainage) aggregated to the corresponding segment. |
| `bridges_results_<timestamp>` | Bridges with individual EAD, EAL, and Priority. |
| `tunnels_results_<timestamp>` | Tunnels with individual EAD, EAL, and Priority. |
| `drainage_results_<timestamp>` | Drainage elements with EAD, EAL, and Priority. |

The `<timestamp>` corresponds to the execution date and time in `YYYYMMDD_HHMMSS` format (e.g., `roads_results_20260413_172736`). This allows maintaining a history of multiple runs without overwriting previous results.

## Output metrics per segment

### EAD — Expected Annual Damage

The **EAD** (*DAE* in Spanish) represents the annualized **direct physical damage** to infrastructure, expressed in USD per year. It is the integral of the damage exceedance curve:

$$
\text{EAD} = \int_0^1 D(p) \, dp \approx \sum_{i} D_i \cdot \Delta p_i
$$

where $D_i$ is the estimated damage for return period $Tr_i$ and $\Delta p_i$ is the difference in annual exceedance probabilities between consecutive Trs.

| Field | Description |
|-------|-------------|
| `DAE` | Total EAD of the road (road infrastructure only, excluding components) |
| `DAE_{hazard}` | EAD disaggregated by hazard (e.g., `DAE_river`, `DAE_earthquake`) |
| `DAE_bridge` | EAD of segment bridges, aggregated to `ID_TRAMO` level |
| `DAE_tunnel` | EAD of segment tunnels |
| `DAE_drainage` | EAD of segment drainage elements |
| `DAE_total` | Combined EAD: road + bridges + tunnels + drainage |

### EAL — Expected Annual Loss

The **EAL** (*PAE* in Spanish) represents the annualized **functional economic loss** from traffic disruption, expressed in USD per year. It is calculated by multiplying the functional interruption level (derived from the vulnerability T-curve) by the daily economic transit value (`DLT`) and annualized similarly to EAD.

| Field | Description |
|-------|-------------|
| `PAE_total` | Total EAL for the segment (sum of all hazards) |
| `PAE_{hazard}` | EAL disaggregated by hazard |

!!! note "EAD vs EAL distinction"
    **EAD** measures the cost of repairing damaged infrastructure. **EAL** measures economic losses from the interruption of vehicle flow while the road is out of service. Both metrics are complementary and necessary for a complete risk assessment.

### PML — Probable Maximum Loss

The **PML** (*Pérdida Máxima Probable*) corresponds to the expected damage or loss for a **specific design event** (generally Tr = 500 years). It is obtained by reading the value of the field `damage_{hazard}_500` or `loss_{hazard}_500` from the result layer.

### Priority — Prioritization Index

The `Priority` field is the synthetic risk indicator used for the ranking:

$$
\text{Priority} = \text{DAE\_total} + \text{PAE\_total}
$$

A higher `Priority` value indicates greater combined risk (physical damage + functional loss) and greater urgency for intervention.

!!! tip "Use in prioritization"
    To generate the prioritization map, symbolize the `roads_results_*` layer using the `Priority` field as the symbolization value (e.g., graduated symbology by line thickness or color scale). Segments with the highest `Priority` are the priority candidates for intervention.

## Intermediate fields

In addition to aggregated fields, result layers include damage and loss fields by event, useful for advanced analyses:

| Field | Description |
|-------|-------------|
| `damage_{hazard}_{Tr}` | Estimated damage (USD) for the specific hazard and Tr |
| `loss_{hazard}_{Tr}` | Functional loss (USD) for the specific hazard and Tr |

These fields allow manually constructing the Loss Exceedance Curve (LEC) for any individual segment.

## Climate change fields (if applicable)

If the climate modification polygon was provided (parameter 9), the layer includes additional fields by scenario:

| Field | Description |
|-------|-------------|
| `DAE_river_mod_{scen}` | Fluvial flooding EAD with Trs modified by scenario `scen` |
| `DAE_coast_mod_{scen}` | Modified coastal flooding EAD |
| `PAE_river_mod_{scen}` | Modified fluvial flooding EAL |
| `PAE_coast_mod_{scen}` | Modified coastal flooding EAL |
| `DAE_mod_{scen}` | Total EAD under climate scenario |
| `PAE_total_mod_{scen}` | Total EAL under climate scenario |
| `Priority_mod_{scen}` | Priority under climate scenario |
| `TP_TR_MODS_{scen}` | Text with the TP→TR mapping applied (e.g., `TP25_TR10; TP100_TR50`) |

## Interpretation for decision-making

BSA 2.0 results allow:

1. **Identifying critical segments:** Sorting the road network by `Priority` from highest to lowest identifies the segments with the greatest combined risk.

2. **Disaggregating by hazard:** The `DAE_{hazard}` and `PAE_{hazard}` fields allow identifying which hazard dominates risk in each area, informing the most appropriate type of mitigation measure.

3. **Quantifying intervention benefits:** If risk reduction measures are applied, a second run with reduced vulnerability parameters allows estimating the reduction in EAD and EAL.

4. **Comparing climate scenarios:** The `_mod_{scen}` fields allow comparing current risk with projections under different climate change scenarios.

5. **Feeding the dashboard:** Output metrics are loaded to the IDB dashboard, where they are visualized interactively at national and regional level.

## Traceability .loc file

Along with results, the tool saves a configuration file in `Loc/run_config_<timestamp>.loc` with the exact parameters used in that run. This file allows reproducing the analysis or auditing the configuration in case of subsequent review.

Example content of a `.loc` file:

```
roads_path=crc_RVN_WGS84
bridge_path=crc_rvn_puentes2
fl_rive_raw=ri_h_CR_10.tif;ri_h_CR_100.tif;...
earthqu_raw=EQ_CR_PGA_100.tif;EQ_CR_PGA_475.tif;...
vulner_data=C:\...\FVU_BSA_V3.csv
gdppca_doub=45249.62
road_segme=30
```
