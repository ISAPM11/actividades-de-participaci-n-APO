#Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y división.
def calcular_operaciones(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = None
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Error: División por cero"

    return suma, resta, multiplicacion, division

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

suma, resta, multiplicacion, division = calcular_operaciones(numero1, numero2)

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")