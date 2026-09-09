# Propósito, alcances y limitaciones

## Propósito

El BSA 2.0 estima y compara las consecuencias económicas esperadas del daño físico y de la interrupción de tramos viales. Su producto es una base técnica homogénea para identificar concentraciones de riesgo y orientar evaluaciones e inversiones posteriores.

Puede aplicarse a corredores, áreas subnacionales o redes nacionales, siempre que la cobertura, resolución y calidad de los insumos sean compatibles con la escala del análisis.

## Alcance del cálculo

- Cruza activos georreferenciados con intensidades de amenaza.
- Aplica funciones de daño y de tiempo de interrupción elegidas por el usuario.
- Calcula daños directos y pérdidas operacionales por escenario.
- Integra probabilidades discretas para obtener DAE y PAE.
- Calcula una prioridad monetaria anual como suma de DAE y PAE.
- Permite un análisis de sensibilidad que modifica la frecuencia de inundación mediante la capa `Climate layer`.

## Fuera del alcance

La herramienta no modela amenazas, no levanta ni corrige inventarios, no calibra funciones de vulnerabilidad y no define automáticamente medidas de intervención. Tampoco evalúa fallas simultáneas de varios tramos, propaga la incertidumbre de las curvas ni reemplaza el análisis de ingeniería de cada activo.

El valor de prioridad no es un análisis multicriterio ni una recomendación automática de inversión. Antes de decidir una intervención deben considerarse factibilidad, costos, beneficios, equidad, ambiente, salvaguardas y criterios institucionales.

## Enfoque probabilístico simplificado

Las consecuencias se calculan para un conjunto discreto de períodos de retorno y se integran numéricamente. Por ello, los resultados dependen de la cobertura de probabilidades, la coherencia entre mallas y la regla aplicada a los extremos de la curva. Consulte [Cálculo de riesgo](calculo-riesgo.md).

