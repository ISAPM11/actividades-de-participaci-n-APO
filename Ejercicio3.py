#Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.
import random
def generar_numeros_aleatorios(cantidad, primero, ultimo):
    lista = [random.randint(primero, ultimo) for _ in range(cantidad)]
    return lista
cantidad = int(input("Ingrese la cantidad de números aleatorios a generar: "))
primero = int(input("Ingrese el numero mínimo de la lista: "))
ultimo = int(input("Ingrese el numero máximo de la lista: "))

numeros_aleatorios = generar_numeros_aleatorios(cantidad, primero, ultimo)
print("Lista de números aleatorios generados es:")
print(numeros_aleatorios)

