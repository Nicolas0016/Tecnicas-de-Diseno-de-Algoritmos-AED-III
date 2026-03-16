### D&C
Imaginemos que tenemos un progblema muy grande. Lo que busca el D&C es:

1. Dividir el problema grande en pedazos (subproblemas) más pequeños.
2. Resolver el cada uno de esos pedazos (generalmente volviendo a aplicar la misma receta, o sea, recursivamente)
3. Juntas las soluciones de los pedazos para formar la solucion del problema más grande.

> Ejemplo (Merge Sort).
>+ ***Problema***: Ordenar una lista de 1000 números desordenados.
>+ ***Dividir***: Parto la lista en dos mitades
>+ ***Resolver***: Ordeno cada mitad (aplicando el mismo método)
>+ ***Combinar***: Mezclo las dos mitades ya ordenadas para obtener la lista de  1000 elementos ordenada

> OBS: Lo importante es "Las subpartes tienen que ser más pequeñas Y ser el mismo tipo de tarea". Si divido el problema de ordenar una lista pero más chica, funciona. Pero si lo divido en "sumar números" es otro tipo de tarea completamente diferente, ya no es D&C.

