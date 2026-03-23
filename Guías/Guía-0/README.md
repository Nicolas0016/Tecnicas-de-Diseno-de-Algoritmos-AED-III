# Solución Guía 0

## 1. Probar por inducción:

### a) $1 + 2 + \dots + n = \frac{n(n+1)}{2},  \forall n \geq 1$

> Respuesta

Reescribimos la proposición:
$1 + 2 + \dots + n = \sum_{i=1}^{n} i$

Luego tengo que ver que $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$

Caso base: $n=1$

$$
\begin{cases}
\sum_{i=1}^{1} i = 1 \\
& \text{Se verifica} \\
\frac{n(n+1)}{2} = \frac{1(1+1)}{2} = \frac{1(2)}{2} = 1 
\end{cases}
$$

Hipótesis inductiva: Asumimos que la proposición es cierta para algún $k \geq 1$

$$
P(k): \sum_{i=1}^{k} i = \frac{k(k+1)}{2}
$$

Tesis inductiva: Debemos demostrar que la proposición es cierta para $k+1$

$$
P(k+1): \sum_{i=1}^{k+1} i = \frac{(k+1)(k+2)}{2}
$$

Demostración:

$$
\begin{aligned}
\sum_{i=1}^{k+1} i = \frac{(k + 1)(k+2)}{2} \\
\sum_{i=1}^{k} i + (k+1) = \frac{(k + 1)(k+2)}{2} \\
\frac{k(k+1)}{2} + (k+1) = \frac{(k + 1)(k+2)}{2} \\
\frac{k(k+1) + 2(k+1)}{2} = \frac{(k + 1)(k+2)}{2} \\
\frac{(k+1)(k+2)}{2} = \frac{(k + 1)(k+2)}{2}
\end{aligned}
$$

>Por lo tanto, la proposición es cierta para todo $n \geq 1$.

### b) $1 + 3 + 5 + \dots + (2n-1) = n^2, \forall n \geq 1$

> Respuesta
Reescribimos la proposición:

$1 + 3 + 5 + \dots + (2n-1) = \sum_{i=1}^{n} (2i-1)$

Luego tengo que ver que $\sum_{i=1}^{n} (2i-1) = n^2$

Caso base: $n=1$

$$
\begin{cases}
\sum_{i=1}^{1} (2i-1) = 2(1)-1 = 1 \\
& \text{Se verifica} \\
n^2 = 1^2 = 1
\end{cases}
$$

Hipótesis inductiva: Asumimos que la proposición es cierta para algún $k \geq 1$

$$P(k): \sum_{i=1}^{k} (2i-1) = k^2$$


Tesis inductiva: Debemos demostrar que la proposición es cierta para $k+1$

$$P(k + 1): \sum_{i=1}^{k+1} (2i-1) = (k+1)^2$$

Demostración:

$$
\begin{aligned}
\sum_{i=1}^{k+1} (2i-1) = \frac{(k + 1)(k+2)}{2} \\
\sum_{i=1}^{k} (2i-1) + (k+1) = \frac{(k + 1)(k+2)}{2} \\
\frac{k(k+1)}{2} + (k+1) = \frac{(k + 1)(k+2)}{2} \\
\frac{k(k+1) + 2(k+1)}{2} = \frac{(k + 1)(k+2)}{2} \\
\frac{(k+1)(k+2)}{2} = \frac{(k + 1)(k+2)}{2}
\end{aligned}
$$

>Por lo tanto, la proposición es cierta para todo $n \geq 1$.

### c) $1 + 2^2 + 3^2 + \dots + n^2 = \frac{n(n+1)(2n+1)}{6}, \forall n \geq 1$

>Respuesta

Reescribimos la proposición:

$1 + 2^2 + 3^2 + \dots + n^2 = \sum_{i=1}^{n} i^2$

Luego tengo que ver que $\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}$

Caso base: $n=1$

$$
\begin{cases}
\sum_{i=1}^{1} i^2 = 1^2 = 1 \\
& \text{Se verifica} \\
\frac{n(n+1)(2n+1)}{6} = \frac{1(1+1)(2(1)+1)}{6} = \frac{1(2)(3)}{6} = \frac{6}{6} = 1
\end{cases}
$$

