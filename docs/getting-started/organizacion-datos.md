# Organización de datos

Antes de ejecutar el BSA 2.0, es recomendable organizar todos los insumos en una estructura de carpetas predecible. Esto facilita la asignación de parámetros en el toolbox y permite reproducir el análisis de forma ordenada.

## Estructura de carpetas recomendada

```
<Proyecto>/
│
├── <Proyecto>.aprx              ← Proyecto de ArcGIS Pro
├── BSA2.atbx                    ← Toolbox de la herramienta
├── BSA2.py                      ← Script del toolbox (no modificar)
│
├── Exposure/                    ← Capas de exposición (inventarios de activos)
│   ├── roads.shp                ← Red vial (polilíneas)
│   ├── bridges.shp              ← Puentes (puntos)
│   ├── tunnels.shp              ← Túneles (puntos)
│   └── drainage.shp             ← Drenajes / alcantarillas (puntos)
│
├── Hazard/                      ← Mallas ráster de amenaza (GeoTIFF)
│   ├── ri_h_<país>_10.tif       ← Inundación fluvial, Tr = 10 años
│   ├── ri_h_<país>_25.tif
│   ├── ri_h_<país>_100.tif
│   ├── ri_h_<país>_500.tif
│   ├── c_h_<país>_10.tif        ← Inundación pluvial/costera
│   ├── EQ_<país>_PGA_475.tif    ← Sismo (PGA)
│   ├── ts_<país>_500.tif        ← Tsunami
│   └── li_<país>.tif            ← Licuefacción (un único ráster)
│
├── Vulnerability/               ← Bases de datos de vulnerabilidad
│   └── FVU_BSA_V3.csv           ← Funciones de vulnerabilidad (daño físico + tránsito)
│
├── Operations/                  ← Bases de datos de operaciones y economía
│   ├── OCO_BSA_<país>_V1.csv    ← Costos operativos por taxonomía de vehículo
│   └── GDP_capita_<país>.csv    ← PIB per cápita por unidad territorial (opcional)
│
└── BSA2.gdb/                    ← Geodatabase de resultados (generada automáticamente)
    ├── roads_results_<stamp>
    ├── bridges_results_<stamp>
    ├── tunnels_results_<stamp>
    └── drainage_results_<stamp>
```

!!! note "Geodatabase de resultados"
    La carpeta `BSA2.gdb` y sus capas de resultados se generan automáticamente al ejecutar la herramienta, en el mismo directorio donde se encuentra `BSA2.py`. No es necesario crearla manualmente.

## Notas sobre cada grupo de datos

### Capas de exposición

Son las capas vectoriales que representan la infraestructura vial a analizar. Deben estar en formato shapefile y proyectadas en el mismo sistema de referencia que los rásters de amenaza.

- **Red vial** (`roads.shp`): polilíneas. Cada tramo debe tener al menos los campos `ID_TRAMO`, `vul_f`, `vul_eq` y `rep_cost_k`. Ver [Datos de entrada](../guia-usuario/datos-entrada.md) para la descripción completa de atributos.
- **Puentes** (`bridges.shp`): puntos. Obligatorio si se quiere calcular DAE y PAE para puentes.
- **Túneles** (`tunnels.shp`): puntos. Opcional; si no se provee, la herramienta lo omite.
- **Drenajes** (`drainage.shp`): puntos. Opcional.

### Mallas de amenaza

Rásters GeoTIFF que contienen la intensidad del fenómeno para cada período de retorno (Tr). Deben seguir la convención de nombres establecida en la ficha de datos de entrada (ver [Datos de entrada → Mallas de amenaza](../guia-usuario/datos-entrada.md#b-mallas-de-amenaza)). La herramienta extrae el valor de Tr directamente del nombre del archivo.

### Bases de datos de vulnerabilidad

El archivo `FVU_BSA_V3.csv` contiene las funciones de vulnerabilidad en formato de texto. Consulte [Datos de entrada → Vulnerabilidad y recuperación](../guia-usuario/datos-entrada.md) para el formato detallado.

### Bases de datos de operaciones

Los archivos de costos operativos y PIB per cápita son necesarios para el cálculo de PAE (pérdidas funcionales por disrupción del tránsito). Si no se proveen, la herramienta calculará solo el DAE (daño físico).

## Consejos de gestión

- Mantenga todos los rásters de una misma amenaza en la misma subcarpeta para facilitar la selección múltiple en el toolbox.
- Evite espacios en los nombres de archivos y carpetas.
- Use nombres descriptivos que incluyan el país y el período de retorno (por ejemplo, `ri_h_CR_100.tif`), tal como lo exige la convención de la herramienta.
- La carpeta `Loc/` (generada automáticamente junto a `BSA2.gdb/`) almacena los archivos `.loc` con la configuración de cada corrida ejecutada. Guárdelos como registro de trazabilidad.
