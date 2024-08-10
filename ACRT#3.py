import math

class Vehículo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar_coordenadas(self):
        print("Las coordenadas del punto son: x{} y{}".format(self.x, self.y))

    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def calcular_distancia(self, otro_punto):
        return math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)
    
class Rectángulo:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2

    def calcular_perimetro(self):
        largo = (self.punto1.x - self.punto2.x)
        ancho = (self.punto1.y - self.punto2.y)
        return 2 * (largo + ancho)

    def calcular_area(self):
        largo = (self.punto1.x - self.punto2.x)
        ancho = (self.punto1.y - self.punto2.y)
        return largo * ancho

    def es_cuadrado(self):
        return (self.punto1.x - self.punto2.x) == (self.punto1.y - self.punto2.y)
    
class Círculo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def punto_pertenece(self, punto):
        return self.centro.calcular_distancia(punto) <= self.radio

class Carta:
    CORAZONES = "Corazones"
    DIAMANTES = "Diamantes"
    TREBOLES = "Tréboles"
    PUNTOS = "Puntos"

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, acciones_deposito):
        self.balance += acciones_deposito

    def retirar(self, acciones_deposito):
        if acciones_deposito <= self.balance:
            self.balance -= acciones_deposito
        else:
            print("Fondos insuficientes")

    def aplicar_cuota_manejo(self):
        self.balance -= self.balance * 0.02

    def mostrar_detalles(self):
        print("Número de cuenta: numero_cuenta {}".format(self.numero_cuenta))
        print("Propietarios: propietarios {}".format(self.propietarios))
        print("Balance: balance {}".format(self.balance))
        
