# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

class NodoArbol:
    def __init__(self,clave,valor=None,izquierdo=None,derecho=None,padre=None):
        self.clave=clave
        self.valor=valor
        self.hijo_izquierdo=izquierdo
        self.hijo_derecho=derecho
        self.padre=padre
        self.factor_equilibrio=0

    def esHijoIzquierdo(self):
            return self.padre != None and self.padre.hijo_izquierdo == self

    def esHijoDerecho(self):
            return self.padre != None and self.padre.hijo_derecho == self

    def esRaiz(self):
            return self.padre == None
    
    def obtenerHijo_izquierdo(self):
        return self.hijo_izquierdo

    def obtenerHijo_derecho(self):
        return self.hijo_derecho

    def obtenerValorRaiz(self):
        return (self.clave, self.valor)


class ArbolAVL:
    def __init__(self):
        self.raiz=None
        self.tamaño=0
        
    def insertar(self, clave, valor):
        if self.raiz is None:
            self.raiz = NodoArbol(clave, valor)
            self.tamaño += 1
        else:
            self._insertar(clave, valor, self.raiz)

    def _insertar(self, clave, valor, nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.hijo_izquierdo is not None:
                self._insertar(clave, valor, nodoActual.hijo_izquierdo)
            else:
                nodoActual.hijo_izquierdo = NodoArbol(clave, valor, padre=nodoActual)
                self.tamaño += 1
                self.rebalancear(nodoActual.hijo_izquierdo)
        else:
            if nodoActual.hijo_derecho is not None:
                self._insertar(clave, valor, nodoActual.hijo_derecho)
            else:
                nodoActual.hijo_derecho = NodoArbol(clave, valor, padre=nodoActual)
                self.tamaño += 1
                self.rebalancear(nodoActual.hijo_derecho)

    def rebalancear(self,nodo):#Sinonimo de actualizar 
        if nodo.factor_equilibrio >1 or nodo.factor_equilibrio <-1:
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
                self.rotarDerecha(nodo.hijo_derecho)
                self.rotarIzquierda(nodo)
            else:
                self.rotarIzquierda(nodo)
        elif nodo.factor_equilibrio>0:
            if nodo.hijo_izquierdo.factor_equilibrio<0:
                self.rotarIzquierda(nodo.hijo_izquierdo)
                self.rotarDerecha(nodo)
            else:
                self.rotarDerecha(nodo)

    def buscar(self,clave,nodoActual):
        if nodoActual.clave==clave:
            return nodoActual.valor
        elif clave<nodoActual.clave and nodoActual.hijo_izquierdo != None:
            return self.buscar(clave,nodoActual.hijo_izquierdo)
        elif clave>nodoActual.clave and nodoActual.hijo_derecho != None:
            return self.buscar(clave,nodoActual.hijo_derecho)
        if nodoActual is None:
            return None

    def obtener(self,clave):
        if self.raiz:
            res = self._obtener(clave,self.raiz)
            if res:
                return res.valor
            else:
                return None
        else:
            return None

    def _obtener(self,clave,nodoActual):
        if not nodoActual:
            return None
        elif nodoActual.clave == clave:
            return nodoActual
        elif clave < nodoActual.clave:
            return self._obtener(clave,nodoActual.hijo_izquierdo)
        else:
            return self._obtener(clave,nodoActual.hijo_derecho)
        
    
    def recorrer_arbol(self, arbol):
        if arbol is not None:
            self.recorrer_arbol(arbol.obtenerHijo_izquierdo())
            print(arbol.obtenerValorRaiz())
            self.recorrer_arbol(arbol.obtenerHijo_derecho())

    def eliminar(self,clave):
        if self.tamaño>1:
           nodoEliminar=self.buscar(clave,self.raiz)
           if nodoEliminar:
               self._eliminar(nodoEliminar)
               self.tamaño-=1
           else:
               raise KeyError('Error, la clave no está en el árbol')
        elif self.tamaño==1 and self.raiz.clave==clave:
            self.raiz=None
            self.tamaño-=1
        else:
            raise KeyError('Error, la clave no está en el árbol')
    def __delitem__(self,clave):
        self.eliminar(clave)

    def _eliminar(self,nodo):
        #Caso 1: El nodo es hoja
        if nodo.hijo_izquierdo is None and nodo.hijo_derecho is None:
            padre = nodo.padre
            if nodo.esRaiz():
                self.raiz = None
            elif nodo.esHijoIzquierdo():
                nodo.padre.hijo_izquierdo = None
            else:
                nodo.padre.hijo_derecho = None
            self.rebalancear(padre)
        # Caso 2: Un solo hijo
        elif nodo.hijo_izquierdo is None:
            hijo = nodo.hijo_derecho
            if nodo.esRaiz():
                self.raiz = hijo
                hijo.padre = None
            elif nodo.esHijoIzquierdo():
                nodo.padre.hijo_izquierdo = hijo
                hijo.padre = nodo.padre
            else:
                nodo.padre.hijo_derecho = hijo
                hijo.padre = nodo.padre
            self.rebalancear(hijo.padre)
        elif nodo.hijo_derecho is None:
            hijo = nodo.hijo_izquierdo
            if nodo.esRaiz():
                self.raiz = hijo
                hijo.padre = None
            elif nodo.esHijoIzquierdo():
                nodo.padre.hijo_izquierdo = hijo
                hijo.padre = nodo.padre
            else:
                nodo.padre.hijo_derecho = hijo
                hijo.padre = nodo.padre
            self.rebalancear(hijo.padre)
        # Caso 3: Dos hijos
        else:
            sucesor = self._minimo(nodo.hijo_derecho)
            nodo.clave = sucesor.clave
            nodo.valor = sucesor.valor
            self._eliminar(sucesor)

    def inorden_rango(self,nodo,fecha1, fecha2,resultados=None):
            if resultados is None:
                resultados=[]
            if nodo is None:
                return resultados
            if nodo.clave > fecha1:
                self.inorden_rango(nodo.obtenerHijo_izquierdo(), fecha1, fecha2, resultados)
            if fecha1 <= nodo.clave <= fecha2:
                resultados.append(f"{nodo.clave.strftime('%d/%m/%Y')}: {nodo.valor} ºC")
            if nodo.clave < fecha2:
                self.inorden_rango(nodo.obtenerHijo_derecho(), fecha1, fecha2, resultados)
            return resultados

    def _minimo(self,nodo):
        while nodo.hijo_izquierdo is not None:
            nodo = nodo.hijo_izquierdo
        return nodo

  
    def min_rango(self, nodo, fecha1, fecha2, min_temp=None):
        if nodo is None:
            return min_temp
        if nodo.clave > fecha1:
            min_temp = self.min_rango(nodo.obtenerHijo_izquierdo(), fecha1, fecha2, min_temp)
        if fecha1 <= nodo.clave <= fecha2:
            if (min_temp is None) or (nodo.valor < min_temp):
                min_temp = nodo.valor
        if nodo.clave < fecha2:
            min_temp = self.min_rango(nodo.obtenerHijo_derecho(), fecha1, fecha2, min_temp)
        return min_temp

    def max_rango(self, nodo, fecha1, fecha2, max_temp=None):
        if nodo is None:
            return max_temp
        if nodo.clave > fecha1:
            max_temp = self.max_rango(nodo.obtenerHijo_izquierdo(), fecha1, fecha2, max_temp)
        if fecha1 <= nodo.clave <= fecha2:
            if (max_temp is None) or (nodo.valor > max_temp):
                max_temp = nodo.valor
        if nodo.clave < fecha2:
            max_temp = self.max_rango(nodo.obtenerHijo_derecho(), fecha1, fecha2, max_temp)
        return max_temp

    def rotarIzquierda(self,rotRaiz=NodoArbol):
        nuevaRaiz = rotRaiz.hijo_derecho
        rotRaiz.hijo_derecho = nuevaRaiz.hijo_izquierdo
        if nuevaRaiz.hijo_izquierdo != None:
            nuevaRaiz.hijo_izquierdo.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo():
                rotRaiz.padre.hijo_izquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijo_derecho = nuevaRaiz
        nuevaRaiz.hijo_izquierdo = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factor_equilibrio = rotRaiz.factor_equilibrio + 1 - min(nuevaRaiz.factor_equilibrio, 0)
        nuevaRaiz.factor_equilibrio = nuevaRaiz.factor_equilibrio + 1 + max(rotRaiz.factor_equilibrio, 0)
        return nuevaRaiz
    
    def rotarDerecha(self,rotRaiz=NodoArbol):
        nuevaRaiz= rotRaiz.hijo_izquierdo
        rotRaiz.hijo_izquierdo=nuevaRaiz.hijo_derecho
        if nuevaRaiz.hijo_derecho!=None:
            nuevaRaiz.hijo_derecho.padre=rotRaiz
        nuevaRaiz.padre= rotRaiz.padre 
        if rotRaiz.esRaiz():
            self.raiz=nuevaRaiz
        else:
            if rotRaiz.esHijoDerecho():
                rotRaiz.padre.hijo_derecho=nuevaRaiz
            else:
                rotRaiz.padre.hijo_izquierdo=nuevaRaiz
        nuevaRaiz.hijo_derecho=rotRaiz
        rotRaiz.padre=nuevaRaiz
        rotRaiz.factor_equilibrio=rotRaiz.factor_equilibrio -1 - max(nuevaRaiz.factor_equilibrio,0)
        nuevaRaiz.factor_equilibrio=nuevaRaiz.factor_equilibrio -1 + min(rotRaiz.factor_equilibrio,0)
        return nuevaRaiz

    def rotarIzquierdaDerecha(self, nodo):
        nodo.hijo_izquierdo = self.rotarIzquierda(nodo.hijo_izquierdo)
        return self.rotarDerecha(nodo)
    
    def rotarDerechaIzquierda(self, nodo):
        nodo.hijo_derecho = self.rotarDerecha(nodo.hijo_derecho)
        return self.rotarIzquierda(nodo)
    
if __name__ == "__main__":
    arbol=ArbolAVL()
    #rbol.insertar(50,10)
    #arbol.eliminar(50)
    