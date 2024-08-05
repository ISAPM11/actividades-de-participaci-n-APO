#Escribir una función que calcule el área de un círculo dado su radio.
import math
def area_circulo(radio):
     return math.pi * (radio ** 2)
radio = float(input("Ingresa el radio del círculo: "))
area = area_circulo(radio)
print(f"El área del círculo con radio {radio} es de {area:.2f}")
