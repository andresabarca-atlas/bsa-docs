# Guía de Usuario

Esta sección describe cómo usar el BSA 2.0 de principio a fin: desde la preparación y estandarización de los datos de entrada hasta la interpretación de los mapas de riesgo y la priorización de inversiones.

## El proceso en síntesis

El BSA 2.0 transforma datos geoespaciales crudos en un ranking de tramos viales según su riesgo ante amenazas naturales. El proceso se puede resumir en cuatro etapas:

```
  Datos brutos                Preparación                 Ejecución               Interpretación
       │                           │                           │                         │
  Red vial        ──────►   Estandarizar capas   ──────►  Toolbox BSA2    ──────►  Mapas DAE / PAE
  Rásters amenaza           Completar atributos            (ArcGIS Pro)            Ranking Priority
  Vulnerabilidad            Calcular PIB/día                                       Dashboard BID
  Costos                    Definir segmentación
```

## Contenido de esta sección

| Página | Qué encontrarás |
|--------|-----------------|
| [Flujo de trabajo](flujo-trabajo.md) | Secuencia paso a paso desde la recepción de datos hasta la carga de resultados al dashboard. |
| [Datos de entrada](datos-entrada.md) | Descripción completa de cada capa de entrada: formato, atributos, obligatoriedad y convención de nombres. |
| [Configuración de una corrida](configuracion-corrida.md) | Cómo asignar parámetros en el toolbox, elegir la longitud de segmento y definir los parámetros económicos. |
| [Resultados](resultados.md) | Descripción de las capas de salida, sus campos y cómo interpretar DAE, PAE y Priority para la priorización. |
| [Caso de ejemplo — Costa Rica](caso-ejemplo.md) | Ejemplo completo con los datos del caso de referencia de Costa Rica. |

!!! tip "Punto de partida sugerido"
    Si es la primera vez que usa el BSA 2.0, lea primero el [Flujo de trabajo](flujo-trabajo.md) para tener una visión global del proceso, luego revise [Datos de entrada](datos-entrada.md) para validar que sus insumos cumplen el formato requerido.
