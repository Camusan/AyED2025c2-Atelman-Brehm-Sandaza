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

    def esta_vacia(self):
        return self.tamanio==0


    def agregar_al_inicio(self,item):
        nuevo_nodo= Nodo(item)
        if self.tamanio==0:
            self.cabeza=nuevo_nodo
            self.cola=nuevo_nodo
        else:
            nuevo_nodo.siguiente=self.cabeza
            self.cabeza.anterior=nuevo_nodo
            self.cabeza=nuevo_nodo
        self.tamanio += 1

    def agregar_al_final(self,item):
        nuevo_nodo=Nodo(item)
        if self.tamanio==0:
            self.cabeza=nuevo_nodo
            self.cola=nuevo_nodo
        else:
            self.cola.siguiente=nuevo_nodo
            nuevo_nodo.anterior=self.cola
            self.cola=nuevo_nodo
        self.tamanio+=1

    def extraer(self, posicion=None):
        if self.esta_vacia():
            raise Exception("Extraer de una lista vacia deberia arrojar un error")
        if posicion is None:
            posicion = self.tamanio - 1  # Extraer el último
        if posicion < 0:
            if abs(posicion) > self.tamanio:
                raise Exception("Extraer de una posicion fuera de rango debe arrojar error")
            posicion = self.tamanio + posicion  # Soporta negativos como Python
        if posicion >= self.tamanio or posicion < 0:
            raise Exception("Extraer de una posicion fuera de rango debe arrojar error")
        # Extraer cabeza
        if posicion == 0:
            dato = self.cabeza.dato
            if self.tamanio == 1:
                self.cabeza = None
                self.cola = None
            else:
                self.cabeza = self.cabeza.siguiente
                self.cabeza.anterior = None
            self.tamanio -= 1
            return dato
        # Extraer cola
        if posicion == self.tamanio - 1:
            dato = self.cola.dato
            if self.tamanio == 1:
                self.cabeza = None
                self.cola = None
            else:
                self.cola = self.cola.anterior
                self.cola.siguiente = None
            self.tamanio -= 1
            return dato
        # Extraer interior
        actual = self.cabeza
        for _ in range(posicion):
            actual = actual.siguiente
        dato = actual.dato
        actual.anterior.siguiente = actual.siguiente
        actual.siguiente.anterior = actual.anterior
        self.tamanio -= 1
        return dato