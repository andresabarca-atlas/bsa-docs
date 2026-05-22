# Requisitos del sistema

El BSA 2.0 se ejecuta como un *toolbox* de ArcGIS Pro. A continuación se detallan los requisitos de software, hardware y conocimientos previos recomendados.

## Software

| Componente | Versión mínima | Notas |
|-----------|---------------|-------|
| **Sistema operativo** | Windows 10 (64 bits) | ArcGIS Pro no está disponible para macOS/Linux. |
| **ArcGIS Pro** | 3.2.x | Requiere licencia activa (Basic, Standard o Advanced). |
| **Spatial Analyst** | Incluido en ArcGIS Pro | Extensión necesaria para el muestreo de rásters. Debe estar habilitada. |
| **Entorno Python** | `arcgispro-py3` | Viene incluido con ArcGIS Pro. No se requiere instalación adicional de Python. |
| **Paquetes Python** | `numpy` ≥ 1.20 | Preinstalado en `arcgispro-py3`; no requiere acción del usuario. |

!!! warning "Versiones anteriores de ArcGIS Pro"
    Las versiones anteriores a 3.2 no han sido validadas. Pueden presentar incompatibilidades en la API de `arcpy` y en la gestión de entornos conda.

## Hardware recomendado

| Recurso | Mínimo | Recomendado |
|---------|--------|-------------|
| **RAM** | 16 GB | 32 GB o más |
| **CPU** | 4 núcleos a 2,5 GHz | 8 núcleos o más |
| **Almacenamiento libre** | 20 GB | 50 GB o más (los rásters de amenaza pueden ser voluminosos) |
| **GPU** | No requerida | — |

!!! tip "Análisis nacionales"
    Para correr el BSA 2.0 sobre redes viales nacionales completas (decenas de miles de tramos), se recomienda RAM ≥ 32 GB. El cuello de botella principal es el muestreo de rásters de alta resolución.

## Conocimientos previos recomendados

### Teóricos

- Conceptos básicos de análisis de riesgo de desastres naturales (amenaza, exposición, vulnerabilidad, riesgo).
- Familiaridad con períodos de retorno y probabilidades anuales de excedencia.
- Comprensión de las métricas de salida del BSA 2.0: DAE (Daño Anual Esperado), PAE (Pérdida Anual Esperada) y PML (Pérdida Máxima Probable).

### Prácticos

- Manejo básico de ArcGIS Pro: abrir proyectos `.aprx`, trabajar con capas vectoriales y ráster, y usar el panel de *Geoprocessing*.
- Organización de datos geoespaciales: shapefiles, GeoTIFF y geodatabases de archivos (`.gdb`).
- Conocimiento general de redes viales georreferenciadas (atributos de tramos, ID de segmento).

!!! note "Sin programación requerida"
    El BSA 2.0 se opera completamente desde la interfaz gráfica de ArcGIS Pro. No es necesario modificar ni ejecutar código Python directamente.
