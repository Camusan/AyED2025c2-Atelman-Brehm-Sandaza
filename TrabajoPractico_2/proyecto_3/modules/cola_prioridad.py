#Codigo extraido del problema 1 TP2
from modules.monticulo_min import Monticulo_Min


class Cola_de_Prioridad:
    def __init__(self):
        self.cola = Monticulo_Min()
        self.tamaño_actual = 0
        
    def estaVacia(self):
        return self.tamaño_actual == 0

    def construirMonticulo(self, lista_valores):
        self.cola.construirMonticulo(lista_valores)
        self.tamaño_actual = len(lista_valores)
    
    def agregar(self, paciente):
        self.tamaño_actual += 1
        return self.cola.insertar_valor(paciente)

    def __iter__(self):
        for elemento in self.cola:
            yield elemento
            
    def __contains__(self, vertice):
        """Permite usar 'if vertice in cp' recorriendo los elementos del montículo."""
        for v in self:
            if v is vertice:
                return True
        return False
            
    def decrementarClave(self,verticeSiguiente, nuevaDistancia):
        "este método se utiliza cuando se decrementa la distancia a un vértice "
        "que ya está en la cola, y por lo tanto ese vértice se mueve hacia el frente de la cola."
        verticeSiguiente.asignarDistancia(nuevaDistancia)
        # Buscar la posición del vértice en el montículo y filtrar hacia arriba.
        # Esto es O(n); para O(log n) habría que mantener un mapa elemento->índice en Monticulo_Min.
        try:
            idx = self.cola.lista_monticulo.index(verticeSiguiente)
        except ValueError:
            # el vértice no está en el montículo (ya fue extraído u otro caso)
            return
        self.cola.infiltrar_arriba(idx)

    def eliminar(self):
        self.tamaño_actual -= 1
        return self.cola.sacar_raiz()