Hipótesis inductiva: Asumimos que la proposición es cierta para algún $k \geq 1$

$$P(k): \sum_{i=1}^{k} i^2 = \frac{k(k+1)(2k+1)}{6}$$

Tesis inductiva: Debemos demostrar que la proposición es cierta para $k+1$

$$P(k + 1): \sum_{i=1}^{k+1} i^2 = \frac{(k+1)(k+2)(2(k+1)+1)}{6}$$

Demostración:

$$
\begin{aligned}
\sum_{i=1}^{k+1} i^2 = \frac{(k+1)(k+2)(2(k+1)+1)}{6} \\
\sum_{i=1}^{k} i^2 + (k+1)^2 = \frac{(k+1)(k+2)(2k+3)}{6} \\
\frac{k(k+1)(2k+1)}{6} + (k+1)^2 = \frac{(k+1)(k+2)(2k+3)}{6} \\
\frac{k(k+1)(2k+1) + 6(k+1)^2}{6} = \frac{(k+1)(k+2)(2k+3)}{6} \\
\frac{(k+1)(k(2k+1) + 6(k+1))}{6} = \frac{(k+1)(k+2)(2k+3)}{6} \\
\frac{(k+1)(2k^2 + k + 6k + 6)}{6} = \frac{(k+1)(k+2)(2k+3)}{6} \\
\frac{(k+1)(2k^2 + 7k + 6)}{6} = \frac{(k+1)(k+2)(2k+3)}{6} \\
\frac{(k+1)(k+2)(2k+3)}{6} = \frac{(k+1)(k+2)(2k+3)}{6}
\end{aligned}
$$

>Por lo tanto, la proposición es cierta para todo $n \geq 1$.

### d) $-1 + 2² -3² + \dots + (-1)^n n² = (-1)^n \frac{n(n+1)}{2}, \forall n \geq 1$

>Respuesta

Reescribimos la proposición:
$-1 + 2² -3² + \dots + (-1)^n n² = \sum_{i=1}^{n} (-1)^i i²$

Luego tengo que ver que $\sum_{i=1}^{n} (-1)^i i² = (-1)^n \frac{n(n+1)}{2}$

Caso base: $n=1$

$$
\begin{cases}
\sum_{i=1}^{1} (-1)^i i² = (-1)^1 1² = -1 \\
& \text{Se verifica} \\
(-1)^n \frac{n(n+1)}{2} = (-1)^1 \frac{1(1+1)}{2} = -1 \frac{2}{2} = -1
\end{cases}
$$

Hipótesis inductiva: Asumimos que la proposición es cierta para algún $k \geq 1$

$$P(k): \sum_{i=1}^{k} (-1)^i i² = (-1)^k \frac{k(k+1)}{2}$$

Tesis inductiva: Debemos demostrar que la proposición es cierta para $k+1$

$$P(k + 1): \sum_{i=1}^{k+1} (-1)^i i² = (-1)^{k+1} \frac{(k+1)(k+2)}{2}$$

Demostración:

$$
\begin{aligned}
\sum_{i=1}^{k+1} (-1)^i i² = (-1)^{k+1} \frac{(k+1)(k+2)}{2} \\
\sum_{i=1}^{k} (-1)^i i² + (-1)^{k+1} (k+1)² = (-1)^{k+1} \frac{(k+1)(k+2)}{2} \\
(-1)^k \frac{k(k+1)}{2} + (-1)^{k+1} (k+1)² = (-1)^{k+1} \frac{(k+1)(k+2)}{2} \\
\frac{(-1)^k k(k+1) + 2(-1)^{k+1} (k+1)²}{2} = (-1)^{k+1} \frac{(k+1)(k+2)}{2} \\
\frac{(-1)^{k+1} (k(k+1) + 2(k+1)²)}{2} = (-1)^{k+1} \frac{(k+1)(k+2)}{2} \\
\frac{(-1)^{k+1} (k+1)(k + 2(k+1))}{2} = (-1)^{k+1} \frac{(k+1)(k+2)}{2} \\
\frac{(-1)^{k+1} (k+1)(3k+2)}{2} = (-1)^{k+1} \frac{(k+1)(k+2)}{2}
\end{aligned}
$$

