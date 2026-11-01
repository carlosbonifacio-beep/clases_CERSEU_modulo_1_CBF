"""
Requisitos:

1. Crear dos variables para los valores de nombre, profesion y ciudad
2. Crear dos varaibles para la remuneración de enero y febrero (mayor a 1500)
3. Crear 1 varibles donde se sumará el ingreso de los dos meses: enero y febrero
4. Mostrar en pantalla el siguiente mensaje (Output)

"Hola soy 'nombre', soy 'profesión' y mi remuneración acumulada es de ''remunera_total"

rem_1
remunera_1
rem_enero

"""
nombre = "Kenichi"
profesion = "Contador"
ciudad = "Lima"

rem_enero = 1600
rem_febrero = 1700

rem_total= rem_enero + rem_febrero

print(f"hola soy {nombre}, soy {profesion} y mi remuneración acumulada {rem_total}")