# Datos de entrada

## Resumen

| Grupo | Archivos o valores | Especificación canónica |
|---|---|---|
| Exposición | Carreteras, puentes, túneles y drenajes | [Diccionario de exposición](../metodologia/modulo-exposicion.md) |
| Amenaza | Rásteres fluviales, costeros, tsunami y sismo; licuefacción opcional | [Contrato de amenaza](../metodologia/modulo-amenaza.md) |
| Vulnerabilidad | CSV de funciones RMD y tiempo | [Estructura de vulnerabilidad](../metodologia/modulo-vulnerabilidad.md) |
| Operaciones | CSV con `taxonomy`, `COV` y `OCU` | [Criticidad](../metodologia/modulo-criticidad.md) |
| Economía | PIB per cápita por día | Moneda local/persona/día |
| Clima | Polígonos de modificación de frecuencia | Campos `TP#S#M` |
| Ejecución | Longitud de segmento | Metros |

## Reglas que no deben mezclarse

- `rep_cost_k` de carreteras está en moneda por kilómetro; `rep_cost` de activos puntuales es un costo total.
- RMD se ingresa como porcentaje 0–100; tiempo de interrupción, en horas.
- `COV` está en moneda por vehículo-km y `OCU` en personas por vehículo.
- PGA y SA se expresan en g; la medida sísmica de la taxonomía usa `SA`.
- La inundación costera se identifica documentalmente con `co`.
- Los costos y el PIB deben compartir moneda y año base.

## Lista de comprobación

1. Abrir cada archivo y confirmar que no esté dañado.
2. Verificar `EPSG:4326` en todas las capas espaciales.
3. Revisar identificadores, topología y vínculo `ID_TRAMO`.
4. Comparar taxonomías de exposición con ambos CSV.
5. Confirmar unidades y rangos de intensidades.
6. Comprobar que el último número del nombre de cada ráster sea su TR.
7. Conservar una copia de los insumos y sus metadatos.

