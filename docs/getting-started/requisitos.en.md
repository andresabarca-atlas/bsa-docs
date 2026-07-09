# System Requirements

BSA 2.0 runs as an ArcGIS Pro *toolbox*. The software, hardware, and recommended prior knowledge requirements are detailed below.

## Software

| Component | Minimum version | Notes |
|-----------|----------------|-------|
| **Operating system** | Windows 10 (64-bit) | ArcGIS Pro is not available for macOS/Linux. |
| **ArcGIS Pro** | 3.2.x | Requires an active license (Basic, Standard, or Advanced). |
| **Spatial Analyst** | Included in ArcGIS Pro | Extension required for raster sampling. Must be enabled. |
| **Python environment** | `arcgispro-py3` | Included with ArcGIS Pro. No additional Python installation required. |
| **Python packages** | `numpy` ≥ 1.20 | Pre-installed in `arcgispro-py3`; no user action required. |

!!! warning "Earlier versions of ArcGIS Pro"
    Versions prior to 3.2 have not been validated. They may present incompatibilities in the `arcpy` API and conda environment management.

## Recommended hardware

| Resource | Minimum | Recommended |
|---------|---------|-------------|
| **RAM** | 16 GB | 32 GB or more |
| **CPU** | 4 cores at 2.5 GHz | 8 cores or more |
| **Free storage** | 20 GB | 50 GB or more (hazard rasters can be large) |
| **GPU** | Not required | — |

!!! tip "National analyses"
    To run BSA 2.0 on complete national road networks (tens of thousands of segments), RAM ≥ 32 GB is recommended. The main bottleneck is the sampling of high-resolution rasters.

## Recommended prior knowledge

### Theoretical

- Basic concepts of natural disaster risk analysis (hazard, exposure, vulnerability, risk).
- Familiarity with return periods and annual exceedance probabilities.
- Understanding of BSA 2.0 output metrics: EAD (Expected Annual Damage), EAL (Expected Annual Loss), and PML (Probable Maximum Loss).

### Practical

- Basic use of ArcGIS Pro: opening `.aprx` projects, working with vector and raster layers, and using the *Geoprocessing* panel.
- Organization of geospatial data: shapefiles, GeoTIFF, and file geodatabases (`.gdb`).
- General knowledge of georeferenced road networks (segment attributes, segment IDs).

!!! note "No programming required"
    BSA 2.0 is operated entirely from the ArcGIS Pro graphical interface. It is not necessary to modify or execute Python code directly.
