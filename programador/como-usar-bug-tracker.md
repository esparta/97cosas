---
layout: programador
title: ¿Cómo usar un Gestor de Errores?
overview: true
author: Matt Doar
translator: Espartaco Palma
original: http://programmer.97things.oreilly.com/wiki/index.php/How_to_Use_a_Bug_Tracker
---

Como sea que lo llames, bug, defecto, o incluso "efecto del lado de diseño", no hay manera de alejarse de ellos. Conocer cómo enviar un buen reporte de error y lo que se debe buscar son habilidades para mantener a un proyecto llevándose bien:

Un buen reporte de error necesita tres cosas:

* Cómo reproducir el error, lo más preciso posible, y la frecuencia con que ésto hará que aparezca el error.
* ¿Qué debería haber ocurrido? al menos en tu opinión
* ¿Qué realmente ocurrió? o al menos toda la información que has registrado.

La cantidad y calidad de la información reportada de un error dice mucho acerca del quien reporta como sobre el error mismo. Los errores con enojo o tensión ("¡Esta función apesta!") nos dice que los desarrolladores estaban teniendo un mal momento, pero no mucho más. Un error con gran cantidad de contexto para que sea más fácil reproducirlo gana el respeto de todo el mundo, incluso si ésto detiene una liberación.

Los errores son como un conversación, con toda la historia ahí en frente de todos. No culpes a otros o niegues la existencia del error. En vez de eso pide más información o considera qué pudiste haber olvidado.

Cambiar el estatus de un error, por ejemplo, de Abierto a Cerrado, es una declaración pública de lo que se piensa del error. Tomarse el tiempo de explicar porqué crees que el error debería estar cerrado ahorrará horas de tedio en justificarlo a directores y clientes frustados. Cambiar la prioridad de un error es similar a las declaraciones públicas, y sólo porque es trivial no significa que alguien está dejando de usar el producto.

No sobrecargues los campos del error para tu propio propósito. Agregar "VITAL:" al campo de título de error puede hacer que sea fácil para que puedas ordenar los resultados en algún informe, pero hará que eventualmente sea copiado por otros e inevitablemente será mal escrito, o necesitará ser removido para su uso en algún otro informe. En vez de eso usa un nuevo valor o un nuevo campo, y documenta cómo el campo se supone debe ser usado, así otras personas no tienen que repetirlo.

Asegúrate que todos sepan cómo encontrar el error en el que se supone está trabajando el equipo. Esto se puede hacer mediante una consulta pública con un nombre obvio. Asegúrate que todos están usando la misma consulta, y no actualices dicha consulta sin primero informar al equipo que estás cambiando algo en lo que todos están trabajando.

Finalmente, recuerda que un error no es una unidad estándar de trabajo más que una línea de código es una medida precisa del esfuerzo.


