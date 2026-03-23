# Problemas bien resueltos
Los algoritmos polinomiales se consideran satisfactorios (cuanto menor sea el grado, mejor), y los algoritmos supra-polinomiales se consideran no-satisfactorios.

No obstante...
+ Si los tamaños de instancia son pequeños, ¿es tan malo un algoritmo exporencial?
+ ¿Cómo se comparan $O(n^{85})$ con $O(1,001^n)$?
+ ¿Puede pasar que un algoritmo de peor caso exporencial sea eficiente en la práctica? ¿Puede pasar que en la práctica sea el mejor?
+ ¿Qué pasa si no encuentro un algoritmo polinomial?

# Problemas de optimización
+ Un problema de optimización consiste en encontrar la mejor solución detro de un conjunto:

$$Z^* = \text{max} f(x) \quad \text{o bien} \quad Z^* = \text{min} f(x)$$
+ La función $f: S \to \mathbb{R}$ se denomina **función objetivo** del problema
+ El conjunto $S$ es la **región factible** y los elementos $x \in S$ se denominan **soluciones factibles**
+ El valor $Z^* \in \mathbb{R}$ es el **valor óptimo** del problema, y cualquier solución factible $x^* \in S$ tal que $f(x^*) = Z^*$ se denomina **óptimo** del problema.

# Problemas de optimización combinatoria

Un problema de **combinación combinatoria** es un problema de optimización cuya región factible es un conjunto definido por consideraciónes combinatorias (!).

La combinatoria es una rama de las matemáticas discreta que estudia la construcción, enumeración y existencia de configuraciones de objetos finitos que satisfacen ciertas propiedades.

> Por ejemplo, las regiones factibles dadas por todos los subconjuntos/permutaciones de un conjunto finito de elementos (posiblemente con alguna restricción adicional), todos los caminos en un grafo, etc.

# Algoritmos de fuerza bruta
Un algoritmo de **fuerza bruta** es un algoritmo que resuelve un problema de optimización combinatoria explorando todas las soluciones factibles y seleccionando la mejor.

1. Se los suele llamar también algoritmos de búsqueda exhaustiva.
2. Se trata de una técnica trivial pero muy general.
3. Suele ser fácil de implementar, y es un algoritmo exacto

Un problema común de este tipo de algoritmo es su complejidad. Habitualmente, un algoritmo de fuerza bruta tiene una complejidad exporencial.

# Ejemplo: El problema de la mochila
Datos de entrada:
+ Capacidad $C \in \mathbb{Z}_+ de la mochila (peso máximo)$
+ Un conjunto de $n \in \mathbb{Z}_+$ items, cada uno con un peso $w_i \in \mathbb{Z}_+$ y un valor $v_i \in \mathbb{Z}_+$

Objetivo:
+ Seleccionar un subconjunto de items tal que su peso total no exceda la capacidad de la mochila y su valor total sea máximo

# Ejemplo: El problema de la mochila
Datos de entrada:
+ Capacidad $C \in \mathbb{Z}_+$ de la mochila (peso máximo)
+ Cantidad $n \in \mathbb{Z}_+$ de objetos 
+ Peso $p_i \in \mathbb{Z}_+$ del objeto $i$, para $i = 1, \cdots, n$
+ Beneficio $b_i \in \mathbb{Z}_+$ del objeto $i$, para $i = 1, \cdots, n$

Problema: Determinar que objetos debemos incluir en la mochila sin excedernos del peso máximo $C$, de modo tal de **máximizar** el beneficio total entre objetos seleccionados

### ¿Cómo es un algoritmo de fuerza bruta para el problema de mochila?
¿Cómo implementar este algoritmo?

```pascal
Mochila(S ⊆ {1, ..., n}, k: ℤ)
    if k = n + 1 then
        if peso(S) ≤ C ∧ beneficio(S) > beneficio(B) then
            B ← S
        end if
    else
        Mochila(S ∪ {k}, k + 1) 
        Mochila(S, k + 1)       
    end if
```

**Variables principales:**
- $S$: Subconjunto de elementos seleccionados en la rama actual.
- $k$: Índice del elemento que estamos evaluando.
- $B$: Mejor solución (subconjunto) encontrada hasta el momento.
- $C$: Capacidad máxima de la mochila.

+ Iniciamos la recursión con $B \leftarrow \emptyset$ y $\text{Mochila}(\emptyset, 1)$.

### ¿Cuál es la complejidad de este algoritmo?

> Respuesta: $O(2^n)$

Podemos **interrumpir la recursión** cuando el subconjunto actual excede la capacidad de la mochila

