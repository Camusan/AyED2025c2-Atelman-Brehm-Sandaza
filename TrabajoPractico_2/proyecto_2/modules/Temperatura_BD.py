from modules.AVL import ArbolAVL
from modules.AVL import NodoArbol

class Temperatuas_DB:
    def __init__(self):
        self.arbol = ArbolAVL()

    def leer_archivo(self,nombre_archivo):
        #lee el archivo de texto y carga las temperaturas en el árbol.
        with open(nombre_archivo,"r") as archi:
            for linea in archi:
                try:
                    fecha, temp = linea.strip().split(";")
                    temperatura=float(temp)
                    self.arbol.insertar(fecha,temperatura)
                except ValueError:
                    print(f"Error al procesar la línea: {linea.strip()}")


    def guardar_temperatura(self,temperatura,fecha):
        #guarda la medida de temperatura asociada a la fecha.
        self.arbol.insertar(temperatura,fecha,self.arbol.raiz)

    def devolver_temperatura(self,fecha): 
        #devuelve la medida de temperatura en la fecha determinada.
        self.arbol.buscar(fecha,self.arbol.raiz)

    def max_temp_rango(self,fecha1, fecha2): 
        #devuelve la temperatura máxima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2). 
        #Esto no implica que los intervalos del rango deban ser fechas incluidas previamente en el árbol
        pass
    
    def min_temp_rango(self,fecha1,fecha2):
        pass
    def temp_extremos_rango(self,fecha1, fecha2): 
        #devuelve la temperatura mínima y máxima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2)
        pass
        
    def borrar_temperatura(self,fecha):
        #recibe una fecha y elimina del árbol la medición correspondiente a esa fecha.
        pass

    def devolver_temperaturas(self,fecha1, fecha2):
        #devuelve un listado de las mediciones de temperatura en el rango recibido por parámetro con el formato “dd/mm/aaaa: temperatura ºC”, ordenado por fechas. 
        pass
    def cantidad_muestras(self):
        #devuelve la cantidad de muestras de temperatura de la DB.
        return self.arbol.tamaño

   
