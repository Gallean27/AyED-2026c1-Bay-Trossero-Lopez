import time
import matplotlib.pyplot as plt
from modules.lde import ListaDobleEnlazada

def medir_tiempos():
    # Rango de tamaños N para evaluar
    tamanos_N = range(100, 10100, 500)
    
    tiempos_len = []
    tiempos_copiar = []
    tiempos_invertir = []

    for N in tamanos_N:
        # Preparar la lista con N elementos
        lista = ListaDobleEnlazada()
        for i in range(N):
            lista.agregar_al_final(i)

        # 1. Medir len() - O(1)
        inicio = time.perf_counter()
        _ = len(lista)
        fin = time.perf_counter()
        tiempos_len.append(fin - inicio)

        # 2. Medir copiar() - O(N)
        inicio = time.perf_counter()
        _ = lista.copiar()
        fin = time.perf_counter()
        tiempos_copiar.append(fin - inicio)

        # 3. Medir invertir() - O(N)
        inicio = time.perf_counter()
        lista.invertir()
        fin = time.perf_counter()
        tiempos_invertir.append(fin - inicio)

    # Gráfica 1: len() vs N
    plt.figure(figsize=(8, 5))
    plt.plot(tamanos_N, tiempos_len, label='len()', color='blue')
    plt.title('Complejidad Temporal de len() - O(1)')
    plt.xlabel('Tamaño de la lista (N)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.grid(True)
    plt.legend()
    plt.savefig('docs/grafica_len.png')
    plt.close()

    # Gráfica 2: copiar() e invertir() vs N
    plt.figure(figsize=(8, 5))
    plt.plot(tamanos_N, tiempos_copiar, label='copiar()', color='green')
    plt.plot(tamanos_N, tiempos_invertir, label='invertir()', color='orange')
    plt.title('Complejidad Temporal de copiar() e invertir() - O(N)')
    plt.xlabel('Tamaño de la lista (N)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.grid(True)
    plt.legend()
    plt.savefig('docs/grafica_copiar_invertir.png')
    plt.close()

    print("¡Mediciones completadas! Las imágenes se guardaron en la carpeta docs/.")

if __name__ == "__main__":
    medir_tiempos()