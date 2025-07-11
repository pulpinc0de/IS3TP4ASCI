import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculos import multiplicacion, suma, cuadrado

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

@pytest.mark.parametrize(
    "valor_a, valor_b, resultado",
    [
        (2, 3, 5),
        (2, -3, -1),
        (0, 5, 5),
        (None, 5, None),
        (None, None, None),
        (2, None, None),
        ('2', 5, 7),
        (2, suma(2, 2), 6),
    ]
)
def test_varios_casos_suma(valor_a, valor_b, resultado):
    assert suma(valor_a, valor_b) == resultado

@pytest.mark.parametrize(
    "valor, resultado",
    [
        (2, 4),
        (-3, 9),
        (0, 0),
        (None, None),
        ('4', 16),
        ('abc', None),
        (2.5, 4),     
        ("2.0", None) 
    ]
)
def test_varios_casos_cuadrado(valor, resultado):
    assert cuadrado(valor) == resultado
