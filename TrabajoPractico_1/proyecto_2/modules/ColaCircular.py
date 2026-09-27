# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código 

class ColaCircular:
    """
    Implementación de una cola circular de tamaño fijo sobre un arreglo de Python.
    
    Atributos:
        _capacidad (int): Tamaño máximo asignado para la cola.
        _items (list): Arreglo que almacena los elementos.
        _frente (int): Índice del primer elemento de la cola.
        _final (int): Índice de la posición disponible para el próximo encolado.
        _tamanio (int): Cantidad de elementos almacenados en tiempo real.
    """

    def __init__(self, capacidad):
        """
        Inicializa una cola circular vacía con una capacidad determinada.

        Parámetros:
            capacidad (int): Capacidad máxima de elementos.
        """
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser un entero positivo.")
        
        self._capacidad = capacidad
        self._items = [None] * capacidad
        self._frente = 0
        self._final = 0
        self._tamanio = 0

    def esta_vacia(self):
        """
        Devuelve True si la cola está vacía.
        """
        return self._tamanio == 0

    def esta_llena(self):
        """
        Devuelve True si la cola alcanzó su capacidad máxima.
        """
        return self._tamanio == self._capacidad

    def encolar(self, item):
        """
        Agrega un elemento al final de la cola circular.

        Excepciones:
            OverflowError: Si se intenta encolar en una cola llena.
        """

        if self.esta_llena():
            raise OverflowError("La cola está llena.")
        
        self._items[self._final] = item
        self._final = (self._final + 1) % self._capacidad
        self._tamanio += 1

    def desencolar(self):
        """
        Elimina y devuelve el elemento del frente de la cola.
        Lanza IndexError si la cola está vacía.
        """
        if self.esta_vacia():
            raise IndexError("La cola está vacía.")
        
        item = self._items[self._frente]
        self._items[self._frente] = None  # Liberar referencia
        self._frente = (self._frente + 1) % self._capacidad
        self._tamanio -= 1
        return item

    def frente(self):
        """
        Devuelve el elemento del frente sin eliminarlo.
        Lanza IndexError si la cola está vacía.
        """
        if self.esta_vacia():
            raise IndexError("La cola está vacía.")
        return self._items[self._frente]

    def primero(self):
        """Alias de frente() para compatibilidad con tests."""
        return self.frente()

    def vaciar(self):
        """Reinicia la cola circular a su estado vacio original."""
        self._items = [None] * self._capacidad
        self._frente = 0
        self._final = 0
        self._tamanio = 0

    def __len__(self):
        """Devuelve la cantidad actual de elementos en la cola."""
        return self._tamanio