# Ejercicio 1 
Dado el algoritmo de *mergesort*, implementado en el siguiente código en python:

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    medio = len(arr) // 2
    mitad_izq = merge_sort(arr[:medio])
    mitad_der = merge_sort(arr[medio:])

    return merge(mitad_izq, mitad_der)

def merge(izq, der):
    resultado = []
    i = j = 0

    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado
```

1. Identificar qué lineas son el *divide*, cuáles son el *conquer* y cuáles el *combine*.
2. En cuantos subproblemas se divide?
3. ¿De qué tamaño son esos subproblemas?
4. ¿Cual es el costo de combinar los resultados de los subproblemas?
5. Escribir en función $T(n)$ de manera recursiva.
6. Determinar la complejidad del algoritmo utilizando el Teorema Maestro.

> Respuesta

1. Las lineas son:
    + Divide: `medio = len(arr) // 2`
    + Conquer: `mitad_izq = merge_sort(arr[:medio])` y `mitad_der = merge_sort(arr[medio:])`
    + Combine: `return merge(mitad_izq, mitad_der)`
2. Se divide en 2 subproblemas.
3. Son de tamaño $\frac{n}{2}$ cada uno.
4. El costo de combinar los resultados de los subproblemas es $O(n)$.
5. $T(n) = 2T(\frac{n}{2}) + O(n)$
6. $T(n) = O(n \log n)$ es el caso 2 del Teorema Maestro.

# Ejercicio 2
Dado el algoritmo de búsqueda binaria, implementado en el siguiente código Python:

```python
def busqueda_binaria(arr, objetivo):
    if izq > der:
        return False
    medio = (izq + der) // 2
    if arr[medio] == objetivo:
        return True
    elif arr[medio] < objetivo:
        return busqueda_binaria(arr, objetivo, medio + 1, der)
    else:
        return busqueda_binaria(arr, objetivo, izq, medio - 1)
```


1. Identificar qué lineas son el *divide*, cuáles son el *conquer* y cuáles el *combine*.
2. En cuantos subproblemas se divide?
3. ¿De qué tamaño son esos subproblemas?
4. ¿Cual es el costo de combinar los resultados de los subproblemas?
5. Escribir en función $T(n)$ de manera recursiva.
6. Determinar la complejidad del algoritmo utilizando el Teorema Maestro.

> Respuesta

1. Las lineas son:
    + Divide: `medio = (izq + der) // 2`
    + Conquer: `return busqueda_binaria(arr, objetivo, medio + 1, der)` y `return busqueda_binaria(arr, objetivo, izq, medio - 1)`
    + Combine: No hay combine, ya que solo se devuelve el resultado de la llamada recursiva.
2. Se divide en 1 subproblema.
3. Son de tamaño $\frac{n}{2}$ cada uno.
4. El costo de combinar los resultados de los subproblemas es $O(1)$.
5. $T(n) = T(\frac{n}{2}) + O(1)$
6. $T(n) = O(\log n)$ es el caso 2 del Teorema Maestro.

# Ejercicio 3
Escriba un algoritmo con dividir y conquistar que determine si un arreglo de tamaño potencia de 2 es *más a la izquierda* donde "más a la izquierda" significa que:

+ La suma de los elementos de la mitad izquierda superan los de la midad derecha.
+ Cada una de las mitades es a su vez "más a la izquierda".

Por ejemplo, el arreglo [8, 6, 7, 4, 5, 1, 3, 2] es “más a la izquierda”, pero [8, 4, 7, 6, 5, 1, 3, 2] no lo es.

Intente que su solución aproveche la técnica de modo que la complejidad del algoritmo sea estrictamente menor a $O(n^2)$.

> Respuesta
```python
def es_mas_izquierda(arr):
    if len(arr) == 1:
        return True
    medio = len(arr) // 2
    suma_izq = sum(arr[:medio])
    suma_der = sum(arr[medio:])
    if suma_izq > suma_der:
        return es_mas_izquierda(arr[:medio]) and es_mas_izquierda(arr[medio:])
    else:
        return False
```
> $$T(n) = 2T(\frac{n}{2}) + O(n)$$
> $$T(n) = O(n \log n)$$


# Ejercicio 4:
Tenemos un arreglo $a = [a_1, a_2, ..., a_n]$ de n enteros distintos en orden estrictamente creciente. Queremos determinar si existe una posición i tal que $a_i = i$. Por ejemplo, dado el arreglo a = [-1, 0, 2, 4, 5, 6, 8, 10] existe una posición i tal que $a_i = i$, ya que $a_2 = 2$ y $a_4 = 4$. 
Diseñar un algoritmo con dividir y conquistar que resuelva este problema con complejidad estrictamente menor a $O(n)$.

> Respuesta

```python
def es_fijo(arr, izq, der):
    if izq > der:
        return False
    medio = (izq + der) // 2
    if arr[medio] == medio:
        return True
    elif arr[medio] < medio:
        return es_fijo(arr, medio + 1, der)
    else:
        return es_fijo(arr, izq, medio - 1)
```
> $$T(n) = T(\frac{n}{2}) + O(1)$$
> $$T(n) = O(\log n)$$

# Ejercicio 5
Encuentre un algoritmo para calcular $a^b$ en tiempo logarítmico en $b$. Piense en como reutilizar los resultados ya calculados.

> Respuesta
```python
def potencia(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return potencia(a, b // 2) * potencia(a, b // 2)
    else:
        return a * potencia(a, b // 2) * potencia(a, b // 2)
```
> $$T(n) = T(\frac{n}{2}) + O(1)$$
> $$T(n) = O(\log n)$$

