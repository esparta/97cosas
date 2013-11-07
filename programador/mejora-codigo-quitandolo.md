---
layout: programador
title: Mejora el código quitándolo
overview: true
author: Pete Goodliffe
translator: Espartaco Palma
original: http://programmer.97things.oreilly.com/wiki/index.php/Improve_Code_by_Removing_It
---

Menos es más. Es una máxima un poco trillada, pero algunas veces es realmente cierto.

Una de las mejoras que he hecho en nuestro código base en las últimas semanas es eliminar trozos de él.

Hemos escrito el software siguiendo los principios de XP, incluyendo YAGNI (esto es, You Aren't Gonna Need It - No vas a necesitarlo). La naturaleza humana es así, inevitablemente nos quedamos cortos en unos pocos lugares.

Observé que el producto estaba tomando demasiado tiempo para ejecutar ciertas tareas - tareas sencillas que deberían ser casi instantáneas. Esto era porque estaban sobreimplementadas; adornadas con campanas y silbatos adicionales que no eran requeridos, pero que en ese momento parecían una buena idea.

Así que he simplificado el código, mejorando el rendimiento del producto, y reduciendo el nivel de entropía global del código al quitar las características infractoras del código base. Afortunadamente, mis Pruebas Unitarias me dijeron que no había roto nada durante más durante la operación.

Una experiencia sencilla y completamente satisfactoria.

Así que ¿porqué terminó ahí ese código innecesario? ¿Porqué un programador sientió la necesidad de escribir código adicional y como pasó la última revisión o el proceso entre pares? Es casi seguro que sucedió algo como esto:

* Era un poco de diversión extra, y el programador quería escribirlo. (Sugerencia: Escribr código porque le agrega valor, no porque te divierte)
* Alguien pensó que podría ser necesario en el futuro, así que sintió que era mejor escribirlo ahora. (Sugerencia: Esto no es YAGNI. Si no lo necesitas en este momento, no lo escribas ahora mismo)
* No parecía ser un gran "extra", así que era más fácil implementarlo en vez de regresar con el cliente para ver si era realmente requerido. (Sugerencia: Siempre toma más tiempo escribir y mantener código adicional. Y el cliente siempre está disponible. Una partecita extra de código se vuelve una bola de nieve en descenso al paso del tiempo, convirtiendose en una gran parte de trabajo que necesita ser mantenido)
* El programador inventó requisitos adicionales que ni fueron documentados, ni discutidos para justificar la función adicional. El requerimiento era en realidad falso. (Sugerencia: Los programadores no establecen los requerimientos del sistema; el cliente sí).

¿En qué trabajas ahora mismo? ¿Es todo necesario?

