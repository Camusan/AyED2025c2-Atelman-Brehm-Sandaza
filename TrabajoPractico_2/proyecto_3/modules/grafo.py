class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self, clave):
        pass

    def obtenerVertice(self, n):
        pass

    def agregarArista(self, de, a, costo=0):
        pass

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())


if __name__=="__main__":
    pass