from modules.grafo import Grafo
from modules.prim import prim, distanciatotal


def run():
    g = Grafo()
    # grafo no dirigido: agregar arista en ambos sentidos
    g.agregarArista('A','B',1)
    g.agregarArista('B','A',1)
    g.agregarArista('B','C',2)
    g.agregarArista('C','B',2)
    g.agregarArista('A','C',3)
    g.agregarArista('C','A',3)

    inicio = g.obtenerVertice('A')
    prim(g, inicio)

    print("Vertice: predecesor_id, distancia")
    for v in g:
        pre = v.predecesor.obtenerId() if getattr(v, 'predecesor', None) is not None else None
        print(v.obtenerId(), pre, v.obtenerDistancia())

    print("Distancia total:", distanciatotal(g))

if __name__ == '__main__':
    run()
