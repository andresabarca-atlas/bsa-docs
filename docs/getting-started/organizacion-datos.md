# Organización de datos

Mantenga una copia inmutable de los insumos y separe datos, configuración, resultados y metadatos.

```text
proyecto_bsa2/
├── 01_exposicion/
├── 02_amenaza/
│   ├── river/
│   ├── coast/
│   ├── tsunami/
│   ├── earthquake/
│   └── liquefaction/
├── 03_vulnerabilidad/
├── 04_operaciones/
├── 05_clima/
├── 06_metadatos/
└── 07_resultados/
```

## Recomendaciones

- use rutas cortas, estables y sin caracteres problemáticos;
- no sobrescriba los insumos originales;
- guarde fuente, licencia, fecha, unidad, resolución y CRS;
- mantenga todos los costos en la misma moneda y año base;
- archive el archivo `.loc` y los mensajes de cada corrida;
- no mueva ni renombre archivos durante la ejecución.

El toolbox escribe la geodatabase de resultados y la carpeta `Loc` junto a su script. Confirme permisos de escritura y espacio disponible.

