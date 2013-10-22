Dos fallas pueden hacer un acierto (y es difícil de arreglar)
===

El código nunca miente, pero puede contradecirse. Algunas contradiciones llevan a esos momentos de "¿Cómo es posible que esto funcione?".

En una [entrevista](http://www.netjeff.com/humor/item.cgi?file=ApolloComputer), el diseñador principal del software del módulo lunar Apolo 11, Allan Klumpp, reveló que el software que controlaba los motores contenía un error que debía hacer el módulo aterrizaje inestable. Sin embargo, otro error fue compensado por el primero y el software fue usado por los aterrizajes lunares del Apolo 11 y 12 antes de que el error fuera encontrado y arreglado.

Considera una función que retorna un estatus de finalización. Imagina que retorna `false` cuando debería regresar un `true`. Ahora imagina que la llamada de función olvida comprobar el valor de retorno. Todo funciona bien hasta que un día alguien nota la falta de verificación y la inserta.

O considera una aplicación que almacena su estado en un documento XML. Imagina que uno de los nodos está escrito incorrectamente como "TimeToLive" en vez de "TimeToDie", como la documentación dice que debería. Todo parece estar bien mientras el código de escritura y el código de lectura contienen ambos el mismo error. Pero arregla uno, o agrega una nueva aplicación de lectura del mismo documento, y la simetría se rompe, al igual que el código.

Cuando dos defectos en el código crean un defecto visible, el enfoque metodológico para arreglar la falla puede, por sí mismo, romperlo. El desarrolador recibe un reporte de error, encuentra el defecto, lo arregla y lo vuelve a probar. Sin embargo, el fallo reportado aún ocorre, debido a que un segundo defecto está en funcionamiento. Así que el primer arreglo es quitado, el código es inspeccionado hasta que el segundo defecto es encontrado, y un arreglo se aplica. Pero el primer defecto ha regresado, el fallo reportado aún se ve, así que se deshace el segundo arreglo. El proceso se repite pero ahora el desarrollador ha desestimado dos posibles soluciones y está buscando hacer un tercero, que nunca va a funcionar.

La interacción entre dos defectos de código que aparecen como sólo un defecto visible no sólo hace difícil de arreglar el problema, además lleva a los desarrolladores a callejones sin salida, sólo para descubrir que intentaron la respuesta correcta desde el inicio.

Esto no pasa sólo en el código: El problema también existe en los documentos de requerimientos escritos. Y puede extenderse, viralmente, de un lugar a otro. Un error en el código compensa un error en la descripción escrita.

Puede extenderse a la gente también: Los usuarios aprenden que cuando la aplicación dice 'Izquierda' se refiere a la 'Derecha', así que ajustan su comportamiento. Ellos incluso lo pasan al nuevo usuarios: "Recuerda que la aplicación dice que hagas click al botón izquierdo cuando realmente se refiere al botón derecho". Arregla ese error y de repente los usuarios necesitan reentrenamiento.

Fallos sencillos pueden ser fáciles de ver y fáciles de arreglar. Son los problemas con múltiples causas, que necesitan múltiples cambios, los que son difíciles de resolver. En parte es porque los problemas fáciles son tan fácilmente arreglados que la gente tiende a arreglarlos con relativa rapidez y se quedan con los más difíciles para una fecha posterior.

No hay un consejo simple que se pueda dar en cómo localizar fallos surgidos de defectos simpatéticos. Es necesario darse cuenta de la posiblidad, una cabeza clara, y una voluntad de considerar todas las posibilidades.

Por Allan Kelly

Traducción: Espartaco Palma

[Leer contribución original](http://programmer.97things.oreilly.com/wiki/index.php/Two_Wrongs_Can_Make_a_Right_%28and_Are_Difficult_to_Fix%29)

[Licencia Creative Commons Attribution 3](http://creativecommons.org/licenses/by/3.0/us/deed.es)