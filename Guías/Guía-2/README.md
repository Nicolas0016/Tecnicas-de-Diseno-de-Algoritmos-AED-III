# Suma de subconjuntos BT
Dado un multiconjunto $C = \{c_1, \cdots, c_n\}$ de números naturales y un natural $k$, queremos determinar si existe un subconjunto de $C$ cuya sumatoria sea $k$. Vamos a suponer que $C$ esta ordenado de alguna forma arbitraria pero conocida. Las soluciones (candidatas) son los vectores $a = (a_1, \cdots, a_n)$ de valores binarios; el subconjunto de $C$ representado por $a$ contiene a $c_i$ si y solo si $a_i = 1$. Luego, $a$ es una solución valida cuando $\sum^{n}_{i=1} {a_i c_i} = k$. Asimismo, una solución parcial es un vector $p = (a_1, \cdots, a_i)$ de números binarios con $0 \leq i \leq n$. Si $i< n$, las soluciones sucesoras de p son $p \oplus 0$ y $p \oplus 1$, donde $\oplus$ indica concatenación.

Ejemplo

Digamos que te doy el conjunto de números $C = \{3,7,2,5\}$ en este caso $n = 4$ porque hay 4 elementos.

El problema de "Suma de subconjutos" nos pied encontrar una combinación de estos números que sume un valor específico $k$. 

Para indicar a la computadora que elementos elegimos para formar nuestro subconjunto y cuals no, usamos un vector de valores binarios de la mismalongitud que $C$. A este vector le llamamos $a$.

+ Si $a_i = 1$, significa que sí incluimos el número de la posición $i$ en nuestro subconjunto.
+ Si $a_i = 0$, significa que NO lo icluimos

Supongamos que nuestra "solución candidata" es el vector $a = (1,0,1,0)$. Entonces, el vector a representa al subconjunto $\{3,2\}$. La suma de esa solución candidata sería: $3 + 2 = 5$.

Si el valor $k$ es 5 entonces la solución candidata es correcta.

> Basicamente, los vcotres inarios son como interruptores (On/Off) para cada número del conjunto original, donde 1 es "Lo agarro" y 0 es "lo dejo". En algoritmos de `Backtraking`, lo que la computadora hace es ir progando todas las combinaciones posibles de ceros y unos hasta encontrar la que suma $k$.


1. Escribir el conjunto de soluciones candidatas para $C = \{6, 12, 6\}$ y $k = 12$

{{0,0,0}, {0,1,0}, {1,0,0},{1,0,1},{0,1,1}}

2. Escribir el conjunto de soluciones válidas para $C = \{6, 12, 6\}$ y $k = 12$
{{1,0,1}, {0,1,0}}

3. Escribir el conjunto de soluciones parciales para $C = \{6, 12, 6\}$ y $k = 12$
{{0},{0,1},{0,1,0},{1},{1,0},{1,0,1}}
4. Dibujar un árbol de backtraking correspondiente al algoritmo descrito para $C = \{6, 12, 6\}$ y $k = 12$, indicando claramente la relación entre las distintas componentes del árbol y los conjuntos de los insisos anteriores.
![alt text](image.png)

5. Sea $C$ la familia de todos los multiconjuntos de números naturales. Considerar la siguiente función recursiva $ss: C \times \mathbb{N}_0 \to \{V, F\}$.

$ss(\{c_1, \cdots, c_n\}, k) = 
\begin{cases}
k = 0 & \text{si} \ n = 0 \\
ss(\{c_1, \cdots, c_{n-1}\}, k) \ \lor ss(\{c_1, \cdots, c_{n-1}, k - c_n\}) & \text{si} \ n > 0 
\end{cases}
$

Converserse de que $ss(C,k) = V$ si y sólo si el problema tiene solución válida para la entrada $C,k$. Para ello, observar que hay dos posibilidades para una solución valida $a = \{a_1, \cdots, a_n\}$ para el caso $n > 0$: o bien $a_n = 0$ o bien $a_n = 1$.

+  En el primer caso, existe un subconjunto de $\{c1, \cdots, c_{n-1}\}$ que suma $k$.
+  En el segundo, existe un subconjunto de  $\{c1, \cdots, c_{n-1}\}$ que suma $k - c_n$.

