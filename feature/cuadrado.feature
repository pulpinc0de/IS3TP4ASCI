Feature: Calcular el cuadrado de un número

  Scenario: Calcular el cuadrado de un número positivo
    Given que ingreso el número 4
    When calculo su cuadrado
    Then el resultado debe ser 16

  Scenario: Calcular el cuadrado de un número negativo
    Given que ingreso el número -3
    When calculo su cuadrado
    Then el resultado debe ser 9

  Scenario: Calcular el cuadrado de cero
    Given que ingreso el número 0
    When calculo su cuadrado
    Then el resultado debe ser 0

  Scenario: Calcular el cuadrado de una cadena numérica válida
    Given que ingreso el número "5"
    When calculo su cuadrado
    Then el resultado debe ser 25

