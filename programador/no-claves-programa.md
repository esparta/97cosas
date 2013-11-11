---
layout: programador
title: No claves tu programa en la posición vertical
author: Verity Stob 
translator: Espartaco Palma
original: http://programmer.97things.oreilly.com/wiki/index.php/Don%27t_Nail_Your_Program_into_the_Upright_Position
---

Una vez escribí un Test de C++ en parodia, en el cuál sugería satíricamente la siguiente estrateia de manejo de excepciones:

> Al realizar un montón de constructos try...catch a través de tu código base, podemos algunas veces prevenir que nuestra aplicación aborte. Creemos que el estado resultante es "clavar el cuerpo en posición vertical"

Dejando a un lado lo frivolidad, realmente estaba resumiendo una lección que recibí de Doña Amarga Experiencia. 

Era una clases base de nuestra aplicación, una biblioteca de C++ hecha en casa. Había sufrido los piquetes de los muchos dedos de los programadores en los últimos años: las manos de nadie estaban limpias. Contenían código para lidiar con todas las excepciones de escape de todo lo demás. Tomando el ejemplo de [Yossarian](http://en.wikipedia.org/wiki/Yossarian) de Catch-22, decidimos, o más bien sentimos (decidir implicaba más bien pensarlo que estar en la construcción de este mounstruo) de que una instancia de esta clase debería vivir para siempre o morir en el intento. 

Al final, interconectamos múltiples manejadores de excepciones. Mezclamos excepciones estructuradas de Windows con las nativas (¿recuerdas try...catch en C++? Yo tampoco). Cuando las cosas se caían inesperadamente, tratabamos de llamarla de nuevo, presionando los parámetros cada vez más fuerte. Mirando atrás, me gustaría pensar que al escribir un manejador interno de try...catch dentro de una cláusula catch de otra, una especie de conciencia se apoderó de mí para haber tomado accidentalmente la ruda ruta de las buenas prácticas en la aromática pero insalubre vía de la locura. De cualquier modo, probablemente es sabiduría retrospectiva

No necesito decir, que cualquier cosa que estuviera mal en las aplicaciones basadas en esta clase, se desvanecía como víctimas de la Mafia en el muelle, dejado atrás ningún rastro útil de las burbujas que indicara que demonios había sucedido, a pesar de las rutinas de volcado que supuestamente grabarían el desastre. Eventualmente -- un largo eventualmente -- hicimos un balance de lo que habíamos hecho, y experimentamos verguenza. Reemplazamos todo el lío con un mecanismo de informe mínimo y robusto. Pero esto fue como ver muchos accidentes en la carretera.

No te molestaré más con esto -- seguramente nadie más podría haber sido tan estúpido como nosotros lo fuimos -- excepto una discusión en línea que tuve recientemente con un individuo cuyo título académico declaró que debía saberlo mejor. Estabamos discutiendo código Java en una transacción remota. Si el código fallaba, el argumentaba, debería capturar y bloquear la excepción in situ. ("¿Y entonces que haría con ello?", pregunté. "¿Cocinarlo para la cena?").

Citó la regla del diseñador de UI: NUNCA DEJES QUE EL USUARIO VEA UN REPORTE DE EXCEPCIÓN, como si esto resolviera el asunto, poniendolo en mayúsculas y todo lo demás. Me preguntaba si era el responsable del código de una de esas pantallas azules de los cajeros automáticos cuyas fotos decoran blogs más endebles, y había sido traumatizado permanentemente.

De cualquier modo, si llegas a verlo, asienta con la cabeza y sonrie, no le hagas caso, mientras te deslizas hacia la puerta.

