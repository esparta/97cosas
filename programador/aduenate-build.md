---
layout: programador
title: Adueñate (y Refactoriza) la compilación
overview: true
author: Steve Berczuk
translator: Espartaco Palma
original: http://programmer.97things.oreilly.com/wiki/index.php/Own_%28and_Refactor%29_the_Build
---

No es poco común para los equipos que aunque son altamente disciplinados sobre las prácticas de codificación descuidan los scripts de compilación, quizás por la creencias que son meramente un detalle de poca importancia o por el miedo de que son complejos y necesitan ser atendidos por el culto de la ingeniería de la liberación. Los scripts que no son posibles de mantener, con duplicaciones y errores causan problemas de la misma magnitud que aquellos con código pobremente factorizado.

Una de las razones por las que los desarrolladores hábiles y disciplinados tratan la compilación como algo secundario a su trabajo es que los scripts de compilación son frecuentemente escritos en un lenguaje diferente que el código fuente. Otra es que la compilación no es realmente "código". Estas justificaciones van en contra de la realidad de que la mayoría de los desarrolladores de software disfrutan aprendiendo nuevos lenguajes y que la compilación es lo que crea artefactos ejecutabes para desarrolladores y usuarios finales para probar y ejecutar. El código es inútil si no ha sido compilado, y la compilación es lo que define el componente de arquitectura de la aplicación. La compilación es una parte escencial del proceso de desarrollo, y las decisiones sobre el proceso compilado pueden hacer más simples tanto el código como la codificación.

Los scripts para la compilación que son escritos usando los modismos erróneos son difíciles de mantener, y más importante, de mejorar. Vale la pena tomarse algún tiempo para entender la forma correcta de realizar un cambio. Los errores pueden aparecen cuando una aplicación se compila con la versión incorrecta de una dependencia o cuando la configuración del tiempo de compilador está mal.

Tradicionalmente las pruebas han sido algo que siempre fue dejado al equipo de "Quality Assurance". Ahora nos damos cuenta que hacer pruebas mientras codificamos es algo necesario para permitirnos el liberar valor predeciblemente. Del mismo modo, el proceso de compilación tiene que ser propiedad del equipo de desarrollo.

Entender la compilación puede simplificar el ciclo de vida completo y reducir costos. Una compilación simple de ejecutar permite al nuevo desarrollador el empezar rápida y fácilmente. La automatización de la configuración de compilación puede permitirte el obtener resultados consistentes cuando muchas personas están trabajando en un proyecto, evitando el "a mí me funciona". Muchas herramientas para el compilación te permiten ejecutar reportes de calidad de código, dejándote sentir problemas potenciales tempranamente. Al pasar tiempo entendiendo cómo hacer tuya la compilación, puedes ayudarte a tí mismo y a todos los demás en tu equipo. Puedes enfocarte en codificar características, en beneficio a las partes interesadas y hacer tu trabajo más agradable.

Aprende lo suficiente de tu proceso de compilación para saber cuándo y cómo realizar los cambios. Los scripts de compilación son código. También son muy importantes para dejarlos a alguien más, no es por otra razón más que la aplicación no está completa hasta que se compila. El trabajo de programación no está completo hasta que hayamos liberado software funcionando.

