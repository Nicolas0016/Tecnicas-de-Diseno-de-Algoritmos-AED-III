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

Tiempo de ejecución de un algoritmo A para una instancia I (T_A(I)): es la suma de los costos (según nuestras reglas) de todas las instrucciones que ejecuta el algoritmo cuando se le da una instancia I como entrada.

Tamaño de la instancia (|I|): Para poder graficar el comportamiento del algoritmo, necesitamos una medida que dependa de "cuan grande" es la entrada. Definimos |I| como la cantidad de bits necesarios para almacenar la entrada I.
> Con nustra regla de celda de tamaño fijo, si la entrada  ocupa n celdas de memoria entonces |I| = b * n = O(n).
> Es decir, el tamaño de la instancia es directamente proporcional a la cantidad de elementos de entrada. Por eso usamos n (la cantidad de datos) como medida de instancia.

Complejidad temporal de un algoritmo A (f_A(n)):
Como el tiempo puede variar para diferentes instancias del mismo tamaño, nos interesa el peor caso. Definimos la complejidad como el máximo tiempo que el algoritmo puede tardar en cualquier instancia de tamaño n.

![f_A(n) = max_{I: |I| = n} T_A(I)](../../img/image.png)

### Notación Asintótica (O, Ω, Θ):
Para no preocuparnos por constantes y detalles menores, usamos la notación asintótica para describir el orden de crecimiento de f_A(n):

***Cota superior (O grande)***: f(n) = O(g(n)) significa que f crece, a lo sumo, tan rápido como g (multiplicada por una constante). Es decir, a partir de un n suficientemente grande, f(n) está siempre por debajo de c * g(n).

> Interpretación: El algoritmo no es peor que g(n).

***Cota inferior (Ω grande)***: f(n) = Ω(g(n)) significa que f crece, al menos, tan rápido como g. A partir de un n grande, f(n) está siempre por encima de c * g(n).

> Interpretación: El algoritmo no es mejor que g(n).

***Cota ajustada (Θ grande)***: f(n) = Θ(g(n)) significa que f y g crecen al mismo ritmo (salvo por constantes). Ocurre cuando f(n) = O(g(n)) y f(n) = Ω(g(n)).


| Complejidad | Nombre |
| :--- | :---: |
| O(1) | Constante |
|O(log n)|	Logarítmico|
| O(n) | Lineal |
|O(log n)|	Logarítmico|
| O(n²) | Cuadratico |
| O(n³) | Cúbico |
| O(n^k) con k constante | Polinomial |
| O(d^n) con d > 1 | Exponencial |

> Cualquier función exponencial crece más rápido que cualquier función polinomial. dⁿ no es O(nᵏ).


> La función logarítmica crece más lentamente que la lineal. log n es O(n), pero n no es O(log n)