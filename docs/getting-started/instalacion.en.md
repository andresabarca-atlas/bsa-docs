# Installation

This page describes the steps to install ArcGIS Pro, add the `BSA2.atbx` toolbox to a project, and verify that the Python environment is correctly configured.

## 1. Install ArcGIS Pro

1. Download ArcGIS Pro 3.2.x from your organization's licensing portal or from [My Esri](https://my.esri.com).
2. Run the installer with administrator privileges.
3. When starting ArcGIS Pro for the first time, sign in with your ArcGIS Online organization account or an Enterprise portal license.
4. Activate the **Spatial Analyst** extension:
    - Go to **Project → Licensing → Configure your licensing options**.
    - In the extensions list, activate **Spatial Analyst**.

!!! warning "License required"
    BSA 2.0 requires the Spatial Analyst extension to be active. Without it, the toolbox will generate an error when trying to read hazard rasters.

## 2. Create or open an ArcGIS Pro project

1. Open ArcGIS Pro and create a new project (**New → Map**) or open an existing one (e.g., `CostaRica.aprx` if working with reference data).
2. Define a working folder where you will store input data and results. See [Data organization](organizacion-datos.md) for the recommended structure.

## 3. Add the BSA2.atbx toolbox

1. In ArcGIS Pro, open the **Catalog** panel (tab **View → Catalog Pane**).
2. Right-click on **Toolboxes** and select **Add Toolbox**.
3. Navigate to the folder where `BSA2.atbx` is located and select it.
4. The toolbox will be available under **Toolboxes** in the Catalog panel with the name **BSA2**.
5. To run the tool, double-click on the **BSA2** tool within the toolbox. The parameters dialog will open.

!!! tip "Quick access"
    You can drag the toolbox to the **Favorites** panel of the Catalog for quick access in future projects.

## 4. Verify the Python environment

BSA 2.0 uses the Python environment included with ArcGIS Pro (`arcgispro-py3`). No additional dependencies need to be installed.

To verify that the environment is available:

1. Open the **Python** panel in ArcGIS Pro: **Analysis → Python Window**.
2. Type the following and press Enter:

    ```python
    import arcpy, numpy
    print(arcpy.__version__, numpy.__version__)
    ```

3. If the command returns versions without errors, the environment is ready.

!!! note "Additional packages"
    The `BSA2.py` script only uses packages included in `arcgispro-py3` (`arcpy`, `numpy`, `csv`, `re`, `os`). No external packages need to be installed.

## 5. Verify the complete installation

Confirm that the installation is correct before the first run:

- [ ] ArcGIS Pro 3.2.x installed and with an active session.
- [ ] Spatial Analyst extension activated.
- [ ] `BSA2.atbx` visible in the Catalog panel of your project.
- [ ] Python Window responds correctly (step 4).
- [ ] Input data organized according to the recommended structure (see [Data organization](organizacion-datos.md)).
