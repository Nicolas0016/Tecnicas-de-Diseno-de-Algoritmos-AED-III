# Backtracking
+ ¿Qué es un algoritmo de fuerza bruta?
+ ¿Qué es un algoritmo de backtracking?
+ ¿Soluciónes candidatas? ¿Soluciones parciales?
+ ¿Poda por factalidad? ¿Poda por optimalidad?

> Respuesta: 
+ Un algoritmo de **fuerza bruta** es un algoritmo que explora todas las posibles soluciones a un problema.
+ Un algoritmo de **backtracking** es un algoritmo que explora todas las posibles soluciones a un problema, pero que poda las soluciones que no son válidas.
+ Una **solución candidata** es una solución parcial que se está evaluando.
+ Una **solución parcial** es una solución que no es completa, pero que se está evaluando.
+ La **poda por factalidad** es una poda que se realiza cuando una solución parcial no es válida.
+ La **poda por optimalidad** es una poda que se realiza cuando una solución parcial no es óptima.

# Ejercicio 1 - Palabras en cadena
Dada una cadena de letras sin espacios o puntos queremos analizar si se puede subdividir de forma de obtener palabras. Suponiendo que se tiene una función `palabra :: [a, z] -> bool` que verifica si una cadena de letras es una palabra.

1. Dar una función recursiva que resuelva el problema. 
2. Calcular la cota superior de complejidad.
3. Demostrar que el algoritmo es correcto. 

$$
separar(S) = 
\begin{cases} 
{True} & \text{si } S \ \text{es vacía} \\
\bigcup_{i=1}^{|S|} \{ \text{palabra}(S[:i]) \land separar(S[i:]) \} & \text{si } S \ \text{no es vacía} \\
\end{cases}
$$

2. Analisis de complejidad, en primer lugar como no sabemos cual es la complejidad de `palabra` entonces lo voy a dejar de lado por ahora.
Asi que debería hacer es contar la cantidad de veces que se llamados de la función `separar`.

$$T(n) = \sum_{n-1}^{k=0} T(k) + O(n)$$

Donde $O(n)$ viene de llamar a `palabra(s[:i])` para todo $i \in [1, |S|]$. Vamos a usar un truco que es abrir el O con una constante $C > 0$ y comparar con la recurrencia de un valor menos.

$$T(n-1) = \sum_{k=0}^{n-2}{T(k) + C(n-1)}$$

Si a esto le restamos esto a la primer recurrencia obtenemos

$$T(n) - T(n-1) = T(n-1) + C(n) - C(n-1)$$

$$T(n) = 2T(n-1) + C$$

Si expandimos esta recursión nos queda un árbol binario totalmente balanceado. Ahora queremos evaluar el costo computacional que es la suma de todos los nodos con su costo. En este caso el costo es constante así que solo necesitamos calcular la cantidad de nodos. Esto nos da la siguiente complejidad, usando la fórmula geométrica.

$$\sum_{i=0}^{n} 2^i = \frac{2^{n+1} - 1}{2 - 1} = 2^{n+1} - 1 = O(2^n)$$

Osea que una cota que podemos dar es:
$$O(costo(palabra) * 2^n)$$
3. Vamos a hacer inducción sobre la longitud de la cadena $n$. Queremos probar que $separar(S)$ computa correctamente si podemos separar $S$ en palabras o no para toda cadena $S$ de tamaño $n$.
Hacemos inducción fuerte sobre la longitud de la cadena S. Esto significa que nuestro predicado va a valer para `todos` los elementos de tamaño más chico que el anterior. El predicado es:

$P(n) = \text{Para toda cadena S de tamaño n vale que separar(S) hay una separación válida o no}$

Caso base: $P(0)$ es verdadero porque la cadena vacía se puede separar en 0 palabras.

Caso inductivo: Como estamos haciendo inducción fuerte / inducción global, si vale $P(n)$ para todo $n \leq j$ entonces vale $P(j+1)$. Es decir podemos asumir que vale **toda** cadena de tamaño $n \leq j$ y queremos ver entonces que pasa con una cadena $n = j + 1$ elementos. Como tenemos que j + 1 > 0, entonces si evaluamos la función recursiva caemos en el segundo caso, donde separamos S en dos cadenas de tamaño $k$ y $n - k$ para $1 \leq k \leq n$, podemos de vuelva separar en dos casos, donde S era una subcadena subdividible en el cual deberíamos porder devolver True y en caso de S no ser una cadena subdivisible:

1. Si $S$ es subdivisible en particular existe un k que da el primer prefijo de la subdivisión, entonces $palabra(s[:k])$, como vale nuestra HI y $|S[k:]| < |S| = j+1$ entonces $separar(S[k:])$ devuelve `True` a la subdivisión del sufijo de S y por lo tanto tenemos un $\land$ de dos True que da True.

