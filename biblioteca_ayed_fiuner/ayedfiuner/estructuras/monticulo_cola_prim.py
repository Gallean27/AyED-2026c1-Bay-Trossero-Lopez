class MonticuloBinario:
    def __init__(self):
        """Inicializa un montículo binario vacío para tuplas (distancia, vértice)."""
        self.listaMonticulo = []
        self.tamanoActual = 0

    def construirMonticulo(self, unaLista):
        """Construye el montículo a partir de una lista de tuplas (distancia, vértice)."""
        self.listaMonticulo = unaLista[:]
        self.tamanoActual = len(unaLista)
        i = len(unaLista) // 2
        while i >= 0:
            self.infiltAbajo(i)
            i -= 1

    def infiltArriba(self, i):
        """Infiltar hacia arriba comparando por distancia."""
        while i > 0:
            padre = (i - 1) // 2
            if self.listaMonticulo[i][0] < self.listaMonticulo[padre][0]:
                self.listaMonticulo[i], self.listaMonticulo[padre] = self.listaMonticulo[padre], self.listaMonticulo[i]
            i = padre

    def insertar(self, elemento):
        """Inserta una tupla (distancia, vértice)."""
        self.listaMonticulo.append(elemento)
        self.tamanoActual += 1
        self.infiltArriba(self.tamanoActual - 1)

    def infiltAbajo(self, i):
        """Infiltar hacia abajo comparando por distancia."""
        while 2 * i + 1 < self.tamanoActual:
            hijoMin = self.hijoMin(i)
            if self.listaMonticulo[i][0] > self.listaMonticulo[hijoMin][0]:
                self.listaMonticulo[i], self.listaMonticulo[hijoMin] = self.listaMonticulo[hijoMin], self.listaMonticulo[i]
            i = hijoMin

    def eliminarMin(self):
        """Elimina y devuelve la tupla (distancia, vértice) mínima."""
        if self.tamanoActual == 0:
            return None
        minElem = self.listaMonticulo[0]
        ultimoElem = self.listaMonticulo.pop()
        self.tamanoActual -= 1
        if self.tamanoActual > 0:
            self.listaMonticulo[0] = ultimoElem
            self.infiltAbajo(0)
        return minElem

    def buscarMin(self):
        """Devuelve la tupla mínima sin eliminarla."""
        if self.tamanoActual == 0:
            return None
        return self.listaMonticulo[0]

    def estaVacio(self):
        """Verifica si el montículo está vacío."""
        return self.tamanoActual == 0

    def tamano(self):
        """Devuelve el tamaño actual del montículo."""
        return self.tamanoActual

    def hijoMin(self, i):
        """Devuelve el índice del hijo con menor distancia."""
        izq = 2 * i + 1
        der = 2 * i + 2
        if der >= self.tamanoActual:
            return izq
        else:
            if self.listaMonticulo[izq][0] < self.listaMonticulo[der][0]:
                return izq
            else:
                return der
