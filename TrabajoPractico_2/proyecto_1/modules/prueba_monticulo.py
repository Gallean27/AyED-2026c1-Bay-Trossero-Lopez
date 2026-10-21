from ayedfiuner.estructuras.monticulo import MonticuloBinario

def main():
    
    heap=MonticuloBinario()
    
    print("\nInsertando elementos al monticulo")

    for i in [5, 3, 8, 1, 2]:
        heap.insertar(i)
    print(heap)

    tamaño_monticulo=heap.tamano()
    print("\nEl tamaño del monticulo es:", tamaño_monticulo)

    print("\nPrueba buscar minimo en monticulo")

    if not heap.estaVacio():
        print("El minimo es:", heap.buscarMin())
    else:
        print("El monticulo esta vacio, no hay minimo")

    while not heap.estaVacio():
        
        minimo=heap.eliminarMin()
        print("\nEliminando el minimo:", minimo)
        print(heap)

if __name__ == "__main__":
    main()