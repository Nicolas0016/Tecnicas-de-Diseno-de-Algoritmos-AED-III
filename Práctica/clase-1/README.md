## Ejercicio 1:

Dado el algoritmo de mergesort, implementado en el siguiente
código Python:

1. Identicar qué líneas son el divide, cuáles son el conquer y
cuáles el combine.
2. En cuántos subproblemas se divide?
3. De qué tamaño son estos subproblemas?
4. Cuál es el costo de combinar los resultados de los
subproblemas?
5. Escribir la función T (n) de manera recursiva.
6. Determinar la complejidad del algoritmo utilizando el Teorema
Maestro.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    medio = len(arr) // 2
    mitad_izq = merge_sort(arr[:medio])
    mitad_der = merge_sort(arr[medio:])

    return merge(mitad_izq, mitad_der)
```

```python
def merge(izq, der):
    mergeados = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            mergeados.append(izq[i])
        i += 1
    else:
        mergeados.append(der[j])
        j += 1

    mergeados.extend(izq[i:])
    mergeados.extend(der[j:])
    return mergeados
```
1. Identificar qué líneas son el *divide*, cuáles son el *conquer* y cuáles el *combine*.

> Respuesta
+ Divide:
   + `medio = len(arr) // 2` (calcula el punto medio)
   + `arr[:medio]` y `arr[medio:]` (creación efectiva de los subproblemas)
 + Conquer: 
   + `mitad_izq = merge_sort(arr[:medio])`
   + `mitad_der = merge_sort(arr[medio:])`
 + Combine:
   + `return merge(mitad_izq, mitad_der)` 
   + Toda la función merge

> OBS: Una forma práctica para detectar las fases es:
> + Divide: Buscar donde se parte el problema original.
> + Conquer: Buscar las llamadas recursivas que resuelven el subproblema
> + Combine: Busca dónde se integran las soluciones parciales 
>
> Ejemplo:
> + `medio = len(arr)//2` y las rebanadas `arr[:medio]`, `arr[medio:]` → Divide
> + Las dos llamadas a `merge_sort` → Conquer
> + La función `merge` completa (ordenando y combinando) → Combine

2. ¿En cuántos subproblemas se divide?

> Respuesta
Se divide en 2 subproblemas
+ La mitad izquierda: arr[:medio]
+ La mitad derecha: arr[medio:]

> OBS: Para detectar en cuántos subproblemas se divide, simplemente **cuento las llamadas recursivas** que aparecen en el código. Cada llamada recursiva representa un subproblema diferente. 

3. ¿De que tamaño son estos subproblemas?
> Respuesta
Cada subproblema tiene un tamaño n/2 
+ Si el arreglo original tiene n elementos
+ La mitad izquierda tiene |n/2| elementos
+ La mitad derecha tiene |n/2| elementos 
+ Para el analisis asintótico: ambos son $\Theta(n/2)$

> OBS: Para determinar el tamaño de los subproblemas, miro el **tamaño de la entrada** que se pasa a cada llamada recursiva respecto al tamaño original `n`.

4. ¿Cuál es el costo de combinar los resultados de los subproblemas?

> Respuesta
El costo de combinar es $O(n)$
+ La función `merge` recorre cada elemento una sola vez.
+ En el peor caso, compara todos los elementos de ambas mitades.
+ Total de operaciones: $$n \ \text{comparaciones} + n \ \text{inserciones} = O(n)$$

> OBS: Para determinar el costo del combine, analizo la función que integra las soluciones parciales (merge) y veo cuánto trabajo se hace con los datos ya resueltos.

> En merge se recorren todos los elementos de ambas mitades exactamente una vez (comparando y fusionando), por lo que el costo es lineal respecto al total de elementos: $O(n)$. No importa que sean dos mitades, el trabajo total es proporcional a $n$.


5. Escribir la función T(n) de manera recursiva.
> Recuerdo (lo tango que revisar)

$$
T(n) = 
\begin{cases} 
    a \cdot T(n/c) + f(n) & \text{si}\ n > 1 \\ \\
    1 & \text{si} \ n = 1