>Por lo tanto, la proposición es cierta para todo $n \geq 1$.

### e) $(1+2+3+\dots+n)² = 1³+2³+3³+\dots+n³, \forall n \geq 1$

>Respuesta

Reescribimos la proposición:
> Lo puedo reescribir como la serie geometrica de los primeros n numeros naturales al cuadrado

$(1+2+3+\dots+n)² = \sum_{i=1}^{n} i³$

Luego tengo que ver que $\sum_{i=1}^{n} i³ = (\frac{n(n+1)}{2})²$

Caso base: $n=1$

$$
\begin{cases}
\sum_{i=1}^{1} i³ = 1³ = 1 \\
& \text{Se verifica} \\
(\frac{n(n+1)}{2})² = (\frac{1(1+1)}{2})² = (\frac{2}{2})² = 1² = 1
\end{cases}
$$

Hipótesis inductiva: Asumimos que la proposición es cierta para algún $k \geq 1$
$$P(k): \sum_{i=1}^{k} i³ = (\frac{k(k+1)}{2})²$$

Tesis inductiva: Debemos demostrar que la proposición es cierta para $k+1$

$$P(k + 1): \sum_{i=1}^{k+1} i³ = (\frac{(k+1)(k+2)}{2})²$$

Demostración:

$$
\begin{aligned}
\sum_{i=1}^{k+1} i³ = (\frac{(k+1)(k+2)}{2})² \\
\sum_{i=1}^{k} i³ + (k+1)³ = (\frac{(k+1)(k+2)}{2})² \\
(\frac{k(k+1)}{2})² + (k+1)³ = (\frac{(k+1)(k+2)}{2})² \\
\frac{k²(k+1)²}{4} + (k+1)³ = (\frac{(k+1)(k+2)}{2})² \\
\frac{k²(k+1)² + 4(k+1)³}{4} = (\frac{(k+1)(k+2)}{2})² \\
\frac{(k+1)²(k² + 4(k+1))}{4} = (\frac{(k+1)(k+2)}{2})² \\
\frac{(k+1)²(k² + 4k + 4)}{4} = (\frac{(k+1)(k+2)}{2})² \\
\frac{(k+1)²(k+2)²}{4} = (\frac{(k+1)(k+2)}{2})² \\
(\frac{(k+1)(k+2)}{2})² = (\frac{(k+1)(k+2)}{2})²
\end{aligned}
$$

>Por lo tanto, la proposición es cierta para todo $n \geq 1$.

### f) $1\cdot1! + 2\cdot2! + 3\cdot3! + \dots + n\cdot n! = (n+1)! - 1, \forall n \geq 1$

>Respuesta

Reescribimos la proposición:
$$1\cdot1! + 2\cdot2! + 3\cdot3! + \dots + n\cdot n! = \sum_{i=1}^{n} i\cdot i!$$

Luego tengo que ver que $\sum_{i=1}^{n} i\cdot i! = (n+1)! - 1$

Caso base: $n=1$

$$
\begin{cases}
\sum_{i=1}^{1} i\cdot i! = 1\cdot1! = 1 \\
& \text{Se verifica} \\
(n+1)! - 1 = (1+1)! - 1 = 2! - 1 = 2 - 1 = 1
\end{cases}
$$

Hipótesis inductiva: Asumimos que la proposición es cierta para algún $k \geq 1$
$$P(k): \sum_{i=1}^{k} i\cdot i! = (k+1)! - 1$$

Tesis inductiva: Debemos demostrar que la proposición es cierta para $k+1$

$$P(k + 1): \sum_{i=1}^{k+1} i\cdot i! = (k+2)! - 1$$

Demostración:

$$
\begin{aligned}
\sum_{i=1}^{k+1} i\cdot i! = (k+2)! - 1 \\
\sum_{i=1}^{k} i\cdot i! + (k+1)\cdot(k+1)! = (k+2)! - 1 \\
(k+1)! - 1 + (k+1)\cdot(k+1)! = (k+2)! - 1 \\
(k+1)! (1 + k+1) - 1 = (k+2)! - 1 \\
(k+1)! (k+2) - 1 = (k+2)! - 1 \\
(k+2)! - 1 = (k+2)! - 1
\end{aligned}
$$

