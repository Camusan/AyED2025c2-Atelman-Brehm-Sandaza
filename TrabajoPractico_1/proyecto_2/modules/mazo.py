from modules.LDE import ListaDobleEnlazada  # Importa la clase ListaDobleEnlazada
from modules.carta import Carta
class DequeEmptyError(Exception):
     pass # Define una excepción personalizada para cuando el mazo está vacío
    


    
class Mazo:
    def __init__(self):
        self.mazo = ListaDobleEnlazada()
        

    def poner_carta_arriba(self,carta1):
        if  not isinstance(carta1,Carta):
            raise Exception("Debemos agregar un objeto de tipo carta al mazo")
        self.mazo.agregar_al_inicio(carta1)

        

    def sacar_carta_arriba(self,mostrar=False):
        if self.mazo.tamanio==0:
            raise DequeEmptyError("El mazo está vacío")
        carta= self.mazo.extraer(0)
        if mostrar:
            print(carta)
        return carta


    def poner_carta_abajo(self,carta1):
        if not isinstance(carta1,Carta):
            raise Exception("Debemos agregar un objeto de tipo carta al mazo")
        self.mazo.agregar_al_final(carta1)
        
    def __len__(self):
        return self.mazo.tamanio

        
if __name__ == "__main__":
    mazo1 = Mazo()
    carta1 = Carta("♣", "3")
    carta2 = Carta("♦", "K")
    carta2.visible = True
    mazo1.poner_carta_arriba(carta1)
    mazo1.poner_carta_arriba(carta2)
    print(mazo1.mazo.cabeza.dato)
    carta_control=mazo1.sacar_carta_arriba()
     # Debería imprimir la carta2
    print(carta_control)  # Debería imprimir la carta2
