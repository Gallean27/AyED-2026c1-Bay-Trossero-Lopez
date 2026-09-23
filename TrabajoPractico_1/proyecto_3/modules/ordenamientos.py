"""
Módulo de algoritmos de ordenamiento para el Proyecto 3.
"""

def ordenamiento_burbuja(lista):
    """
    Ordena una lista de elementos comparables de menor a mayor usando Ordenamiento Burbuja.
    
    Precondiciones:
        - lista (list): Debe ser una lista mutable con elementos comparables.
        
    Postcondiciones:
        - Modifica la lista original (in-place) dejando sus elementos en orden ascendente.
        - Retorna la referencia a la misma lista ordenada.
        
    Complejidad:
        - Temporal: O(n^2) peor/promedio, O(n) mejor caso.
        - Espacial: O(1) auxiliar (in-place).
    """
    n = len(lista)
    for i in range(n):
        intercambio = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        if not intercambio:
            break
    return lista


def ordenamiento_radix(lista):
    """
    Ordena una lista de enteros no negativos usando el algoritmo Radix Sort (LSD).
    
    Precondiciones:
        - lista (list): Lista de enteros no negativos (elementos >= 0).
        
    Postcondiciones:
        - Retorna una nueva lista ordenada de menor a mayor.
        - Preserva la estabilidad del orden original.
        
    Complejidad:
        - Temporal: O(d * (n + k)), d = dígitos del máximo, k = base 10.
        - Espacial: O(n + k) auxiliar para los baldes.
    """
    if not lista:
        return []

    max_num = max(lista)
    exp = 1
    lista_ordenada = list(lista)

    while max_num // exp > 0:
        lista_ordenada = _counting_sort_por_digito(lista_ordenada, exp)
        exp *= 10

    return lista_ordenada


def _counting_sort_por_digito(lista, exp):
    """Función auxiliar para Radix Sort: ordena por la posición del dígito exp."""
    n = len(lista)
    salida = [0] * n
    conteo = [0] * 10

    for i in range(n):
        digito = (lista[i] // exp) % 10
        conteo[digito] += 1

    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    for i in range(n - 1, -1, -1):
        digito = (lista[i] // exp) % 10
        salida[conteo[digito] - 1] = lista[i]
        conteo[digito] -= 1

    return salida


def quicksort(lista):
    """
    Ordena una lista usando el algoritmo Quicksort (Divide y Vencerás).
    
    Precondiciones:
        - lista (list): Lista de elementos comparables.
        
    Postcondiciones:
        - Retorna una nueva lista ordenada de menor a mayor.
        
    Complejidad:
        - Temporal: O(n log n) promedio, O(n^2) peor caso.
        - Espacial: O(n) por sublistas recursivas.
    """
    if len(lista) <= 1:
        return lista
    
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    
    return quicksort(menores) + iguales + quicksort(mayores)