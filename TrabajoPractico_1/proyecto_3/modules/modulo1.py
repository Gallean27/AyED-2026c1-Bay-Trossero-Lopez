# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

import random

def ordenamiento_burbuja(lista):
    """
    Ordena una lista de elementos comparables utilizando el algoritmo de Ordenamiento Burbuja.
    
    Complejidad temporal: O(n^2) en el peor y promedio de los casos.
    Complejidad espacial: O(1) auxiliar (ordena in-place).
    
    Parámetros:
        lista (list): Lista de elementos a ordenar.
        
    Retorna:
        list: La misma lista ordenada de menor a mayor.
    """
    n = len(lista)
    for i in range(n):
        intercambio = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        # Si no hubo intercambios en la pasada, la lista ya está ordenada
        if not intercambio:
            break
    return lista