6. Convencerse de la siguiente implementación recursiva de $ss$ en lenguaje imperativo y de que retorna la solución para $C,k$ cuando se llama con $C, |C|, k$. ¿Cuál es su complejidad?

```haskell
subset_sum(C, i, j):
    Si i = 0, retornar j = 0;
    Si no, retornar subset_sum(C, i-1, j) V subset_sum(C, i-1, j - C[i]);
```
Como tal el peor caso se recorrerian todas las hojas del arbol entonces:
$T(n) = 2^n - 1$ donde n es la cantidad de elementos del conjunto.

7. Dibujar el árbol de llamadas recursivas para la entrada $C = \{6, 12, 6\}$ y $k = 12$, y compararlo con el árbol de backtraking.

![alt text](image-1.png)

8. Considerar la siguiente regla de factibilidad: 
$p = (a_1, \cdots, a_n)$ se puede extender a una solución válida si $\sum^i_{q=1}a_qc_q \leq k$. Convencerse de que la siguiente implementación incluye la regla de factibilidad.

```hs
subset_sum(C,i,j):
    Si j < 0, retornar Falso 
    Si i = 0, retornar (j=0)
    Si no, retornar subset_sum(C,i-1,j) V subset_sum(C,i-1,j-C[i])
```

9. Definir otra regla de factibilidad, mostrando que la misma es correcta; no es necesario implementarla.

Otra regla de factibilidad:
Una solución parcial $p = (a_1, \cdots, a_i)$ es directamente una solución válida (y no hace falta seguir extendiéndola) si $\sum_{q=1}^{i} a_q c_q = k$.

Esto equivale a verificar si $j = 0$ antes de llegar a las hojas del árbol ($i = 0$). Dado que estamos trabajando con números naturales (no negativos), agregar cualquier otro elemento estricatmente mayor a cero haría que la suma supere $k$. Por lo tanto, podemos detener la búsqueda en esa rama y retornar Verdadero inmediatamente, asumiendo que el resto de los elementos no se incluyen (es decir, $a_q = 0$ para los elementos restantes).

10. Modificar la implementación para imprimir el subconjunto $C$ que suma k, si existe.

# MagiCuadrados

Un cuadrado mágico de orden n, es un cuadrado con los números $\{1,\cdots, n²\}$, tal que todas sus filas, columnas y dos diagonales suman lo mismo. El número que suma cada fila es llamado número mágico.

$$
\begin{array}{|c|c|c|}
\hline
2 & 7 & 6 \\
\hline
9 & 5 & 1 \\
\hline
4 & 3 & 8 \\
\hline
\end{array}
$$

Existen muchos métodos para generar cuadrados mágicos. El objetivo de este ejercicio es contar cuántos cuadrados mágicos de orden n existen.
 

1. ¿Cúantos cuadrados mágicos habría que generar para encontrar todos los cuadrados mágicos si se utiliza una solución de fuerza bruta?

Si n = 3, entonces n² = 9. Por lo tanto, habría que generar 9! = 362,880 cuadrados mágicos. Considerando que cada cuadrado mágico tiene 9 celdas, y que cada celda puede tener un valor de 1 a 9, sin repetir valores.

2. Enuciar un algoritmo que use *backtraking* para resolver este problema que se base en las siguientes ideas:

    + La solución parcial tiene los valores de las primeras $i-1$ filas establecidos, a igual que los valores de las primeras $j$ columnas de la fila $i$.
    + Para establecer el valor de la posición $(i, j + 1)$ (o $(i+1,1)$ si $j = n$ y $i \neq n$) se consideran todos los valores que aún no se encuentran en el cuadrado. Para cada valor posible, se establece dicho valor en la posición y se cuentan todos los cuadrados mágicos con esta nueva solución parcial.

    mostrar los primeros dos niveles del árbol de backtraking para $n = 3$.

Explicacion de la idea:

El algoritmo llena las celdas del cuadrado mágico paso a paso, avanzando de izquierda a derecha y de arriba hacia abajo. Al terminar una fila, continúa por la primera celda de la fila siguiente.

