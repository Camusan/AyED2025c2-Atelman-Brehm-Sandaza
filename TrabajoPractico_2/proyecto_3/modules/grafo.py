from modules.vertice import Vertice
import os 
class Grafo:
    def __init__(self):
        self.listaVertices = {} #
        self.numVertices = 0

    def agregarVertice(self, clave:str):
        "agrega una instancia de vertice al grafo "
        if clave in self.listaVertices:
            raise KeyError("El vértice ya existe en el grafo")
        vertice=Vertice(clave)
        self.listaVertices[clave]=vertice
        self.numVertices += 1
        return vertice
        

    def obtenerVertice(self, n:str):
        " encuentra el vértice en el grafo con nombre n."
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def agregarArista(self, de:str, a:str, costo:int=0):
        "agrega al grafo una nueva arista dirigida que conecta dos vértices."
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)


    def obtenerVertices(self):
        "devuelve la lista de todos los vértices en el grafo."
        return self.listaVertices.keys()
    
    def obtenerVerticesOrdenados(self):
        "devuelve la lista de todos los vértices en el grafo ordenados por clave."
        return sorted(self.listaVertices.keys())
    
    def cargar_aldeas(self, nombre_archivo):
        "Carga las aldeas y sus conexiones desde un archivo de texto."
        try:    
            with open(nombre_archivo, 'r') as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if not linea or ',' not in linea:
                        continue
                    partes = [p.strip() for p in linea.split(',')]
                    if len(partes) != 3:
                        print(f"Ignorada (formato incorrecto): {linea}")
                        continue
                    aldea_origen, aldea_destino, distancia_s = partes
                    try:
                        distancia = int(distancia_s)
                    except ValueError:
                        print(f"Ignorada (distancia no válida): {linea}")
                        continue
                    self.agregarArista(aldea_origen, aldea_destino, distancia)    
        except FileNotFoundError:
            print(f"Error: El archivo {nombre_archivo} no se encontró.")
        except Exception as e:
            print(f"Error al cargar las aldeas: {e}")

    def __iter__(self):
        return iter(self.listaVertices.values())


if __name__=="__main__":
    # Obtener la ruta absoluta del directorio actual
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    # Subir un nivel y entrar a la carpeta data
    ruta_archivo = os.path.join(directorio_actual, "..", "data", "aldeas.txt")
    
    
    grafo=Grafo()
    grafo.cargar_aldeas(ruta_archivo)
    aldeas_ordenadas = grafo.obtenerVerticesOrdenados()
    for aldea in aldeas_ordenadas:
        print(aldea)



    #g = Grafo()
# for i in range(6):
#    g.agregarVertice(i)
# g.listaVertices
# {0: <__main__.Vertice object>,
#  1: <__main__.Vertice object>,
#  2: <__main__.Vertice object>,
#  3: <__main__.Vertice object>,
#  4: <__main__.Vertice object>,
#  5: <__main__.Vertice object>}
# g.agregarArista(0,1,5)
# g.agregarArista(0,5,2)
# g.agregarArista(1,2,4)
# g.agregarArista(2,3,9)
# g.agregarArista(3,4,7)
# g.agregarArista(3,5,3)
# g.agregarArista(4,0,1)
# g.agregarArista(5,4,8)
# g.agregarArista(5,2,1)
# for v in g:
#    for w in v.obtenerConexiones():
#        print("( %s , %s )" % (v.obtenerId(), w.obtenerId()))

# ( 0 , 1 )
# ( 0 , 5 )
# ( 1 , 2 )
# ( 2 , 3 )
# ( 3 , 5 )
# ( 3 , 4 )
# ( 4 , 0 )
# ( 5 , 2 )
# ( 5 , 4 )
