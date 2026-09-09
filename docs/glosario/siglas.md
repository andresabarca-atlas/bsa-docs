# Diccionario de siglas

Siglas y acrónimos utilizados en la metodología, la herramienta y la documentación del BSA 2.0. Ordenados alfabéticamente.

*Fuente principal: Tabla 4.1 del Concept Report BSA 2.0. Se añaden DAE, EAD y EAL para alinear con las reglas de terminología del proyecto.*

---

| Sigla | Significado | Descripción técnica |
|-------|-------------|---------------------|
| **BSA** | Blue Spot Analysis | Herramienta para identificar, priorizar y recomendar soluciones para puntos críticos de riesgo (*Blue Spots*) por amenazas naturales en redes de infraestructura vial. |
| **CEP** | Curva de Excedencia de Pérdidas | Representación gráfica de la relación entre la probabilidad de ocurrencia y la magnitud de la pérdida. El área bajo la curva equivale al PAE/EAL. |
| **DAE** | Daño Anual Esperado | Valor monetario promedio anual de los daños físicos directos a la infraestructura vial, integrado sobre todos los períodos de retorno evaluados. Equivale al *Expected Annual Damage* (EAD) en inglés. Mide el impacto físico sobre la vía, no la pérdida por interrupción del servicio. |
| **DMVi** | Daño Medio Vial – Infraestructura | Valor esperado del daño físico para un tramo vial ante un evento dado, según su tipo y condición estructural. |
| **EAD** | Expected Annual Damage | Traducción al inglés de Daño Anual Esperado (DAE). Véase DAE. |
| **EAL** | Expected Annual Loss | Traducción al inglés de Pérdida Anual Esperada (PAE). Véase PAE. |
| **EE** | Elemento Expuesto | Tramo vial discretizado (representado como punto o línea en un shapefile) sobre el cual se calculan los impactos por evento. |
| **FVU** | Función de Vulnerabilidad | Relación funcional entre la intensidad de la amenaza (TH, V) y el grado de daño esperado para un tipo de activo vial. |
| **FVU tráfico** | Función de Vulnerabilidad para el Tránsito | Función que modela el impacto del evento sobre la operatividad o el valor económico del tránsito que circula por el tramo afectado. |
| **Mód. Criticidad Funcional** | Módulo de Criticidad Funcional del Tránsito | Módulo de la herramienta BSA 2.0 que estima el impacto funcional de la disrupción de un tramo vial sobre la red y el tránsito. |
| **Mód. Exposición** | Módulo de Exposición | Base de datos georreferenciada que caracteriza todos los elementos expuestos susceptibles de sufrir un daño o pérdida. |
| **Mód. Vuln. Física** | Módulo de Vulnerabilidad Física | Módulo de la herramienta que contiene el conjunto de funciones de vulnerabilidad correspondientes a cada tramo vial y tipología de tránsito identificados en el modelo de exposición. |
| **PAE** | Pérdida Anual Esperada | Valor monetario promedio anual de las pérdidas funcionales y económicas por interrupción del tránsito o del servicio vial, integrado sobre todos los períodos de retorno evaluados. Equivale al *Expected Annual Loss* (EAL) en inglés. Mide la pérdida por interrupción del servicio, no el daño físico directo. |
| **PML** | Pérdida Máxima Probable | Pérdida estimada para un evento de diseño específico (p. ej. Tr = 500 años). Representa el escenario extremo de referencia para dimensionamiento de reservas o medidas estructurales de alto estándar. |
| **PMVt** | Pérdida Media Vial – Tránsito | Valor esperado de la pérdida funcional o económica por disrupción del tránsito ante un evento dado. |
| **TH** | Tirante Hídrico | Profundidad de la lámina de agua sobre una superficie durante un evento de inundación, expresada en metros. Parámetro de intensidad de amenaza en las funciones de vulnerabilidad. |
| **Tr** | Período de Retorno | Frecuencia estadística con la que se espera que se iguale o exceda la magnitud de un evento. Se expresa en años (p. ej. Tr = 100 años significa una frecuencia anual de excedencia del 1 %). |
| **V** | Velocidad | Velocidad del flujo superficial durante el evento de inundación, en metros por segundo. Parámetro complementario al TH en las funciones de vulnerabilidad. |
| **VFi** | Valor Físico de la Infraestructura | Costo estimado de reposición del tramo vial expuesto, según tipología y longitud. Base del cálculo del DAE. |
| **VFt** | Valor Económico del Tránsito | Valor económico asociado al tránsito por tramo vial (vehículos, carga, tiempo de viaje). Base del cálculo del PAE. |

---

!!! tip "DAE/EAD vs. PAE/EAL"
    En la documentación del BSA 2.0 se usan los términos en español (DAE, PAE) como nombres primarios y los acrónimos en inglés (EAD, EAL) como equivalentes. **DAE = EAD** (daño físico directo) y **PAE = EAL** (pérdida por interrupción del servicio). Estas dos métricas no deben confundirse: cuantifican tipos de impacto distintos y complementarios.
