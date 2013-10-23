Escribe las pruebas para las personas
===================
Autor: Gerard Meszaros
-------------------

Estás escribien pruebas automatizadas para algún o todo tu código de producción. ¡Felicidades! ¿Estás escribiendo tus pruebas antes de que escribas el código? ¡¡Mucho mejor!! El sólo hacerlo te convierte en uno de los primeros adoptantes de más avanzadas prácticas de la ingeniería de software. Pero, ¿estás escribiendo buenas pruebas? ¿cómo saberlo? Una mera es preguntar "¿Para quién estoy escribiendo estas pruebas?". Si la respuesta es "Para mí, para ahorrarme el esfuerzo de corregir errores" o "Para el compilador, con eso puede ser ejecutado", entonces las apuestas están en que no estás escribiendo las mejores pruebas posibles. Así que, ¿para quién deberías estár escribien las pruebas? Para las personas tratando de entender tu código.

Las buenas pruebas actúan como documentación para el código que estás probabdo. Describen cómo funciona el código. Por cada escenario de uso la(s) prueba(s):
* Describe el contexto, un punto inicial, o precondiciones que deben ser satisfacidas.
* Ilustra cómo el software es invocado.
* Describen los resultados esperados o postcondiciones a ser verificadas.

Los diferentes escenarios de uso tendrán una versión un poco diferente de cada uno de ellas. Las personas tratando de entender tu código deberían poder mirar unas cuantas pruebas y comparando estas tres partes de las pruebas en cuestion, poder ver qué causa que el código se comporte diferente. Cada prueba debería ilustrar claramente la relación de causa y efecto entre estas tres partes. Esto implica que lo que no es visible en las pruebas es tan importante como lo que es visible. Mucho código en las pruebas distrae al lector con trivialidades sin importancia. Cuando sea posible oculta dichas trivialidades detrás de llamados a métodos con significado -- la refactorización "Extraer Método" es tu mejor amigo. Y asegurate de darle a cada prueba un nombre con significado que describa el escenario de uso particular, con esto el lector de la prueba no tiene que hacer ingeniería inversa de cada prueba para entender de qué se tratan los distintos escenarios. Entre ellos, el nombre de las clases de prueba y los métodos de clases deben incluir al menor el punto inicial y cómo el software está siendo invocado. Esto permite que la covertura de prueba sea verificado vía un rápido escaneo de los nombres de los métodos. También puede ser útil el incluir los resultados esperados en el nombre del método de prueba mientras esto no cause que el nombre sea demasiado largo para ver o leer.

También es buena idea el poner a prueba tus pruebas. Puedes verificar que detectan el error que creer que detectan al incluir dicho error en el código de producción (por supuesto, en una copia privada que desecharás). Asegurate que reporte los errores de manera significativa. También debes verificar que tus pruebas hablan claramente a una persona tratanto de entender tu código. La única manera de hacerlo es tener alguien que no está familiarizado con tu código para que lea tus pruebas y te diga que ha aprendido. Escucha cuidadosamente lo que te diga. Si no entiendió algo claramente no es porque no sea muy brillante. Es más probable que tu fueras muy claro. (¡Continúa e inverte los roles, lee sus pruebas!)

Traducción: Espartaco Palma


[Leer contribución original](http://programmer.97things.oreilly.com/wiki/index.php/Write_Tests_for_People)

[Licencia Creative Commons Attribution 3](http://creativecommons.org/licenses/by/3.0/us/deed.es)
