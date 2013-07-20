Escribe pequeñas funciones usando ejemplos
===

Nos gustaría escribir código que fuese correcto, y tener evidencia en mano de que es correcto. Puede ayudar con ambos temas el pensar en el "tamaño" de una función. No en el sentido de la cantidad de código que implementa una función -- a pesar de que es interesante -- sino más bien del tamaño como una función matemática que nuestro código manifiesta.

Por ejemplo, en el juego de Go hay una condición llamada atari, en la cual la piedra del jugador puede ser capturada por su oponente: Una puedra con dos o más espacios libres adyacentes a él (llamados liberties) no está en atari. Puede ser difícil de contar cuántas liberties tiene una piedra, pero determinar el atari es fácil si se sabe. Podría empezar escribiendo una función como esta:

```java
boolean atari(int libertyCount)
    libertyCount < 2
```
Esto es más grande de lo que parece. Una función matemática puede ser entendida como un conjunto, algún subconjunto del producto Carteriano de el conjunto que son su dominio (en este caso, un entero) y rango (en este caso, un booleano). Si esos conjuntos de valores fueran del mismo tamaño como en Java, entonces sería `2L*(Integer.MAX_VALUE+(-1L*Integer.MIN_VALUE)+1L)` o `8,589,934,592` miembros en el conjunto int × boolean. La mitad de estas son miembros de un conjunto que es nuestra función, así que para proveer una evidencia completa de que nuestra función es correcta necesitariamos revisar al rededor de $4.3 × 10^9$ ejemplos.

Esta es la esencia de la afirmación de que la pruebas no pueden probar la ausencia de errores. Las pruebas pueden demostrar la presencia de características, sin embargo. Pero aún tenemos este tema del tamaño.

El dominio del problema nos ayuda. La natura de Go significa que el número de liberties de una piedra no es cualquier entero, pero exactamente uno de {1,2,3,4}. Así pues, podríamos escribir alternativamente:

```java
LibertyCount = {1,2,3,4} 
boolean atari(LibertyCount libertyCount)
    libertyCount == 1
```

Esto es mucho más manejable: La función calculada es ahora un conjunto con cuando mucho ocho miembros. De hecho, cuatro ejemplos seleccionados constituiría la evidencia de la certeza completa de que la función es correcta. Esta es la razón por la cual es una buena idea usar tipos estrechamente relacionados al dominio del problema para escribir programas, en vez de tipos nativos. Usar tipos inspirados en dominios a menudo puede hacer que nuestra funciones sean mucho más pequeñas. Una forma de encontrar que tipo sería es encontrar los ejemplos para comprobar en terminos del dominio del problema, antes de escribir la función.

Por Keith Braithwaite 

Traducción: Espartaco Palma

[Leer contribución original](http://programmer.97things.oreilly.com/wiki/index.php/Write_Small_Functions_Using_Examples)

[Licencia Creative Commons Attribution 3](http://creativecommons.org/licenses/by/3.0/us/deed.es)