\end{cases}
$$

> Respuesta

$$
T(n) = 
\begin{cases} 
    1 \ & \text{si} \ n ≤ 1 \\
    2 \cdot T(n/2) + \Theta(n) & \text{si}\ n > 1 
\end{cases}
$$

+ $\Theta(1)$: Caso base (arreglo de un elemento o vacío)
+ $2 \cdot T(n/2)$: Dos llamadas recursivas de tamaño n/2
+ $\Theta(n)$: Costo de combinar los resultados (merge).

> OBS: Para escribir la función T(n) de manera recursiva, identifico:
>+ El caso base (cuando n es pequeño, típicamente n ≤ 1)
>+ El número de subproblemas (a)
>+ El tamaño de cada subproblema (c)
>+ El costo de combinar (f(n))  

6. Determinar la complejidad del algoritmo utilizando el Teorema Maestro.
> Recuerdo el Teorema Maestro:
$$
T(n) = 
\begin{cases} 
    a \cdot T(n/c) + f(n) \ \text{si}\ n > 1 \\ \\
    1 \ \text{si} \ n = 1
\end{cases}
$$
Caso 1: $Si f(n) = O(n^{log_c {a - \epsilon}})$ para $\epsilon > 0$ entonces: $\ T(n) = \Theta(n^{\log_c a})$

Caso 2: $Si f(n) = \Theta(n^{\log_c a} \cdot \log^k n)$ para $k \geq 0$ entonces: $\ T(n) = \Theta(n^{\log_c a} \cdot \log^{k+1} n)$

Caso 3: $Si f(n) = \Omega(n^{\log_c a + \epsilon})$ para $\epsilon > 0$ y $a \cdot f(n/c) \leq k \cdot f(n)$ para alguna constante $k < 1$ entonces: $\ T(n) = \Theta(f(n))$

Donde:
+ $a$: número de subproblemas (en nuestro caso, $a = 2$)
+ $c$: factor de reducción del tamaño (en nuestro caso, $c = 2$)
+ $f(n)$: costo de combinar (en nuestro caso, $f(n) = \Theta(n)$)
+ $n$: tamaño del problema original
+ $\epsilon$: una constante positiva que representa una pequeña diferencia en el crecimiento de las funciones
+ $k$: una constante que representa una relación de crecimiento entre $f(n)$ y $n^{\log_c a}$

> Puedo usar esto: 
+ si $f(n)$ crece más lento que $n^{\log_c a}$, entonces la solución es dominada por el término recursivo (caso 1).

+ si $f(n)$ crece exactamente igual que $n^{\log_c a}$, entonces la solución es dominada por el término recursivo multiplicado por un factor logarítmico (caso 2).

+ si $f(n)$ crece más rápido que $n^{\log_c a}$, entonces la solución es dominada por el término de combinación (caso 3).

> Respuesta:

Aplicamos el Teorema Maestro con:

+ $a = 2$ (número de subproblemas)
+ $c = 2$ (factor de división)
+ $f(n) = \Theta(n)$ (costo de combinar)

Calculamos $\log_c a$ = $\log_2 2$ = 1

Como $f(n) = \Theta(n) = \Theta(n¹) = \Theta(n^{loc_c a})$ ⇒ estamos en el caso 2 del Teorema Maestro.

Por lo tanto: $\boxed{T(n) = \Theta(n \log n)}$

## Ejercicio 2:
Dado un algoritmo de búsqueda binaria, implementado en el siguiente código Python:
1. Identicar qué líneas son el divide, cuáles son el conquer y cuáles el combine.
2. En cuántos subproblemas se divide?
3. De qué tamaño son estos subproblemas?
4. Cuál es el costo de combinar los resultados de los subproblemas?
5. Escribir la función T (n) de manera recursiva.
6. Determinar la complejidad del algoritmo utilizando el Teorema Maestro.

