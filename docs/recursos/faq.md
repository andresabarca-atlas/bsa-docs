# Preguntas frecuentes

---

## Sobre la herramienta y los requisitos

??? question "¿Qué software necesito para usar el BSA 2.0?"

    El BSA 2.0 requiere **ArcGIS Pro** (versión 3.0 o superior) con una licencia activa, ya que la herramienta se distribuye como un *toolbox* (`.atbx`) nativo de esa plataforma. Además, Python 3 debe estar disponible en el entorno de ArcGIS Pro (viene incluido por defecto). No se requieren otros programas de modelación hidráulica ni SIG adicionales para ejecutar la herramienta; los datos de amenaza deben prepararse externamente y cargarse como insumos.

??? question "¿El BSA 2.0 incluye la generación de mapas de inundación?"

    No. El BSA 2.0 es una herramienta de **análisis de riesgo y priorización**, no de modelación hidráulica. Los mapas de inundación (profundidad, velocidad) para cada período de retorno deben obtenerse de estudios hidrológicos e hidráulicos previos y cargarse como datos de entrada. La herramienta los consume para calcular el daño y la pérdida sobre la infraestructura expuesta.

---

## Sobre los datos de entrada

??? question "¿Cómo debo organizar los datos de entrada?"

    La herramienta requiere una **geodatabase** con la red vial georreferenciada y una **ficha de parámetros** en formato Excel (22 hojas). La geodatabase debe incluir los tramos viales como elementos puntales o lineales, con atributos de tipo de vía, longitud y valor de reposición. Los mapas de amenaza deben estar en formato raster y proyectados en el mismo sistema de coordenadas que la red vial. Consulte la sección [Organización de datos](../getting-started/organizacion-datos.md) para la estructura detallada.

??? question "¿Qué licencias necesitan los datos de amenaza (inundación, sismo, etc.)?"

    El BSA 2.0 es neutral respecto a la fuente de los datos de amenaza. Pueden usarse datos de libre acceso (OpenStreetMap, GEBCO, USGS, GloFAS, OpenQuake, etc.) o datos propietarios de estudios hidrológicos e hidráulicos existentes. El equipo del proyecto ha trabajado principalmente con datos nacionales e internacionales de acceso abierto, pero la calidad y escala de los insumos impacta directamente la precisión de los resultados.

---

## Sobre la metodología y los resultados

??? question "¿Cuál es la diferencia entre DAE y PAE?"

    Son dos métricas complementarias que cuantifican distintos tipos de impacto:

    | Métrica | Nombre completo | Qué mide |
    |---------|-----------------|----------|
    | **DAE** (EAD) | Daño Anual Esperado / *Expected Annual Damage* | Daño físico directo a la infraestructura: costo de reparar o reponer la vía dañada |
    | **PAE** (EAL) | Pérdida Anual Esperada / *Expected Annual Loss* | Pérdida funcional y económica por interrupción del tránsito o del servicio vial |

    Un tramo puede tener bajo DAE (el daño físico es pequeño) pero alto PAE si conecta zonas de alto tráfico o es la única ruta disponible en caso de emergencia.

??? question "¿Qué amenazas naturales cubre el BSA 2.0 en su versión actual?"

    La versión actual del BSA 2.0 tiene implementados módulos para:

    - Inundación fluvial
    - Inundación pluvial / costera
    - Sismo
    - Tsunami
    - Licuefacción

    Los módulos de **deslizamientos** y **huracanes** están previstos para fases futuras del proyecto y no están disponibles en la versión actual.

??? question "¿A qué escala trabaja el BSA 2.0?"

    El BSA 2.0 está diseñado para análisis a **escala nacional o regional**. No está orientado al diseño de obras individuales ni al análisis de sitio puntual. Su propósito es generar rankings de priorización que orienten la distribución de inversiones entre múltiples activos de una red vial completa.

??? question "¿Qué es la Pérdida Máxima Probable (PML) y cómo se usa?"

    La **PML** (Pérdida Máxima Probable) es la pérdida estimada asociada a un evento de diseño específico, generalmente el correspondiente a un período de retorno de 500 años. A diferencia del DAE y el PAE (que son promedios anuales), la PML representa un escenario extremo útil para el dimensionamiento de fondos de contingencia, seguros o medidas estructurales de alto estándar.

---

## Sobre la aplicación en nuevos países

??? question "¿Cómo se aplica el BSA 2.0 a un nuevo país?"

    La implementación en un nuevo país sigue estos pasos principales:

    1. **Recopilación de datos de amenaza:** mapas de inundación, curvas de peligro sísmico, etc., para los períodos de retorno requeridos (p. ej. Tr = 10, 25, 50, 100, 200, 500 años).
    2. **Inventario vial:** base de datos georreferenciada de la red con tipologías, longitudes y costos de reposición.
    3. **Parámetros de tránsito:** volúmenes de tránsito (TPDA), valores del tiempo de viaje y de la carga transportada.
    4. **Configuración de la ficha Excel:** completar las 22 hojas de parámetros con los valores locales.
    5. **Ejecución de la herramienta:** correr los módulos secuencialmente (amenaza → exposición → vulnerabilidad → criticidad → riesgo).
    6. **Publicación del dashboard:** cargar los resultados a ArcGIS Online y configurar el dashboard.

    Para acceder a la guía detallada, contacte al equipo del proyecto en [MARIAESC@IADB.ORG](mailto:MARIAESC@IADB.ORG).

??? question "¿El BSA 2.0 es de uso libre?"

    No en esta etapa. El proyecto se distribuye bajo la **licencia AM-331-A3 del BID** y no está disponible públicamente. El acceso a la herramienta y los datos es restringido a equipos autorizados por el Banco Interamericano de Desarrollo. Consulte el archivo [LICENSE.md](../../LICENSE.md) para los términos completos.

---

## Sobre el dashboard

??? question "¿Puedo acceder al dashboard sin una cuenta de ArcGIS?"

    Los dashboards están publicados como aplicaciones de ArcGIS Experience Builder. En la mayoría de los casos son accesibles públicamente desde cualquier navegador sin necesidad de cuenta. Sin embargo, algunas funciones avanzadas de edición o análisis pueden requerir una cuenta institucional del BID en ArcGIS Online.

??? question "¿Los valores del dashboard se actualizan automáticamente?"

    No. El dashboard refleja los resultados de la última corrida del modelo BSA 2.0 cargada a ArcGIS Online. Para actualizar los resultados (por ejemplo, al incorporar nuevos datos de amenaza o ampliar la red evaluada), es necesario ejecutar nuevamente la herramienta y recargar los resultados en el servicio.
