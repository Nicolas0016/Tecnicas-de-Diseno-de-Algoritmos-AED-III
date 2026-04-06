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


 