```python
def busqueda_binaria(arr, objetivo, izquierda = 0, derecha=len(arr)-1):
    if izquierda > derecha:
        return False # Elemento no encontrado

    medio = (izquierda + derecha) // 2

    if arr[medio] == objetivo:
        return medio
    elif arr[medio] > objetivo:
        return busqueda_binaria(arr, objetivo, izquierda, medio - 1)
    else:
        return busqueda_binaria(arr, objetivo, medio + 1, derecha)
```
1. Identicar qué líneas son el divide, cuáles son el conquer y cuáles el combine.
> Respuesta
+ Divide:
   + `medio = (izquierda + derecha) // 2` (calcula el punto medio)
   + Comparación `arr[medio] > objetivo` para decidir la dirección de búsqueda.

+ Conquer:
   + `return busqueda_binaria(arr, objetivo, izquierda, medio - 1)`
   + `return busqueda_binaria(arr, objetivo, medio + 1, derecha)`
+ Combine:
   + No hay fase de combinación - simplemente se retorna el
resultado
    + La búsqueda binaria no necesita combinar resultados
> OBS: Para detectar las fases, busco:
>+ Divide: Donde se parte el problema original (calculo del medio y decisión de dirección)
>+ Conquer: Las llamadas recursivas que resuelven los subproblemas (búsqueda en la mitad izquierda o derecha)
>+ Combine: En este caso, no hay una fase de combinación explícita, ya que cada llamada recursiva retorna directamente el resultado sin necesidad de integrar resultados parciales.

2. En cuántos subproblemas se divide?
> Respuesta

Se divide en 1 subproblema
+ A diferencia del MergeSort que explora ambas mitades, la búsqueda binaria solo explora una mitad dependiendo de la comparación con el objetivo.

3. De qué tamaño son estos subproblemas?
>Respuesta
El subproblema tiene un tamaño de n/2
+ En cada llamada recursiva, el tamaño del problema se reduce a la mitad, ya sea buscando en la mitad izquierda o derecha del arreglo.
+ Si el arreglo original tiene n elementos:
    + Primera llamada: tamaño n
    + Segunda llamada: tamaño n/2
    + Tercera llamada: tamaño n/4
    + ... hasta llegar al caso base.
+ Máximo número de llamadas: $\log_2 n$
4. Cuál es el costo de combinar los resultados de los subproblemas?
> Respuesta

El costo de combinar es $O(1)$
+ No hay una fase de combinación explícita en la búsqueda binaria.
+ Solo se retorna el resultado:
    + El índice si se encuentra el objetivo.
    + False si no se encuentra.
+ Las operaciones adicionales son:
    + Cálculo del medio: $O(1)$
    + Comparar con el objeto: $O(1)$

5. Escribir la función T(n) de manera recursiva.

> Respuesta
$$
T(n) = 
\begin{cases} 
    1 \ & \text{si} \ n ≤ 1 \\
    T(n/2) + \Theta(1) &  \text{si}\ n
    > 1
\end{cases}
$$
+ $\Theta(1)$: Caso base (arreglo de un elemento o vacío)
+ $T(n/2)$: Una llamada recursiva de tamaño n/2
+ No hay costo de combinación adicional, ya que se retorna directamente el resultado.

6. Determinar la complejidad del algoritmo utilizando el Teorema Maestro.
> Respuesta: Aplicamos el Teorema Maestro con:
+ $a = 1$ (número de subproblemas)
+ $c = 2$ (factor de división)
+ $f(n) = \Theta(1)$ (costo de combinar)

Calculamos $\log_c a$ = $\log_2 1$ = 0

Como $f(n) = \Theta(1) = \Theta(n^0) = \Theta(n^{\log_c a})$ ⇒ estamos en el caso 2 del Teorema Maestro.

Por lo tanto: $\boxed{T(n) = \Theta(\log n)}$


## Cuando un algoritmo no es divide y vencerás.
BusquedaLienalModificicada(A, elem)
    If |A| == 0 return False
    If A[0] == elem return True
    return BusquedaLienalModificada(A[1:], elem) OR BusquedaLienalModificada(A[:-1], elem)

División de problema:
+ Subproblema 1: Tamaño 1 (un elemento)
+ Subproblema 2: Tamaño n-1 (el resto del arreglo)

