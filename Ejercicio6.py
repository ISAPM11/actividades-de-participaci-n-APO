#Crear un programa que calcule la suma de los números en una lista dada.
def sumar_lista(numeros):
    return sum(numeros)

lista_de_numeros = [80, 2, 47, 74, 225]
suma = sumar_lista(lista_de_numeros)
print(f"La suma de los números en la lista definida {lista_de_numeros} es {suma}.")
