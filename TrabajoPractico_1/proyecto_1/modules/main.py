# -*- coding: utf-8 -*-
"""
Sala de emergencias
"""

from ayedfiuner.estructuras.cola_de_prioridad import ColaPrioridad
import time
import datetime
import random
import paciente as pac

n = 20

cola_de_espera = ColaPrioridad()

orden_llegada = 0

for i in range(n):

    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')

    print('-*-' * 15)
    print('\n', fecha_y_hora, '\n')

    # Crear paciente
    paciente = pac.Paciente()

    print('Ingresa paciente:')
    print('\t', paciente)

    # Insertar en cola de prioridad
    cola_de_espera.insertar((paciente.get_riesgo(), orden_llegada, paciente))

    orden_llegada += 1

    print()

    # Atención de paciente
    if random.random() < 0.5 and not cola_de_espera.esta_vacia():

        paciente_atendido = cola_de_espera.atender()[2]

        print('*' * 40)
        print('Se atiende el paciente:',
              paciente_atendido)
        print('*' * 40)

        print('\nCola de espera luego de atender al paciente:')

        if cola_de_espera.esta_vacia():
            print('No hay pacientes en espera.')
        else:
            elementos = cola_de_espera.monticulo.listaMonticulo[1:] 
            # elementos_ordenados = sorted(elementos) 

            for riesgo, llegada, paciente in elementos:
                print(f'Riesgo: {riesgo} | 'f'Orden llegada: {llegada} | 'f'Paciente: {paciente}')

    print()
    print('Pacientes que faltan atenderse:',
          cola_de_espera.tamano())

    print()
    print('-*-' * 15)

    time.sleep(0)

print("\nTERMINADO")

print("\nPacientes pendientes al finalizar la simulación:")

if cola_de_espera.esta_vacia():
    print("No quedaron pacientes pendientes.")
else:
    elementos = cola_de_espera.monticulo.listaMonticulo[1:]
    elementos_ordenados = sorted(elementos)

    for riesgo, llegada, paciente in elementos_ordenados:
        print(f'Riesgo: {riesgo} | 'f'Orden llegada: {llegada} | 'f'Paciente: {paciente}')