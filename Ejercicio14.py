#Escribir una función que calcule la media aritmética de una lista de números.
def media_aritmetica(lista):

    if not lista:
        raise ValueError("La lista no puede estar vacía.")
    
    suma = sum(lista)
    cantidad = len(lista)
    return suma / cantidad

lista_numeros = [110, 30, 19, 4, 18]
try:
    resultado = media_aritmetica(lista_numeros)
    print(f"La media aritmética de la lista {lista_numeros} es {resultado:.2f}.")
except ValueError as e:
    print(e)