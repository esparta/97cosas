---
layout: page
title: Conoce tu IDE
overview: true
permalink: /libro/conoce-tu-ide/
---

En la década de 1980s nuestros entornos de progración eran por lo general nada mejor que editores de texto glorificados... si teníamos suerte. El resaltado de sintaxis, que damos por sentado hoy en día era un lujo que ciertamente no estaba disponible para todos. Los Pretty Printers para formatear bien nuestro código eran usualmente herramientas externas que tenían que ser ejecutadas para corregir nuestro espaciamiento. Los depuradores eran tambien programas separados ejecutándose paso a paso a través de nuestro código, pero con un montón de teclazos crípticos.

Durate la década de 1990s las compañías comenzaron a reconocer el potencial de ingresos que pudieran derivarse de equipar a los programadores con mejores y más útiles herramientas. El Entorno Integrado de Desarrollo (IDE, por sus siglas en inglés) combinaban las características de edición previas con un compilador, un depurador, pretty printer, y otras herramientas. Durante ese tiempo, los menus y el ratón también se volvieron populares, lo cuál significaba que los desarrolladores ya no necesitaban aprender combinaciones de tecla crípticos para usar sus editores. Podían simplemente seleccionar su comando en el menú.

En el siglo 21 los IDEs se convirtieron en un lugar tan común que eran regalados por las compañías que deseaban ganar un segmento del mercado en otras áreas. El IDE moderno está equipado con una increible variedad de características. Mi favorita es la refactorización automatizada, particularmente la Extracción de Método, donde puedo seleccionar y convertir un fragmento de código en un método. La herramienta de refactorización recogerá todos los parámetros que deben ser transferidos al método, lo cuál hace extremadamente fácil el modificar código. Mi IDE detectará incluso otro fragmento de código que podría también ser reemplazado por este método y preguntarme si deseo reemplazarlo también.

Otra característica sorprendente en los IDE modernos es la capacidad de hacer cumplir las reglas de estilo dentro de una empresa. Por ejemplo, en Java, algunos programadores han empezado a hacer todos los parámetros como `final` (lo cual, en mi opinión, es una pérdida de tiempo). Sin embargo, como ellos tienen esto como una regla de estilo, todo lo que necesitaría hacer a continuación es configurarlo en mi IDE: Obtendría algunas advertencias por cada parametro que no fuese `final`. Las reglas de estilo también pueden ser utilizadas para encontrar errores probables, tales como comparar objetos autoboxed para la igualdad de referencia, por ejemplo, usando == en los valores primitivos que están autoboxed en referencias a objetos.

Desafortunadamente los IDE modernos no requiere de invertir esfuerzo para aprender a usarlos. Cuando programé por primera vez en C bajo Unix, tuve que pasar un poco de tiempo aprendiendo cómo trabajaba el editor vi, debido a su curva de aprendizaje. Este tiempo gastando pagó por adelantando bellamente al paso de los años. Incluso he escrito el borrador de este artículo con vi. Los IDE modernos tienen una curva de aprendizaje muy gradual, la cual puede tener como consecuencia que nunca progresamos más allá del uso básico de la herramienta.

Mis primeros pasos al aprender un IDE es memorizar los atajos de teclado. Ya a que mis dedos están en el teclado cuando estoy escribiendo mi código, presionar Ctrl+Shift+I para alinear una variable me ahorra el tener que romper mi flujo, el navegar por el menu con el ratón interrumpe este flujo. Estas interrupciones lleva a cambios de contexto innecesarios, haciendome mucho menos productivo si trato de hacer todo por el camino perezoso. La misma regla también aplica a las habilidades del teclado: Aprende a teclear, no te arrepentirás del tiempo invertido por adelantado.

Por último, como programadores tenemos herramientas streaming Unix que pueden ayudarnos a manipular el código. Por ejemplo, si durante una revisión de código, me doy cuenta que el programador ha nombrado muchas de sus clases igual, puedo encontrar muchas de ellas fácilmente usando las herramientas buscar, sed, sort, uniq, y grep, así:

{% highlight sh %}

find . -name "*.java" | sed 's/.*\///' | sort | uniq -c | grep -v "^ *1 " | sort -r

{% endhighlight %}

Esperamos que un plomero venga a nuestra casa para poder usar su soplete. Pasemos un poco de tiempo estudiando cómo ser más efectivos con nuestro IDE.

Por Heinz Kabutz 

Traducción: Espartaco Palma

[Leer contribución original](http://programmer.97things.oreilly.com/wiki/index.php/Know_Your_IDE)

[Licencia Creative Commons Attribution 3](http://creativecommons.org/licenses/by/3.0/us/deed.es)