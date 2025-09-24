# 🐍Implementaciòn de una Lista Doblemente Enlazada 

Trabajamos en el TAD "Lista Doblemente Enlazada"(estructura de tipo lineal) en la cual usamos dos clases para su correcto funcionamiento, una es la lista propiamente dicha y la otra es el nodo es cual nos porporcioa la estructura interna de la misma,a su vez teniendo referencias  del nodo siguiente y del anterior.Una vez implementado esto comenzamos a crear opreaciones tipicas de un TAD como lo puede ser el ver un elemento, agregar o eliminarr.Las operaciones concretas que implementamos fueron las siguientes:
   -esta_vacia()
   -agregar_al_inicio(item)
   -agregar_al_final(item)
   -insertar(item, posicion)
   -extraer(posicion)
   -copiar()
   -invertir()
   -concatenar(Lista)
   -__len__()
   -__add__(Lista)
   -__iter__()
Por ultimo para saber si nuestros metodos funcionan ejecutamos sus respectivos test(buscamos testear las funciones principales) y tambien graficamos tres metodos para analisar su complejidad(variando la cantidad de elementos de una lista y observar su costo temporal)

---
## 🏗Arquitectura General

-En la carpeta Modules tenemos los siguientes archivos:
   _Problema1:En este sitio tenemos la implementacion del codigo respecto a la LDE con sus opeaciones tipicas 
   _Graficacion:En este sitio implementamos un metodo para graficar los metodos len(),copiar() e invertir()

-En la carpeta tests tenemos el siguiente archivo:
   _testE1:Aqui testeamos las operaciones de nuestra lista doblemente enlazada 
---
## 📑Dependencias

1. **Python 3.x**
2. **matplotlib** (`pip install matplotlib`)


---
## 🚀Cómo Ejecutar el Proyecto
1. **Clonar o descargar** el repositorio.

2. **Crear y activar** un entorno virtual.

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
   El archivo `requirements.txt` se encuentran en la carpeta [deps](./deps) del proyecto.

---
## 🙎‍♀️🙎‍♂️Autores

-Atelman Maia
-Brehm Mauro Xavier 
-Sandaza Iturraspe Camila 



> 
