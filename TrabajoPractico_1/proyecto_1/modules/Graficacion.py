from modules.Problema1 import ListaDobleEnlazada
from matplotlib import pyplot as plt
from random import randint
import time

elementos = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
tiempo_len = []
tiempo_copiar= []
tiempo_invertir= []
for n in elementos:
    lista= ListaDobleEnlazada()
    for i in range(n):
        dato=randint(1,100)
        lista.agregar_al_final(dato)
    contador=0
    for i in range(n):
        inicio=time.perf_counter()
        lista.__len__()
        fin=time.perf_counter()
        contador=fin-inicio
    tiempo_len.append(contador)
    
    contador=0
    for i in range(n):
        inicio=time.perf_counter()
        lista.copiar()
        fin=time.perf_counter()
        contador=fin-inicio
    tiempo_copiar.append(contador)

    contador=0
    for i in range(n):
        inicio=time.perf_counter()
        lista.invertir()
        fin=time.perf_counter()
        contador=fin-inicio
    tiempo_invertir.append(contador)

#Grafico de los tres metodos
plt.figure(figsize=(10, 6))
plt.plot(elementos, tiempo_len, marker='o', label='Tiempo de len()')
plt.plot(elementos, tiempo_copiar, marker='o', label='Tiempo de copiar()')
plt.plot(elementos, tiempo_invertir, marker='o', label='Tiempo de invertir()')
plt.xlabel('Número de elementos en la lista')
plt.ylabel('Tiempo en segundos')
plt.title('Comparación de cantidad de elementos vs tiempo de ejecucion de los metodos len(), copiar() e invertir()')
plt.legend()
plt.grid()
plt.show()    