# Ejercicio 6
Un arreglo de enteros se denomina *montaña* si está compuesto por una secuencia estrictamente creciente seguida de una estrictamente decreciente. Dado un arreglo *montaña* de longitud n, dar un algoritmo que encuentre el máximo del arreglo en complejidad $O(log n)$. Por ejemplo, para un arreglo $[-1, 3, 8, 22, 30, 22, 8, 4, 2, 1]$, el máximo está en la posición 4 y vale 30.

> Respuesta
```python
def encontrar_pico(arr):
    medio = len(arr) // 2
    if len(arr) == 1:
        return arr[0]
    elif arr[medio] > arr[medio + 1]:
        return encontrar_pico(arr[:medio])
    else:
        return encontrar_pico(arr[medio + 1:])
```

# Ejercicio 7 
Calcule la complejidad de un algoritmo utilizando $T(n)$ pasos para una entrada de tamaño $n$, donde $T$ cumple:

1. $T(n) = T(n-2)+5$
2. $T(n) = T(n-1)+n$
3. $T(n) = T(n-1) + \sqrt{n}$
4. $T(n) = T(n-1) + n²$
5. $T(n) = 2T(n-1)$
6. $T(n) = T(n/2) + n$
7. $T(n) = T(n/2) + \sqrt{n}$
8. $T(n) = T(n/2) + n²$
9. $T(n) = 2T(n-4)$
10. $T(n) = 2T(n/2) + \log(n)$
11. $T(n) = 3T(n/4)$
12. $T(n) = 3T(n/4) + n$

Intentar estimar la complejidad para cada ítem directamente y luego calcularla utilizando el teorema maestro de ser posible. Para simplificar los cálculos se puede asumir que n es potencia o multiplo de 2 o 4 según sea conveniente.

> Respuesta

1. $T(n) = \Theta(n)$
2. $T(n) = \Theta(n^2)$
3. $T(n) = \Theta(n \sqrt{n})$
4. $T(n) = \Theta(n^3)$
5. $T(n) = \Theta(2^n)$
6. $T(n) = \Theta(n)$
7. $T(n) = \Theta(\sqrt{n})$
8. $T(n) = \Theta(n^2)$
9. $T(n) = \Theta(2^n)$
10. $T(n) = \Theta(n)$
11. $T(n) = \Theta(n^{\log_4 3})$
12. $T(n) = \Theta(n)$

# Ejercicio 8
Dada una secuencia de $n$ enteros, se desea encontrar el máximo valor que se puede obtener sumando elementos continuos. Diseñar un algoritmo basado en la técnica de dividir y conquistar que resuelva el problema en $O(n \log n)$. Por ejemplo, para la secuencia $[-2, 1, -3, 4, -1, 2, 1, -5, 4]$, el máximo valor es 6, obtenido sumando los elementos $[4, -1, 2, 1]$.

```python
def maximo_subarreglo(arr):
    if len(arr) == 1:
        return arr[0]
    medio = len(arr) // 2
    max_izq = maximo_subarreglo(arr[:medio])
    max_der = maximo_subarreglo(arr[medio:])
    max_cruce = maximo_cruce(arr, medio)
    return max(max_izq, max_der, max_cruce)

def maximo_cruce(arr, medio):
    max_izq = -float('inf')
    suma = 0
    for i in range(medio - 1, -1, -1):
        suma += arr[i]
        if suma > max_izq:
            max_izq = suma
    max_der = -float('inf')
    suma = 0
    for i in range(medio, len(arr)):
        suma += arr[i]
        if suma > max_der:
            max_der = suma
    return max_izq + max_der
```

> $$T(n) = 2T(\frac{n}{2}) + O(n)$$
> $$T(n) = O(n \log n)$$

# Ejercicio 9
Suponga que se tiene un método de *potencia* que dada una matriz A de orden 4 x 4 y un número n, computa la matriz $A^n$. 
Dada una matriz cuadrada A de orden 4 x 4 y un número natural n que es potencia de 2, desarrollar, utilizando la técnica dividir y conquistar y el método *potencia*, que permita calcular:

$$A¹ + A² + A³ + ... + A^n$$

Preocure que el algoritmo propuesto aplique el método *potencia*, sume y haga productos de matrices una cantidad estrictamente menor que O(n).
```python
def potencia(A, n):
    if n == 1:
        return A
    elif n % 2 == 0:
        return potencia(A, n // 2) * potencia(A, n // 2)
    else:
        return A * potencia(A, n // 2) * potencia(A, n // 2)
    
def suma_potencias(A, n):
    if n == 1:
        return A
    return suma_potencias(A, n // 2) + potencia(A, n // 2) * suma_potencias(A, n // 2)
```

> $$T(n) = T(\frac{n}{2}) + O(1)$$
> $$T(n) = O(\log n)$$

# Ejercicio 10:
Dado un árbol binario cualquiera, diseñar un algoritmo de dividir y conquistar que devuelva la máxima diferencia entre dos nodos. El algoritmo no debe hacer recorridos innecesarios sobre el árbol.

> Para saber el camino más largo de un árbol, posiblemente necesite conocer más que sólo los caminos más largos de sus subárboles.

> Respuesta
```python
def max_diff(arbol):
    if arbol is None:
        return 0
    return max(max_diff(arbol.izq), max_diff(arbol.der), arbol.val - min_val(arbol.izq), arbol.val - min_val(arbol.der))
```

