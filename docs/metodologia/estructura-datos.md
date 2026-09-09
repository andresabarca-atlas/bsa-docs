# Estructura de datos

Esta página resume el contrato transversal. Los diccionarios detallados se encuentran en los capítulos de [amenaza](modulo-amenaza.md), [exposición](modulo-exposicion.md) y [vulnerabilidad](modulo-vulnerabilidad.md).

## Reglas comunes

- Todos los datos espaciales: WGS 84, `EPSG:4326`.
- Identificadores: únicos, estables, sin nulos.
- Moneda: local, homogénea y con año base documentado.
- Valores numéricos: sin separadores ambiguos ni texto.
- Nulos: distinguir entre ausencia de dato y valor cero.
- Nombres de campos: respetar exactamente mayúsculas, guiones bajos y longitud admitida por el formato.
- Metadatos: fuente, fecha, versión, unidad, resolución y transformaciones.

## Inventario de entradas

| Entrada | Formato | Cardinalidad | Clave o regla principal |
|---|---|---:|---|
| Carreteras | Feature layer / SHP | 1 | `ID_TRAMO`; línea nodo–nodo |
| Puentes | Feature layer / SHP | 0–1 | `ID_PUENTE`, `ID_TRAMO` |
| Túneles | Feature layer / SHP | 0–1 | `ID_TUNEL`, `ID_TRAMO` |
| Drenajes | Feature layer / SHP | 0–1 | `ID_DRENAJE`, `ID_TRAMO` |
| Mallas de amenaza | GeoTIFF | 2 o más TR por amenaza recomendados | TR como última secuencia entera del nombre |
| Licuefacción | Ráster | 0–1 | clases 1–4 |
| Climate layer | Polígonos | 0–1 | campos `TP#S#M` |
| Vulnerabilidad | CSV UTF-8 | 1 | `taxonomy`, arreglos de intensidad y valor |
| Operaciones | CSV UTF-8 | 0–1 | `taxonomy`, `COV`, `OCU` |
| PIB per cápita por día | Número | 0–1 | moneda local/persona/día |
| Longitud de segmento | Número | 1 | metros |

La base de operaciones y el PIB per cápita diario se suministran juntos. Aunque algunos parámetros aparecen como opcionales en la definición visual del toolbox, el código exige carreteras, longitud de segmento, vulnerabilidad y al menos una malla de amenaza.

## Relaciones clave

- `ID_TRAMO` vincula activos puntuales con la carretera.
- `vul_f` y `vul_eq` vinculan cada activo con la función del CSV.
- `T9`–`T15` vinculan tránsito con `taxonomy` de la base de operaciones.
- el TR extraído del nombre vincula cada ráster con los campos `damage_*_TR` y `loss_*_TR`.

!!! warning
    Los shapefiles limitan los nombres de campo. Verifique los nombres después de cada exportación y evite que ArcGIS los trunque o duplique.

