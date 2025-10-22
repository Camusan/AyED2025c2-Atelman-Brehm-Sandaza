# 🐍Simulación de Sala de Emergencias 

Breve descripción del proyecto:

En este script temenos la implementacion de una cola de prioridad cuyo funcionamiento interno es la de un algoritmo de ordenamiento, concretamente estamos hablando de un monticulo de minimo.El fin de nuestra cola de prioridad es usarla en la simulacion de una sala de espera donde van llegando pacientes y son ordenados en la cola de espera segun su nivel de criticidad y orden de llegada

---
## 🏗Arquitectura General

En la carpeta Modules constamos con los siguientes archivos:

-Cola_de_espera:Aqui tenemos definida la clase Cola_de_espera que implementa la cola de prioridad usando un monticulo de minimo con los 
siguientes dos metodos agregar y eliminar.

-monticulo_min:Aqui implementamos nuestro monticulo que funnciona mediante el parametro de criticidad de los objetos pacientes, el mismo cuenta con los metodos raiz, sacar_raiz, insertar_valor, hijo_min, infiltrar_abajo, infiltrar_arriba.

-paciente:Esta clase fue proporcionada por la catedra y posee una lista con determinados apellidos y nombres ára que a la hora de instanciar objetos pacientes su nombre sea aleatorio, tambien cuenta con los parametros riesgo, descripcion y prioridad.A su vez posee los siguientes tres metodos get_nombre, get_apellido, get_descripcion_riesgo

-sala_emergencias:Dicho archivo fue proporionado por la catedra y simula una sala de emergencias con un evento de llegada de un paciente con cierta probabilidad de ser atendido, a su vez se simulada la llegada de un paciente mediante la iteracion for 20 veces,.Aqui es donde implementamos todas las clases que desarrollamos anteriormente. 





---
## 📑Dependencias

1. **Python 3.x**
2. 

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


