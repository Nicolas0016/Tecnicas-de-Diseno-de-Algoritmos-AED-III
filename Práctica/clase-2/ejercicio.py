VOCALES = set("aeiouAEIOU")
CONSONANTES = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
LETRAS = VOCALES | CONSONANTES

def es_valida(cadena):
    """Verifica si la cadena cumple todas las condiciones"""
    # Condición 1: Contiene al menos una E/e
    if 'e' not in cadena.lower():
        return False
    
    # Condición 2 y 3: No tener 3 vocales o 3 consonantes consecutivas
    if len(cadena) < 3:
        return True
    
    contador = 1
    tipo_anterior = "vocal" if cadena[0] in VOCALES else "consonante" if cadena[0] in CONSONANTES else None
    
    for i in range(1, len(cadena)):
        if cadena[i] not in LETRAS:
            continue
            
        tipo_actual = "vocal" if cadena[i] in VOCALES else "consonante"
        
        if tipo_anterior == tipo_actual:
            contador += 1
            if contador >= 3:
                return False
        else:
            contador = 1
            tipo_anterior = tipo_actual
    
    return True

def generar_solucion_candidata(patron):
    resultado = list(patron)
    volcales_sin_e = "aio u".replace(" ", "")
    for i in range(len(resultado)):
        if resultado[i] == "_":
            if i>0 and i < len(resultado) -1:
                if resultado[i-1] in VOCALES or resultado[i+1] in VOCALES:
                    resultado[i] = "b"
                else:
                    resultado[i] = "a"
            else:
                resultado[i] = "b"
    if 'e' not in ''.join(resultado).lower():
        for i in range(len(resultado)):
            if patron[i] == '_' or i == 0:
                resultado[i] = 'E'
                break

    return ''.join(resultado)
print(generar_solucion_candidata("__b_a_e"))

class SolucionParcial:
    def __init__(self,cadena_actual,posicion,tiene_e,ultimos_dos):
        self.cadena = cadena_actual
        self.pos = posicion
        self.tiene_e = tiene_e
        self.ultimos_dos = ultimos_dos

    def __str__(self):
        return f"Pos:{self.pos}, E: {self.tiene_e}, Cadena: {self.cadena}"