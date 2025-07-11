from .calculos import multiplicacion
import pytest


@pytest.mark.parametrize(
    "valor_a, valor_b, resultado",
    [
        (2, 3, 6),           
        (2, -3, -6),           
        (0, 5, 0),
        (None, 5, None),     
        (None, None, None), 
        (2, None, None),    
        ('2', 5, 10),
        (2, multiplicacion(2, 2), 8),
    ]
)
def test_varios_casos_multiplicacion(valor_a, valor_b, resultado):
    assert multiplicacion(valor_a, valor_b) == resultado

