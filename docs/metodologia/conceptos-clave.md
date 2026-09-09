# Conceptos clave

Esta página es la referencia conceptual del sitio. Aquí se definen los términos y métricas empleados de manera transversal en la metodología BSA 2.0. Familiarizarse con estas definiciones es esencial para interpretar correctamente los resultados y la documentación.

---

## Los cuatro componentes del riesgo

### Amenaza

Peligro latente de que un evento físico de origen natural —o inducido por la acción humana de manera accidental— se presente con severidad suficiente para causar daños y pérdidas en infraestructura, bienes, medios de vida o servicios ambientales.

En el BSA 2.0, la amenaza se representa mediante **mallas ráster** que contienen valores de intensidad asociados a distintos períodos de retorno. Las medidas de intensidad varían según el tipo de amenaza:

| Amenaza | Medida de intensidad | Símbolo |
|---|---|---|
| Inundación fluvial / pluvial / costera | Tirante hídrico (profundidad de lámina de agua) | TH |
| Inundación fluvial / pluvial / costera | Velocidad media del flujo | V |
| Sismo | Aceleración pico del suelo | PGA |
| Deslizamiento *(fase futura)* | Profundidad de depósito / velocidad de movimiento | LD |
| Huracán *(fase futura)* | Velocidad máxima del viento | WS |

### Exposición

La presencia de personas, servicios, bienes e infraestructura que, por su localización, pueden ser afectados por la manifestación de una amenaza. En el BSA 2.0, la exposición se modela como un inventario georeferenciado de la red vial, denominado **modelo de exposición**.

Cada elemento expuesto (EE) es un punto representativo de un tramo vial, con atributos que incluyen su valor físico (**VFi**) y su valor económico de tránsito (**VFt**).

### Vulnerabilidad

Susceptibilidad o fragilidad física de la infraestructura de ser afectada ante un evento de amenaza. Se expresa mediante **funciones de vulnerabilidad** que relacionan la intensidad del evento con la **Relación Media de Daño (RMD)**, expresada como fracción del valor físico del activo (entre 0 y 1).

A diferencia de las funciones de fragilidad —que estiman la *probabilidad* de alcanzar un estado de daño—, las funciones de vulnerabilidad del BSA 2.0 producen directamente el daño económico esperado.

### Criticidad

Medida de la importancia relativa de un tramo vial dentro de la red, en función de su papel funcional y del impacto que tendría su interrupción sobre la conectividad, accesibilidad y tránsito. Se determina mediante un **análisis multicriterio** que considera funcionalidad, redundancia, accesibilidad, valor estratégico y disrupción ante eventos extremos.

---

## Período de retorno (Tr)

El período de retorno (o intervalo de recurrencia) mide el *tiempo promedio* —en años— que transcurre entre eventos independientes que igualan o superan un nivel de intensidad determinado. Es equivalente al inverso de la **frecuencia anual de excedencia**:

$$
T_r = \frac{1}{\lambda}
$$

donde $\lambda$ es la tasa anual de excedencia. Por ejemplo, un evento con $T_r = 100$ años tiene una probabilidad de ocurrencia anual del 1 %.

En el BSA 2.0 se usan típicamente períodos de retorno de 10, 50, 100, 200 y 500 años para construir la curva de excedencia de pérdidas.

---

## Métricas de riesgo: la distinción fundamental entre daño y pérdida

!!! danger "Distinción crítica"
    En el BSA 2.0, **daño** y **pérdida** son conceptos distintos y no deben usarse como sinónimos.

### DAE — Daño Anual Esperado *(EAD en inglés)*

El **Daño Anual Esperado** cuantifica el impacto económico por **afectación física directa** a la infraestructura vial. Es el costo promedio anualizado de reparar o reponer los activos dañados por eventos naturales.

$$
\text{DAE} = \int_0^\infty D(p) \, d\lambda(p)
$$

donde $D(p)$ es el daño asociado a un evento de magnitud $p$ y $d\lambda(p)$ es el diferencial de la tasa de excedencia.

En la práctica discreta del BSA 2.0 se aproxima mediante la integral trapezoidal entre niveles de período de retorno:

$$
\text{DAE} \approx \sum_{i=1}^{n-1} \frac{D_i + D_{i+1}}{2} \cdot (\lambda_i - \lambda_{i+1})
$$

### PAE — Pérdida Anual Esperada *(EAL en inglés)*

La **Pérdida Anual Esperada** cuantifica el impacto económico por **disrupción funcional del tránsito**: el costo anualizado de la interrupción del servicio vial (pérdida de tiempo de viaje, desvíos, costo de logística, etc.) causada por eventos naturales que afectan la operabilidad de la red.

La fórmula es análoga a la del DAE, pero empleando la pérdida funcional $L(p)$ en lugar del daño físico.

### PML — Pérdida Máxima Probable

La **Pérdida Máxima Probable** es el daño o pérdida esperado asociado a un **evento de diseño** de referencia, típicamente el de $T_r = 500$ años. Representa el peor escenario plausible para fines de planificación de contingencias y aseguramiento.

### CEP — Curva de Excedencia de Pérdidas

La **Curva de Excedencia de Pérdidas** representa gráficamente la relación entre la magnitud de la pérdida y su frecuencia anual de excedencia. Integrar el área bajo esta curva equivale a calcular la PAE.

---

## Otras siglas y términos clave

| Sigla | Término completo | Definición breve |
|---|---|---|
| EE | Elemento Expuesto | Tramo vial discretizado como punto en el modelo de exposición |
| FVU | Función de Vulnerabilidad | Relación entre intensidad de amenaza y daño esperado (RMD) |
| RMD | Relación Media de Daño | Fracción del valor físico del activo que se espera perder; entre 0 y 1 |
| DMVi | Daño Medio Vial – Infraestructura | Daño físico esperado en un EE ante un evento de amenaza |
| PMVt | Pérdida Media Vial – Tránsito | Pérdida funcional esperada en un EE ante un evento de amenaza |
| VFi | Valor Físico de la Infraestructura | Costo de reposición del tramo vial expuesto |
| VFt | Valor Económico del Tránsito | Valor económico del tránsito por el EE (vehículos, carga, tiempo) |
| BSA | Blue Spot Analysis | Herramienta para identificar y priorizar puntos críticos de riesgo en redes viales |
| Tr | Período de Retorno | Tiempo medio entre eventos que igualan o exceden una intensidad dada |
| TH | Tirante Hídrico | Profundidad de la lámina de agua durante una inundación |
| PGA | Peak Ground Acceleration | Aceleración pico del suelo durante un evento sísmico |
| CEP | Curva de Excedencia de Pérdidas | Relación entre magnitud de pérdida y frecuencia de excedencia |

---

*Véase el [Glosario completo](../glosario/index.md) para definiciones adicionales. Para la estructura computacional de estos datos, véase [Estructura de datos](estructura-datos.md).*
