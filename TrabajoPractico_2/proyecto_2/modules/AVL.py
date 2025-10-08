# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

class NodoArbol:
    def __init__(self,clave,valor=None,izquiero=None,derecho=None,padre=None):
        self.clave=clave
        self.valor=valor
        self.hijo_izquiero_izquierdo
        self.hijo_derecho=derecho
        self.padre=padre
        self.factor_equilibrio=0

        def esHijoIzquierdo(self):
            return self.padre != None and self.padre.hijo_izquierdo == self

        def esHijoDerecho(self):
            return self.padre != None and self.padre.hijo_derecho == self

class ArbolAVL:
    def __init__(self):
        self.raiz=None
        self.tamaño=0
        
    def insertar(self,clave,valor,nodoActual):
        if clave<nodoActual.clave:
            if nodoActual.hijo_izquiero != None:
                self.insertar(clave,valor,nodoActual.hijo_izquiero)
            else:
                nodoActual.hijo_izquiero=NodoArbol(clave,valor,padre=nodoActual)
                self.tamaño+=1
                self.rebalancear(nodoActual.hijo_izquiero)
        else:
            if nodoActual.hijo_derecho != None:
                self.insertar(clave,valor,nodoActual.hijo_derecho)
            else:
                nodoActual.hijo_derecho=NodoArbol(clave,valor,padre=nodoActual)
                self.tamaño+=1
                self.rebalancear(nodoActual.hijo_derecho)

    def rebalancear(self,nodo):#Sinomimo de actualizar 
        if nodo.factor_equlibrio >1 or nodo.factor_equilibrio <-1:
            self.requilibrar(nodo)
            return
        if nodo.padre != None:
            if nodo.esHijoIzquierdo():
                nodo.padre.factor_equilibrio+=1
            elif nodo.esHijoDerecho():
                nodo.padre.factor_equilibrio-=1
            if nodo.padre.factor_equilibrio !=0:
                self.rebalancear(nodo.padre)

    def requilibrar(self,nodo):
        if nodo.factor_equilibrio<0:
            if nodo.hijo_derecho.factor_equilibrio>0:
                self.rotacionDerecha(nodo.hijo_derecho)
                self.rotacionIzquierda(nodo)
            else:
                self.rotacionIzquierda(nodo)
        elif nodo.factor_equilibrio>0:
            if nodo.hijo_izquierdo.factor_equilibrio<0:
                self.rotacionIzquierda(nodo.hijo_izquierdo)
                self.rotacionDerecha(nodo)
            else:
                self.rotacionDerecha(nodo)

    def rotacionIzquierda(self,nodo):
        pass
                