# Módulo de Amenaza

El módulo de amenaza del BSA 2.0 caracteriza las amenazas naturales relevantes para la infraestructura vial, priorizando aquellas que generan interrupciones recurrentes o daños estructurales significativos. La herramienta trabaja con mallas ráster de intensidad de amenaza asociadas a períodos de retorno discretos, que son el tipo de dato más comúnmente disponible en los países de América Latina y el Caribe.

## Amenazas implementadas

### Inundación fluvial

Se genera por desbordamiento de cauces como resultado de lluvias prolongadas o intensas sobre una cuenca hidrográfica. El enfoque combina:

- **Modelación hidrológica** (estimación de caudales de diseño): herramientas como HEC-HMS, HydroBID o SWAT.
- **Modelación hidráulica** (propagación del flujo): herramientas como HEC-RAS 2D, LISFLOOD-FP o HydroBID Flood.

Los productos son mapas de **tirante hídrico (TH)** y **velocidad media del flujo (V)** para distintos períodos de retorno.

### Inundación pluvial y costera

**Pluvial**: se origina por lluvias intensas que exceden la capacidad de los sistemas de drenaje urbano. Se modela mediante enfoques hidrológicos e hidrodinámicos urbanos (EPA SWMM, InfoWorks ICM, MIKE URBAN+).

**Costera**: se asocia a la acción combinada de oleaje, marea astronómica, marea de tormenta (*storm surge*) y ascenso del nivel del mar. Se representan con modelos como ADCIRC, Delft3D, MIKE 21 o XBeach.

Ambas amenazas producen mallas de TH y V por período de retorno.

### Sismo

La amenaza sísmica se representa mediante **análisis de amenaza sísmica probabilista (PSHA)**, que integra fuentes sismogénicas, leyes de atenuación y catálogos históricos. El producto son mapas de **aceleración pico del suelo (PGA)** para distintos períodos de retorno. Herramientas como OpenQuake o CRISIS permiten la modelación regional o nacional.

### Tsunami

Los tsunamis se modelan a partir de fuentes sismogénicas costeras y submarinas, propagando las ondas hasta la costa mediante modelos numéricos. Los productos son mallas de altura de inundación y velocidad de flujo por evento de diseño.

### Licuefacción

La licuefacción es el fenómeno por el cual suelos saturados pierden resistencia durante un sismo. Se modela a partir de mapas de susceptibilidad de suelos, aceleración sísmica y nivel freático. Los productos son índices de susceptibilidad o mapas de probabilidad de ocurrencia por período de retorno sísmico.

---

!!! note "Amenazas en fases futuras"
    Las amenazas de **deslizamientos** y **huracanes** están contempladas en el diseño del BSA 2.0, pero están previstas para fases futuras de desarrollo. No se encuentran implementadas en la versión actual de la herramienta.

---

## Resumen de tipos de amenaza

| Amenaza | Estado | Herramientas de referencia | Medida de intensidad |
|---|---|---|---|
| Inundación fluvial | ✅ Implementada | HEC-RAS, LISFLOOD-FP, HydroBID Flood | TH, V |
| Inundación pluvial | ✅ Implementada | EPA SWMM, InfoWorks ICM, MIKE URBAN+ | TH, V |
| Inundación costera | ✅ Implementada | ADCIRC, Delft3D, MIKE 21, XBeach | TH, V |
| Sismo | ✅ Implementada | OpenQuake, CRISIS | PGA |
| Tsunami | ✅ Implementada | Modelos de propagación de ondas | TH, V |
| Licuefacción | ✅ Implementada | Modelos de susceptibilidad | Índice / Probabilidad |
| Deslizamientos | 🔜 Fase futura | SHALSTAB, TRIGRS, modelos de ML | LD |
| Huracanes | 🔜 Fase futura | HAZUS-MH, ADCIRC+SWAN, CHAZ | WS |

## Escalas temporales y espaciales

Los modelos de amenaza se diseñan para operar desde el nivel regional hasta el nacional, cubriendo extensas redes viales y corredores estratégicos. En cuanto a la escala temporal, el módulo emplea **períodos de retorno representativos**: 10, 50, 100, 200 y 500 años (o sus equivalentes en frecuencia anual de excedencia).

El módulo es compatible con datos de amenaza provenientes de iniciativas internacionales como:

- **GLOFAS** (inundación fluvial global)
- **AQUEDUCT** (riesgo hídrico)
- **ThinkHazard!** (múltiples amenazas)
- **World Bank Disaster Risk Data Platform**

Esta estructura captura el comportamiento probabilista de las amenazas y es coherente con el enfoque de estimación simplificada de la PAE y la CEP.

## Escenarios de cambio climático

El módulo de amenaza permite la incorporación de **escenarios climáticos futuros**, en particular los *Shared Socioeconomic Pathways* (SSP) del CMIP6:

- **SSP2-4.5**: escenario de emisiones intermedias.
- **SSP5-8.5**: escenario de altas emisiones.

Se pueden incluir mapas de amenaza generados con proyecciones de precipitación o nivel del mar bajo estos escenarios, permitiendo la **comparación entre escenarios actuales y futuros** para capturar el efecto incremental del cambio climático sobre la amenaza. Esto es coherente con los Modelos de Circulación General del CMIP5 y CMIP6 (Eyring et al., 2016).

!!! tip "Interoperabilidad con datos existentes"
    La herramienta acepta mallas de amenaza en formatos GeoTIFF y Raster Esri Grid, lo que facilita el uso de modelos de amenaza ya generados por agencias nacionales o instituciones internacionales, sin necesidad de ejecutar nuevas modelaciones hidrodinámicas.

---

*Para entender cómo se intersectan las mallas de amenaza con los elementos expuestos, véase [Módulo de Exposición](modulo-exposicion.md) y [Lógica funcional y arquitectura](arquitectura.md).*
