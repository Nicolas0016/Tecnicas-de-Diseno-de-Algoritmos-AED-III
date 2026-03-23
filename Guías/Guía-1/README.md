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

