# Propósito, alcances y limitaciones

## Propósito general

El BSA 2.0 tiene como propósito ofrecer una plataforma metodológica escalable y participativa que permita a instituciones de la región:

- Tomar **decisiones más informadas** sobre puntos críticos en la infraestructura de un país.
- **Priorizar inversiones** e intervenciones en la red vial expuesta a amenazas naturales.
- Mejorar la **planificación nacional y territorial** del mantenimiento y desarrollo de infraestructura crítica.
- Gestionar de manera dinámica el **inventario de activos** viales y de puentes.

En términos operativos, la plataforma facilita el cálculo de daños y pérdidas en la red vial nacional por amenazas naturales —con influencia de cambio climático—, la identificación de los tramos más críticos sobre los cuales enfocar inversiones, y la evaluación de las medidas de intervención más costo-efectivas.

## Preguntas que responde la herramienta

El BSA 2.0 está diseñado para ayudar a responder cuatro interrogantes estratégicos:

!!! question "¿Dónde están los activos y cuáles son sus características?"
    Mantener un inventario completo y actualizado de la red vial, incluyendo tipología estructural, valor económico y condición de adaptación.

!!! question "¿Qué elementos están en mayor riesgo?"
    Para el inventario actual de activos y el perfil de riesgos catastróficos del país, identificar cuáles elementos tienen mayor probabilidad de verse afectados por fenómenos naturales.

!!! question "¿En qué tramos debo enfocar la inversión?"
    En un contexto de incertidumbre económica, cambio climático y amenazas naturales, señalar los segmentos que merecen atención prioritaria.

!!! question "¿Qué tipo de intervención priorizar y a qué costo?"
    Ofrecer recomendaciones de arquetipos de medidas estructurales y no estructurales para reducir el riesgo, con estimaciones de la inversión requerida.

## Escalas de aplicación

Una característica distintiva del BSA 2.0 es su **diseño multiescala**. Las métricas generadas pueden informar decisiones en cuatro niveles:

```mermaid
graph LR
    A["🌎 Regional\n(entes internacionales)"] --> B["🇨🇷 Nacional\n(instituciones gubernamentales)"]
    B --> C["🛣️ Corredor vial\n(gobiernos locales)"]
    C --> D["📍 Tramo puntual\n(intervenciones específicas)"]
```

No todas las escalas se atienden desde las primeras iteraciones de la herramienta. La incorporación de análisis más detallados por corredor y tramo se habilitará conforme avance la integración de datos y funcionalidades.

## Consideración metodológica: enfoque probabilista simplificado

El BSA 2.0 adopta un **modelo probabilista simplificado**, adecuado para contextos donde los modelos de amenaza entregan mallas espaciales (rásteres) de intensidad asociadas a períodos de retorno discretos —que es el formato más comúnmente disponible en la región— en lugar de catálogos exhaustivos de eventos simulados estocásticamente (enfoques *event-based*).

Bajo este enfoque, la Curva de Excedencia de Pérdidas (CEP) no se deriva directamente, pero sí es posible estimar el **DAE y la PAE** mediante interpolación entre niveles discretos de amenaza, asumiendo continuidad funcional entre ellos y aplicando funciones de daño calibradas por intensidad. Este enfoque es compatible con el utilizado en el *Global Assessment Report on Disaster Risk Reduction 2015* (UNISDR), donde se calculó la PAE para más de 140 países a partir de mallas de amenaza para períodos de retorno de 25, 50, 100, 200, 500 y 1 000 años.

## Limitaciones reconocidas

### Sin propagación de incertidumbre en la vulnerabilidad

En las versiones iniciales del BSA 2.0, las pérdidas se estiman usando el **valor esperado** de las funciones de vulnerabilidad. Estas funciones están sujetas a una variabilidad inherente:

- **Incertidumbre epistémica**: limitación de datos históricos y calibración.
- **Incertidumbre aleatoria**: dispersión natural de la respuesta física del activo.

Dado que esta incertidumbre no se propaga explícitamente, los valores de DAE y PAE reportados son **estimaciones puntuales del valor medio**, no representaciones del espectro completo de posibles pérdidas.

!!! warning "Uso en procesos de diseño financiero"
    Se recomienda precaución al emplear estos valores para aseguramiento, diseño financiero o planificación de contingencias que requieran análisis de extremos. En esos casos, un análisis probabilístico completo —por ejemplo mediante simulaciones Monte Carlo— sería necesario.

### Datos de entrada: disponibilidad y calidad variable

La calidad de los resultados del BSA 2.0 depende directamente de la calidad de los datos de entrada: inventarios viales, modelos de amenaza y funciones de vulnerabilidad. En muchos países de la región, estos datos presentan cobertura incompleta o cronología desactualizada. La plataforma incorpora procedimientos de validación y actualización participativa para mitigar esta limitación.

### Amenazas fuera del alcance actual

Las amenazas **deslizamientos** y **huracanes**, aunque contempladas en el diseño del BSA 2.0, están previstas para fases futuras. Las amenazas actualmente implementadas son:

| Amenaza | Estado |
|---|---|
| Inundación fluvial | ✅ Implementada |
| Inundación pluvial / costera | ✅ Implementada |
| Sismo | ✅ Implementada |
| Tsunami | ✅ Implementada |
| Licuefacción | ✅ Implementada |
| Deslizamientos | 🔜 Fase futura |
| Huracanes | 🔜 Fase futura |

### No reemplaza estudios de diseño estructural

El enfoque probabilista simplificado del BSA 2.0 es apto para **priorización y planificación estratégica**, no para el diseño estructural de obras o la evaluación de pérdidas indirectas complejas, que requieren modelos dinámicos más detallados.

---

*Véase también: [Conceptos clave](conceptos-clave.md) para una definición precisa de las métricas DAE, PAE y PML.*