2. El anterior fue el caso fácil, tenemos que ver si pasa si $S$ no admite una subdivisión en palabras, esto significa que dado el prefijo, o bien es invalido o el sufijo lo es. Veamos que nuestra función es correcta con respecto a esto. Dado un k, si $palabra(S[:k])$ es False listo no tenemos que hacer nada, pero si la palabra $palabra(S[:k]) = \text{True}$, tiene que ser $separar(S[k:]) = \text{False}$, porque como sabemos que estamos en un caso donde S no tiene ninguna subdivisión válida y $separar(S[k:])$ dio True y como sabemos que por HI separar funciona correctamente cadenas de tamaño $\leq j $ tiene que ser False.
# Ejercicio 2 - Árboles binarios de búsqueda óptimos

Dado un conjunto de elementos de $[n] = \{1, \cdots, n\}$ y una funcíon $f:[n] -> \mathbb{N}$ que nos da la frecuencia de acceso a dichos elementos, decimos que `A` es un arbol binario de busqueda óptimo si este minimiza el costo de todos los accesos dados por `f`.

1. Escribir una función recursiva que devuelva el costo de acceder a todos los elementos de un `AB` dado usando `f`.

> El costo de acceder a un elemento es el producto de la frecuencia de acceso por el nivel del elemento. El nivel de la raíz es 1.

2. Escribir un algoritmo backtraking que encuentre el AB óptimo para un `f` dado.

3. Dar una cota superior para la complejidad.

4. Probar que el algoritmo es correcto.


# Ejercicio 3 - Dobra 
Dobra se encuentra con muchas palabras en su vida, como es una persona particular la mayoría de estas no le gustan (comunistas, socialistas, gays, más de dos generos, etc). Para comenzar empezó a inverntar palabras más agradables. Dobra crea palabras nuevas escribiendo una cadena de caracteres que considera buena, luego borra los caracteres que peor le caen y los remplaza con _. Luego para mejorar su vida intenta reemplazar estos guiones bajos con letras más aceptables intentando crear palabras más lindas.

Dobra considera una palabra como buena si no contiene 3 vocales consecutivas, 3 consonantes consecutivas y al menos contiene una E. Dobra nos pide conseguir todas las posibles palabras válidas que se pueden armar a partir de una cadena con comodines.

1. Mostrar alguna solución candidata posible y alguna solución parcial.
2. Proponer una función recursiva y estimar su complejidad.
3. Probar que la función o programa es correcto.
4. Proponer al menos una poda por factibilidad.
5. Si 2. no tiene una cota superior $O(3^n)$ para la complejidad, analizar el caso donde se separa la recursión en tener o no una letra E y ver si mejora la misma.

> La idea es yo de doy una cadena con comodines y vos me devolves todas las palabras válidas que se pueden armar a partir de esa cadena. Por ejemplo si la cadena es `a_b` y las palabras válidas son `aba`, `aca`, `ada`, `aea`, `afa`, `aga`, `aha`, `aja`, `aka`, `ala`, `ama`, `ana`, `apa`, `ara`, `asa`, `ata`, `ava`, `axa`, `aya`, `aza`, `eba`, `eca`, `eda`, `efa`, `ega`, `eha`, `eja`, `eka`, `ela`, `ema`, `ena`, `epa`, `era`, `esa`, `eta`, `eva`, `exa`, `eya`, `eza`, `iba`, `ica`, `ida`, `ifa`, `iga`, `iha`, `ija`, `ika`, `ila`, `ima`, `ina`, `ipa`, `ira`, `isa`, `ita`, `iva`, `ixa`, `iya`, `iza`, `oba`, `oca`, `oda`, `ofa`, `oga`, `oha`, `oja`, `oka`, `ola`, `oma`, `ona`, `opa`, `ora`, `osa`, `ota`, `ova`, `oxa`, `oya`, `oza`, `uba`, `uca`, `uda`, `ufa`, `uga`, `uha`, `uja`, `uka`, `ula`, `uma`, `una`, `upa`, `ura`, `usa`, `uta`, `uva`, `uxa`, `uya`, `uza`. 

> Esto si cumple lo que el PJ considera palabras válidas. Por ejemplo `aaa` no es una palabra válida porque tiene 3 vocales consecutivas. `bbb` no es una palabra válida porque tiene 3 consonantes consecutivas. `aeb` es una palabra válida porque tiene una E y no tiene 3 vocales o consonantes consecutivas. `a_b` no es una palabra válida porque tiene un comodín. 


> una solución candidata es `aba` y una solución parcial es `a_b`.

