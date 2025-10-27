#Codigo extraido del problema 1 TP2
from modules.monticulo_min import Monticulo_Min


class Cola_de_Prioridad:
    def __init__(self):
        self.cola = Monticulo_Min()
        self.tamaño_actual = 0
        
    def estaVacia(self):
        return self.tamaño_actual == 0

    
    def agregar(self, paciente):
        self.tamaño_actual += 1
        return self.cola.insertar_valor(paciente)

    def __iter__(self):
        for i in self.cola:
            yield 
            
    def decrementarClave(self,verticeSiguiente, nuevaDistancia):
        "este método se utiliza cuando se decrementa la distancia a un vértice "
        "que ya está en la cola, y por lo tanto ese vértice se mueve hacia el frente de la cola."
        verticeSiguiente.asignarDistancia(nuevaDistancia)
        self.cola.infiltrar_arriba(verticeSiguiente)

    def eliminar(self):
        self.tamaño_actual -= 1
        return self.cola.sacar_raiz()