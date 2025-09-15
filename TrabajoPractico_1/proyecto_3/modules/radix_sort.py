def ordenamiento_radix(una_lista):
    max_digito=max(una_lista)#Obtenemos el numero mas grande y lo vamos diviviendo por 10 cada vez
    exp=1#Empieza en 1 y lo vamos multiplicando por 10, pasando de unidades a decenas y cenetnas, ect.
    lista_aux=una_lista.copy()
    while max_digito/exp>0:
        categoria=[]
        for i in range(10):
            categoria.append([])#Creamos una lista vacia con 10 sulistas en su interior donde pondremos digitos del 0 al 9
        for numero in lista_aux:
            digito=(numero//exp)%10#Obtenemos el numero segun el indice 
            categoria[digito].append(numero)#Lo agregamos a la sublista correspondiente
        lista_aux=[]
        for i in range(10):
            lista_aux.extend(categoria[i])
        exp*=10#Multiplicamos por 10 para pasar a la siguiente posicion
    return lista_aux

if __name__ == '__main__':
    una_lista = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Lista original:", una_lista)
    lista_ordenada = ordenamiento_radix(una_lista)
    print("Lista ordenada:", lista_ordenada)
