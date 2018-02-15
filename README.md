# Python Basic

**Sintaxis**

 - No se utiliza el punto y coma.
 - Se debe respetar la identación al realizar funciones.
 
 **Ejemplo de Hola Mundo**
 

    print "Hola Mundo"

**Definición de variables**

    name = juan

**Listas y Tuplas**

> Listas: Conjunto ordenado de valores dinámicos

> Tuplas: Conjunto ordenado de valores estáticos

    fruits = ['apple','orange','grape']
    print(fruits[0]) // Imprime el primer elemento de la lista
    print(fruits[-1]) // Imprime el primer elemento empezando desde el final

 - Slicing

       numbers = [0,1,2,3,4,5,6,7]
       print(numbers[2:5]) // Imprime los valores del array de la posición 2 al 5
       print(numbers[5:] // Imprime los valores de la posición 5 en adelante
       print(numbers[::2] // Imprime los valores en las posiciones pares
       print(numbers[1::2] // Imprime los valores en posición impar
      

> *En las listas se pueden usar funciones como **append()**, **insert()** o **remove()**

> *Para obtener el tamaño de una lista o tupla se usa la función **len()**

> *Se puede convertir listas en tuplas y viceversa usando las funciones **tuple()** y **list()**

**Diccionarios**

> Es una colección no ordenada de objetos. La identificación de valores se hace por medio de key - value

    fighter = {"name":"chuck","last_name":"norris"}
    print fighter["name"] // Se obtiene valor de la clave name - Mala práctica
    print fighter.get("name") // Recomendable