>Por lo tanto, la proposición es cierta para todo $n \geq 1$.

## 2. Encontrar una fórmula 

Encontrar una fórmula para la siguiente suma y demostrar por inducción: $1 + 2 + 2² + \dots + 2^{n}$.

>Respuesta

Reescribimos la proposición:

$$2⁰ + 2¹ + 2² + \dots + 2^{n}= \sum_{i=0}^{n} 2^{i}$$

Calculo los primeros términos:

$\boxed{n=0}: 2⁰ = 1$

$\boxed{n=1}: 2⁰ + 2¹ = 1 + 2 = 3$

$\boxed{n=2}: 2⁰ + 2¹ + 2² = 1 + 2 + 4 = 7$

$\boxed{n=3}: 2⁰ + 2¹ + 2² + 2³ = 1 + 2 + 4 + 8 = 15$

Observo que los resultados son de la forma $2^{n+1} - 1$

Luego tengo que ver que $\sum_{i=0}^{n} 2^{i} = 2^{n+1} - 1$

Caso base: $n=0$

$$
\begin{cases}
\sum_{i=0}^{0} 2^{i} = 2^{0} = 1 \\
& \text{Se verifica} \\
2^{0+1} - 1 = 2^{1} - 1 = 2 - 1 = 1
\end{cases}
$$

Hipótesis inductiva: Asumimos que la proposición es cierta para algún $k \geq 0$

$$P(k): \sum_{i=0}^{k} 2^{i} = 2^{k+1} - 1$$

Tesis inductiva: Debemos demostrar que la proposición es cierta para $k+1$

$$P(k + 1): \sum_{i=0}^{k+1} 2^{i} = 2^{k+2} - 1$$

Demostración:

$$
\begin{aligned}
\sum_{i=0}^{k+1} 2^{i} = 2^{k+2} - 1 \\
\sum_{i=0}^{k} 2^{i} + 2^{k+1} = 2^{k+2} - 1 \\
2^{k+1} - 1 + 2^{k+1} = 2^{k+2} - 1 \\
2 \cdot 2^{k+1} - 1 = 2^{k+2} - 1 \\
2^{k+2} - 1 = 2^{k+2} - 1
\end{aligned}
$$

>Por lo tanto, la proposición es cierta para todo $n \geq 0$.

## 3. Hormigas
La población de una colina de hormigas se duplica todos los años. Si se establece una colina inicial de 10 hormigas, ¿cuántas habrá al cabo de $n$ años?

>Respuesta

Como necesito que la población inicial se duplique lo que puedo hacer es tener una función de dos argumentos la cual:

$P(n, h)$ donde $n$ es el número de años y $h$ es la población inicial

$P(n, h) = h \cdot 2^{n}$

Luego para responder la pregunta tengo que ver que $\boxed{P(n, 10) = 10 \cdot 2^{n}}$

## 4. Probar por Inducción

Probar por inducción que para $n\geq5$ se cumple que $2^n > n^2$

>Respuesta

Caso base: $n=5$

$$
\begin{cases}
2^5 = 32 \\ & \text{Se verifica} \\ 5^2 = 25
\end{cases}
$$

Hipótesis inductiva: Asumimos que la proposición es cierta para algún $k \geq 5$

$$P(k): 2^k > k^2$$

Tesis inductiva: Debemos demostrar que la proposición es cierta para $k+1$

$$P(k + 1): 2^{k+1} > (k+1)^2$$

Demostración:

$$
\begin{aligned}
2^{k+1} > (k+1)^2 \\
2 \cdot 2^k > (k+1)^2 \\
2 \cdot k^2 > (k+1)^2 \\
2k^2 > k^2 + 2k + 1 \\
k^2 - 2k - 1 > 0
\end{aligned}
$$

Como la función $f(k) = k^2 - 2k - 1$ es una parábola con concavidad positiva y su vértice está en $k = 1$, entonces para $k \geq 5$ se cumple que $k^2 - 2k - 1 > 0$

>Por lo tanto, la proposición es cierta para todo $n \geq 5$.

