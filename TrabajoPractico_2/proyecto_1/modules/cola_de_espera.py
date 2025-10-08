from modules.monticulo_min import Monticulo_Min


class Cola_de_Espera:
    def __init__(self):
        self.cola = Monticulo_Min()
        self.tamaño_actual = self.cola.tamaño_actual

    
    def insertar_paciente(self, paciente):
        return self.cola.insertar_valor(paciente)

    def __iter__(self):
        for i in self.cola:
            yield i
    
    def atiende_paciente(self):
        return self.cola.sacar_raiz()
    
