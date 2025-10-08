class Temperatuas_DB:
    def __init__(self):
        pass
    
    def guardar_temperatura(temperatura,fecha):
        #guarda la medida de temperatura asociada a la fecha.
        pass

    def devolver_temperatura(fecha): 
        #devuelve la medida de temperatura en la fecha determinada.
        pass

    def max_temp_rango(fecha1, fecha2): 
        #devuelve la temperatura máxima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2). 
        #Esto no implica que los intervalos del rango deban ser fechas incluidas previamente en el árbol
        pass
    
    def min_temp_rango(fecha1,fecha2):
        pass
    def temp_extremos_rango(fecha1, fecha2): 
        #devuelve la temperatura mínima y máxima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2)
        pass
        
    def borrar_temperatura(fecha):
        #recibe una fecha y elimina del árbol la medición correspondiente a esa fecha.
        pass

    def devolver_temperaturas(fecha1, fecha2):
        #devuelve un listado de las mediciones de temperatura en el rango recibido por parámetro con el formato “dd/mm/aaaa: temperatura ºC”, ordenado por fechas. 
        pass
    def cantidad_muestras():
        #devuelve la cantidad de muestras de temperatura de la DB.
        pass

    def lector_de_archivos():
        pass
