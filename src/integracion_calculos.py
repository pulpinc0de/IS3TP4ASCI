
from calculos import suma, multiplicacion, cuadrado 

def cuadrado_binomio(a, b):
    try:
        a2 = cuadrado(a)
        b2 = cuadrado(b)
        ab   = multiplicacion(a, b)
        dosab = multiplicacion(2, ab)

        if None in (a2, b2, ab, dosab):
            return None
    
        return suma(suma(a2, dosab), b2)

    except (TypeError, ValueError):
        return None
   
