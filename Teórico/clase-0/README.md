# Clase de repaso


### Definir el "Territorio" (El problema).
Antes de medir la eficiencia de un algoritmo, deberiamos definir claramente
qué problema estamos resolviendo. En complejidad, esto es fundamental:

**Problema**: Es una descripción abstracta de lo que quiero resolver. 
> Define un conjunto de entradas válidas y la salida esperada para cada una de las entradas.
**Instancia**: Es un caso concreto y específico del problema.
> Es un conjunto de entradas wue cumple con las restricciones del problema.

> Ejemplo 
> + **Problema:** Dado un número entero n no negativo, determinar si es primo.
>+ **Instancia:** `N = 17` es una intancia de ese problema. `n = 25` es otra instancia diferente


### El campo de juego: El Modelo de Máquina.

Para hablar de tiempos de ejecución de forma rigurosa, necesitamos un modelo de computación estándar. Nosotros utilizaremos el modelo
de Máquina RAM (Random Access Memory). Este modelo nos da un conjunto de reglas claras sobre lo que cuesta cada operación.

Características de nuestra Máquina RAM:
1. Memoria: Es una gran sucesión de celdas (como un vector). Cada celda tiene una dirección (como un índice) y puede almacenar un valor.  

2. Tamaño de la celda (b): Asumimos que cada celda tiene un tamaño fijo de `b` bits. Este tamaño es suficiente para almacenar cualquier dato elemental que use nuestro algoritmo (un entero, un booleano, un caracter, un puntero, etc.). Una simple simplificación.

3. Programa: El algoritmo se ejecuta como un programa imperativo con asignaciones, condicionales, ciclos, etc.

4. Acceso a memoria: El acceso a cualquier celda de memoria (leer o escribir) toma un tiempo constante, O(1). Sin importar si quiero acceder a la celda 1 0 1000, el tiempo es el mismo.

### Costo de las operaciones
Cada instrucción tiene un costo asociado. El costo de las operaciones aritméticas depende crucialmente de nuestra suposición sobre el tamaño de la celda b.


| Operación | Costo (Generalmente) | Costo (en nuestro caso) |
| :--- | :---: | ---: |
| Acceso a memoria (leer/escribir) | O(1) | O(1) |
| Estructura de control | O(1) | O(1) |
| Operaciones lógicas | O(1) | O(1) |
| Asignaciones simples | O(1) | O(1) |
| (Suma / Resta) de enteros | O(b) | O(1) (porque b es fijo) |
| (Multiplicación / División) de enteros | O(b) | O(1) (porque b es fijo)|

Dado que asumimos un tamaño de celda fijo (b constante), todas las operaciones básicas entre números (sumar, resta, multiplicar, dividir, comparar) se considera un tiempo constante O(1). Esto nos permite concentrarnos en la eficiencia del algoritmo en sí, y no en los detalles de la implementación de la aritmética.

### Tiempo de ejecución y complejidad
Con las reglas claras, podemos definir cómo medimos:
