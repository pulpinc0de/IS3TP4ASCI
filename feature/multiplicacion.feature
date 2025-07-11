Feature: Multiplicación de dos números

  Scenario: Multiplicación de dos números positivos
    Given que ingreso los números 4 y 5
    When los multiplico
    Then el resultado debe ser 20

  Scenario: Multiplicación de un número negativo y uno positivo
    Given que ingreso los números -3 y 6
    When los multiplico
    Then el resultado debe ser -18

  Scenario: Multiplicación por cero
    Given que ingreso los números 0 y 9
    When los multiplico
    Then el resultado debe ser 0
