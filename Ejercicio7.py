#Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.
def encontrar_max_min(lista):
    if not lista:
        return None, None
    
    max_num = max(lista)
    min_num = min(lista)
    
    return min_num, max_num
    
lista_numeros = [890, 506, 2, 7, 90, 40]
min_num, max_num = encontrar_max_min(lista_numeros)
print(f"En la lista {lista_numeros}, el número más pequeño es {min_num} y el número más grande es {max_num}.")