5. Gatos
La población de gatos en un depósito tiene la propiedad de que el número de gatos en un año es igual a la suma del número de gatos de los dos años anteriores. Si en el primer año (empezando a contar desde 1) hay un solo gato, y el segundo dos, probar que el número de gatos en el año n es:

$$\sqrt{\frac{1}{5}} \left[ \left( \frac{1+\sqrt{5}}{2} \right)^{n+1} - \left( \frac{1-\sqrt{5}}{2} \right)^{n+1} \right]$$

>Respuesta

Si llamo a la población de gatos en el año $n$ como $P(n)$, entonces tenemos que:

$$P(n) = P(n-1) + P(n-2)$$

Donde:
$P(1) = 1$
$P(2) = 2$

Luego calculo los primeros términos:

$P(3) = P(2) + P(1) = 2 + 1 = 3$

$P(4) = P(3) + P(2) = 3 + 2 = 5$

Entonces tengo que ver que:

$$P(n) = \sqrt{\frac{1}{5}} \left[ \left( \frac{1+\sqrt{5}}{2} \right)^{n+1} - \left( \frac{1-\sqrt{5}}{2} \right)^{n+1} \right]$$

Voy a usar inducción global:

Caso base: $P(1)$

$$P(1) = \sqrt{\frac{1}{5}} \left[ \left( \frac{1+\sqrt{5}}{2} \right)^{1+1} - \left( \frac{1-\sqrt{5}}{2} \right)^{1+1} \right] = \sqrt{\frac{1}{5}} \left[ \left( \frac{1+\sqrt{5}}{2} \right)^{2} - \left( \frac{1-\sqrt{5}}{2} \right)^{2} \right]$$

$$P(1) = \sqrt{\frac{1}{5}} \left[ \frac{1+2\sqrt{5}+5}{4} - \frac{1-2\sqrt{5}+5}{4} \right] = \sqrt{\frac{1}{5}} \left[ \frac{6+2\sqrt{5}}{4} - \frac{6-2\sqrt{5}}{4} \right] = \sqrt{\frac{1}{5}} \left[ \frac{4\sqrt{5}}{4} \right] = \sqrt{\frac{1}{5}} \cdot \sqrt{5} = 1$$

Luego calculo $P(2)$:

$$P(2) = \sqrt{\frac{1}{5}} \left[ \left( \frac{1+\sqrt{5}}{2} \right)^{2+1} - \left( \frac{1-\sqrt{5}}{2} \right)^{2+1} \right] = \sqrt{\frac{1}{5}} \left[ \left( \frac{1+\sqrt{5}}{2} \right)^{3} - \left( \frac{1-\sqrt{5}}{2} \right)^{3} \right]$$

$$P(2) = \sqrt{\frac{1}{5}} \left[ \frac{1+3\sqrt{5}+3(5)+5\sqrt{5}}{8} - \frac{1-3\sqrt{5}+3(5)-5\sqrt{5}}{8} \right] = \sqrt{\frac{1}{5}} \left[ \frac{16+8\sqrt{5}}{8} - \frac{16-8\sqrt{5}}{8} \right] = \sqrt{\frac{1}{5}} \left[ \frac{16\sqrt{5}}{8} \right] = \sqrt{\frac{1}{5}} \cdot 2\sqrt{5} = 2$$

Por hipótesis inductiva asumimos que la proposición es cierta para algún $k \geq 1$

Entonces tengo que ver que $P(k) = P(k-1) + P(k-2)$

$$P(k) = P(k-1) + P(k-2)$$

$$
P(k) = \sqrt{\frac{1}{5}} \left[ \left( \frac{1+\sqrt{5}}{2} \right)^{k} - \left( \frac{1-\sqrt{5}}{2} \right)^{k} \right] + \sqrt{\frac{1}{5}} \left[ \left( \frac{1+\sqrt{5}}{2} \right)^{k-1} - \left( \frac{1-\sqrt{5}}{2} \right)^{k-1} \right]$$

