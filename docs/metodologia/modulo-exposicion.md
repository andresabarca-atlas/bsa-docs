# Módulo de Exposición

El módulo de exposición identifica, caracteriza y valora los elementos de infraestructura expuestos a las amenazas modeladas. Su producto central es el **modelo de exposición**: un inventario georeferenciado de la red vial que sirve como base de datos espacial para todos los cálculos posteriores de daño y pérdida.

## Tipos de infraestructura analizada

El BSA 2.0 analiza cuatro categorías principales de infraestructura de transporte:

| Categoría | Descripción |
|---|---|
| **Vías** | Redes de carreteras principales y secundarias, municipales o corredores estratégicos |
| **Puentes y pasos elevados** | Estructuras transversales en la red vial; alta importancia funcional y valor económico por unidad |
| **Sistemas de drenaje** | Canalizaciones, cajas, rejillas, zanjas y obras hidráulicas menores dentro de los corredores |
| **Estructuras de control** | Diques, muros de contención y obras hidráulicas que influyen en la dinámica de flujos |

## Métodos de caracterización

La construcción del modelo de exposición se apoya en cuatro fuentes complementarias:

1. **Datos nacionales institucionales**: inventarios viales y registros de puentes disponibles en sistemas de gestión vial o catálogos de infraestructura (HAZUS, FHWA).
2. **Sensores remotos**: teledetección LiDAR, imágenes ópticas y radar SAR para extraer información sobre geometría de red, puentes y canalizaciones.
3. **Inteligencia artificial**: técnicas de aprendizaje automático y visión por computadora (CNN sobre imágenes aéreas o SAR) para detectar automáticamente puentes, accesos y daño potencial.
4. **Talleres de validación técnica**: verificación presencial de la información digital con ingenieros locales, especialmente para calibrar capacidad de diseño, nivel de mantenimiento y vulnerabilidad estructural.

## Segmentación y valoración económica

### Segmentación

La infraestructura se divide en **unidades homogéneas** (Elementos Expuestos, EE) por tipo, ubicación, jerarquía funcional o exposición al riesgo. Cada EE se representa como un punto en un shapefile, usualmente a intervalos regulares a lo largo de la red vial (p. ej., cada 1 km entre intersecciones, o por puente individual).

### Valoración económica

Cada elemento se valora según su **costo de reposición estimado** a partir de parámetros como longitud, área, materiales y tipo de construcción. En ausencia de datos locales se utilizan ecuaciones estándar ajustadas por país y tipo de infraestructura (catálogos FHWA, BID o unidades locales de obra).

Se asignan dos valores monetarios a cada EE:

- **VFi (Valor Físico de la Infraestructura)**: costo de reposición del tramo; interviene en el cálculo del *daño físico*.
- **VFt (Valor Económico del Tránsito)**: valor económico del tránsito que circula por el tramo; interviene en el cálculo de la *pérdida funcional*.

## Supuestos del modelo de exposición

!!! note "Carácter estático del modelo"
    El modelo de exposición representa un **momento específico** en el tiempo (la fecha de actualización del inventario). No refleja cambios dinámicos en la red vial ni en los valores económicos.

- Cubre todos los elementos de la red vial: lineales (carreteras y calles) y puntuales (puentes, pontones, viaductos).
- Se construye a partir de supuestos y consideraciones derivados de la naturaleza de los datos disponibles.
- Cada EE puede contener varias tipologías estructurales con participaciones porcentuales que caracterizan la zona homogénea de análisis.

## Atributos del modelo de exposición

La tabla siguiente muestra los campos mínimos recomendados para la base de datos georeferenciada:

| Campo | Descripción |
|---|---|
| `Id_ElementoExp` | Identificador único del elemento expuesto |
| `Long`, `Lat` | Coordenadas en WGS84 |
| `Zona_homog` | Zona homogénea a la que pertenece el EE |
| `Tipo_Estruct` | Tipología estructural (material, tipo de pavimento, etc.) |
| `Znatural` | Cota topográfica natural (m s.n.m.) |
| `Zartificial` | Altura artificial sobre la rasante de la vía |
| `Val_Inf` (VFi) | Valor económico expuesto – infraestructura vial |
| `Val_Tr` (VFt) | Valor económico expuesto – tránsito |
| `Poblacion` | Número de habitantes en el área de influencia |
| `Tipo_Via` | Clasificación funcional (autopista, primaria, secundaria, etc.) |
| `Cond_Adaptado` | Condición de adaptación a inundación (0 = no adaptado, 1 = adaptado) |
| `Dist_Cauce` | Distancia ortogonal al cuerpo de agua más cercano (m) |

---

*Para comprender cómo el modelo de exposición se intersecta con las mallas de amenaza y las funciones de vulnerabilidad, véase [Arquitectura y módulos](arquitectura.md).*
