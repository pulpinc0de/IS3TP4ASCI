def multiplicacion(a, b):
    try:
        num_a = int(a)
        num_b = int(b)
        return num_a * num_b
    except (TypeError, ValueError):
        return None

def suma(a, b):
    try:
        num_a = int(a)
        num_b = int(b)
        return num_a + num_b
    except (TypeError, ValueError):
        return None
    return None

def cuadrado(num):
    try:
        numero = int(num)
        return numero ** 2
    except (TypeError, ValueError):
        return None
    

