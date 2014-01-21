---
layout: programador
title: Usa el algoritmo y estructura de datos correcto
overview: true
author: JC van Winkel
translator: Espartaco Palma
original: http://programmer.97things.oreilly.com/wiki/index.php/Use_the_Right_Algorithm_and_Data_Structure
---

Un gran banco con muchas sucursales se quejó de que las nuevas
computadoras que había comprado para los cajeros eran muy lentas. Esto
era en el tiempo antes de que todos usaran la banca electrónica y los
cajeros automáticas no estaban tan extendidos como lo están ahora. La
gente visitaba el banco mucho más frecuentemente, y las computadoras
lentas estaban haciendo filas de gente. En consecuencia, el banco
amenazó con romper su contrato con el proveedor.

El proveedor envió un especialista en análisis y _tuning_ para
determinar la causa de los retrasos. Pronto encontró un programa
específico ejecutándose en la terminal consumiendo casi toda la
capacidad del CPU. Usando una herramienta de perfilado se enfocó en el
programa y pudo ver la función culpable. El código se leía:


    for (i=0; i<strlen(s); ++i) {
      if (... s[i] ...) ...
    }


La cadena `s` tenía en promedio, miles de caracteres de longitud. El
código (escrito por el banco) fué rápidamente cambiado, y los cajeros
vivieron felices por siempre...

¿No debía el programador haberlo hecho algo mejor que un código que
innecesariamente escalaba cuadráticamente?

Cada llamada a `strlen` recorría cada uno de los miles de caracteres en
la cadena para encontrar su caracter de terminación nula. La cadena, sin
embargo, nunca cambiaba. El determinar su longitud por adelantado, el
programador podía haber ahorrado cientos de llamadas a `strlen` (y
millones de ejecuciones del bucle):


    n=strlen(s);
    for (i=0; i<n; ++i) {
      if (... s[i] ...) ...

    }


Todos conocen el viejo dicho "primero haz que funcione, luego haz que
funcione rápido" para evitar los trampas de la micro-optimización. Pero
el ejemplo de arriba casi nos hace creer que el programador siguió el
Maquiavélico adagio "primero haz que funcione lentamente".

Este tipo de descuido es algo con lo podrías cruzarte más de una vez. Y
no es sólo un "no reinventes la rueda". Algunas veces los programadores
novatos sólo empiezan a escribir sin realmente pensar y de repente han
'inventado' el ordenamiento por burbuja. Incluso podrían estar
alardeando sobre eso.

El otro lado de elegir el algoritmo correcto es la elección de la
estructura de datos. Puede hacer una gran diferencia: Usar una lista
enlazada para una colección de millones de elementos por las que quieres
buscar -- comparada con una estructura de datos de hash -- va a tener un
gran impacto en la apreciación del usuario de tu programación.

Los programadores no deberían reinventar la rueda, y deberían usar
bibliotecas existente cuando fuera posible. Pero, para ser capaces de
evitar problemas como el del banco, deberían tambien ser educados acerca
de los algoritmos y cómo escalan. ¿Es sólo la vistosidad en los editores
lo que hace que sean tan lentos como los anticuados programas como
WordStar en la década de 1980? Muchos dicen que el reuso en la
programación es de gran importancia. Por encima de todo, sin embargo,
los programadores deben saber cuándo, qué y cómo reutilizar. Para poder
hacer eso deben tener el dominio del problema y los algoritmos y
estructuras de datos.

Un buen programador debería también saber cuándo usar un algoritmo
abominable. Por ejemplo, si el dominio del problema dicta que nunca
puede haber más de cinco elementos (como el número del dado en el juego
Yahtzee) y sabes que siempre tendrás que ordenar al menos cinco
elementos. En éste caso, el ordenamiento por burbuja puede ser la más
eficiente forma de ordenar los elementos. Cada perro tiene su día.

Entonces, lee algunos buenos libros -- y asegúrate que los entiendas. Si
realmente lees bien "El Arte de la programación" de Donald Knuth,
podrías incluso ser afortunado: Encuentra una equivocación del autor y
gana uno de los cheques de dólares hexadecimales ($2.56).

