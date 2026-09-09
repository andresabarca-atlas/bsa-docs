# Ejemplo de verificación de una corrida

Esta guía evita asociar la metodología a un país específico. Use un subconjunto pequeño y conocido de su propia red para verificar la instalación y los datos.

## Conjunto mínimo recomendado

- una capa de carreteras con varios enlaces nodo–nodo, incluido al menos un tramo con desvío y otro sin alternativa;
- dos o más rásteres de una misma amenaza con TR distintos;
- un CSV de vulnerabilidad que cubra todas las taxonomías;
- opcionalmente, una capa puntual vinculada por `ID_TRAMO`;
- para PAE, base de operaciones y PIB per cápita diario en moneda local;
- una distancia de muestreo coherente con el tamaño de celda.

## Resultados esperados

1. Se crean capas con marca temporal en `BSA2.gdb`.
2. Los campos de daño aumentan de manera plausible con la intensidad.
3. DAE y PAE son no negativos.
4. El tramo con alternativa utiliza distancia adicional; el tramo aislado utiliza ocupación y PIB.
5. `Priority` coincide exactamente con la suma correspondiente.
6. El archivo `.loc` conserva los parámetros de la prueba.

Documente este ensayo como control de aceptación antes de procesar una red completa.

