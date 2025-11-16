from paciente import Paciente
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
    
    

    def sacar_raiz(self):#Se atiende paciente con mayor criticidad
        '''Saca la raiz de un arbol y toma el ultimo valor agrega y lo pone en la raiz
        y va infiltrando hacia abajo si es necesario'''
        valorSacado = self.lista_monticulo[1]
        self.lista_monticulo[1] = self.lista_monticulo[self.tamaño_actual]
        self.tamaño_actual = self.tamaño_actual - 1
        self.lista_monticulo.pop()
        self.infiltrar_abajo(1)
        return valorSacado
    
    def insertar_valor(self, valor):#LLega un nuevo paciente 
        self.lista_monticulo.append(valor)
        self.tamaño_actual += 1
        self.infiltrar_arriba(self.tamaño_actual)
        



    def hijo_min(self, i):
        "Devuelve el hijo menor del monticulo de minimo según riesgo y prioridad"
        if i > len(self.lista_monticulo)-1:
            raise IndexError("El indice esta fuera de rango")
        if i * 2 + 1 > self.tamaño_actual:
            return i * 2
        else:
            hijo_izq = self.lista_monticulo[i*2]
            hijo_der = self.lista_monticulo[i*2+1]
            if (hijo_izq.riesgo, -hijo_izq.prioridad) < (hijo_der.riesgo, -hijo_der.prioridad):
                return i * 2
            else:
                return i * 2 + 1

    
    def infiltrar_abajo(self, i):
        # se infiltra hacia abajo cuando el ancestro es mayor al hijo
        while (i*2) <= self.tamaño_actual:
            hijo_min = self.hijo_min(i)
            actual = self.lista_monticulo[i]
            hijo = self.lista_monticulo[hijo_min]
            if (actual.riesgo, -actual.prioridad) > (hijo.riesgo, -hijo.prioridad):
                self.lista_monticulo[i], self.lista_monticulo[hijo_min] = hijo, actual
            i = hijo_min



    def infiltrar_arriba(self, i):
        # se infiltra hacia arriba cuando el hijo es menor al ancestro
        # se infiltra hacia arriba cuando el hijo es menor al ancestro
        while i // 2 > 0:
            actual = self.lista_monticulo[i]
            padre = self.lista_monticulo[i // 2]
            if (actual.riesgo, -actual.prioridad) < (padre.riesgo, -padre.prioridad):
                self.lista_monticulo[i], self.lista_monticulo[i // 2] = padre, actual
            i = i // 2

    


'''if __name__ == "__main__":
    monticulo = Monticulo_Min()
    pac1=Paciente()
    print(pac1.criticidad)
    pac2=Paciente()
    print(pac2.criticidad)
    monticulo.insertar_valor(pac1.criticidad)
    monticulo.insertar_valor(pac2.criticidad)
    print("Raíz del montículo:", monticulo.raiz())'''  # Debería imprimir la criticidad menor
    # monticulo.insertar_valor(5)
    # monticulo.insertar_valor(3)
    # monticulo.insertar_valor(8)
    # monticulo.insertar_valor(1)
    # monticulo.insertar_valor(4)

    # print("Raíz del montículo:", monticulo.raiz())  # Debería imprimir 1

    # print("Sacando la raíz:", monticulo.sacar_raiz())  # Debería imprimir 1
    # print("Nueva raíz del montículo:", monticulo.raiz())  # Debería imprimir 3

    # print("Sacando la raíz:", monticulo.sacar_raiz())  # Debería imprimir 3
    # print("Nueva raíz del montículo:", monticulo.raiz())  # Debería imprimir 4

if __name__ == "__main__":
        monticulo = Monticulo_Min()
        pac1=Paciente()
        print(pac1.riesgo, pac1.prioridad)
        pac2=Paciente()
        print(pac2.riesgo, pac2.prioridad)
        monticulo.insertar_valor(pac1)
        monticulo.insertar_valor(pac2)     
        # print("Raíz del montículo:", monticulo.raiz())  # Debería imprimir la criticidad menor
        # monticulo.insertar_valor(5)
        # monticulo.insertar_valor(3)       
        #   print("Sacando la raíz:", monticulo.sacar_raiz())
        #  print("Nueva raíz del montículo:", monticulo.raiz())
        # print("Sacando la raíz:", monticulo.sacar_raiz())
        # print("Nueva raíz del montículo:", monticulo.raiz())




