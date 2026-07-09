# Exposure Module

The exposure module identifies, characterizes, and values the infrastructure elements exposed to modeled hazards. Its central product is the **exposure model**: a georeferenced inventory of the road network that serves as the spatial database for all subsequent damage and loss calculations.

## Types of infrastructure analyzed

BSA 2.0 analyzes four main categories of transport infrastructure:

| Category | Description |
|---|---|
| **Roads** | Main and secondary road networks, municipal or strategic corridors |
| **Bridges and overpasses** | Transverse structures in the road network; high functional importance and economic value per unit |
| **Drainage systems** | Culverts, box culverts, gratings, ditches, and minor hydraulic works within corridors |
| **Control structures** | Dikes, retaining walls, and hydraulic works that influence flow dynamics |

## Characterization methods

Construction of the exposure model relies on four complementary sources:

1. **National institutional data**: road inventories and bridge records available in road management systems or infrastructure catalogs (HAZUS, FHWA).
2. **Remote sensing**: LiDAR, optical imagery, and SAR radar for extracting information on network geometry, bridges, and culverts.
3. **Artificial intelligence**: machine learning and computer vision techniques (CNN on aerial or SAR imagery) for automatic detection of bridges, accesses, and potential damage.
4. **Technical validation workshops**: on-site verification of digital information with local engineers, especially to calibrate design capacity, maintenance level, and structural vulnerability.

## Segmentation and economic valuation

### Segmentation

Infrastructure is divided into **homogeneous units** (Exposed Elements, EE) by type, location, functional hierarchy, or risk exposure. Each EE is represented as a point in a shapefile, usually at regular intervals along the road network (e.g., every 1 km between intersections, or per individual bridge).

### Economic valuation

Each element is valued according to its **estimated replacement cost** based on parameters such as length, area, materials, and construction type. In the absence of local data, standard equations adjusted by country and infrastructure type are used (FHWA, IDB, or local unit cost catalogs).

Two monetary values are assigned to each EE:

- **VFi (Physical Infrastructure Value)**: replacement cost of the segment; used in the calculation of *physical damage*.
- **VFt (Economic Transit Value)**: economic value of the transit through the segment; used in the calculation of *functional loss*.

## Exposure model assumptions

!!! note "Static nature of the model"
    The exposure model represents a **specific point in time** (the inventory update date). It does not reflect dynamic changes in the road network or economic values.

- Covers all elements of the road network: linear (roads and streets) and point (bridges, pontoons, viaducts).
- Built from assumptions and considerations derived from the nature of available data.
- Each EE may contain several structural typologies with percentage shares that characterize the homogeneous zone of analysis.

## Exposure model attributes

The following table shows the minimum recommended fields for the georeferenced database:

| Field | Description |
|---|---|
| `Id_ElementoExp` | Unique identifier of the exposed element |
| `Long`, `Lat` | Coordinates in WGS84 |
| `Zona_homog` | Homogeneous zone to which the EE belongs |
| `Tipo_Estruct` | Structural typology (material, pavement type, etc.) |
| `Znatural` | Natural topographic elevation (m a.s.l.) |
| `Zartificial` | Artificial height above road level |
| `Val_Inf` (VFi) | Exposed economic value – road infrastructure |
| `Val_Tr` (VFt) | Exposed economic value – transit |
| `Poblacion` | Number of inhabitants in the area of influence |
| `Tipo_Via` | Functional classification (highway, primary, secondary, etc.) |
| `Cond_Adaptado` | Flood adaptation condition (0 = not adapted, 1 = adapted) |
| `Dist_Cauce` | Orthogonal distance to the nearest waterbody (m) |

---

*To understand how the exposure model intersects with hazard grids and vulnerability functions, see [Architecture and modules](arquitectura.md).*