En cada celda vacía, realiza los siguientes pasos de exploración (*backtracking*):
1. **Elige:** Toma el primer número disponible (que no se haya utilizado en las celdas anteriores) y lo coloca en la celda actual.
2. **Explora:** Realiza una llamada recursiva para calcular cuántos cuadrados mágicos válidos se pueden terminar de armar a partir de este tablero parcial.
3. **Deshace:** Una vez obtenida la respuesta de esa recursión, deshace el movimiento (saca el número de la celda).
4. **Repite:** Prueba colocando el siguiente número disponible y vuelve a explorar.

Finalmente, suma los resultados obtenidos de todas las ramas iteradas y devuelve la cantidad total de cuadrados mágicos encontrados.
```hs
numerosDisponibles = [1..n²]
esUnCuadradoValido = 1 | 0 -- depende si lo es ono
```
$$
\text{MagiCuadrados}(matriz, i, j, numDisponibles) = \\
\begin{cases}
\sum\limits_{c \in numDisponibles} MagiCuadrados(asig(matriz, i, j, c), i, j+1, numDisponibles \setminus \{c\}) & \text{si } j < n \\
\sum\limits_{c \in numDisponibles} MagiCuadrados(asig(matriz, i, j, c), i+1, 1, numDisponibles \setminus \{c\}) & \text{si } j = n \\ 
esUnCuadradoValido(matriz) & \text{si } numDisponibles = \emptyset
\end{cases}
$$

3. Demostrar que el árbol de backtracking tiene O((n²)!) nodos en el peor caso.

Esto se puede demostrar de menera sencilla observando la naturaleza del problema. Nuestro objetivo es ubicar $n²$ números distintos (del 1 al $n²$) en $n²$ celdas vacias, sin repetir ningún valor.

Cada posible asignación completa del tablero equivale a una **permutación** única de esos $n²$ elemenots. Por principios básicos de combinatoria, la cantidad total de formulas que podemos ordenar o permutar $n²$ elementos es exactamente $(n²)!$.

Dado que el árbol de *backtraking* debe generar y explorar todas estas permutaciones posibles para encontrar cuáles suman el valor mágico, su tamaño y complejidad asinótica estan directamente acotados por $O((n²)!)$.

4. Considere la siguiente poda al árbol de backtraking: al momento de elegir el valor de una nueva posición, verificar que la suma parical de la fila no supere el número mágico. Verificar también que la suma parcial de las columnas no supere el número mágico. Introducir las podas al algoritmo e implementarlo en computadora. ¿Puede mejorar estas podas?

5. Demostrar que el número de un cuadrado mágico de orden n es siempre $\frac{n³ + n}{2}$. Adaptar la poda del algoritmo anterior del ítem anterior para que tenga en cuenta esta nueva información. Modificar la implementación y comparar los tiempos obtenidos para calcular la cantidad de cuadrados mágicos.

Un cuadrado mágico de orden $n$ contiene todos los números enteros desde el 1 hasta $n^2$. La suma de todos estos números se calcula con la fórmula de la serie aritmética:

$$
S_{\text{total}} = \frac{\text{máximo}(\text{máximo}+1)}{2}
$$

Reemplazamos el máximo por su valor real, $n^2$:

$$
S_{\text{total}} = \frac{n^2(n^2+1)}{2}
$$

Como el cuadrado tiene n filas y cada una suma el número mágico $M$, entonces:

$$
S_{\text{total}} = n \cdot M
$$

Por lo tanto:

$$
M = \frac{n(n^2+1)}{2}
$$

# MaxiSubconjunto
Dada una matriz simétrica $M$ de $n \times n$ naturales y un número $k$, queremos encontrar un subconjunto $I$ de $\{1, \cdots, n\}$ con $|I| = k$ que maximice $\sum_{i,j \in I} M_{i,j}$. Por ejemplo, si $k = 3$ y:

$$M = \begin{pmatrix}
0 & 10 & 10 & 1 \\
10 & 0 & 5 & 2 \\
10 & 5 & 0 & 1 \\
1 & 2 & 1 & 0
\end{pmatrix}
$$
Entonces $I = \{1, 2, 3\}$ es una solución óptima.

