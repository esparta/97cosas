97cosas.com
=======

Este es el proyecto de traducción al español de la serie de libros "97 cosas...", creados por la editorial [O'Reilly][1], los cuales, gracias a su licencia [Creative Commons Attribution 3][2], nos es posible traducir libremente. Es un esfuerzo compartido para poner a disposición de toda el habla hispana el contenido que actualmente sólo se encuentra en inglés.

Se tienen tres libros disponibles:

# LEEME para Contribuidores<sup>1</sup>

Este es un how-to amigable para los contribuidores de la traducción de "97 cosas...".

# Guía del Contribuidor

Si quieres colaborar, basta con que hagas un _fork_ de este repositorio. La traducción está escrita como un sitio de [Jekyll](http://jekyllrb.com/), hospedada en páginas de GitHub. Está configurado para que puedes escribir las páginas en Markdown.  Una guía de markup está más adelante.

Los archivos de traducción están en estas carpetas:

* programador/ ---> 97 cosas que todo programador
* pm/  --> 97 cosas que todo Projet Manager
* as/  --> 97 cosas que todo Arquitecto de Software

Todo está ligado en `index.md` en cada directorio.

# Previsualizando el contenido

Cuando haces _push_ a github (y hago un merge de ese _push request_), el sitio oficial en http://97cosas.com queda automáticamente actualizado.

Para generar y ver el sitio (con el correcto CSS, etc) con tu propia computadora, puedes instalar Jekyll y despues ejecutarlo así:

    cd ~/repos/97cosas  ##tu directorio donde se encuentra este repositorio
    jekyll --serve --auto
    # o
    jekyll serve --watch

Después navega hacia http://localhost:4000 para ver el contenido de la traducción. Si dejas el servidor ejecutándose, Jekill regenerará automáticamente el sitio cuando éste cambie.

# Mandando incidencias (issues)

Si no quieres, o no puedes (por tiempo o lo que sea) mandar un _push request_ también puedes utilizar el gestor de incidencias de github de el repositorio principal, aquí: https://github.com/esparta/97cosas/issues

Será necesario indicar en qué página está el error y su correción pertinente, por ejemplo:

>En la página "programador/no-te-repitas.html"
> dice: "parmetros"
> debe decir: "parámetros"

## Editando texto

* Usamos líneas largas (no saltos de línea en párrafos) para mantener los diffs moderadamente limpios.
* El código está indentado con 4 espacios.
* El HTML/CSS está indentado con 2 espacios.

En Vim, quizás desees esta configuración:

    set tabstop=4
    set shiftwidth=4
    set expandtab

# Guía Markup

# Sección de primer nivel
## Sección de segundo nivel
### Sección de tercer nivel
#### Sección de cuarto nivel

* Elemento de una lista
  * sub-elemento
  * sub-elemento 2
* Segundo elemento

1. Elemento de lista ordenada
2. Elemento 2 de lista ordenada
3. Elemento 3 de lista ordenada
  * Sub-elemento 1
  * Sub-elemento 2
4. Elemento 4 de lista ordenada
  1. Sub-elemento ordenado 1
  2. Sub-elemento ordenado 2
5. Elemento 4 de lista ordenada


*énfasis de texto* para énfasis

**texto en negritas** para negritas

Obtén literales con `backticks`

    O usa una identación de 4 espacios,
    para obtener un bloque de código,
    que luce bello.

> Haz unas cuantas citas. Puedes realizar reflujo de texto tanto como quieras. El salto de línea es impresionante. Y hecho de triunfos.

[enlaces para nerds](http://slashdot.org)

[enlaces para cosas](section8.html)

Esta es una división horizontal:

******

<sup>1</sup>: Pirateado y traducido de aquí: http://opentechschool.github.io/python-data-intro/

[1]: http://www.oreilly.com/
[2]: http://creativecommons.org/licenses/by/3.0/us/deed.es
[3]: http://programmer.97things.oreilly.com/wiki/index.php/97_Things_Every_Programmer_Should_Know
[4]: http://pm.97things.oreilly.com/wiki/index.php/Main_Page
[5]: http://softarch.97things.oreilly.com/wiki/index.php/Home_Page_for_97_Things