### ¿Por qué no es divide y vencerás?
Caracteristicas del divide y vencerás:
1. **Dividir** el problema en subproblemas más pequeños.
2. Subproblemas de tamaño **considerablemente menor**.
3. División **balanceada**.
4. Reducción **significativa** del tamaño.

BusquedaLienalModificada:
+ Divide el problema en dos subproblemas: uno de tamaño 1 (el primer elemento) y otro de tamaño n-1 (el resto del arreglo).
+ Subproblema principal: **n - 1**
+ Reducción: **Solo un elemento**
+ División: **desbalanceada** (un subproblema es mucho más grande que el otro)
Recurrencia: 
$$ T(n) = T(1) + T(n-1) + O(1) $$
$$T(n) = T(n-1) + O(1)$$
Resultado: $T(n) = O(n)$ <- Es una recursión lineal.

### Segunda versión:
BusquedaLienalModificada(A, elem)
    If |A| == 0 return False
    If A[0] == elem return True
    return BusquedaLienalModificada(A[1:|A|//2], elem) 
    OR BusquedaLienalModificada(A[|A|//2:], elem)

División de problema:
+ Subproblema 1: Tamaño n/2 
+ Subproblema 2: Tamaño n/2 

Verificación D&C:
1. [x] División en subproblemas
2. [x] Tamaño n/2 (fracción del original)
3. [x] División balanceada
4. [x] Reducción significativa

BusquedaLienalModificadaV2:
+ División: n → n/2 + n/2
+ Reducción: 50% en cada nivel
+ División perfectamente balanceada
+ Cumple el paradigma D&C

Recurrencia:
$$ T(n) = 2 \cdot T(n/2) + O(1) $$
Aplicando el Teorema Maestro:
+ $a = 2$ (número de subproblemas)
+ $c = 2$ (factor de reducción)
+ $f(n) = O(1)$ (costo de combinar)

Calculamos $\log_c a$ = $\log_2 2$ = 1

Resultado como $f(n) = O(1) = O(n^0)$, entonces $f(n)$ crece más lento que $n^{\log_c a}$, por lo que estamos en el caso 1 del Teorema Maestro.
Por lo tanto: $\boxed{T(n) = \Theta(n)}$
Aunque es D&C verdadero, no mejora la complejidad sigue siendo $O(n)$

#### Conclusiones:
No todo algoritmo recursivo que divide el problema es divide and conquer.

NO es D&C si:
+ División desbalanceada extrema.
+ Subproblema de tamaño n - k.
+ Reducción no significativa.
+ Reducción lineal disfrazada.

SÍ es D&C si:
+ División balanceada.
+ Subproblemas de tamaño n/c.
+ Reducción por factor constante.
+ Verdadera descomposición.

Divide and Conquer requiere una división 
## Ejercicio 6 (MaximoMontaña):
Un arreglo de enteros se denomina "montaña" si esta compuesto por una secuencia estrictamente creciente seguida de una estrictamente decreciente. 

Dado un arreglo montaña de longitud n, dar un algoritmo que encuentre el máximo del arreglo en complejidad O(log n).

Ejemplo: Para el arreglo [-1, 3, 8, 22, 30, 22, 8, 4, 2, 1], el máximo está en el índice 4 (valor 30).

Objetivo: 
+ Diseñar un algoritmo divide and conquer.
+ Demostrar que tiene complejidad $O(\log_2 n)$.
+ Aplicar el Teorema Maestro. 

>OBS: En un arreglo montaña, el máximo es un punto donde cambia de creciente a decreciente.

Estrategia Divide and Conquer:
1. Dividir el arreglo al medio.
2. Comparar el elemento del medio con sus vecinos.
3. Decidir en que mitad buscar.

Casos posibles para arr[medio]:
+ Es mayor que ambos vecinos → es el máximo.
+ Es menor que el vecino izquierdo → el máximo está en la mitad izquierda.
+ Es menor que el vecino derecho → el máximo está en la mitad derecha.

```python
def maximo_montana(arr, izq=0, der=None):
    if der is None:
        der = len(arr) - 1
    if izq == der:
        return izq  # Solo un elemento, es el máximo   
    medio = (izq + der) // 2

    # Comparar con vecino
    if  medio > 0 and arr[medio] < arr[medio - 1]:
        # EL máximo está en la mitad izquierda
        return maximo_montana(arr, izq, medio - 1)  
    elif medio < len(arr) - 1 and arr[medio] < arr[medio + 1]:
        # EL máximo está en la mitad derecha
        return maximo_montana(arr, medio + 1, der)  
    else:
        # arr[medio] es el máximo
        return medio  
```
Identificar las partes del algoritmo divide and conquer:
+ Divide: `medio = (izq + der) // 2` (calcula el punto medio)

+ Conquer: Las llamadas recursivas a `maximo_montana    (arr, izq, medio - 1)` y `maximo_montana(arr, medio + 1, der)`. Solo se ejecuta una de las dos llamadas.

+ Combine: No hay una fase de combinación explícita, ya que cada llamada recursiva retorna directamente el resultado sin necesidad de integrar resultados parciales.

En cuantos subproblemas se divide?
+ Se divide en 1 subproblema, ya que solo se explora una mitad dependiendo
+ La decisión depende de las comparaciones de los vecinos:
    + Si el medio es menor que el vecino izquierdo, se busca en la mitad izquierda.
    + Si el medio es menor que el vecino derecho, se busca en la mitad derecha.
    + Si el medio es mayor que ambos vecinos, se retorna como máximo.

Escribir la función T(n) de manera recursiva:
$$
T(n) = 
\begin{cases} 
    1 \ & \text{si} \ n = 1 \\
    T(n/2) + \Theta(1) &  \text{si}\ n > 1
\end{cases}
$$
+ $\Theta(1)$: Caso base (arreglo de un elemento)
+ $T(n/2)$: Una llamada recursiva de tamaño n/2
+ $\Theta$: Costo de comparaciones con los vecinos

Determinar la complejidad del algoritmo utilizando el Teorema Maestro:
Aplicamos el Teorema Maestro con:
+ $a = 1$ (número de subproblemas)
+ $c = 2$ (factor de reducción)
+ $f(n) = \Theta(1)$ (costo de combinar)

Calculamos $\log_c a$ = $\log_2 1$ = 0

Tenemos que $f(n) = \Theta(1) = \Theta(n^0)$, entonces $f(n)$ crece más lento que $n^{\log_c a}$, por lo que estamos en el caso 1 del Teorema Maestro.

Por lo tanto: $\boxed{T(n) = \Theta(\log n)}$

Por qué funciona el algoritmo?
Propiedades del arreglo montaña:
+ Existe un único máximo global.
+ A la izquierda del máximo: secuencia creciente.
+ A la derecha del máximo: secuencia decreciente.

Invariante: El máximo siempre se encuentra en el intervalo [izq, der] actual. 

Demostración por casos:
1. Si arr[medio] < arr[medio - 1]: El máximo está a la izquierda, ya que la secuencia es creciente hacia el máximo.
2. Si arr[medio] < arr[medio + 1]: El máximo está a la derecha, ya que la secuencia es decreciente hacia el máximo.
3. Si arr[medio] es mayor que ambos vecinos: arr[medio] es el máximo, ya que es el punto de inflexión entre la secuencia creciente y decreciente.

Difernetes estrategias para encontrar el máximo:
| Enfoque | Complejidad | Descripción |
|---------|-------------|-------------|
| Fuerza Bruta | O(n) | Recorrer todo el arreglo|
| Divide and Conquer | O(log n) | Descartar mitades |

Ventajas del enfoque Divide and Conquer:
+ Aprovecha la estructura del arreglo montaña.
+ Complejidad logarítmica, mucho más eficiente que la fuerza bruta
+ Eficiente en arreglos grandes

Aplicación practica:
+ Busqueda de picos de señales
+ Optimización de funciones unimodales
+ Análisis de datos con tendencias crecientes y decrecientes


## Ejercicio 8 (MaximaSubsecuencia):
Dada una secuencia de n enteros, se desea encontrar el máximo valor que se puede obtener sumando elementos continuos.

Diseñar un algoritmo divide and conquer para resolver este problema en complejidad O(n log n).

Ejemplo: Para la secuencia [3, -1, 4, 8, -2, 2, 7, 5], este valor es 14, que se obtiene de la subsecuencia [3,-1, 4, 8 ].

> Este problema también es conocido como el problema de la máxima subsecuencia o el problema de la suma máxima de subarreglo (Maximum Subarray Problem).

Idea principal: Dividir el arreglo por la mitad y considerar tres casos:

1. Caso izquierda: La subsecuencia máxima está completamente en la mitad izquierda.
2. Caso derecha: La subsecuencia máxima está completamente en la mitad derecha.
3. Caso cruzado: La subsecuencia máxima cruza el punto medio, es decir, incluye elementos de ambas mitades.

Solución: El máximo de estos tres casos:
```python
max_suma = max(caso_izquierda, caso_derecha, caso_cruzado):
```
> El caso cruzado requiere un trato especial.

¿Cómo calcular la suma máxima que cruza el medio?

La subsecuencia debe incluir:
+ Al menos el último elemento de la mitad izquierda.
+ Al menos el primer elemento de la mitad derecha.

Algoritmo:
1. Desde el medio hasta la izquierda: encontrar la suma máxima
2. Desde el medio + 1 hacia la derecha: encontrar la suma máxima
3. Sumar ambas máximas para obtener el caso cruzado.

Ejemplo: [3, -1, 4, 8, -2, 2, 7, 5]
+ Máximo izquierda (desde el medio): 3 + (-1) + 4 + 8 = 14
+ Máximo derecha (desde el medio + 1): -2 + 2 = 0
+ Suma cruzada: 14 + 0 = 14

```python
def max_suma_subsecuencia(arr, izq, medio, der):
    # Suma máxima en la mitad izquierda
    suma_izq = float('-inf')
    suma_actual = 0
    for i in range(medio, izq - 1, -1):
        suma_actual += arr[i]
        suma_izq = max(suma_izq, suma_actual)

    # Suma máxima en la mitad derecha
    suma_der = float('-inf')
    suma_actual = 0
    for i in range(medio + 1, der + 1):
        suma_actual += arr[i]
        suma_der = max(suma_der, suma_actual)

    return suma_izq + suma_der
```
Complejidad de esta función: $O(n)$ donde $n = der - izq + 1$ 

Identificar las partes del algoritmo divide and conquer:
+ Divide:
    + `medio = (izq + der) // 2` (calcula el punto medio)
    + Separar el arreglo en dos mitades
+ Conquer:
    + `max_izq = max_suma_subsecuencia(arr, izq, medio, der)` (calcula el máximo en la mitad izquierda)
    + `max_der = max_suma_subsecuencia(arr, medio + 1, der)` (calcula el máximo en la mitad derecha)
+ Combine:
    + Calcular la máxima cruzada.
    + `return max(max_izq, max_der, max_cruzado)`

¿En cuantos problemas se divide el problema?

Respuesta: se divide en 2 subproblemas
+ Mitad Izquierda: arr[izq ... medio]
+ Mitad Derecha: arr[medio+1 ... der]

¿De que tamaño son estos subproblemas?

Respuesta: Cada subproblema tiene tamaño n/2

¿Cual es el costo de combinar?
Respuesta: $O(n)$ debido al cálculo de suma cruzada
+ Recorrer desde el medio hacia la izquierda: $O(n/2)$
+ Recorrer desde el $medio+1$ hacia la derecha: O(n/2)
+ Total $O(n)$ 
Escribir la función T(n) de manera recursiva:

respuesta: 
$$
T(n) = 
\begin{cases}
    \Theta(1) & \text{si} \ n = 1 \\
    2 T(n/2) + \Theta(n) & \text{si} \ n > 1
\end{cases}
$$

Determinar la complejidad del algoritmo utilizando el Teorema Maestro:

Párametros:
+ $a = 2$ (número de subproblemas)
+ $c = 2$ (factor de reducción)
+ $f(n) = \Theta(n)$ (costo de combinar)

Calculamos $\log_c a$ = $\log_2 2$ = 1

Tenemos $f(n) = \Theta(n) = \Theta(n^1) = \Theta(n^{\log_c a})$, entonces estamos en el caso 2 del Teorema Maestro.

Por lo tanto: $\boxed{T(n) = \Theta(n \log n)}$

Diferentes enfoques del problema:

|Algoritmo|Complejidad|Descripción|
|---------|-----------|-----------|
|Fuerza Bruta|O(n^3)|Probar todos los pares (i, j)|
|Fuerza Bruta Optimizada|O(n^2)|Sumas Aculomadas|
|Divide and Conquer|O(n log n)|This ejercicio|
|Kadane's Algorithm|O(n)|Programación dinámica|

Ventajas del enfoque Divide and Conquer:
+ Más eficiente que la fuerza bruta
+ Ilustra bien la técnica D&C
+ Paralelizable (las llamadas son independientes)

## Ejercicio 14 (Diferencia Mínima):

Se tienen dos arreglos de n naturales A y B:
+ A esta ordenado de manera creciente
+ B esta ordenado de manera decreciente
+ Ningún valor aparece más de una vez en el mismo arreglo

Para cada posición i consideramos la diferencia absoluta entre los valores de ambos arreglos $|A[i] - B[i]|$. Se desea buscar el mínimo posible de dicha cuenta.

Ejemplo:
+ A = [1, 3, 5, 7, 9]
+ B = [10, 8, 6, 4, 2]
Diferencias: |1-10|, |3-8|, |5-6|, |7-4|, |9-2| → 9, 5, 1, 3, 7
El mínimo es 1 (en la posición i = 2)

Objetivo: Implementar minDif con complejidad O(log n).

Observación clave sobre el comportamiento de las diferencias:
Como A es creciente y B es decreciente: 
+ Al inicio: A[0] es pequeño y B[0] es grande → diferencia grande
+ Al avanzar: A[i] aumenta y B[i] disminuye → diferencia disminuye
+ En algún punto, la diferencia alcanzará un mínimo
+ Al final: A[n-1] es grande y B[n-1] es pequeño → diferencia grande

Propiedad importante: 
La función f(i) = |A[i] - B[i]| es unimodal, es decir, tiene un único mínimo.
+ Puede decrecer y luego crecer
+ O puede crecer y luego decrecer
+ Tiene un mínimo global

### Busqueda ternaría:

1. Inicialización
$$left = 0 $$
$$$$right = n - 1$$

2. División en tercios
mientras right - left > 2:
$$mid_1 = left + (right - left) // 3$$
$$mid_2 = right - (right - left) // 3$$

3. Evaluación
$$diff_1 = |A[mid_1] - B[mid_1]|$$
$$diff_2 = |A[mid_2] - B[mid_2]|$$

4. Decisión
+ Si $\text{diff}_1 > \text{diff}_2$:
    + El mínimo está cerca de $\text{mid}_2$
    + Actualizamos $right = \text{mid}_2$
    + Descartamos el primer tercio [left, mid_1)
+ Si $\text{diff}_1 <= \text{diff}_2$:
    + El mínimo está cerca de $\text{mid}_1$
    + Actualizamos $left = \text{mid}_1$
    + Descartamos el tercer tercio (mid_2, right]

5. Búsqueda final
cuando quedan 3 o menos elementos:
$$resultado = \min(|A[i] - B[i]|) \text{ para } i \in [left, right]$$

### Función minDif
```python
def minDif(A,B):
    n = len(A)
    left, right = 0, n - 1
    while right - left > 2:
        mid_1 = left + (right - left) // 3
        mid_2 = right - (right - left) // 3
        diff_1 = abs(A[mid_1] - B[mid_1])
        diff_2 = abs(A[mid_2] - B[mid_2])
        if diff_1 > diff_2:
            right = mid_2
        else:
            left = mid_1
    # Verificar los últimos elementos
    min_diff = float('inf')
    for i in range(left, right + 1):
        min_diff = min(min_diff, abs(A[i] - B[i]))
    return min_diff
```

