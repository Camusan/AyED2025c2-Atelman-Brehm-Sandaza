# Algoritmo de ordenamiento burbuja
# el ordenamiento burbuja es un algoritmo de ordenamiento simple
# que compara cada elemento de la lista con el siguiente y los intercambia si están en el orden incorrecto
# el algoritmo se repite varias veces
# en cada pasada se coloca el elemento más grande en su lugar correcto
# el algoritmo se detiene cuando no se realizan intercambios en una pasada

# orden de complejidad del ordenamiento burbuja corto es O(n^2)

from random import randint




def ordenamiento_burbuja(lista):
    for num_pasadas in range(len(lista)-1, 0, -1):#Nos aseguramos de hacer muchas pasadas como elementos tenga la lista
        for j in range(num_pasadas):
            if lista[j] > lista[j+1]:#Comparamos el elemento actual con el siguiente y si es necesario los cambiamos de lugar 
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista



if __name__ == '__main__':
    #Probamos si anda nuestro algortimo de ordenamiento 

    numeros = [5, 3, 8, 6, 7, 2]
    numeros = ordenamiento_burbuja(numeros)
    print(numeros)

    


