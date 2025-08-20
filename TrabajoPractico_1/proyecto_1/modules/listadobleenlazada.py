# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
        self.anterior=None    

    @property
    def dato(self):
        return self.dato
        
class ListaDobleEnlazada:   
    def __init__(self):
        self.cabeza=None
        self.cola=None
        self.tamaño=0
        
    def esta_vacia(self):
        if self.tamaño == 0:
            return True
        else:
            return False

    def agregar_al_inicio(self,item):
        nuevo_nodo= Nodo(item)
        if self.tamaño==0:
            self.cabeza=nuevo_nodo
            self.cola=nuevo_nodo
        else:
            nuevo_nodo.siguiente=self.cabeza
            self.cabeza.anterior=nuevo_nodo
            self.cabeza=nuevo_nodo
        self.tamaño += 1

    def agregar_al_final(self,item):
        nuevo_nodo=Nodo(item)
        if self.tamaño==0:
            self.cabeza=nuevo_nodo
            self.cola=nuevo_nodo
        else:
            self.cola.siguiente=nuevo_nodo
            nuevo_nodo.anterior=self.cola
            self.cola=nuevo_nodo
        self.tamaño+=1
    
    def insertar(self,dato,posicion):
        if posicion < 0 or posicion > self.tamaño:
            raise Exception("Posicion Invalida")
        if posicion == 0:
            self.agregar_al_inicio(dato)
        elif posicion == self.tamaño:
            self.agregar_al_final(dato)
        else:
            nuevo_nodo = Nodo(dato)
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            nuevo_nodo.anterior = actual.anterior
            nuevo_nodo.siguiente = actual
            actual.anterior.siguiente = nuevo_nodo
            actual.anterior = nuevo_nodo
            self.tamaño +=1
        
    def extraer_posicion(self,posicion=None):
        if self.esta_vacia():
            raise IndexError("La lista está vacía")
        if posicion is None:
            posicion = self.tamaño - 1
        if posicion < 0 or posicion >= self.tamaño:
            raise IndexError("Posición fuera de rango")
        if posicion == 0:
            dato = self.cabeza.dato
            if self.tamaño == 1:
              self.cabeza = None
              self.cola = None
            else:
                self.cabeza = self.cabeza.siguiente
                self.cabeza.anterior = None
            self.tamaño -= 1
            return dato
        if posicion == self.tamaño - 1:
            dato = self.cola.dato
            if self.tamaño == 1:
                self.cabeza = None
                self.cola = None
            else:
                self.cola = self.cola.anterior
                self.cola.siguiente = None
            self.tamaño -= 1
            return dato
        actual = self._obtener_nodo(posicion)
        dato = actual.dato

        actual.anterior.siguiente = actual.siguiente
        actual.siguiente.anterior = actual.anterior

        self.tamaño -= 1
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
        while actual is not None:
            actual.siguiente, actual.anterior = actual.anterior, actual.siguiente
            if actual.anterior is None:
                self.cabeza = actual
            actual = actual.anterior
        self.cola = self.cabeza
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
            self.tamaño += copiar_otra.tamaño
            return self
        
    def __len__(self):
        return self.tamaño
        
    def __add__(self, otra_lista):
        nueva_lista = self.copiar()
        nueva_lista.concatenar(otra_lista)
        return nueva_lista

    def __iter__(self):
        actual = self.cabeza
        for i in range(self.tamaño):
            yield actual.dato
            actual = actual.siguiente


if __name__ == "__main__":
    nodo=Nodo(5.2)
    print(nodo.dato)


