class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
        self.anterior=None    

    
        
class ListaDobleEnlazada:   
    def __init__(self):
        self.cabeza=None
        self.cola=None
        self.tamanio=0