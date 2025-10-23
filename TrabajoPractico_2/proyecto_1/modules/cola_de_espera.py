from modules.monticulo_min import Monticulo_Min


class Cola_de_Espera:
    def __init__(self):
        self.cola = Monticulo_Min()
        self.tamaño_actual = 0

    
    def agregar(self, paciente):
        self.tamaño_actual += 1
        return self.cola.insertar_valor(paciente)

    def __iter__(self):
        for i in self.cola:
            yield i
    
    def eliminar(self):
        self.tamaño_actual -= 1
        return self.cola.sacar_raiz()
    
