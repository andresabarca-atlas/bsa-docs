# Preguntas frecuentes

??? question "¿El BSA 2.0 genera las mallas de amenaza o el inventario?"
    No. El usuario debe producir, seleccionar y validar estos insumos antes de cargarlos.

??? question "¿Qué archivos son obligatorios?"
    El código actual requiere una capa de carreteras, el CSV de vulnerabilidad, al menos una malla de amenaza y una longitud de segmento. Los activos puntuales y Climate layer son opcionales. La base de operaciones y el PIB diario deben cargarse juntos.

??? question "¿Todos los datos deben usar el mismo CRS?"
    Sí. La especificación del proyecto exige coordenadas geográficas WGS 84, `EPSG:4326`. Reproyecte y valide antes de ejecutar.

??? question "¿Por qué obtengo DAE o PAE igual a cero?"
    Revise que haya al menos dos TR válidos, que el último número del nombre sea el TR, que la taxonomía exista, que las intensidades no sean NoData y que costos, tránsito y tiempos sean mayores que cero.

??? question "¿El BSA calcula PML?"
    No. La versión actual genera daños y pérdidas por TR, DAE y PAE, pero no un indicador PML.

??? question "¿La priorización es multicriterio?"
    No. Es la suma monetaria anual de DAE y PAE. No incorpora ponderaciones ni reemplaza una evaluación de inversiones.

??? question "¿Qué hace Climate layer?"
    Modifica la frecuencia asignada a los daños y pérdidas de inundación fluvial y costera mediante TR futuros por zona. No cambia las intensidades ni modela el clima.

??? question "¿Cómo elijo Road segment length?"
    Relacione la distancia con el tamaño de celda del ráster. Valores pequeños aumentan el detalle y el tiempo; valores grandes reducen ambos. Haga una prueba de sensibilidad.

??? question "¿El dashboard recalcula los resultados?"
    No. Visualiza capas ya procesadas y aprobadas.

