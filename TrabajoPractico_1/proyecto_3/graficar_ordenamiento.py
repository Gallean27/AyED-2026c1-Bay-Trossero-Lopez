import time
import random
import matplotlib.pyplot as plt
from modules.ordenamientos import ordenamiento_burbuja, ordenamiento_radix, quicksort

def medir_tiempos():
    tamanos_N = [100, 500, 1000, 2000, 3000, 5000]
    
    tiempos_burbuja = []
    tiempos_radix = []
    tiempos_quicksort = []
    tiempos_python = []

    print("Iniciando mediciones de tiempos de ordenamiento...")

    for N in tamanos_N:
        lista_base = [random.randint(0, 10000) for _ in range(N)]

        # 1. Burbuja
        l_burbuja = list(lista_base)
        inicio = time.perf_counter()
        ordenamiento_burbuja(l_burbuja)
        fin = time.perf_counter()
        tiempos_burbuja.append(fin - inicio)

        # 2. Radix Sort
        l_radix = list(lista_base)
        inicio = time.perf_counter()
        ordenamiento_radix(l_radix)
        fin = time.perf_counter()
        tiempos_radix.append(fin - inicio)

        # 3. Quicksort
        l_quick = list(lista_base)
        inicio = time.perf_counter()
        quicksort(l_quick)
        fin = time.perf_counter()
        tiempos_quicksort.append(fin - inicio)

        # 4. sorted() nativo de Python (Timsort)
        l_python = list(lista_base)
        inicio = time.perf_counter()
        sorted(l_python)
        fin = time.perf_counter()
        tiempos_python.append(fin - inicio)

        print(f"Completado N = {N}")

    # Graficar resultados
    plt.figure(figsize=(10, 6))
    plt.plot(tamanos_N, tiempos_burbuja, label='Burbuja - O(N^2)', color='red', marker='o')
    plt.plot(tamanos_N, tiempos_quicksort, label='Quicksort - O(N log N)', color='orange', marker='s')
    plt.plot(tamanos_N, tiempos_radix, label='Radix Sort - O(d*N)', color='blue', marker='^')
    plt.plot(tamanos_N, tiempos_python, label='sorted() Python - O(N log N)', color='green', marker='d')

    plt.title('Comparativa de Algoritmos de Ordenamiento')
    plt.xlabel('Tamaño de la lista (N)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.grid(True)
    plt.legend()
    
    plt.savefig('docs/grafica_ordenamientos.png')
    plt.close()

    print("\n¡Mediciones finalizadas! La imagen se guardó en docs/grafica_ordenamientos.png")

if __name__ == "__main__":
    medir_tiempos()