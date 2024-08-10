class Vehiculo:
    def _init_(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima= velocidad_maxima
        self.kilometraje= kilometraje

class Punto:
    def _init_(self, x,y):
        self.x= x
        self.y= y

    def mostrar_coordenadas(self):
        print("Las coordenadas del punto son: x:{} y:{}".format(self.x,self.y)) # mi_punto.x mi_punto.y
 
    def mover_cambio_coordenadas(self):
        print("Las coordenadas nuevas del punto son: x:{} y:{}".format(self.x,self.y)) 

    def calcular_distancia(self):
        print("Las coordenadas nuevas del punto son: x:{} y:{}".format(self.x,self.y))

mi_punto = Punto(64,23)
mi_cambio_de_punto = Punto(9,15)
calcular_distancia = Punto(3,6)


mi_punto.mostrar_coordenadas()
mi_cambio_de_punto.mover_cambio_coordenadas()
calcular_distancia.mover_cambio_coordenadas()

"""
class Rectangulo: 
    def _init_(self, puntos_parte_superior, puntos_parte_inferior):
        self.puntos_largo= puntos_largo
        self.puntos_ancho= puntos_ancho

def perimetro(self):
    return self.puntos_largo + self.puntos_ancho *2

def area(self):
    return self.puntos_largo * self.puntos_ancho

if puntos



class Circulo: 
    def _init_(self, centro, radio):
        self.centro= centro
        self.radio= radio 

def area(self):
    return 3.14 * self.radio ^2

def perimetro(self):
    return 2 * 3.14 * self.radio

"""