```pascal
Mochila(S ⊆ {1, ..., n}, k: ℤ)
    if k = n + 1 then
        if peso(S) ≤ C ∧ beneficio(S) > beneficio(B) then
            B ← S
        end if
    else if peso(s) ≤ C then
        Mochila(S ∪ {k}, k + 1) 
        Mochila(S, k + 1)       
    end if
```
Con este agregado, decimos que tenemos un **backtracking**, porque interrumpimos la recursión cuando el subconjunto actual excede la cierto umbral.
¿Cuál es la complejidad de este algoritmo?
> Respuesta: $O(2^n)$
¿Podemos implementar alguna otra poda?

```pascal
Mochila(S ⊆ {1, ..., n}, k: ℤ)
    if k = n + 1 then
        if peso(S) ≤ C ∧ beneficio(S) > beneficio(B) then
            B ← S
        end if
    else if peso(s) ≤ C ∧ beneficio(S) + ∑b_i > beneficio(B) then
        Mochila(S ∪ {k}, k + 1) 
        Mochila(S, k + 1)       
    end if
```

Este tipo de algoritmo se denomina habitualmente **branch and bound**, porque ramifica la búsqueda y poda las ramas que no son prometedoras.

# Backtracking
Recorrer sistemáticamente todas las posibles configuraciones del espacio de soluciones de un problema computacional, eliminando las **configuraciones parciales** que no puedan completarse a una solución.
+ Habitualmente, utiliza un vector $a = (a_1, a_2, \cdots, a_n)$ para representar una solución candidata, cada $a_i$ representa una decisión.
+ El espacio de soluciones es el producto cartesiano $A_1 \times A_2 \times \cdots \times A_n$, donde $A_i$ es el conjunto de valores que puede tomar la variable $a_i$.

En cada paso se extienden las soluciones parciales $a = (a_1, \cdots, a_k)$, $k < n$, agregando un elemento más $a_{k+1} \in S_{k+1} \subseteq A_{k+1}$, al final del vector $a$. Las nuevas soluciones parciales son sucesores de la anterior.

En caso de $S_{k+1} = \emptyset$, se retrocede a la solución parcial $(a_1, \cdots, a_{k-1})$.Se puede pensar este espacio como un árbol dirigido, donde cada vértice representa una solución parcial y un vértice x es hijo de y si la solución parcial x se puede extender desde la solución parcial y
> Obs: En el caso de backtracking, el árbol es un árbol binario.

> Permite descartar configuraciones antes de explorar todo el espacio de soluciones.

backtraking: Todas las soluciones 
```
algoritmo BT(a,k):
    si a es solucion entonces:
        procesar(a)
        retornar 
    sino 
        para cada a' ∈ sucesores(a) hacer:
            BT(a', k+1)
        fin para
    fin si
    retornar
```

backtraking: Una solución
```
algoritmo BT(a,k)
    si a es solucion entonces:
        procesar(a)
        retornar
    sino
        para cada a' ∈ sucesores(a) hacer:
            BT(a', k+1)
            su encontro entonces 
                retornar
        fin para
    fin si
    retornar
```

> Obs: En el caso de una solución óptima, el algoritmo termina cuando encuentra la primera solución.

Resolver un sudoku con backtracking.
El problema de resolver un sudoku se resuelve en forma muy eficiente con un algoritmo de backtracking (no obstante su complejidad es exponencial).

# Fuerza bruta 
Problema de n damas 
Problema ubicar $n$ damas en un tablero de ajedrez de $n \times n$ de modo tal que no se ataquen entre sí.

Solución por fuerza bruta: hallar todas las formas posibles de colocar n damas en un tablero de $n \times n$ y seleccionar una solución válida.

Por ejemplo para n = 8 una implementación directa consiste en generar todos los conjuntos de casillas.

$$2^{64} = 18.446.744.073.709.551.616 \text{ combinaciones XD}$$

Pero sabemos que dos damas no pueden estar en la misma casilla.
$$\binom{64}{8} = \frac{64!}{8!(64-8)!} = \frac{64!}{8!56!} = 4.426.165.368 \text{ combinaciones}$$

Además que cada columna debe tener exactamente una dama. Cada solución parcial puede estar representada por $(a_1, a_2, \cdots, a_k)$, con $a_i \in \{1, \cdots, n\}$ indicando la fila de la dama que está la columna i.

Esto logra reducir el espacio de soluciones a:
$$n! = 8! = 40.320 \text{ combinaciones}$$

> Esto está mejor, pero se puede mejorar observando que no es necesario analizar muchas de estas combinaciones (¿por qué?).

