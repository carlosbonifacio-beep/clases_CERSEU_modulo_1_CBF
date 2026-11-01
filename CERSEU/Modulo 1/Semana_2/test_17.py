"""
1. Crear 2 variables enteras, 2 variables flotantes, 2 variables string, 1 variable string que contiene
valor numérico y una variable boolean
2. Obtener y mostrar la suma de una variable entera con una variables string numérica
(Realizar conversión si fuera necesario)
3. Obtener y mostrar la suma de las 2 variables enteras más la variable string numérica
y la variable flotante
4. Obtener y mostrar el módulo de las variables enteras: %
5. Obtener y mostrar el resultado de las parte entera, usando las varaibles enteras: //
6. Obtener una potencia usando una de las variables flotantes como base y
una variable entera como potencia

Nota: Las variables string pueden ser tu nombre y apellido
"""

"""
Requisitos:
1. Crear 2 variables enteras, 2 variables flotantes, 2 variables string, 
   1 variable string que contiene valor numérico y una variable boolean
2. Obtener y mostrar la suma de una variable entera con una variable string numérica (Realizar conversión si fuera necesario)
3. Obtener y mostrar la suma de las 2 variables enteras más la variable string numérica y la variable flotante
4. Obtener y mostrar el módulo de las variables enteras: %
5. Obtener y mostrar el resultado de la parte entera, usando las variables enteras: //
6. Obtener una potencia usando una de las variables flotantes como base y una variable entera como potencia
Nota: Las variables string pueden ser tu nombre y apellido
"""

# 1.
entero_1 = 200
entero_2 = 30

float_1 = 3.14
float_2 = 5.5

nombre = "Carlos"
apellido = "Bonifacio"

string_num = "1122"
es_activo = True

print("---------------------------------------")

# 2.
suma_2 = entero_1 + int(string_num)
print("La suma de {} + {} es {}".format(entero_1, string_num, suma_2))

print("---------------------------------------")

# 3.
suma_3 = entero_1 + entero_2 + int(string_num) + float_1
print("La suma de {} + {} + {} + {} es {}".format(entero_1, entero_2, string_num, float_1, suma_3))

print("---------------------------------------")

# 4.
modulo = entero_1 % entero_2
print("El módulo de {} % {} es {}".format(entero_1, entero_2, modulo))

print("---------------------------------------")

# 5.
division = entero_1 // entero_2
print("La división entera de {} // {} es {}".format(entero_1, entero_2, division))

print("---------------------------------------")

# 6.
potencia = float_1 ** entero_2
print("La potencia de {} elevado a {} es {}".format(float_1, entero_2, potencia))

print("---------------------------------------")