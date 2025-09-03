# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
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

    def insertar(self,dato,posicion=None):#Salio error en el test al insertar en el interior
        if posicion < 0 or posicion > self.tamanio:
            raise Exception("Posicion Invalida")
        if posicion == 0:
            self.agregar_al_inicio(dato)
        elif posicion == self.tamanio:
            self.agregar_al_final(dato)
        else:
            nuevo_nodo = Nodo(dato)
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            
            anterior = actual.anterior
            nuevo_nodo.anterior = anterior
            nuevo_nodo.siguiente = actual
            anterior.siguiente = nuevo_nodo
            actual.anterior = nuevo_nodo
            self.tamanio += 1

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

    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self.cabeza
        while actual is not None:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia

    def invertir(self):
        if self.esta_vacia():
            return self
        actual = self.cabeza
        self.cola = self.cabeza 
        while actual is not None:
            actual.siguiente, actual.anterior = actual.anterior, actual.siguiente
            if actual.anterior is None:
                self.cabeza = actual 
            actual = actual.anterior
        return self
        
    def concatenar(self, otra_lista):
        if otra_lista.esta_vacia():
            return self
        copiar_otra = otra_lista.copiar()
        if self.esta_vacia():
            self.cabeza = copiar_otra.cabeza
            self.cola = copiar_otra.cola
        else:
            self.cola.siguiente = copiar_otra.cabeza
            copiar_otra.cabeza.anterior = self.cola
            self.cola = copiar_otra.cola
        self.tamanio += copiar_otra.tamanio
        return self
        
    def __len__(self):
        return self.tamanio
        
    def __add__(self, otra_lista):
        nueva_lista = self.copiar()
        nueva_lista.concatenar(otra_lista)
        return nueva_lista

    def __iter__(self):
        actual = self.cabeza
        for i in range(self.tamanio):
            yield actual.dato
            actual = actual.siguiente

    def __str__(self):
        elementos = []
        actual = self.cabeza
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " <-> ".join(elementos)

if __name__ == "__main__":
    lista=ListaDobleEnlazada()
    
    
