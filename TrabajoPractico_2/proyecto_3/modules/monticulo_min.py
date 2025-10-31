#Codigo extraido del problema 1 TP2 pero modificado para que el criterio de orden en el monticulo sea
#la distancia entre aldeas vecinas 
from modules.vertice import Vertice
 
class Monticulo_Min:
    def __init__(self):
        self.lista_monticulo=[None]
        self.tamaño_actual=0


    def __iter__(self):
        return iter(self.lista_monticulo[1:])  # Ignorar el primer elemento NoneS

    def raiz(self):#Seria paciente con mayor criticidad
        if self.tamaño_actual>=1:
            return self.lista_monticulo[1]
        else:
            return None
    
    def construirMonticulo(self, lista_valores):
        "Construye un montículo mínimo a partir de una lista de valores."
        self.tamaño_actual = len(lista_valores)
        self.lista_monticulo = [None] + lista_valores[:]
        i = self.tamaño_actual // 2
        while i > 0:
            self.infiltrar_abajo(i)
            i -= 1

    def sacar_raiz(self):#Se atiende paciente con mayor criticidad
        '''Saca la raiz de un arbol y toma el ultimo valor agrega y lo pone en la raiz
        y va infiltrando hacia abajo si es necesario'''
        valorSacado = self.lista_monticulo[1]
        self.lista_monticulo[1] = self.lista_monticulo[self.tamaño_actual]
        self.tamaño_actual = self.tamaño_actual - 1
        self.lista_monticulo.pop()
        self.infiltrar_abajo(1)
        return valorSacado

    def insertar_valor(self, vertice:Vertice):#LLega un nuevo paciente
        self.lista_monticulo.append(vertice)
        self.tamaño_actual += 1
        self.infiltrar_arriba(self.tamaño_actual)
        self.infiltrar_abajo(self.tamaño_actual)


    def hijo_min(self, i):
        "Devuelve el hijo menor del monticulo de minimo según riesgo y prioridad"
        if i > len(self.lista_monticulo)-1:
            raise IndexError("El indice esta fuera de rango")
        if i * 2 + 1 > self.tamaño_actual:
            return i * 2
        izq_idx = i * 2
        der_idx = i * 2 + 1

        hijo_izq = self.lista_monticulo[izq_idx]
        hijo_der = self.lista_monticulo[der_idx]
        d_izq = hijo_izq.obtenerDistancia()
        d_der = hijo_der.obtenerDistancia()
        if d_izq <= d_der:
            return izq_idx
        else:
            return der_idx

    def infiltrar_abajo(self, i):
        # se infiltra hacia abajo cuando el ancestro es mayor al hijo
        while (i*2) <= self.tamaño_actual:
            hijo_min = self.hijo_min(i)
            actual = self.lista_monticulo[i]
            hijo = self.lista_monticulo[hijo_min]
            # comparar por la distancia asociada (criterio para Prim)
            try:
                if actual.obtenerDistancia() > hijo.obtenerDistancia():
                    self.lista_monticulo[i], self.lista_monticulo[hijo_min] = hijo, actual
            except Exception:
                # si por alguna razón los elementos no exponen obtenerDistancia,
                # caemos silenciosamente (no intercambiamos)
                pass
            i = hijo_min

    def infiltrar_arriba(self, i):
      # se infiltra hacia arriba cuando el hijo es menor al ancestro
        while i // 2 > 0:
            actual = self.lista_monticulo[i]
            padre = self.lista_monticulo[i // 2]
            try:
                if actual.obtenerDistancia() < padre.obtenerDistancia():
                    self.lista_monticulo[i], self.lista_monticulo[i // 2] = padre, actual
            except Exception:
                # si no tienen obtenerDistancia, no intentar comparar
                pass
            i = i // 2
