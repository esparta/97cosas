# LEEME para Editores

Este es un how-to amigable para los editore de la traducción de
"97 cosas...". <sup>1</sup>

## Breves lineamientos en la edición

La traducción está escrita como un sitio de [Jekyll][1], hospedada en
páginas de GitHub. Está configurado para que puedes escribir las páginas
en [Markdown][2]. Una [guía de markup](#gu%C3 %ADa-markup) está más
adelante.

* Usamos líneas de un máximo de 80 caracteres (por [petición
popular][3] y decisión del administrador: @esparta)
* El código está indentado con 4 espacios.
* El HTML/CSS está indentado con 2 espacios.
* Los enlaces deberán ser al estilo "corto": `[Enlace][1]`

En Vim, quizás desees esta configuración:

    set tabstop=4
    set shiftwidth=4
    set expandtab
    set columns=80

## Estructura de archivos

Los archivos de traducción están en estas carpetas:

* programador/ ---> 97 cosas que todo programador
* pm/  --> 97 cosas que todo Project Manager
* as/  --> 97 cosas que todo Arquitecto de Software

Todo está ligado en `index.md` en cada directorio.


## Previsualizando el contenido

Para generar y ver el sitio (con el correcto CSS, etc) con tu propia
computadora, puedes instalar Jekyll y después ejecutarlo así:

```bash
# Jekyll se instala así: gem install jekyll
cd ~/repos/97cosas  ##tu directorio donde se encuentra este repositorio
jekyll --serve --auto
# o
jekyll serve --watch
```
Después navega hacia http://localhost:4000 para ver el contenido de la
traducción. Si dejas el servidor ejecutándose, Jekyll regenerará
automáticamente el sitio cuando éste cambie.

## Enviando peticiones de actualización

Primero, deberás hacer los cambios locales en tu repositorio (ya sabes,
`git add `, luego `git commit ...`), luego haz _push_ a github, toca
hacer [_pull request_][4]) y es todo. Una vez que hago el _merge_ de esa
petición, el sitio oficial en http://97cosas.com queda automáticamente
actualizado.

De preferencia envía un _pull request_ por archivo a modificar, así nos
podemos organizar mejor.

## Guía Markup

```markdown
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

> Haz unas cuantas citas. Puedes realizar reflujo de texto tanto como
quieras. El salto de línea es impresionante. Y hecho de triunfos.

Hay varias formas de crear enlaces en Markdown, pero por legibilidad
estamos usando los enlaces "abreviados", donde los links van al final
del archivo:

[enlaces para nerds][1]

[enlace interno][2]

[1]: http://slashdot.org
[2]: no-te-repitas.html

Esta es una división horizontal:

******
```
******
<sup>1</sup>: Pirateado y traducido de aquí: http://opentechschool.github.io/python-data-intro/


[1]: http://jekyllrb.com/
[2]: http://daringfireball.net/projects/markdown/
[3]: https://github.com/esparta/97cosas/issues/3
[4]: https://help.github.com/articles/using-pull-requests