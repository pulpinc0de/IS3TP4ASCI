import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from calculos import cuadrado
from behave import given, when, then

@given('que ingreso el número {a:d}')
def step_given_numero(context, a):
    context.a = a

@when('calculo su cuadrado')
def step_when_calculo_cuadrado(context):
    context.resultado = cuadrado(context.a)

@then('el resultado debe ser {esperado:d}')
def step_then_resultado(context, esperado):
    assert context.resultado == esperado, f"Esperado {esperado}, pero se obtuvo {context.resultado}"
