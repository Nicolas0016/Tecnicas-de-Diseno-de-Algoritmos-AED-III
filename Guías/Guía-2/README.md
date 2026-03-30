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















