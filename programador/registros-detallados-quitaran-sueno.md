---
layout: programador
title: Los registros detallados perturbarán tu sueño
overview: true
author: Johannes Brodwall
translator: Espartaco Palma
original: http://programmer.97things.oreilly.com/wiki/index.php/Verbose_Logging_Will_Disturb_Your_Sleep
---

Cuando me encuentro un sistema que ya ha estado en desarollo o producción por un tiempo, la primera señal de un verdadero problema es siempre un registro sucio. Sabes a lo que me refiero. Cuando al hacer click en un link un flujo normal de una página web resulta en un diluvio de mensajes en el único registro que el sistema provee. Demasiados registros pueden ser inútiles como ninguno.

Si tus sistemas son como los míos, cuando se termina tu trabajo empieza el trabajo de alguien más. Después de que el sistema ha sido desarrollado, es de esperar que vivirá una larga y próspera vida de servicio a los clientes. Si tienes suerte. ¿Cómo sabrás si algo va mal cuando el sistema está en producción y cómo lidiar con él?

Quizás alguien más lo monitoreará por tí, o quizás lo monitorearás tú mismo. De cualquier forma, los registros probablemente serán parte del monitoreo. Si algo sucede y tu tienes que estar despierto para lidiar con él, entonces quieres estar seguro que hay una buena razón en ello. Si el sistema está muriendo, quiero saberlo. Pero si es sólo hipo, preferiría distrutar de mi bello sueño.

Para muchos sistemas, el primer indicador de que algo está mal es un mensaje de registro escrito en alguna bitácora. Generalmente, este será un registro de error. Así que haste un favor: Asegúrate desde el día uno que si registras algo en la bitácora de errores, estás dispuesto a tener a alguien llamando y despertándote a la mitad de la noche por ello. Si puedes simular carga en tu sistema durante las pruebas, mirar en una bitácora de errores libre de ruido es también una buena primera indicación que tu sistema es razonablemente robusto. O una alerta temprana si no lo es.

Los sistemas distribuidos agregan otro nivel de complejidad. Tienes que decidir cómo hacer frente a una de dependencia externa. Si tu sistema está muy distribuido, esto será una ocurrencia común. Asegurate que tu política de registro lo tome en cuenta.

En general, el mejor señal de que todo está bien es que los mensajes de menor prioridad están tildando felizmente. Deseo algo así como un mensaje de registro de nivel INFO por cada evento importante de la aplicación.

Una bitácora desordenada es un indicador de que el sistema será difícil de controlar una vez que llegue a producción. Si no esperas que nada se muestre en la bitácora de error, será mucho más fácil saber que hacer cuando algo aparezca.

