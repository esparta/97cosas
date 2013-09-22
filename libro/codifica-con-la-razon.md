---
layout: page
title: Codificando con la razón
overview: true
permalink: /libro/codifica-con-la-razon/
---

Trata de razonar sobre la correctitud de software de mano resulta en una prueba formal de que es más que el código y es más contener errores que el código. Las herramientas automatizadas son preferibles, pero no siempre posibles. Lo siguiente describe una ruta intermedia: razonamiento semi-formal sobre la corrección.

El plantamiento de fondo es dividir todo el código en cuestión de secciones cortas -- desde una sóla línea, como una llamar una función, hasta bloques de menos de 10 línes -- y discutir acerca de su exactitud. Los argumentos sólo necesitan ser suficientemente fuertes para convencer al compañero del diablo como tu pareja de programación.

Una sección debería ser elegida de modo que en cada terminal el estado del programa (léase, el conteo del programa, y los valores de todos los objetos "vivos") satisface una propiedad fácilmente descrita, y que la funcionalidad de esa sección (transformación de estado) sea fácil de describir como una sola tarea -- éstos harán el razonamiento más sencillo. Tales propiedades terminales generalizan conceptos como precondinción y postcondición de funciones, e invariantes para ciclos y clases (con respecto a sus instancias). La lucha para que las secciones sean independientes de las otras tanto como sea posible simplifica el razonamiento y es indisponesable cuando estas secciones son modificadas.

Muchas de las prácticas de codificación que son bien conocidas (aunque quizás menos seguidas) y consideradas 'buenas' hacen el razonamiento más fácil. Por lo tanto, sólo la intención de razonar sobre tu código, ya estás comenzando a pensar acerca de un mejor estilo y estructura. Como era de esperarse, la mayoría de éstas prácticas pueden ser revisadas por analizadores de código estático:

1. Evita usar sentencias goto, ya que hacen las secciones remotas altamente interdependientes.
2. Evitar usar variables globales modificables, debido a que hacen a toda s las secciones que las usan, dependientes.
3. Cada variable debería tener el mínimo alcane posible. Por ejemplo, un objeto local puede ser declarado justo antes de su primer uso.
4. Haz los objetos inmutables cuando sea relevante.
5. Haz al código leible usando espacios, tanto horizontales como verticales. Por ejemplo, alineando estructuras relacionadas y usando una línea vacia para separar dos secciones.
6. Haz al código semi-documentable escogiendo nombres descriptivos (pero relativamente cortos) para los objetos, tipos, funciones, etc.
7. Si necesitas una sección anidada, haz una función.
8.- Crea tus funciones cortas y enfocadas en una sóla tarea. El viejo límite de 24 líneas aún aplica. A pesar que los tamaños de las pantallas han cambiado, nada ha cambiado en la cognición humana desde la decada de 1960.
9. Las funciones deben tener pocos parámetros (cuatro es buen límite superior). Esto no restringe los datos comunicados a las funciones: Agrupando parámetros relacionados en un objeto beneficia desde sus invariantes y ahorra razonamiento, tales como su coherencia y consistencia.
10. Más en general, cada unidad de código, desde un bloque hasta una librería, debería tener una interface rala. Menos comunicación reduce el razonamiento requerido. Esto significa que que los getters que regresar estados internos son una liabilidad -- no pidas a un objeto la información que ya tiene. En otras palabras, la encapsulación es todo -- y no sólo -- sobre interfaces limitadas.
11. Para poder preservar las clases invariantes, el uso de setters debería debería ser no recomendada, debido a que los setters tienden a permitir invariantes que gobiernan el estado de un objeto hacia su ruptura.

Conforme se razone sobre la correctitud, argumentar sobre tu código te ofrece entendimiento sobre él. Comunica sus descubrimientos para el beneficio de todos.

Por Yechiel Kimchi 

Traducción: Espartaco Palma

[Leer contribución original](http://programmer.97things.oreilly.com/wiki/index.php/Coding_with_Reason)

[Licencia Creative Commons Attribution 3](http://creativecommons.org/licenses/by/3.0/us/deed.es)