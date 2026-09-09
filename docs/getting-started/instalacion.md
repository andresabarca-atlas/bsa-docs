# Instalación

Esta página describe los pasos para instalar ArcGIS Pro, agregar el toolbox `BSA2.atbx` a un proyecto y verificar que el entorno Python esté configurado correctamente.

## 1. Instalar ArcGIS Pro

1. Descargue ArcGIS Pro 3.2.x desde el portal de licencias de su organización o desde [My Esri](https://my.esri.com).
2. Ejecute el instalador con privilegios de administrador.
3. Al iniciar ArcGIS Pro por primera vez, inicie sesión con su cuenta de organización ArcGIS Online o con una licencia de portal Enterprise.
4. Active la extensión **Spatial Analyst**:
    - Vaya a **Project → Licensing → Configure your licensing options**.
    - En la lista de extensiones, active **Spatial Analyst**.

!!! warning "Licencia requerida"
    El BSA 2.0 requiere que la extensión Spatial Analyst esté activa. Sin ella, el toolbox generará un error al intentar leer rásters de amenaza.

## 2. Crear o abrir un proyecto ArcGIS Pro

1. Abra ArcGIS Pro y cree un nuevo proyecto (**New → Map**) o abra uno existente (por ejemplo, `CostaRica.aprx` si está trabajando con los datos de referencia).
2. Defina una carpeta de trabajo donde almacenará los datos de entrada y los resultados. Consulte [Organización de datos](organizacion-datos.md) para la estructura recomendada.

## 3. Agregar el toolbox BSA2.atbx

1. En ArcGIS Pro, abra el panel **Catalog** (pestaña **View → Catalog Pane**).
2. Haga clic derecho en **Toolboxes** y seleccione **Add Toolbox**.
3. Navegue hasta la carpeta donde se encuentra `BSA2.atbx` y selecciónelo.
4. El toolbox quedará disponible bajo **Toolboxes** en el panel Catalog con el nombre **BSA2**.
5. Para ejecutar la herramienta, haga doble clic en la herramienta **BSA2** dentro del toolbox. Se abrirá el diálogo de parámetros.

!!! tip "Acceso rápido"
    Puede arrastrar el toolbox al panel **Favorites** del Catalog para acceder a él rápidamente en futuros proyectos.

## 4. Verificar el entorno Python

El BSA 2.0 usa el entorno Python incluido con ArcGIS Pro (`arcgispro-py3`). No es necesario instalar dependencias adicionales.

Para verificar que el entorno está disponible:

1. Abra el panel de **Python** en ArcGIS Pro: **Analysis → Python Window**.
2. Escriba lo siguiente y presione Enter:

    ```python
    import arcpy, numpy
    print(arcpy.__version__, numpy.__version__)
    ```

3. Si el comando devuelve versiones sin errores, el entorno está listo.

!!! note "Paquetes adicionales"
    El script `BSA2.py` solo usa paquetes incluidos en `arcgispro-py3` (`arcpy`, `numpy`, `csv`, `re`, `os`). No es necesario instalar paquetes externos.

## 5. Verificar la instalación completa

Confirme que la instalación es correcta antes de la primera ejecución:

- [ ] ArcGIS Pro 3.2.x instalado y con sesión activa.
- [ ] Extensión Spatial Analyst activada.
- [ ] `BSA2.atbx` visible en el panel Catalog de su proyecto.
- [ ] Python Window responde correctamente (paso 4).
- [ ] Datos de entrada organizados según la estructura recomendada (ver [Organización de datos](organizacion-datos.md)).
