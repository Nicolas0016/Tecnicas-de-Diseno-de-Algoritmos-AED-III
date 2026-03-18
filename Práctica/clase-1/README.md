### Ejercicio 1:

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

### Ejercicio 2:
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