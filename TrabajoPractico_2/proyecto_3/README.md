# 🕊️ Palomas mensajeras  🕊️ 

Este proyecto implementa un sistema para optimizar la red de comunicación entre aldeas utilizando el algoritmo de Prim para encontrar el Árbol de Expansión Mínima (MST). El objetivo es establecer una red eficiente que permita la distribución de noticias entre todas las aldeas con el menor costo posible en términos de distancia total.

---
## 🏗Arquitectura General


 # 📦 Módulos principales

- **grafo.py**: Implementa la clase `Grafo` que representa la red de aldeas
  - Maneja la estructura del grafo y sus conexiones
  - Permite cargar datos desde archivo de texto
  - Gestiona las conexiones entre vértices y sus pesos

- **vertice.py**: Define la clase `Vertice` para representar cada aldea
  - Almacena información de distancias y predecesores
  - Mantiene registro de conexiones con otras aldeas
  - Implementa métodos para obtener/asignar atributos

- **cola_prioridad.py**: Implementa la `Cola_de_Prioridad` para el algoritmo de Prim
  - Basada en montículo mínimo
  - Permite operaciones de inserción y extracción eficientes
  - Soporta actualización de prioridades

- **monticulo_min.py**: Implementa el `Monticulo_Min` como estructura base
  - Mantiene la propiedad de montículo mínimo
  - Proporciona operaciones fundamentales del montículo

- **prim.py**: Contiene el algoritmo principal y funciones auxiliares
  - Implementa el algoritmo de Prim para MST
  - Calcula la distancia total de la red
  - Genera el plan de distribución de noticias

### 📊 Datos y Documentación
- Los datos de entrada se encuentran en la carpeta [data](./data) del proyecto
- La documentación detallada está disponible en la carpeta [docs](./docs)

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
- Brehm Mauro
- Sandaza Iturraspe Camila 

---
