#Crear una función que invierta el orden de los elementos en una lista dada.
def invertir_lista_dada(lista):
    return lista[::-1]

lista_numeros = [45, 40, 39, 18, 13]
lista_invertida = invertir_lista_dada(lista_numeros)

print(f"La lista original es: {lista_numeros}")
print(f"La lista invertida es: {lista_invertida}")
