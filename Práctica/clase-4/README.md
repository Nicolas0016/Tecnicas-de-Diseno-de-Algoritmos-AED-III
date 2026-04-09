Sea M una matriz de tamaño $(n+1) \times(n+1)$ inicializada en $-\infty$.

Algoritmo:

```
M[0][0] <- 0
Para d <- 1...n:
    Para a <- 0...n:
        ans <- M[d-1][a] # Tomo el valor de la fila anterior en la misma columna
        Si (a > 0):
            ans <- máx(ans, M[d-1][a-1] - p[d]) # Tomo el valor de la fila anterior en la columna anterior
        Si (a < n):
            ans <- máx(ans, M[d-1][a+1] + p[d]) # Tomo el valor de la fila anterior en la columna siguiente
        M[d][a] <- ans
Devolver M[n][0]
```

Para p = (3,2,5,6) y n = 4

| d | a=0 | a=1 | a=2 | a=3 | a=4 |
|---|-----|-----|-----|-----|-----|
| 0 | 0   | -∞  | -∞  | -∞  | -∞  |
| 1 | 0   | -3   | -∞  | -∞  | -∞  |
| 2 | 0   | -2   | -5   | -∞  | -∞  |
| 3 | 3   | 0   | -5   | -10   | -∞  |
| 4 | 6   | 1   | -4   | -10   | -∞  |

Devuelve M[4][0] = 6 (Compro los dos primeros días dos ateroides a precio de 2 y 3, luego vendo 1 a 5 pesos y al último día vendo el restante a 6 pesos, obteniendo una ganacia de 6).

> No necesitamos tener los resultados de los últimos n días, con tener los del día anterior ya es suficente.

Algoritmo:

```
M[0][0] <- 0 
Para d <- 1...n:
    Sea prev <- (d-1) mód 2, curr <- d mód 2
    Para a <- 0...n:
        ans <- M[prev][a]
        Si (a > 0):
            ans <- máx(ans, M[prev][a-1] - p[d-1])
        Si (a < n):
            ans <- máx(ans, M[prev][a+1] + p[d-1])
        M[curr][a] <- ans
Devolver M[n mód 2][0]
```
Ahora la matriz se ve así:

Para p = (3,2,5,6) y n = 4

d = 0 (inicialización)
| d | a=0 | a=1 | a=2 | a=3 | a=4 |
|---|-----|-----|-----|-----|-----|
| 0 | 0   | -∞  | -∞  | -∞  | -∞  |

d = 1 (p[0] = 3)
prev = 0, curr = 1.

a=0: max(M[0][0]=0, -, M[0][1]+3=-∞) = 0

a=1: max(M[0][1]=-∞, M[0][0]-3=-3, M[0][2]+3=-∞) = -3


| d | a=0 | a=1 | a=2 | a=3 | a=4 |
|---|-----|-----|-----|-----|-----|
| 0 | 0   | -∞  | -∞  | -∞  | -∞  |
| 1 | 0   | -3   | -∞  | -∞  | -∞  |


d = 2 (p[1] = 2 )
prev =  1, curr = 0 (reciclamos la fila 0)


| d | a=0 | a=1 | a=2 | a=3 | a=4 |
|---|-----|-----|-----|-----|-----|
| 2 | 0   | -2  | -5  | -∞  | -∞  |
| 1 | 0   | -3   | -∞  | -∞  | -∞  |


d = 3 (p[2] = 5)
prev = 0, curr = 1 (reciclamos la fila 1)

| d | a=0 | a=1 | a=2 | a=3 | a=4 |
|---|-----|-----|-----|-----|-----|
| 3 | 3   | 0   | -5   | -10   | -∞  |
| 2 | 0   | -2  | -5  | -∞  | -∞  |


d = 4 (p[3] = 6)
prev = 1, curr = 0 (reciclamos la fila 0)

| d | a=0 | a=1 | a=2 | a=3 | a=4 |
|---|-----|-----|-----|-----|-----|
| 4 | 6   | 1   | -4   | -10   | -∞  |
| 3 | 3   | 0   | -5   | -10   | -∞  |

Resultado final:
M[n mod 2][0] = M[0][0] = 6

¿Cómo se ve la matriz en memoria?
Solo guardamos 2 filas. Al final el algoritmo:
| Fila | a=0 | a=1 | a=2 | a=3 | a=4 |
|------|-----|-----|-----|-----|-----|
| Fila 0 (curr)    | 6   | 1   | -4  | -10 | -∞  |
| Fila 1 (prev)    | 3   | 0   | -5  | -10 | -∞  |


# Mi Buenos Aires Crecido
Sasha vive en San Nicolás hace mucho tiempo, y tiene una eterna discusión con su vecina Tasha. Sasha dice que si se mira el horizonte de izquierda a derecha terminando en el obelisco, los edificios están ordenados en un perfil principalmente ascendente para que la altura del obelisco sea más impresionante. Tasha le dice que con las nuevas torres que se construyeron en la zona eso ya no es verdad, y que en realidad ahora menos de la mitad del ancho del horizonte está en orden ascendente.


Entrada: Recibimos una lista de edificios ordenados de izquierda a derecha con dos datos para cada uno, el ancho de cada edificio y por otro lado el alto

Buscamos la longitud de la máxima subsecuencia ascendente, es decir, la subsecuencia creciente que ocupe el mayor espacio horizontal.

Una posible respuesta 

Sea alto(-1) = 0

$$
f(i, ult) = 
\begin{cases}
    0 & \text{si } i \geq n  \\
    f(i+1, ult) & \text{si } alto[i] \leq alto[ult] \\
    max(f(i+1, ult), ancho[i] + f(i+1, i)) & \text{En cualquier otro caso}
\end{cases}
$$
Donde ult es el índice del último edificio incluido en la subsecuencia. 

> Hay una versión con la misma complejidad temporal pero con complejidad espacial $O(n)$ ¿Como podriamos adaptar nuestra nueva solución?

Si queremos que nuestra memoria sea $O(n)$ entonces nuestra cantidad de estados debe ser $O(n)$.

Funcion recursiva 