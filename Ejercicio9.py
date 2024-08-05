#Crear un programa que genere una matriz de números y la imprima en pantalla.
import random

def generar_matriz(filas, columnas, inicio, fin):
    
    matriz = [[random.randint(inicio, fin) for _ in range(columnas)] for _ in range(filas)]
    return matriz

def imprimir_matriz(matriz):
   
    for fila in matriz:
        print(' '.join(map(str, fila)))

filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))
inicio = int(input("Ingrese el valor mínimo del rango de los números: "))
fin = int(input("Ingrese el valor máximo del rango de los números: "))

matriz = generar_matriz(filas, columnas, inicio, fin)

print("La matriz generada es:")
imprimir_matriz(matriz)
