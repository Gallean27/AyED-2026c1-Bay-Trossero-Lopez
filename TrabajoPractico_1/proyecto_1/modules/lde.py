class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDobleEnlazada:
    def __init__(self):
        self._cabeza = None
        self._cola = None
        self._tamanio = 0

    @property
    def cabeza(self):
        return self._cabeza

    @property
    def cola(self):
        return self._cola

    @property
    def tamanio(self):
        return self._tamanio

    def esta_vacia(self):
        return self._tamanio == 0

    def __len__(self):
        return self._tamanio

    def agregar_al_inicio(self, item):
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
        if self.esta_vacia():
            raise IndexError("No se puede extraer de una lista vacía")

        if posicion is None:
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
        nueva_lista = ListaDobleEnlazada()
        actual = self._cabeza
        # O(n) porque recorre una sola vez y inserta al final en O(1)
        while actual is not None:
            nueva_lista.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return nueva_lista

    def invertir(self):
        actual = self._cabeza
        temp = None

        # Intercambiar anterior y siguiente para cada nodo
        while actual is not None:
            temp = actual.anterior
            actual.anterior = actual.siguiente
            actual.siguiente = temp
            actual = actual.anterior  # Avanzamos usando el puntero anterior original

        # Ajustar cabeza y cola
        if temp is not None:
            self._cola = self._cabeza
            self._cabeza = temp.anterior

    def concatenar(self, lista):
        actual = lista._cabeza
        while actual is not None:
            self.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return self

    def __add__(self, lista):
        nueva_lista = self.copiar()
        nueva_lista.concatenar(lista)
        return nueva_lista

    def __iter__(self):
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente