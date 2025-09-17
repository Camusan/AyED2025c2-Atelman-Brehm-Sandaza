from matplotlib import pyplot as plt
from modules.tiempos import medir_tiempos
from modules.Burbuja import ordenamiento_burbuja
from modules.quicksort import ordenamientoRapido,ordenamientoRapidoAuxiliar,particion
from modules.radix_sort import ordenamiento_radix
import time 
from random import randint

def graficar_tiempos(lista_metodos_ord):
    tamanos = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

    # figsize es el tamaño de la figura en pulgadas (width, height)
    plt.figure(figsize=(10, 6))
    for metodo_ord in lista_metodos_ord:
        
        tiempos = medir_tiempos(metodo_ord, tamanos)

        # plot es para graficar los tiempos de ordenamiento
        # plot es el método de matplotlib para graficar
        # marker='o' es para poner un punto en cada coordenada
        plt.plot(tamanos, tiempos, marker='o', label=metodo_ord.__name__)

    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de tiempos de ordenamiento')
    plt.legend() # para mostrar el nombre del método de ordenamiento. Es el "label" del metodo plot
    plt.grid() # cuadriculado
    plt.show()

if __name__ == '__main__':
    lista_metodos_ord = [ordenamiento_burbuja, ordenamiento_radix, ordenamientoRapido]
    graficar_tiempos(lista_metodos_ord)