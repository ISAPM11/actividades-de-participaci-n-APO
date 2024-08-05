#Crear un programa que genere una lista de números pares entre 1 y 100.
def generar_pares(inicio, fin):
    
    return [num for num in range(inicio, fin + 1) if num % 2 == 0]

numeros_pares = generar_pares(1, 100)
print(f"Los números pares entre 1 y 100 son: {numeros_pares}")