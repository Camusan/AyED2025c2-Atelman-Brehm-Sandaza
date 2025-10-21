from modules.monticulo_min import Monticulo_Min


class Cola_de_Espera:
    def __init__(self):
        self.cola = Monticulo_Min()
        self.tamaño_actual = self.cola.tamaño_actual

    
    def agregar(self, paciente):
        return self.cola.insertar_valor(paciente)

    def __iter__(self):
        for i in self.cola:
            yield i
    
    def eliminar(self):
        return self.cola.sacar_raiz()
    
