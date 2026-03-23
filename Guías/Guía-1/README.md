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
