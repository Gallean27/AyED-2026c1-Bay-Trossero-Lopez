from modules.lde import ListaDobleEnlazada

def main():
    # prueba de metodos
    lista = ListaDobleEnlazada()
    
    lista.agregar_al_inicio(1)
    lista.agregar_al_inicio(2)
    lista.agregar_al_inicio(3)
    lista.agregar_al_inicio(4)
    lista.agregar_al_inicio(5)
    lista.agregar_al_inicio(6)
    
    print("¡Felicidades! Los datos se cargaron en la lista correctamente.")

if __name__ == "__main__":
    main()
