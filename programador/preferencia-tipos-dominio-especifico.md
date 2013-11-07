---
layout: programador
title: Da preferencia a tipos de Dominio Específico que los tipos primitivos
overview: true
author: Einar Landre
translator: Espartaco Palma
original: http://programmer.97things.oreilly.com/wiki/index.php/Prefer_Domain-Specific_Types_to_Primitive_Types
---

El 23 de Septiembre de 1999 el Mars Climite Orbiter de U$327.6 millones se perdió mientras entraba a la órbita alrededor de Marte debido a un error del software aquí en la Tierra. Error que más tarde fue llamado de "Métrica mixta". El software de la estación en tierra estaba trabajando en libras, mientras que la nave esperaba newtons, llevando a la estación en tierra a subesestimar el poder de los propulsores la nave en un favtor de 4.45.

Este es uno de los muchos ejemplos de fallas de software que se pudo haber prevenido si se hubiera aplicado un tipado más fuerte y de dominio específico. Es también un ejemplo del razonamiento detras de muchas características del lenguaje Ada, uno de sus principales metas de diseño era el implementar software de seguridad crítica embebida. Ada estaba fuertamente tipeado con revisiones estáticas de ambos: tipos primitivos y tipos definidos por el usuario.

    type Velocity_In_Knots is new Float range 0.0 .. 500.00;

    type Distance_In_Nautical_Miles is new Float range 0.0 .. 3000.00;

    Velocity: Velocity_In_Knots;

    Distance: Distance_In_Nautical_Miles;

    Some_Number: Float;

    Some_Number:= Distance + Velocity; -- Será capturado por el compilador como un error de tipos.

Los desarrolladores en dominios menos demandantes también se deberían beneficiar del aplicando más tipeado de dominio específico, donde pudieran de otro modo continuar usando tipos de datos primitivos ofrecidos por el lenguaje y sus librerías, tales como cadenas y flotantes. En Java, C++, Python y otros lenguajes modernos, los tipos de datos abstractos son conocidos como clases. Usar clases como `Velocity_In_Knots` y `Distance_In_Nautical_Miles` agrega mucho valor con respecto a la calidad del código:

* El código se vuelve más legible conforme expresa conceptos de un dominio, no sólo Flotantes o Cadenas.
* El código se vuelve más testeable conforme el código encapsula su comportamiento, así es fácilmente probado.
* El código facilita el reuso a través de aplicaciones y sistemas.


El enfoque es igualmente válido para usuarios de ambos lenguajes de tipo estáticos y dinámicos. La única diferencia es que los desarrolladores usando lenguajes de tipado estático obtienen más ayuda desde el compilados, mientras aquellos que adoptan lenguajes de tipado dinámico es más común que confíen en sus pruebas unitarias. El estilo de revisión podría ser diferente, pero la motivación y estilo de expresión no.

La moraleja es iniciar explorando los tipos de dominio específico para con el fin de desarrollar la calidad del software.

