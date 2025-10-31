# 🐍Base de Datos de Temperaturas 

Breve descripción del proyecto:

Para este proyecto se nos solicito implementar una base de datos capaz de manetener las mediciones de la temepartura realizadas en una cierta fecha ,pero que a su vez tenga el funcionamiento interno de un Arbol AVL.Dicha base de datos debe ser capaz que agregar, quitar y mostrar las  mediciones, tambien deberia mostrar la temepratura maxina y minima en un rango determinado de timpo(fecha1 y fecha2) y poder leer un archivo de mediciones y ser cargadas  a la base de datos 

---
## 🏗Arquitectura General

En la carpeta Modules contamos con los siguientes archivos:
-AVL:Aqui tenemos implementado nuestro arbol AVL con los metodos necesarios para su correcto funcionamiento 
-Temperatura_BD:Esta clase tiene en su funcionamiento interno una instancia de un objeto AVL y llama a los metodos del mismo cuando debe trabajar con las mediciones 

En la carpeta Docs tenemos dos archivos:
-Informe 2 TP2:Aqui tendremos todo nuestro analisis de los ordenes de complejidad que poseen los metodos de nuestra Base de Datos
-TP N2:Tenemos a mano las consignas del TP2 para mayor comodidad y ver que requisitos debemos cumplir para cada ejercicio
---
## 📑Dependencias

1. **Python 3.x**


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
- Atelman Maia
- Brehm Mauro Xavier 
- Sandaza Iturraspe Camila 

---

