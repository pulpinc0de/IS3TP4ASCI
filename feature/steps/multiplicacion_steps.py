import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from calculos import multiplicacion
from behave import given, when, then

@given('que ingreso los números {a:d} y {b:d}')
def step_given_numeros(context, a, b):
    context.a = a
    context.b = b

@when('los multiplico')
def step_when_multiplico(context):
    context.resultado = multiplicacion(context.a, context.b)

@then('el resultado debe ser {esperado:d}')
def step_then_resultado(context, esperado):
    assert context.resultado == esperado, f"Esperado {esperado}, pero se obtuvo {context.resultado}"
