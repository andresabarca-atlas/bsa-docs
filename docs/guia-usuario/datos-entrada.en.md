# Input Data

BSA 2.0 requires four groups of inputs: **(a) asset inventories / exposure**, **(b) hazard grids**, **(c) vulnerability and recovery**, and **(d) criticality and operating costs**. This page describes each set with its description, format, requirements, and main attributes.

---

## a) Asset inventories — Exposure

These layers represent the road infrastructure susceptible to being affected by natural hazards. All must be in **shapefile** format and projected in the same CRS as the hazard rasters.

### Road network (roads)

| Field | Description | Type | Required |
|-------|-------------|------|----------|
| `ID_TRAMO` | Unique segment identifier | Long / String | Yes |
| `Nombre` | Road or route name | String | No |
| `Longitud` | Segment length in meters | Double | Yes |
| `Jerarquía` | Road level (1 = primary, 2 = secondary, 3 = tertiary) | String | No |
| `ID_País` | Country code (e.g. CR, DO, SV) | String | No |
| `vul_f` | Vulnerability taxonomy code for flooding | String | Yes |
| `vul_eq` | Vulnerability taxonomy code for earthquake | String | Yes (if seismic hazard present) |
| `rep_cost_k` | Replacement cost in thousands of USD/meter of road | Double | Yes |
| `T9`–`T15` | AADT by vehicle type (pick-up, car, bus, trucks) | Double | Yes (for EAL) |

- **Format:** Polyline shapefile (`.shp`)
- **Source:** Ministries of Public Works / Transport; secondary sources
- **Required:** Base layer; always required

### Bridges

| Field | Description | Type |
|-------|-------------|------|
| `ID_TRAMO` | Links the bridge to its road segment | Long / String |
| `Nombre` | Bridge name | String |
| `País` | Country of location | String |
| `Puente` | Structural typology (beams, truss, etc.) | String |
| `Estado` | Infrastructure condition (Good / Fair / Poor) | String |
| `Año` | Year of construction | Double |
| `vul_f` | Vulnerability taxonomy for flooding | String |
| `vul_eq` | Vulnerability taxonomy for earthquake | String |
| `rep_cost` | Bridge replacement cost in USD | Double |

- **Format:** Point shapefile (`.shp`)
- **Source:** Ministries of Public Works / Transport; field inventories
- **Required:** Optional; if provided, the tool calculates EAD and EAL per bridge independently

### Tunnels

Same attribute structure as bridges. The `rep_cost` field corresponds to the tunnel replacement cost.

- **Format:** Point shapefile
- **Required:** Optional

### Drainage (culverts and drainage elements)

| Field | Description | Type |
|-------|-------------|------|
| `ID_TRAMO` | Road segment to which the element belongs | Long / String |
| `Drenaje` | Typology (pipe culvert, box culvert, ford, ditch, etc.) | String |
| `Estado` | Structural condition | String |
| `Año` | Year of construction | Double |
| `vul_f` | Vulnerability taxonomy for flooding | String |
| `rep_cost` | Replacement cost in USD | Double |

- **Format:** Point shapefile
- **Required:** Optional

---

## b) Hazard grids

Hazard grids are **GeoTIFF rasters** containing, for each cell, the phenomenon intensity associated with a design event with a specific return period (Tr).

### Hazard types and intensity measures

| Hazard | ID | Intensity measure | Unit |
|---------|----|------------------|------|
| Fluvial flooding | `ri` | Water depth | meters |
| Pluvial / coastal flooding | `pl` / `c` | Water depth | meters |
| Tsunami | `ts` | Wave height / water depth | meters |
| Earthquake | `eq` | Peak Ground Acceleration (PGA) | g or gals |
| Liquefaction | `li` | Susceptibility (scale 1–4) | dimensionless |

!!! note "Future hazards"
    Landslides and hurricanes are planned for future phases of BSA 2.0, but are not implemented in the current version.

### Raster naming convention

The tool **automatically extracts the return period (Tr) from the file name**. It is essential to follow this convention:

**Historical flooding:**
```
{hazard}_{h}_{country}_{Tr}.tif
```

**Climate change flooding:**
```
{hazard}_{cc}_{scenario}_{year}_{country}_{Tr}.tif
```

**Earthquake:**
```
eq_{country}_{intensity_measure}_{Tr}.tif
```

**Tsunami:**
```
ts_{country}_{Tr}.tif
```

**Liquefaction** (single raster, no Tr):
```
li_{country}.tif
```

#### Identification codes

| Component | Code | Options |
|-----------|------|---------|
| Hazard | `{hazard}` | `pl` (pluvial), `ri` (fluvial), `ts` (tsunami), `eq` (earthquake), `li` (liquefaction) |
| Time horizon | `{h}` / `{cc}` | `h` (historical), `cc` (climate change) |
| Climate scenario | `{scenario}` | `rcp26`, `rcp45`, `rcp60`, `rcp85` |
| Projection year | `{year}` | e.g. `2050`, `2080` |
| Country | `{country}` | `AR`, `CR`, `DO`, `SV`, `GT`, `HN`, `MX`, `NI`, `PA`, etc. |
| Intensity measure (earthquake) | `{measure}` | `PGA`, `SAT03`, `SAT06`, etc. |
| Return period | `{Tr}` | Any integer: `10`, `25`, `50`, `100`, `500`, `1000`, etc. |

#### Valid name examples

| File | Interpretation |
|------|---------------|
| `ri_h_CR_100.tif` | Fluvial flooding, historical, Costa Rica, Tr = 100 years |
| `pl_cc_rcp85_2080_DO_25.tif` | Pluvial flooding, climate change RCP8.5 year 2080, Dom. Rep., Tr = 25 years |
| `eq_CR_PGA_475.tif` | Earthquake, Costa Rica, PGA, Tr = 475 years |
| `ts_DO_1500.tif` | Tsunami, Dom. Rep., Tr = 1500 years |
| `li_CR.tif` | Liquefaction, Costa Rica (no Tr) |

