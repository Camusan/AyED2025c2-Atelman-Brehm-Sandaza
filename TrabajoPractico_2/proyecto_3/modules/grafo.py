from modules.vertice import Vertice
class Grafo:
    def __init__(self):
        self.listaVertices = {} #
        self.numVertices = 0

    def agregarVertice(self, clave):
        "agrega una instancia de vertice al grafo "
        if clave in self.listaVertices:
            raise KeyError("El vértice ya existe en el grafo")
        vertice=Vertice(clave)
        self.listaVertices[clave]=vertice
        self.numVertices += 1
        return vertice
        

    def obtenerVertice(self, n):
        " encuentra el vértice en el grafo con nombre n."
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def agregarArista(self, de, a, costo=0):
        "agrega al grafo una nueva arista dirigida que conecta dos vértices."
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)


    def obtenerVertices(self):
        "devuelve la lista de todos los vértices en el grafo."
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())


if __name__=="__main__":
    pass