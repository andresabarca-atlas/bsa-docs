# Configuración de una corrida

## 1. Abrir BSA2

Desde **Catalog**, agregue o localice `BSA2.atbx` y abra la herramienta `BSA2`.

## 2. Cargar exposición

Cargue la red en **Road exposure layer**. Añada puentes, túneles y drenajes si forman parte del análisis. Confirme que los activos puntuales referencian los tramos correctos.

## 3. Cargar amenaza

En cada cuadro multivalor, cargue todos los rásteres pertenecientes a esa amenaza. No combine tipos diferentes en el mismo cuadro. Compruebe que el último entero del nombre sea el período de retorno.

## 4. Cargar bases

Seleccione el CSV de vulnerabilidad. Para calcular pérdidas operacionales, cargue además la base de operaciones e ingrese el PIB per cápita por día; estos dos parámetros funcionan como pareja.

## 5. Definir muestreo

Ingrese **Road segment length (m)**. Use la resolución del ráster como referencia y pruebe más de un valor cuando la escala o el tiempo de ejecución sean sensibles.

## 6. Añadir Climate layer, si aplica

Cargue la capa poligonal sólo si desea recalcular la integración con períodos de retorno futuros. Verifique campos `TP#S#M` y valores positivos.

## 7. Ejecutar y controlar

Pulse **Run**, conserve el panel de mensajes y no mueva los insumos durante la corrida. Al terminar, verifique las capas con marca temporal en `BSA2.gdb` y el archivo de configuración en `Loc`.

!!! warning
    La interfaz visual marca varios parámetros como opcionales, pero el código requiere carreteras, longitud de segmento, CSV de vulnerabilidad y al menos una malla de amenaza.

