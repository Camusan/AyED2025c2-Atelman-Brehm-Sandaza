# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
# -*- coding: utf-8 -*-
from monticulo_min import Monticulo_Min 
from paciente import Paciente
from cola_de_espera import Cola_de_Espera
"""
Sala de emergencias
"""

import time
import datetime
import modules.paciente as pac
import random

n = 20  # cantidad de ciclos de simulación

cola_de_espera = Cola_de_Espera()
# Ciclo que gestiona la simulación
for i in range(n):
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente un paciente por segundo
    # La criticidad del paciente es aleatoria
    paciente =Paciente()
    print('*'*40)
    print('Llega un nuevo paciente:', paciente)
    print('*'*40)
    cola_de_espera.insertar_paciente(paciente)
    for paciente in cola_de_espera:
        paciente.prioridad+=1
    

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5:
        # se atiende paciente que se encuentra al frente de la cola
        paciente_atendido = cola_de_espera.atiende_paciente()
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido, 'con prioridad', paciente_atendido.prioridad)
        print('*'*40)
    else:
        # se continúa atendiendo paciente de ciclo anterior
        pass
    
    print()

    # Se muestran los pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', cola_de_espera.tamaño_actual)
    for paciente in cola_de_espera:
        print('\t', paciente,paciente.prioridad)
    
    print()
    print('-*-'*15)
    
    time.sleep(1)