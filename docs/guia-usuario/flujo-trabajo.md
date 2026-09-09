# Flujo de trabajo

## Secuencia

Preparar insumos → validar el contrato de datos → configurar el toolbox → ejecutar → controlar calidad → aprobar resultados → publicar en el dashboard.

## Preparación

Reúna versiones congeladas de las capas y CSV. Registre fuente, fecha, responsable, moneda, año base, resolución, escenario y cualquier transformación. La preparación del modelo de amenaza, inventario o función de vulnerabilidad ocurre fuera del toolbox.

## Control previo

Use la [lista de datos](datos-entrada.md). Revise especialmente topología nodo–nodo, taxonomías, TR, NoData, costos y `EPSG:4326`.

## Ejecución

Configure los parámetros conforme a la [interfaz](../getting-started/interfaz.md). Para análisis comparativos, mantenga constantes los criterios y documente cualquier cambio entre corridas.

## Control posterior

- comprobar que las cuatro capas esperadas se crearon cuando había insumos;
- revisar una muestra manual de intensidades, RMD, daño y tiempo;
- confirmar que DAE y PAE no contengan valores negativos;
- investigar ceros inesperados y taxonomías no resueltas;
- contrastar tramos con y sin desvío;
- verificar la identidad `Priority = DAE_total + PAE_total`;
- archivar el `.loc` y los mensajes de geoprocesamiento.

Sólo después de la aprobación técnica deben publicarse capas en el dashboard.

