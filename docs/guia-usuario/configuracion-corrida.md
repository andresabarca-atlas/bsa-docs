# Configuración de una corrida

Esta página explica cómo asignar correctamente cada parámetro del toolbox BSA2, elegir la longitud de segmento y definir los parámetros económicos antes de ejecutar el análisis. Para la descripción técnica de cada parámetro, consulte [Interfaz de la herramienta](../getting-started/interfaz.md).

## Abrir el toolbox

1. En el panel **Catalog** de ArcGIS Pro, expanda la sección **Toolboxes**.
2. Haga doble clic sobre la herramienta **BSA2** dentro de `BSA2.atbx`.
3. Se abrirá el panel de parámetros del toolbox.

## Asignación de capas de exposición

Para cada parámetro de exposición, haga clic en el ícono de carpeta del parámetro y navegue hasta la capa correspondiente:

| Parámetro | Qué seleccionar |
|-----------|----------------|
| Red vial | Shapefile de polilíneas con atributos `ID_TRAMO`, `vul_f`, `vul_eq` y `rep_cost_k` completos. |
| Puentes | Shapefile de puntos. Déjelo vacío si no dispone de inventario de puentes. |
| Túneles | Shapefile de puntos. Opcional. |
| Drenajes | Shapefile de puntos. Opcional. |

!!! warning "Atributos incompletos"
    Si la capa de red vial no tiene los campos `vul_f`, `vul_eq` o `rep_cost_k`, la herramienta no podrá calcular daños ni pérdidas. Verifique que los atributos están completos **antes** de ejecutar.

## Asignación de rásters de amenaza

Los parámetros de amenaza aceptan **múltiples rásters** mediante selección múltiple. En el diálogo de selección de archivos:

1. Navegue a la carpeta `Hazard/`.
2. Seleccione todos los rásters correspondientes al tipo de amenaza (mantenga presionado `Ctrl` para selección múltiple).
3. Haga clic en **OK**.

**Orden de asignación:**

- Parámetro 4 → todos los rásters de inundación fluvial (`ri_h_*`)
- Parámetro 5 → todos los rásters de inundación pluvial/costera (`pl_h_*` o `c_h_*`)
- Parámetro 6 → rásters de tsunami (`ts_*`); déjelo vacío si no aplica
- Parámetro 7 → rásters de sismo (`eq_*`); déjelo vacío si no aplica
- Parámetro 8 → ráster de licuefacción (`li_*`, un único archivo); déjelo vacío si no aplica

!!! tip "Mezcla de amenazas"
    No es necesario tener datos de todas las amenazas. Basta con proveer al menos un ráster en cualquiera de los parámetros 4–7. La herramienta procesará solo las amenazas que reciban datos.

## Asignación de bases de datos

| Parámetro | Archivo |
|-----------|---------|
| Base de datos FVU (10) | `FVU_BSA_Vx.csv` — localizado en la carpeta `Vulnerability/` |
| Costos operativos (11) | `OCO_BSA_{país}.csv` — localizado en `Operations/`; déjelo vacío si no quiere calcular PAE |
| PIB per cápita/día (12) | Valor numérico; déjelo en blanco si no provee el parámetro 11 |

## Definición de la longitud de segmento

Ingrese un valor entero en metros en el parámetro **Longitud de segmento (13)**. Considere:

- **30 m** — Recomendado para corredores prioritarios o estudios de alta resolución.
- **50 m** — Balance adecuado para análisis nacionales estándar.
- **100 m** — Solo para pruebas rápidas o redes de más de 20 000 km.

Para correr una prueba inicial antes del análisis definitivo, comience con 100 m para verificar que los datos están bien configurados; luego corra la versión final con la resolución deseada.

## Polígono de cambio climático (opcional)

Si dispone de un polígono vectorial con campos `TP###S#M` (períodos de retorno modificados por escenario climático), asígnelo al parámetro 9. La herramienta calculará versiones adicionales de DAE y PAE para cada escenario (p. ej. RCP 4.5, RCP 8.5).

Si no dispone de este polígono, deje el parámetro vacío. El análisis se ejecutará solo con los datos históricos.

## Verificación previa a la ejecución

Antes de hacer clic en **Run**, revise la siguiente lista:

- [ ] Red vial con `ID_TRAMO`, `vul_f`, `vul_eq` y `rep_cost_k` completos.
- [ ] Al menos un conjunto de rásters de amenaza asignado.
- [ ] El archivo FVU está asignado al parámetro 10.
- [ ] Si se asigna el parámetro 11 (costos operativos), el parámetro 12 (PIB per cápita/día) también está completo.
- [ ] La longitud de segmento está definida.
- [ ] Todos los archivos están en el mismo SRC.

## Ejecución y seguimiento

Haga clic en **Run**. El progreso se muestra en la barra inferior del panel de geoprocesamiento. Los mensajes de avance incluyen:

- Confirmación de lectura de la base de vulnerabilidad.
- Progreso por amenaza y período de retorno.
- Mensajes de advertencia si algún ráster no tiene un Tr parseable en su nombre.
- Mensaje final `✅ Computation complete.` al terminar.

Al finalizar, las capas de resultados se agregan automáticamente al mapa activo y la configuración de la corrida se guarda en `Loc/run_config_<timestamp>.loc`.

## Ejemplo de configuración — Costa Rica

La siguiente tabla muestra la configuración usada para el caso de referencia de Costa Rica (ver [Caso de ejemplo](caso-ejemplo.md)):

| Parámetro | Valor |
|-----------|-------|
| Red vial | `crc_RVN_WGS84` |
| Puentes | `crc_rvn_puentes2` |
| Túneles | `cr_tuneles_rvn_WGS84` |
| Drenajes | `crc_rvn_drenaje2` |
| Inundación fluvial | 7 rásters: `ri_h_CR_{10,20,50,75,100,200,500}.tif` |
| Inundación costera | 10 rásters: `c_h_CR_{1,2,5,10,25,50,100,250,500,1000}.tif` |
| Tsunami | *(no disponible para CR)* |
| Sismo | 5 rásters: `EQ_CR_PGA_{100,225,475,2475,4975}.tif` |
| Licuefacción | *(no disponible para CR)* |
| FVU | `FVU_BSA_V3.csv` |
| Costos operativos | `OCO_BSA_CR_V1.csv` |
| PIB per cápita/día | `45249.62` |
| Longitud de segmento | `30` metros |
