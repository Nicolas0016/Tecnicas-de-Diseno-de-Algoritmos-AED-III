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
> Recuerdo

$$
T(n) = 
\begin{cases} 
    a \ T(n/c) + f(n) \ \text{si}\ n > 1 \\
    1 \ \text{si} \ n = 1
\end{cases}
$$

> Respuesta