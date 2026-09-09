# Registro de actualización documental — 9 de septiembre de 2026

## Alcance

Se actualizó la versión en español del sitio con base en `Documentacion_BSA_2_0_08092026.docx` y se contrastaron los contenidos operativos con `BSA2.py` y `BSA2.atbx` incluidos en el repositorio.

No se modificaron `fuentes/`, `PLAN_Documentacion_BSA2.md` ni `PROMPT_Claude_Code.md`.

## Cambios principales

- Se explicitó que BSA 2.0 no genera modelos de amenaza, exposición o vulnerabilidad.
- Se documentó el enfoque probabilístico simplificado y la referencia BID de 2019.
- Se incorporaron entorno tecnológico, requisitos, acceso e interfaz del toolbox.
- Se actualizaron contratos de amenaza, exposición, vulnerabilidad, operaciones y Climate layer.
- Se sustituyó la criticidad multicriterio por el cálculo tramo–nodo, Dijkstra, desvío y viajes no realizados.
- Se eliminó PML como salida de la versión actual.
- Se creó el capítulo de Priorización con la regla única `DAE + PAE`.
- Se conservaron e incorporaron las capturas originales del dashboard.
- Se corrigieron FAQ, ejemplo, resultados, siglas y referencias.
- Se añadieron 22 imágenes revisadas/originales en `docs/assets/bsa2/`.
- Se añadió Priorización a la navegación de `mkdocs.yml`.

## Verificaciones

- Compilación ejecutada con `python -m mkdocs build --strict`.
- Resultado: compilación correcta para español e inglés.
- Se comprobaron rutas internas e imágenes mediante la compilación estricta.

## Decisiones técnicas derivadas del código

- El tipo de amenaza se toma del cuadro de la interfaz; el TR es la última secuencia entera del nombre del ráster.
- DAE y PAE requieren dos o más TR válidos por amenaza para producir una integral distinta de cero.
- La integración incluye la cola `p_min × C(p_min)`.
- El código asigna PAE a activos puntuales usando el costo diario de su `ID_TRAMO` y el tiempo propio del activo.
- El código actual no calcula PML.
- La interfaz declara parámetros como opcionales, pero el script exige carreteras, distancia de muestreo, vulnerabilidad y al menos una amenaza.

## Punto técnico pendiente

El contrato documental de licuefacción define clases 1–4 asociadas a `LQ1`–`LQ4`. El `BSA2.py` incluido agrupa 1 y 2 en `LQ1` y desplaza las clases siguientes. Se dejó una advertencia visible en el capítulo de vulnerabilidad. Se recomienda corregir o confirmar el código antes de una corrida productiva con licuefacción.

## Idioma

La versión en español quedó actualizada. Los archivos `*.en.md` se conservaron sin cambios y deben traducirse o sincronizarse en una fase posterior.

