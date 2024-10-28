from typing import Tuple
import numpy as np 

class DatosMeteorologicos:
    DIRECCIONES_VIENTO = {
        'N': 0,
        'NNE': 22.5,
        'NE': 45,
        'ENE': 67.5,
        'E': 90,
        'ESE': 112.5,
        'SE': 135,
        'SSE': 157.5,
        'S': 180,
        'SSW': 202.5,
        'SW': 225,
        'WSW': 247.5,
        'W': 270,
        'WNW': 292.5,
        'NW': 315,
        'NNW': 337.5
    }
    
    DIRECCION_ABREVIACIONES = {v: k for k, v in DIRECCIONES_VIENTO.items()}

    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo
        self.temperaturas = []
        self.humidades = []
        self.presiones = []
        self.velocidades_viento = []
        self.direcciones_viento = []

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        with open(self.nombre_archivo, 'r') as archivo:
            for linea in archivo:
                
                partes = linea.strip().split()
                temperatura = float(partes[7].split(':')[1])  
                humedad = float(partes[8].split(':')[1])      
                presion = float(partes[9].split(':')[1])      
                viento_info = partes[10].split(':')[1]        
                velocidad, direccion = viento_info.split(',')  
                velocidad = float(velocidad)

               
                self.temperaturas.append(temperatura)
                self.humidades.append(humedad)
                self.presiones.append(presion)
                self.velocidades_viento.append(velocidad)
                self.direcciones_viento.append(self.DIRECCIONES_VIENTO[direccion])

       
        temperatura_promedio = np.mean(self.temperaturas)
        humedad_promedio = np.mean(self.humidades)
        presion_promedio = np.mean(self.presiones)
        velocidad_promedio = np.mean(self.velocidades_viento)

       
        direccion_promedio = np.arctan2(np.mean(np.sin(np.radians(self.direcciones_viento))),
                                         np.mean(np.cos(np.radians(self.direcciones_viento)))) * (180 / np.pi)
        direccion_promedio = (direccion_promedio + 360) % 360  
        
        direccion_predominante = min(self.DIRECCION_ABREVIACIONES.keys(), key=lambda x: abs(x - direccion_promedio))

        return (temperatura_promedio, humedad_promedio, presion_promedio, velocidad_promedio, self.DIRECCION_ABREVIACIONES[direccion_predominante])
