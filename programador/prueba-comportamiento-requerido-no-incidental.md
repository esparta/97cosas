---
layout: programador
title: Prueba el comportamiento requerido, no el comportamiento incidental
overview: true
author: Kevlin Henney
translator: Espartaco Palma
original: http://programmer.97things.oreilly.com/wiki/index.php/Test_for_Required_Behavior%2C_not_Incidental_Behavior
---

Una trampa común en las pruebas es asumir que lo que hace exactamente una implementación es precisamente lo que quieres probar. De primera instancia suena más como una virtud que una trampa. Sin embargo, expresado de otra manera, el tema se vuelve más obvio: Una trampa común en las pruebas es escribir las pruebas para las especificaciones de una implementación, donde estas especificaciones son incidentales y no tienen nada que ver con la funcionalidad deseada.

Cuando las pruebas están amarradas a la implementaciones incidentales, los cambios en la implementación son compatibles con el comportamiento requerido y  pueden provocar que las pruebas fallen, conduciéndonos a falsos positivos. Los programadores frecuentemente responden ya sea reescribiendo los test o reescribiendo el código. Asumir que un falso positivo es realmente un verdadero positivo es frecuentemente una consecuencia de miendo, incertidumbre o duda. Al reescribir una prueba, los programadores o reenfocan la prueba al comportamiento requerido (bien) o simplemente lo amarran a la nueva implementación (mal). Las pruebas necesitan ser lo suficientemente precisas, pero también necesitan ser exactas.

Por ejemplo, en una comparación de tres vías, tales como el `strcpm`de C o el `String.compareTo` de Java, el requerimiento en el resultado es que es negativo si el lado izquierdo es menor que el derecho, positivo si el lado izquierdo es mayor que el derecho, y cero si son considerados iguales. Este estilo de comparación es usado en muchas APIs, incluído el comparador de la función `qsort` de C y el `compareTo`en la interfaz `Comparable` de Java. Aunque los valores específicos -1 y +1 son comunmente usados en la implementación para significar menor-que y mayor-que, respectivamente, los programadores a menudo asumen erróneamente que estos valores representan el requerimiento actual y consecuentemente  escriben pruebas que clavan esta suposición en público.

Un tema similar surge cuando las pruebas que hacen asserts en el espaciado, texto exacto y otros aspectos del formato de texto y representación que son incidentales. A menos de que estés escribiendo, por ejemplo, un generador XML que ofrece un formateo configurable, el espaciado no debería ser significativo en la salida. Del mismo modo, amarrar el posicionamiento de botones y etiquetas en controles de Interfaz de Usuario (UI) reduce la opción de cambio y refina estas incidencias en el futuro. Los cambios menores en la implementación, así como los cambios insignificantes en el formato se vuelven de repente en cosas que rompen la construcción.

Las pruebas sobre-especificadas son frecuentemente un problema con enfoques de "caja blanca" en las pruebas unitarias. Las pruebas de "cajas blanca" usan la estructura del código para determinar los casos de prueba necesarios. La típica falla en las pruebas de "caja blanca" es que las pruebas terminan afirmando que el código hace lo que hace el código. El sólo reiterar lo que ya está siendo obvio del código no agrega valor y conduce a una falsa sensación de progreso y seguridad.

Para ser eficaces, las pruebas necesitan establecer obligaciones contractuales en lugar de parlotear la implementación. Necesitan tomar una visión de "caja negra" en las pruebas unitarias a probar, esbozando los contratos de las interfaz de manera ejecutable. Y así, alinear el comportamiento probado con el comportamiento requerido.