$$
P(k) = \sqrt{\frac{1}{5}} \left[ \left( \frac{1+\sqrt{5}}{2} \right)^{k} + \left( \frac{1+\sqrt{5}}{2} \right)^{k-1} - \left( \frac{1-\sqrt{5}}{2} \right)^{k} - \left( \frac{1-\sqrt{5}}{2} \right)^{k-1} \right]$$

$$
P(k) = \sqrt{\frac{1}{5}} \left[ \left( \frac{1+\sqrt{5}}{2} \right)^{k-1} \left( \frac{1+\sqrt{5}}{2} + 1 \right) - \left( \frac{1-\sqrt{5}}{2} \right)^{k-1} \left( \frac{1-\sqrt{5}}{2} + 1 \right) \right]$$

$$
P(k) = \sqrt{\frac{1}{5}} \left[ \left( \frac{1+\sqrt{5}}{2} \right)^{k-1} \left( \frac{3+\sqrt{5}}{2} \right) - \left( \frac{1-\sqrt{5}}{2} \right)^{k-1} \left( \frac{3-\sqrt{5}}{2} \right) \right]$$

$$
P(k) = \sqrt{\frac{1}{5}} \left[ \left( \frac{1+\sqrt{5}}{2} \right)^{k-1} \left( \frac{1+\sqrt{5}}{2} \right)^{2} - \left( \frac{1-\sqrt{5}}{2} \right)^{k-1} \left( \frac{1-\sqrt{5}}{2} \right)^{2} \right]$$

$$
P(k) = \sqrt{\frac{1}{5}} \left[ \left( \frac{1+\sqrt{5}}{2} \right)^{k+1} - \left( \frac{1-\sqrt{5}}{2} \right)^{k+1} \right]$$

## 6. Programar de manera recursiva
Programar de manera recursiva (en su lenguaje favorito) la función del punto anterior. Escribir casos de test para la función, utilizando la fórmula cerrada demostrada en el punto anterior.

> Respuesta

Programa
```hs
poblaciónGatuna :: Int -> Int
poblaciónGatuna n
    | n == 1 = 1
    | n == 2 = 2
    | n > 2 = poblaciónGatuna (n-1) + poblaciónGatuna (n-2)
```
Test:
```hs
formulaCerrada :: Int -> Int
formulaCerrada n = floor $ sqrt (1/5) * ((1 + sqrt 5) / 2) ** (n + 1) - ((1 - sqrt 5) / 2) ** (n + 1)

testCorrecto :: Bool
testCorrecto = all (== True) [poblaciónGatuna n == formulaCerrada n | n <- [1..100]]
```

## 7. Error en la demostración
¿Cuál es el error de la siguiente demostración?
Se quiere probar que los elementos $x_1, x_2, \dots, x_n$ de un conjunto son todos iguales entre sí.

a) Paso inicial $n = 1$: El conjunto tiene un sólo elemento $x_1$ que es igual a si mismo.

b) Paso inductivo: Supongamos que $x_1 = x_2 = \dots = x_{n-1}$. Como también vale la hipótesis inductiva para un conjunto de dos elementos, tenemos que $x_{n-1} = x_n$. Por lo tanto, $x_1 = x_2 = \dots = x_n$.

> Respuesta

El error está en el paso inductivo. Si bien es cierto que $x_1 = x_2 = \dots = x_{n-1}$ y que $x_{n-1} = x_n$, no podemos concluir que $x_1 = x_2 = \dots = x_n$. Para que esto sea cierto, necesitaríamos que $x_1 = x_n$, lo cual no está garantizado.

## 8. Error en la demostración
¿Cuál es el error de la siguiente demostración?
Se quiere probar que $\forall a \neq 0$  vale que $a^n = 1$

a) Paso inicial (n=0): $a^0 = 1$

b) Paso inductivo: Supongamos que $a^{n-1} = 1$. Entonces $a^n = \frac{a^{n-1} \dot a^{n-1}}{a^{n-2}} = \frac{1 \dot 1}{1} = 1$

>Respuesta

El error está en el paso inductivo. Si bien es cierto que $a^{n-1} = 1$ y que $a^n = \frac{a^{n-1} \dot a^{n-1}}{a^{n-2}}$, no podemos concluir que $a^n = 1$. Para que esto sea cierto, necesitaríamos que $a = 1$, lo cual no está garantizado.