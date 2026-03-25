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

```python
def palabra(cadena: str) -> bool:
    pass

def es_subdivisible(texto: str, inicio: int = 0) -> bool:
    if inicio >= len(texto): return True
    
    for fin in range(inicio + 1, len(texto) + 1):
        prefijo = texto[inicio:fin]
        if palabra(prefijo) and es_subdivisible(texto, fin):
            return True
    return False
```

Si suponemos que la función `palabra` toma tiempo constante, la cota superior de complejidad es $O(2^n)$ porque en el peor de los casos se explora todas las posibles subdivisiones de la cadena. (producto cartesiano de las posibles subdivisiones)

TENGOQUEPREGUNTARCOMODEMOSTRARESTO

# Ejercicio 2 - Árboles binarios de búsqueda óptimos

Dado un conjunto de elementos de $[n] = \{1, \cdots, n\}$ y una funcíon $f:[n] -> \mathbb{N}$ que nos da la frecuencia de acceso a dichos elementos, decimos que `A` es un arbol binario de busqueda óptimo si este minimiza el costo de todos los accesos dados por `f`.

1. Escribir una función recursiva que devuelva el costo de acceder a todos los elementos de un `AB` dado usando `f`.

> El costo de acceder a un elemento es el producto de la frecuencia de acceso por el nivel del elemento. El nivel de la raíz es 1.

2. Escribir un algoritmo backtraking que encuentre el AB óptimo para un `f` dado.

3. Dar una cota superior para la complejidad.

4. Probar que el algoritmo es correcto.

```python
class ArbolBinario:
    def __init__(self, izquierdo, valor, derecho):
        self.izquierdo = izquierdo
        self.valor = valor
        self.derecho = derecho

def costo_acceso(arbol: ArbolBinario | None, f: dict[int, int], nivel: int = 1) -> int:
    if arbol is None:
        return 0
    return (f[arbol.valor] * nivel + 
            costo_acceso(arbol.izquierdo, f, nivel + 1) + 
            costo_acceso(arbol.derecho, f, nivel + 1))

def generar_arboles(elementos: list[int]) -> list[ArbolBinario | None]:
    if not elementos:
        return [None]
    
    arboles = []
    # Backtracking: probamos definir cada elemento como raíz local
    # (Los elementos deben estar ordenados para asegurar que sea un ABB válido)
    for i in range(len(elementos)):
        raiz = elementos[i]
        sub_izq = generar_arboles(elementos[:i])
        sub_der = generar_arboles(elementos[i+1:])
        
        # Combinamos todos los sub-árboles izquierdos y derechos posibles
        for izq in sub_izq:
            for der in sub_der:
                arboles.append(ArbolBinario(izq, raiz, der))
                
    return arboles

def arbol_optimo(elementos: list[int], f: dict[int, int]) -> ArbolBinario | None:
    elementos.sort()
    todos_los_arboles = generar_arboles(elementos)
    
    mejor_arbol = None
    mejor_costo = float('inf')
    
    for arbol in todos_los_arboles:
        costo = costo_acceso(arbol, f, nivel=1) # El nivel de la raíz es 1
        if costo < mejor_costo:
            mejor_costo = costo
            mejor_arbol = arbol
            
    return mejor_arbol
```
Cota superior: $\mathcal{O}(n \cdot C_n) \subseteq \mathcal{O}(n \cdot 4^n)$ (donde $C_n$ es la cantidad de árboles posibles).

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

```py
def es_valido(texto):
    vocales = "aeiou"
    
    for i in range(len(texto) - 2):
        # Verificar 3 vocales seguidas
        if (texto[i] in vocales and 
            texto[i+1] in vocales and 
            texto[i+2] in vocales):
            return False
        
        # Verificar 3 consonantes seguidas
        if (texto[i] not in vocales and 
            texto[i+1] not in vocales and 
            texto[i+2] not in vocales and
            texto[i].isalpha() and 
            texto[i+1].isalpha() and
            texto[i+2].isalpha()):
            return False
    
    return True
def toggle_values(texto:str, inicio = 0) -> str:
    if not es_valido(texto): return []
    elif inicio >= len(texto): return [texto]
    
    resultados = []
    if texto[inicio] == "_":
        
        for letra in alfabeto:
            nuevo_texto = texto[:inicio] + letra + texto[inicio+1:]
            resultados.extend(toggle_values(nuevo_texto, inicio+1))
    else: 
        return toggle_values(texto, inicio + 1)
    return resultados
```
complejidad: $O(26^k \cdot n)$ donde $k$ es la cantidad de comodines.