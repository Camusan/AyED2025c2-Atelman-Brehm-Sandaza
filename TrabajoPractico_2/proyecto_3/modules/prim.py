import os
import sys
from modules.grafo import Grafo
from modules.vertice import Vertice
from modules.cola_prioridad import Cola_de_Prioridad
from modules.monticulo_min import Monticulo_Min

def prim(grafo:Grafo, inicio:Vertice):
    cp = Cola_de_Prioridad()
    
    for vertice in grafo:
        vertice.asignarDistancia(sys.maxsize)
        vertice.asignarPredecesor(None)
    inicio.asignarDistancia(0)
    # construir el montículo con los objetos Vertice (no con tuplas)
    cp.construirMonticulo([v for v in grafo])

    
    
    while not cp.estaVacia():
        verticeActual = cp.eliminar()
        for verticeSiguiente in verticeActual.obtenerConexiones():
            nuevoCosto = verticeActual.obtenerPonderacion(verticeSiguiente)
            if verticeSiguiente in cp and nuevoCosto < verticeSiguiente.obtenerDistancia():
              verticeSiguiente.asignarPredecesor(verticeActual)
              verticeSiguiente.asignarDistancia(nuevoCosto)
              cp.decrementarClave(verticeSiguiente,nuevoCosto)

                
def distanciatotal(grafo:Grafo): # Suma las distancias del árbol de expansión mínima
    total = 0
    for v in grafo:
        # usar getters para mantener consistencia con el resto del código
        pre = v.obtenerPredecesor() if hasattr(v, 'obtenerPredecesor') else getattr(v, 'predecesor', None)
        dist = v.obtenerDistancia() if hasattr(v, 'obtenerDistancia') else getattr(v, 'distancia', None)
        # ignorar vértices que no pertenezcan al árbol (distancia infinita o sin predecesor)
        if pre is not None and dist is not None:
            if dist != sys.maxsize:
                total += dist

    return total

if __name__ == "__main__":
    # Obtener la ruta absoluta del directorio actual
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    # Subir un nivel y entrar a la carpeta data
    ruta_archivo = os.path.join(directorio_actual, "..", "data", "aldeas.txt")
    
    
    grafo=Grafo()
    grafo.cargar_aldeas(ruta_archivo)
    vertice_inicio = grafo.obtenerVertice("Peligros")
    if vertice_inicio is None:
        print("Error: No se encontró la aldea 'Peligros' en el grafo")
    else:
        prim(grafo, vertice_inicio)
        print("Distancia total de la red de comunicación:", distanciatotal(grafo))
        print("\nPlan de distribución de noticias:")
        print("-" * 50)
        
        for aldea in grafo:
            # De quién recibe la noticia
            predecesor = "Origen de la noticia" if aldea.predecesor is None else aldea.predecesor.obtenerId()
            
            # A quiénes debe enviar la noticia (solo los sucesores directos en el árbol)
            sucesores = []
            for otra_aldea in grafo:
                if otra_aldea.predecesor is aldea:  # si esta aldea es el predecesor de otra
                    distancia = otra_aldea.obtenerDistancia()
                    sucesores.append(f"{otra_aldea.obtenerId()} (a {distancia}km)")
            
            print(f"\nAldea: {aldea.obtenerId()}")
            print(f"Recibe de: {predecesor}")
            if sucesores:
                print(f"Debe enviar a: {', '.join(sucesores)}")
            else:
                print("No necesita reenviar la noticia")

    