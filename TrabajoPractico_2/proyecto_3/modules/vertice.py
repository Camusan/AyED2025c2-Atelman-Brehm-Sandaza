# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

class Vertice:
    def __init__(self, clave):
        self.id = clave
        self.conectadoA = {}
        self.distancia = float("inf")#Parametro que usaremos en dijkstra
        self.predecesor = None
        

    def agregarVecino(self, vecino, ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        return str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self, vecino):
        return self.conectadoA[vecino]
    
    def asignarDistancia(self, distancia:int):
        self.distancia = distancia

    def obtenerDistancia(self):
        return self.distancia
        
    def asignarPredecesor(self, predecesor):
        self.predecesor = predecesor
    
if __name__=="__main__":
    peligros=Vertice("peligros")
    accidentes=Vertice("accidentes")
    