1. Diseñar un algorito de *backtraking* para resolver este problema, indicando claramente cómo se codifica una solución candidata, cuáles soluciones son válida y qué valor tienen, qué es una solución parcial y cómo se extiende cada solución parcial.

2. Calcular la complejidad temporal y espacial del mismo.

3.  Propopner una poda por optimalidad y mostrar que es correcta.
---
1. Usando índices entre $0$ y $n - 1$ como hace python, en vez de $1$ al $n$ como dice el enunciado, un algoritmo de backtracking para resolver este problema es:

```python
def main(M: list[list[int]], k: int) -> list[int] | None:
    n = len(M)
    
    def value(I: list[int]) -> int:
        suma = 0
        for i in I:
            for j in I:
                # Sumamos todas las permutaciones de los índices en I
                suma += M[i][j]
        return suma
    
    def backtracking(I: list[int], i: int) -> list[int] | None:
        # Caso base: Ya seleccionamos k elementos
        if len(I) == k:
            return I
        
        # Caso base: No quedan más elementos por explorar
        if i == n:
            return None
            
        # Opción 1: Incluyo el elemento i
        con_i = backtracking(I + [i], i + 1)
        # Opción 2: No incluyo el elemento i
        sin_i = backtracking(I, i + 1)
        
        # Filtramos los caminos que no llegaron a una solución válida
        if con_i is None:
            return sin_i
        if sin_i is None:
            return con_i
            
        # Nos quedamos con la opción que maximiza el valor
        if value(con_i) > value(sin_i):
            return con_i
        else:
            return sin_i
    
    return backtracking([], 0)
```

La semántica de g es g(I, i) es la mejor forma de completar I, usando sólo números mayores o iguales a i. Acá I es una sub-solución, es decir, una lista de a lo sumo k índices de M. Por ejemplo, si $k = 3$, $I=[1]$ es una subsolución, como también lo es $I=[0,1,2]$. Extender una sub-solución a otra sub-solución es agregar números a la lista. Una sub-solución I es solución cuando $len(I) = K$, y ahí tiene valor $\text{value}(I)$.

2. 
Podemos acotar la complejidad del algoritmo anterior tomando como peor caso $k = n$. Esto porque mientras más bajo el $k$, más temprano llegamos a $\text{len}(I)= k$ y terminamos. Luego, haciendo k lo más grende posible (n) hacemos que el algoritmo explore la mayor cantidad de casos posibles. De hecho, como $\text{len}(I) \leq i$, y $i \leq n$, al tener $\text{len}(I) = k = n$, debemos tener $i = n$, y tenemos una sola guarda: `if i == n: return None`.

Sabiendo eso, el comportamiento del algoritmo es relativamente simple: Cada vez que hacemos dos llamadas, con $i+1$, y cuando `i = n`, el árbol termina. Luego tenemos exactamente $2^n$ vértices en nuestro árbol de recursión, y al hacer $O(n)$ trabajo en cada vértice, la complejidad temporal asintótica es el en peor caso $O(n \cdot 2^n)$.

Como máximo vamos a tener n niveles de stack, y en cada nivel de stack vamos a tener una lista ($I$ o $I + 1$), de tamaño a lo sumo $n$. Luego usamos $O(n)$ para copiar la lista en cada paso. Por lo tanto, la complejidad espacial es $O(n^2)$.

# Palabras en cadena

Dada una cadena de letras sin espacios o puntos queremos analizar si se puede subdividir de forma de obtener todas palabras válidas. Suponiendo que se tiene una función `palabra` que verifica si una cadena $c$ de letras es una palabra en $O(|c|)$.
1. Dar una función recursiva que resuelva el problema.
2. Calcular una cota superior para la complejidad. Ayuda: calcular cantidad de llamadas a `palabra`.
3. Demostrar que el algoritmo es correcto.

---
1.

$$
\text{separar}(S) = 
\begin{cases}
    \text{True} & \text{si } |S| = 0  \\
    \bigvee_{k=1}^{|S|} (palabra(S[0:k]) \land separar(S[k:])) & \text{si } |S| > 0
\end{cases}
$$

