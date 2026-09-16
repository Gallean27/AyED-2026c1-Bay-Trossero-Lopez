class Nodo:
    """
    Representa un elemento dentro de la lista doblemente enlazada.

    Atributos:
        dato: El valor almacenado en el nodo.
        siguiente (Nodo): Puntero al siguiente nodo en la lista.
        anterior (Nodo): Puntero al nodo anterior en la lista.
    """
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDobleEnlazada:
    """
    Estructura de datos lineal que permite insertar y eliminar elementos 
    en ambas direcciones mediante punteros al nodo siguiente y anterior.
    """

    def __init__(self):
        """Inicializa una lista doblemente enlazada vacía."""
        self._cabeza = None
        self._cola = None
        self._tamanio = 0

    @property
    def cabeza(self):
        """Retorna el primer nodo de la lista."""
        return self._cabeza

    @property
    def cola(self):
        """Retorna el último nodo de la lista."""
        return self._cola

    @property
    def tamanio(self):
        """Retorna la cantidad actual de elementos en la lista."""
        return self._tamanio

    def esta_vacia(self):
        """Verifica si la lista está vacía."""
        return self._tamanio == 0

    def __len__(self):
        """Permite usar la función nativa len(lista) para obtener el tamaño."""
        return self._tamanio

    def agregar_al_inicio(self, item):
        """
        Inserta un nuevo elemento al principio de la lista.

        Parámetros:
            item: El dato que se desea agregar.
        """
        nuevo_nodo = Nodo(item)
        if self.esta_vacia():
            self._cabeza = nuevo_nodo
            self._cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self._cabeza
            self._cabeza.anterior = nuevo_nodo
            self._cabeza = nuevo_nodo
        self._tamanio += 1

    def agregar_al_final(self, item):
        """
        Inserta un nuevo elemento al final de la lista.

        Parámetros:
            item: El dato que se desea agregar.
        """
        nuevo_nodo = Nodo(item)
        if self.esta_vacia():
            self._cabeza = nuevo_nodo
            self._cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self._cola
            self._cola.siguiente = nuevo_nodo
            self._cola = nuevo_nodo
        self._tamanio += 1

    def insertar(self, item, posicion=None):
        """
        Inserta un elemento en una posición específica de la lista.

        Parámetros:
            item: El dato a insertar.
            posicion (int, opcional): Índice donde se insertará el elemento. 
                                      Si es None o igual al tamaño, inserta al final.

        Excepciones:
            IndexError: Si la posición está fuera de los límites válidos.
        """
        if posicion is None or posicion == self._tamanio:
            self.agregar_al_final(item)
            return

        if posicion < 0 or posicion > self._tamanio:
            raise IndexError("Posición fuera de rango")

        if posicion == 0:
            self.agregar_al_inicio(item)
            return

        # Avanzar hasta el nodo en la posición deseada
        actual = self._cabeza
        for _ in range(posicion):
            actual = actual.siguiente

        nuevo_nodo = Nodo(item)
        nuevo_nodo.anterior = actual.anterior
        nuevo_nodo.siguiente = actual

        actual.anterior.siguiente = nuevo_nodo
        actual.anterior = nuevo_nodo

        self._tamanio += 1

    def extraer(self, posicion=None):
        """
        Remueve y retorna el elemento en la posición especificada.

        Parámetros:
            posicion (int, opcional): Índice del elemento a eliminar. 
                                      Por defecto (o -1) remueve el último.

        Retorna:
            El dato almacenado en el nodo eliminado.

        Excepciones:
            IndexError: Si la lista está vacía o la posición es inválida.
        """
        if self.esta_vacia():
            raise IndexError("No se puede extraer de una lista vacía")

        # Convertir posicion vacía o -1 al índice del último elemento
        if posicion is None or posicion == -1:
            posicion = self._tamanio - 1

        if posicion < 0 or posicion >= self._tamanio:
            raise IndexError("Posición fuera de rango")

        # Caso O(1): Extraer del inicio
        if posicion == 0:
            dato = self._cabeza.dato
            self._cabeza = self._cabeza.siguiente
            if self._cabeza is not None:
                self._cabeza.anterior = None
            else:
                self._cola = None
            self._tamanio -= 1
            return dato

        # Caso O(1): Extraer del final
        if posicion == self._tamanio - 1:
            dato = self._cola.dato
            self._cola = self._cola.anterior
            if self._cola is not None:
                self._cola.siguiente = None
            else:
                self._cabeza = None
            self._tamanio -= 1
            return dato

        # Caso intermedio O(n): Buscar el elemento
        actual = self._cabeza
        for _ in range(posicion):
            actual = actual.siguiente

        dato = actual.dato
        actual.anterior.siguiente = actual.siguiente
        actual.siguiente.anterior = actual.anterior

        self._tamanio -= 1
        return dato

    def copiar(self):
        """
        Crea una copia independiente (superficial) de la lista actual.

        Retorna:
            ListaDobleEnlazada: Una nueva instancia con los mismos datos.
        """
        nueva_lista = ListaDobleEnlazada()
        actual = self._cabeza
        # O(n) porque recorre una sola vez y inserta al final en O(1)
        while actual is not None:
            nueva_lista.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return nueva_lista

    def invertir(self):
        """Invierte el orden de los elementos de la lista sobre la misma instancia."""
        actual = self._cabeza
        
        while actual is not None:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior

        self._cabeza, self._cola = self._cola, self._cabeza
        
    def concatenar(self, lista):
        """
        Agrega todos los elementos de otra lista al final de la lista actual.

        Parámetros:
            lista (ListaDobleEnlazada): La lista que se agregará.

        Retorna:
            ListaDobleEnlazada: La misma lista modificada.
        """
        actual = lista._cabeza
        while actual is not None:
            self.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return self

    def __add__(self, lista):
        """
        Permite usar el operador '+' para unir dos listas en una nueva.

        Ejemplo:
            nueva = lista1 + lista2
        """
        nueva_lista = self.copiar()
        nueva_lista.concatenar(lista)
        return nueva_lista

    def __iter__(self):
        """Permite iterar la lista directamente mediante un bucle for."""
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente