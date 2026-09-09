# Requisitos del sistema y acceso

## Requisitos

| Componente | Mínimo / base | Recomendado para uso fluido |
|---|---|---|
| Sistema operativo | Windows 10/11, 64 bits | Windows 10/11 actualizado, 64 bits |
| Plataforma SIG | ArcGIS Pro 3.2.x con licencia Standard o Advanced | ArcGIS Pro 3.2.x y extensiones activas según el proyecto |
| Extensiones | Spatial Analyst para ráster y geoprocesos básicos | Spatial Analyst y extensiones pertinentes, como Network o 3D Analyst |
| Python | Entorno `arcgispro-py3` instalado con ArcGIS Pro | Entorno administrado y capacidad de instalar dependencias autorizadas |
| Memoria RAM | 8 GB | 16 GB o más para redes nacionales o regionales |
| Procesador | 4 núcleos | 8 núcleos o más, con multiprocesamiento |
| Almacenamiento | 20 GB libres para datos y resultados | SSD dedicado para proyectos SIG y datos de riesgo |
| Conectividad | Acceso autorizado al repositorio y a los datos | Conexión estable para sincronización, respaldo y versiones |

## Acceso

Se requieren:

1. licencia válida de ArcGIS Pro;
2. acceso al paquete vigente del toolbox `BSA2.atbx` y su script;
3. permisos de lectura sobre los insumos y de escritura en la carpeta del toolbox;
4. acceso a los datos oficiales o técnicamente validados del país.

El código crea `BSA2.gdb` y la carpeta `Loc` junto al script. Por ello, no instale el toolbox en una ubicación de solo lectura.

## Conocimientos recomendados

El usuario debe poder revisar proyecciones, geometrías, atributos, rásteres y CSV; además de interpretar amenaza, vulnerabilidad, período de retorno, DAE, PAE y las limitaciones de una evaluación probabilística simplificada.

