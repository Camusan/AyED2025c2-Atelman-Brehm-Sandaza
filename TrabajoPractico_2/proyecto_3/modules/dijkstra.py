from modules.grafo import Grafo
from modules.vertice import Vertice
from modules.cola_prioridad import Cola_de_Prioridad
from modules.monticulo_min import Monticulo_Min

def dijkstra(grafo:Grafo, inicio:Vertice):
    cp = Cola_de_Prioridad()
    inicio.asignarDistancia(0)
    cp.construirMonticulo([(v.obtenerDistancia(),v) for v in grafo])
    while not cp.estaVacia():
        verticeActual = cp.eliminar()
        for verticeSiguiente in verticeActual.obtenerConexiones():
            nuevaDistancia = verticeActual.obtenerDistancia() \
                    + verticeActual.obtenerPonderacion(verticeSiguiente)
            if nuevaDistancia < verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarDistancia( nuevaDistancia )
                verticeSiguiente.asignarPredecesor(verticeActual)
                cp.decrementarClave(verticeSiguiente,nuevaDistancia)

def distanciatotal(grafo:Grafo): # Suma las distancias del árbol de expansión mínima
    total = 0
    for v in grafo:
        if v.predecesor is not None:
            total += v.distancia
    return total