- **Format:** GeoTIFF (`.tif`)
- **Source:** National official sources, multilateral platforms (e.g. AIGHF, GloFAS, USGS ShakeMap)
- **Required:** At least one hazard raster is required; others are optional based on hazards present in the country

---

## c) Vulnerability and recovery

### Vulnerability functions (VF)

The vulnerability functions CSV file (`FVU_BSA_Vx.csv`) contains the physical damage curves (MDR) and the interruption time curves (T) for each infrastructure taxonomy and hazard type.

**Line format:**
```
taxonomy,[intensities],[percentage_values]
```

| Field | Description | Example |
|-------|-------------|---------|
| `taxonomy` | Compound key identifying hazard, curve type, horizon, and infrastructure typology | `FL_RMD_H_TRNP` |
| `[intensities]` | List of intensity values (depth in meters, PGA in g, etc.) | `[0,0.2,0.5,1.5,50]` |
| `[percentage_values]` | Mean damage percentage or interruption time (hours ÷ 24) | `[0,1,2,20,20]` |

#### Taxonomy key structure

The key follows the pattern `{hazard}_{curve_type}_{horizon}_{typology}`:

| Prefix | Meaning |
|--------|---------|
| `FL_RMD_` | Flooding (Flood), Repair Mean Damage curve |
| `FL_T_` | Flooding, Transit interruption time curve |
| `EQ_RMD_LQ{n}_` | Earthquake with liquefaction zone `n` (1–4), mean damage |
| `EQ_T_LQ{n}_` | Earthquake with liquefaction zone `n`, interruption time |

The final part of the key identifies the infrastructure typology (e.g., `H_TRNP` = historical, paved trunk; `H_REGP` = historical, paved regional).

- **Format:** CSV (`.csv`), UTF-8 encoding
- **Source:** Specialized literature, analytical models, expert judgment, technical workshops
- **Required:** Always required

### Rehabilitation times

Database with estimated rehabilitation times by infrastructure typology and hazard intensity level. Used to scale functional losses.

| Field | Description | Type |
|-------|-------------|------|
| `Tipo` | Unique infrastructure typology code | String |
| `Pais` | Country (no diacritical marks) | String |
| `Int_inunda` | Flooding intensity measures (m) | Double |
| `Int_sismo` | Seismic intensity measures (gals) | Double |
| `T_int_inunda` | Interruption times for flooding (hours) | Double |
| `T_int_sismo` | Interruption times for earthquake (hours) | Double |

- **Format:** Table included in the Excel input data sheet (`IDB_InputData_BSA.xlsx`, sheet `Tiempo_rehab`)
- **Required:** Required for EAL calculation

---

## d) Criticality and operating costs

### Operating costs by vehicle type

CSV file (`OCO_BSA_{country}.csv`) with vehicle operating parameters by taxonomy, used to value functional losses.

| Field | Description | Type |
|-------|-------------|------|
| `taxonomy` | Vehicle type: T9, T10, T11, T12, T13, T14, T15 | String |
| `COV` | Vehicle operating cost (USD/km per vehicle) | Double |
| `OCU` | Average occupants per vehicle (persons) | Double |

#### Vehicle taxonomies

| Code | Type |
|------|------|
| T9 | Pick-up |
| T10 | Car |
| T11 | Bus |
| T12 | Light truck |
| T13 | Medium truck |
| T14 | Heavy truck |
| T15 | Articulated truck |

- **Format:** CSV (`.csv`)
- **Source:** Ministry of Finance or multilateral development bank of the country
- **Required:** Required to calculate EAL (must be accompanied by GDP per capita per day)

### GDP per capita per day

Scalar value in USD used to value travel time lost by users during a road interruption.

| Field | Description | Type |
|-------|-------------|------|
| `Id` | Second-level administrative unit identifier | String |
| `Pais` | Country | String |
| `GDP_Cap` | Annual GDP per capita per territorial unit (USD) | Double |

!!! tip "Calculating the daily value"
    The tool receives the value already converted to **per day**. Divide the annual GDP per capita by 365 before entering it.

- **Format:** Scalar value (entered directly in toolbox parameter 12)
- **Source:** Central banks, World Bank, ECLAC
- **Required:** Required if operating costs database is provided (parameter 11)

---

## Summary of layers by component

| Component | Layer | Importance |
|-----------|-------|------------|
| Exposure | Road network (polylines) | Core — required |
| Exposure | Bridges (points) | Core — recommended |
| Exposure | Drainage (points) | Core — recommended |
| Exposure | Corridor names | Core |
| Exposure | Pavement condition | Core |
| Exposure | Pavement failures | Core |
| Exposure | Service level | Core |
| Exposure | AADT (traffic) | Core — required for EAL |
| Exposure | Border crossings | Reference |
| Exposure | Ports | Reference |
| Exposure | Airports | Reference |
| Exposure | Production/export nodes | Reference |
| Exposure | Logistics chains | Reference |
| Vulnerability | Damage functions (VF CSV) | Core — required |
| Vulnerability | Rehabilitation times | Core — required |
| Operations | GDP per capita | Core — for EAL |
| Operations | Operating costs (OCO CSV) | Core — for EAL |
| Hazard | Fluvial flooding (rasters by Tr) | Core |
| Hazard | Tsunami (rasters by Tr) | Core |
| Hazard | Earthquake (rasters by Tr) | Core |
| Hazard | Pluvial flooding (rasters by Tr) | Core |
| Hazard | Fluvial flooding — climate change | Reference |
| Hazard | Climate change zones | Reference |
