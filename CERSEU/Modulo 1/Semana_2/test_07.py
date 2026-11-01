"""
Requisitos:
  1. Crear 4 variables, entre enteros, booleans, strings
  2. Realizar el uso de condincionales de las variables, para 2 casos true y 2 casos false
  3. En casos que valide True, imprimir el valor de las dos variables
  4. En dos condicionales comparar variables (< o >)
"""
numero = 100
limite = 50
EsEntero = True
País = "España"

if numero < limite:
    print("{} si es menor a {}".format(numero, limite))
    print(EsEntero)
    print(País)

if EsEntero:
    print("EsEntero es verdadero")
    print(numero)
    print(limite)

if not EsEntero:
    print("EsEntero no es verdadero")
    print(numero)
    print(limite)

if numero > limite:
    print("{} si es mayor a {}".format(numero, limite))
    print(EsEntero)
    print(País)