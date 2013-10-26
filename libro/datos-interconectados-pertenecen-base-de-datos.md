---
layout: page
title: Los grandes datos interconectados pertenecen a una base de datos
overview: true
permalink: /libro/datos-interconectados-pertenecen-base-de-datos/
author: Diomidis Spinellis
---

Si tu aplicación está manejando un conjunto de elementos de datos grandes, persistentes e intenconectados, no dudes en almacenarlos en una base de datos relacional. En el pasado los Sistemas de Administración de Bases de Datos Relacionales (RDBMS, por sus siglas en inglés) solían ser caras, escasas, complejas, y unas bestias indomables. Ya no es el caso. Hoy en día los RDBMS son fáciles de encontrar -- lo más probable es que el sistema que estás usando ya tenga uno o dos instalados. Algunos RDBMS muy capaces como MySQL y PostgreSQL están disponibles como software de código abierto, por lo que el costo de compra ya no es un tema. Aún mejor, los llamados sistemas de bases de datos embebidos se pueden vincular como librerías directamente en tu aplicación, requiriendo casi ninguna configuración o administración -- dos notables proyectos de código abierto son SQLite y HSQLDB. Estos sistemas son extremadamente eficientes.

Si los datos de tu aplicación son más grandes que la RAM del sistema, una tabla indexada del RBDMS tendrá un rendimiento de órdenes de magnitud más rápida que librería de tipos de mapas de colección, los cuales gastará páginas de memoria virtual. Los productos de bases de datos modernos pueden crecer fácilmente con tus necesidades. Con el cuidado adecuado, puedes ampliar una base de datos embebida a un sistema de base de datos más grande cuando sea requerido. Después puedes cambiar de un producto código abierto gratuito a un mejor soportado o más poderoso sistema propietario.

Una vez que sepas los trucos de SQL, la creación de aplicaciones centradas en bases de datos es una alegría. Después de que hayas almacenado tus datos correctamente normalizados en la base de datos es fácil extraer los hechos eficientemente con una legible consulta SQL; no hay necesidad de escribir ningún código complejo. Similarmente, un sólo comando SQL puede realizar cambios de datos complejos. Para modificiones únicas, digamos, un cambio en la forma en que organizas los datos, nisiquiera necesitas escribir código: Sólo lanza la interface directa de SQL. Esta misma interface también te permite experimentar con consultas, dejando un lado el ciclo de compilación-edición de un regular lenguaje de programación.

Otra de las ventajas de basar tu código en un RDBMS implica el manejar las relaciones entre los elementos de tus datos. Puedes describir las limitaciones de consistencia en los datos en una manera declarativa, evitando el riesgo de punteros se cuelguen si olvidas actualizar los datos en un caso extremo. Por ejemplo, puedes especificar que si un usuario es eliminado, entonces los mensajes enviados por ese usuario deberían ser eliminados también.

También puedes crear enlaces eficientes entre tus entidades almacenadas en la base de datos en el momento que lo desees, simplemente creando un índice. No hay necesidad de realizar caras y extensas refactorizaciones de campos de clases. En adición, codificar en torno de una base de datos permite que varias aplicaciones accedan a tus datos en manera segura. Esto hace fácil el actualizar tu aplicación para el uso concurrente y también permite codificar cada parte de tu aplicación usando el lenguaje y plataforma más adecuada. Por ejemplo, puedes escribir el back-end XML de una aplicación web en Java, algunos scripts de autoría en Ruby y una interfaz de visualización en Processing.

Finalmente, recuerda que el RDBMS sudará duro para optimizar los comandos SQL, permitiendote el concentrarte en la funcionalidad de tu aplicación en vez de la refinación de algoritmos. Los sistemas avanzados de bases de datos incluso tomarán ventaja de los procesadores multicore a tu espalda. Y, conforme la tecnología mejora, también el rendimiento de tu aplicación.


Traducción: Espartaco Palma

[Leer contribución original](http://programmer.97things.oreilly.com/wiki/index.php/Large_Interconnected_Data_Belongs_to_a_Database)