2. 
Analicemos la complejidad, en principio no sabemos cuanto cuesta palabra(...), así que lo que vamos a hacer es contar la cantidad de llamados que tiene la función, tenemos la siguiente recurrencia:

$$
T(n) = \sum_{k=0}^{n-1} T(k) + O(n)
$$

Donde $O(n)$ es el costo de llamar a la función palabra(S[:k]) para todo $k \in [1, n]$. Vamos a usar el siguiente truco para resolver la recurrencia:

$$
T(n-1) = \sum_{k=0}^{n-2} T(k) + C(n-1)
$$

Si le restamos esto a la primer recurrencia tenemos:

$$
T(n) - T(n-1) = T(n-1) + C(n) - C(n-1)
$$

$$
T(n) = 2T(n-1) + C
$$

Donde $C = C(n) - C(n-1)$.

Si expandimos esta recursión nos queda un árbol binario totalmente balanceado. Ahora queremos evaluar el costo computacional que es la suma de todos los nodos con su costo. El costo de cada nodo es constante así que solo necesitamos contar la cantidad de nodos.

$$
\sum_{i=0}^{n} 2^i = \frac{2^{n+1} - 1}{2 - 1} = 2^{n+1} - 1
$$

Por lo tanto, la complejidad temporal es $O(2^n)$.

3. 
Vamos a hacer inducción sobre la longitud de la cadena n. Queremos probar que separar(S) devuelve True si y solo si S se puede subdividir de forma de obtener todas palabras válidas.

Hacemos inducción fuerte sobre la longitud de la cadena S. Esto significa que el predicado debe ser válido para todos los casos base y que para cualquier caso mayor a los casos base, el predicado debe ser válido si es válido para todos los casos anteriores.

El predicado va a ser:

`Para toda cadena S de tamaño n vale que separar(S) nos dice si hay una relacion de válida o no.`

Caso base: P(0), tenemos que probar que vale para toda cadena de longitud 0. Como no podemos subdividr más la cadena deberíamos devolver `True`que es exáctamente lo que devuelve la función si resivimos una cadena de longitud 0.

# Árboles binarios de búsqueda óptimos

Dado un conjunto de elementos de $[n] = \{1, ..., n\}$, y una función $f: [n] \to \mathbb{N}$ que nos da la frecuencia de acceso a dichos elementos, decimos que $A$ es un árbol de búsqueda óptimo si este minimiza el costo de todos los accesos dados por $f$.

1. Escribir una función recursiva que devuelva el costo de acceder a todos los elementos usando $f$.
2. Dar una cota superior para la complejidad. Ayuda: pasar de la función recursiva a una
recurrencia que solo dependa del tamaño de la entrada.
3. Probar que el algoritmo es correcto.
---
1. 

$$
AO(i,j) = 
\begin{cases}
    0 & \text{si } i > j \\
    \sum_{k=i}^{j} f(k) + \min_{k=i}^{j} (AO(i,k-1) + AO(k+1,j))  & \text{si } i \leq j
\end{cases}
$$

El costo óptimo de armar un árbol con nodos del $i$ al $j$ es: **la suma de las frecuencias** de todos esos nodos, más el costo óptimo de armar el subárbol izquierdo y el subárbol derecho.

2.
La función anterior representa la siguiente recursión:

$$
T(n) = \sum_{i=1}^{n} T(i-1) + T(n-i) + O(n)
$$

Notemos que cada parte de la suma se repite ($k = n - (n-k)$), es decir que cada término $T(k)$ aparece dos veces en la suma. Por lo tanto, podemos reescribir la recurrencia como:

$$
T(n) = 2 \sum_{k=0}^{n-1} T(k) + O(n)
$$

Restando $T(n) - T(n-1)$ obtenemos:

$$
T(n) - T(n-1) = 2T(n-1) + O(1)
$$

$$
T(n) = 3T(n-1) + O(1)
$$

De la misma manera que el ejercicio anterior podemos concluir que la complejidad temporal es $O(3^n)$.

3. 
Veamos que nuestra función recursiva consigue un costo de un ABB de menor costo. La función tiene dos parámetros y nos gustaría hacer inducción sobre el tamaño de la lista, para esto podemos usar como parámetro para la función de los dos índices, es decir 