---
layout: programador
title: El linker no es un programa mágico
overview: true
author: Walter Bright
translator: Espartaco Palma
original: http://programmer.97things.oreilly.com/wiki/index.php/The_Linker_Is_not_a_Magical_Program
---

Con una frecuencia depresiva (me sucedió otra vez justo antes de
escribir esto), la visión que tienen muchos programadores sobre el
progrceso de pasar de código fuente a un ejecutable estáticamente
enlazado en un lenguaje compilado es:

1. Editar código fuente
2. Compilar el código fuente en archivos _objeto_
3. Algo mágico sucede
4. Ejecutar ejecutable

El paso 3 es, por supuesto, el paso de enlazado. ¿Por qué diría cosa tan
atroz? He estado en soporte técnico por décadas, y tengo las siguientes
preguntas una y otra vez:


1. El linker dice "def está definido más de una vez".
2. El linker dice "abc es un símbolo sin resolver".
3. ¿Porqué el ejecutable es tan grande?

Seguido de "¿Ahora qué hago?" usualmente mezclado junto con las frases
"parece que" y "de alguna manera", y un aura total desconcierto. Son los
"parece que" y "de alguna manera" los que indican que el proceso de
enlace es visto como un proceso mágico, presumiblemente entendible sólo
por magos y brujos. El proceso de compilado no provoca este tipo de
frases, implicando que los programadores generealmente entienden cómo
funcionan los compiladores, o al menos qué hacen.

Un linker es programa muy estúpido, ordinario y directo. Todo lo que
hace es concatenar el código y las secciones de datos de los archivos
_objeto_, conectar las referencias a los símbolos con sus definiciones,
empujar símbolos sin resolver fuera de la biblioteca, y escribir un
ejecutable. Eso es todo. ¡Sin hechizos! ¡Sin magia! Lo tedioso de
escribir un linker es usualmente por decodificar y generar formatos de
archivo ridículamente sobrecomplicados en general, pero eso no cambia la
escencia natural de un linker.

Digamos que el linker está diciendo "def está definido más de una vez".
Muchos lenguajes de programación, tales como C, C++, y D, tienen ambos,
declaraciones y definiciones. Las declaraciones normalmente van en
archivos de encabezados, tales como:

    extern int iii;

lo cual genera una referencia externa al símbolo iii. Una definición,
por otro lado, en realidad establece el almacenamiento para el símbolo,
usualmente aparece en el archivo de implementación, y luce así:

    int iii = 3;

¿Cuántas definiciones puede haber por cada símbolo? Como en la película
¿Highlander, sólo puede haber uno. Así que, que tal si una definición de
¿iii aparece en más de un archivo de implementación?

    // Archivo a.c
    int iii = 3;

    // Archivo b.c
    double iii(int x) { return 3.7; }

El linker se quejará porque iii está siendo definido varias veces.

No sólo puede haber sólo uno, debe haber uno. Si iii sólo aparece como
una declaración, pero nunca en una definición, el linkers se quejará
sobre iii siendo un símbolo no resuelto.

Para determinar por qué un ejecutable es del tamaño que es, dale un
vistazo al archivo de map que los linkers general opcionalmente. Un
archivo de mapa es nada más que una lista de todos los símbolos en el
ejecutable junto con sus direcciones. Te dice qué módules fueron
enlazados desde la biblioteca, y el tamaño de cada módulo. Ahora puedes
ver dónde viene tanto hinchazón. Frecuentemente habrá módulos de
biblioteca que no tendrás ideas porqué fueron enlazados. Para saberlo,
quita temporalmente el módulo sospechoso de la biblioteca, y vuelve a
enlazar. El error de "símbolo no definido" generado indicará quién está
referenciando ese módulo.

Aunque no siempre es inmediatamente obvio por qué aparece un mensaje del
linker en particular, no hay nada mágico sobre los linkers. La mecánica
es directa; son los detalles lo que hay que tienes que averiguar en cada
caso.

