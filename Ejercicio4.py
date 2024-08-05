#Escribir un programa que determine si un número dado es par o impar.
def numero_es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
numero = int(input("Ingrese un número: "))
resultado = numero_es_par_o_impar(numero)
print(f"El número {numero} es {resultado}.")


