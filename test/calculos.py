def suma(a, b):
    try:
        num_a = int(a)
        num_b = int(b)
        return num_a + num_b
    except (TypeError, ValueError):
        return  None

def multiplicacion(a, b):
    try:
        num_a = int(a)
        num_b = int(b)
        return num_a * num_b
    except (TypeError, ValueError):
        return None

