import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculos import suma, multiplicacion, cuadrado
from integracion_calculos import cuadrado_binomio


def setup():
    return cuadrado_binomio


def test_integrado_binomio():
    f = setup()
    a = 3
    b = 4

    total_fc = f(a, b)

    a2 = cuadrado(a)
    b2 = cuadrado(b)
    ab = multiplicacion(a, b)
    dosab = multiplicacion(2, ab)
    total_fs = suma(suma(a2, dosab), b2)

    assert total_fc == total_fs
