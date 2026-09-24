from modules.modulo1 import ColaCircular  # Donde tengo la clase ColaCircular

class Proceso:
    """Clase que representa un proceso en el sistema operativo."""
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def simular_round_robin(procesos_datos, tq=2, capacidad_cola=10):
    """
    Simula el algoritmo de planificación Round Robin y calcula Turnaround y Waiting time.
    
    Precondiciones:
        - procesos_datos es una lista de tuplas/listas con (PID, arrival_time, burst_time).
        - tq > 0 y capacidad_cola > 0.
    """
    # Crear lista de objetos Proceso ordenados por tiempo de llegada
    procesos = [Proceso(pid, at, bt) for pid, at, bt in procesos_datos]
    procesos.sort(key=lambda p: p.arrival_time)
    
    ready_queue = ColaCircular(capacidad_cola)
    
    tiempo_actual = 0
    completados = 0
    n = len(procesos)
    
    # Control de procesos que ya entraron a la cola
    ingresados = [False] * n
    
    # Encolar los primeros procesos que llegan en t = 0
    for i in range(n):
        if procesos[i].arrival_time <= tiempo_actual:
            ready_queue.encolar(procesos[i])
            ingresados[i] = True

    # Si en t=0 no llegó ningún proceso, avanzar el reloj al primer arribo
    if ready_queue.esta_vacia() and completados < n:
        proximos = [p.arrival_time for p in procesos if p.remaining_time > 0]
        if proximos:
            tiempo_actual = min(proximos)
            for i in range(n):
                if not ingresados[i] and procesos[i].arrival_time <= tiempo_actual:
                    ready_queue.encolar(procesos[i])
                    ingresados[i] = True

    # Bucle principal del Scheduler
    while completados < n:
        if ready_queue.esta_vacia():
            # Avanzar tiempo si la CPU está ociosa
            tiempo_actual += 1
            for i in range(n):
                if not ingresados[i] and procesos[i].arrival_time <= tiempo_actual:
                    ready_queue.encolar(procesos[i])
                    ingresados[i] = True
            continue

        proceso_actual = ready_queue.desencolar()
        
        # Determinar cuánto tiempo se va a ejecutar (min de Quantum y tiempo restante)
        tiempo_ejecucion = min(tq, proceso_actual.remaining_time)
        
        # Ejecutar en la CPU
        proceso_actual.remaining_time -= tiempo_ejecucion
        tiempo_actual += tiempo_ejecucion

        # 1. Verificar si llegaron nuevos procesos DURANTE la ejecución del Quantum actual
        for i in range(n):
            if not ingresados[i] and procesos[i].arrival_time <= tiempo_actual:
                ready_queue.encolar(procesos[i])
                ingresados[i] = True

        # 2. Si el proceso actual NO terminó, se re-encola al final del ready_queue
        if proceso_actual.remaining_time > 0:
            ready_queue.encolar(proceso_actual)
        else:
            # El proceso finalizó
            proceso_actual.completion_time = tiempo_actual
            proceso_actual.turnaround_time = proceso_actual.completion_time - proceso_actual.arrival_time
            proceso_actual.waiting_time = proceso_actual.turnaround_time - proceso_actual.burst_time
            completados += 1

    # Imprimir la tabla requerida por la consigna
    imprimir_tabla(procesos)

def imprimir_tabla(procesos):
    """Imprime por consola la tabla de salida formateada."""
    # Ordenar por PID original para mostrar P1, P2, P3...
    procesos.sort(key=lambda p: p.pid)
    
    header = f"{'ProcessID':<12} | {'ArrivalTime':<12} | {'BurstTime':<10} | {'Turnaround Time':<16} | {'WaitingTime':<12}"
    separador = "-" * len(header)
    
    print("\n" + separador)
    print("                 RESULTADOS PLANIFICACIÓN ROUND ROBIN")
    print(separador)
    print(header)
    print(separador)
    
    for p in procesos:
        print(f"{p.pid:<12} | {p.arrival_time:<12} | {p.burst_time:<10} | {p.turnaround_time:<16} | {p.waiting_time:<12}")
    
    print(separador + "\n")

if __name__ == "__main__":
    # Datos de prueba especificados en la página 5 del enunciado del TP
    datos_catedra = [
        ("P1", 0, 5),
        ("P2", 2, 3),
        ("P3", 3, 1),
        ("P4", 5, 2),
        ("P5", 6, 5),
        ("P6", 8, 4)
    ]
    
    print("Ejecutando simulación de Round Robin (tq=2, capacidad=10)...")
    simular_round_robin(datos_catedra, tq=2, capacidad_cola=10)