class NodoArbol:
    def __init__(self, clave, valor, izquierdo=None, derecho=None, padre=None):
        """
        Pre: Ninguna.
        Post: Nodo creado con clave, valor, referencias y factorEquilibrio en 0.
        """
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
        self.factorEquilibrio = 0

    def tieneHijoIzquierdo(self):
        """
        Pre: Ninguna.
        Post: Devuelve el hijo izquierdo (u objeto evaluable como Booleano).
        """
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        """
        Pre: Ninguna.
        Post: Devuelve el hijo derecho (u objeto evaluable como Booleano).
        """
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        """
        Pre: Ninguna.
        Post: Devuelve True si tiene padre y es su hijo izquierdo; False en caso contrario.
        """
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        """
        Pre: Ninguna.
        Post: Devuelve True si tiene padre y es su hijo derecho; False en caso contrario.
        """
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        """
        Pre: Ninguna.
        Post: Devuelve True si no posee padre; False en caso contrario.
        """
        return not self.padre

    def esHoja(self):
        """
        Pre: Ninguna.
        Post: Devuelve True si no tiene ningún hijo; False en caso contrario.
        """
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        """
        Pre: Ninguna.
        Post: Devuelve True si cuenta con al menos un hijo; False si es hoja.
        """
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        """
        Pre: Ninguna.
        Post: Devuelve True si posee tanto hijo izquierdo como derecho; False en caso contrario.
        """
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self, clave, valor, hizq, hder):
        """
        Pre: Ninguna.
        Post: Atributos actualizados; los nuevos hijos apuntan a este nodo como padre.
        """
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder

        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self

        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

    def encontrarSucesor(self):
        """
        Pre: El nodo existe en la estructura.
        Post: Devuelve el nodo sucesor en orden simétrico, o None si no existe.
        """
        sucesor = None
        if self.tieneHijoDerecho():
            sucesor = self.hijoDerecho.encontrarMin()
        else:
            if self.padre:
                if self.esHijoIzquierdo():
                    sucesor = self.padre
                else:
                    self.padre.hijoDerecho = None
                    sucesor = self.padre.encontrarSucesor()
                    self.padre.hijoDerecho = self
        return sucesor

    def encontrarMin(self):
        """
        Pre: Ninguna.
        Post: Devuelve el nodo con la clave mínima a partir de este subárbol.
        """
        actual = self
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo
        return actual

    def empalmar(self):
        """
        Pre: El nodo es hoja o tiene un solo hijo (no apto para nodos con dos hijos).
        Post: El nodo es removido y sus enlaces son delegados a su padre/hijo.
        """
        if self.esHoja():
            if self.esHijoIzquierdo():
                self.padre.hijoIzquierdo = None
            else:
                self.padre.hijoDerecho = None
        elif self.tieneAlgunHijo():
            if self.tieneHijoIzquierdo():
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoIzquierdo
                else:
                    self.padre.hijoDerecho = self.hijoIzquierdo
                self.hijoIzquierdo.padre = self.padre
            else:
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoDerecho
                else:
                    self.padre.hijoDerecho = self.hijoDerecho
                self.hijoDerecho.padre = self.padre

    def __str__(self):
        """
        Pre: Ninguna.
        Post: Devuelve la representación en cadena de texto del nodo.
        """
        return f'{self.clave}: {self.cargaUtil}'

    def __iter__(self):
        """
        Pre: El nodo no es nulo.
        Post: Genera (yield) las cadenas de los nodos en recorrido in-orden.
        """
        if self:
            if self.tieneHijoIzquierdo():
                for elem in self.hijoIzquierdo:
                    yield elem
            yield self.__str__()
            if self.tieneHijoDerecho():
                for elem in self.hijoDerecho:
                    yield elem


class ArbolBinarioBusqueda:
    """
    Árbol Binario de Búsqueda Estándar.
    Invariante: Claves izquierdas < clave nodo < claves derechas.
    """

    def __init__(self):
        """
        Pre: Ninguna.
        Post: Árbol inicializado vacío con tamano = 0 y raiz = None.
        """
        self.raiz = None
        self.tamano = 0

    def longitud(self):
        """
        Pre: Ninguna.
        Post: Devuelve el número entero de elementos en el árbol.
        """
        return self.tamano

    def agregar(self, clave, valor):
        """
        Pre: clave es comparable con las claves del árbol.
        Post: Nodo insertado; tamano incrementado en 1; propiedad ABB preservada.
        """
        if self.raiz:
            self._agregar(clave, valor, self.raiz)
        else:
            self.raiz = NodoArbol(clave, valor)
        self.tamano = self.tamano + 1

    def _agregar(self, clave, valor, nodoActual):
        """
        Pre: nodoActual es un NodoArbol válido.
        Post: Recorre recursivamente el árbol e inserta el nodo en su lugar ordenado.
        """
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave, valor, nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave, valor, padre=nodoActual)
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave, valor, nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(clave, valor, padre=nodoActual)

    def obtener(self, clave):
        """
        Pre: Ninguna.
        Post: Devuelve la cargaUtil asociada a la clave, o None si no existe.
        """
        if self.raiz:
            res = self._obtener(clave, self.raiz)
            if res:
                return res.cargaUtil
            else:
                return None
        else:
            return None

    def _obtener(self, clave, nodoActual):
        """
        Pre: Ninguna.
        Post: Devuelve la instancia NodoArbol que coincide con la clave, o None.
        """
        if not nodoActual:
            return None
        elif nodoActual.clave == clave:
            return nodoActual
        elif clave < nodoActual.clave:
            return self._obtener(clave, nodoActual.hijoIzquierdo)
        else:
            return self._obtener(clave, nodoActual.hijoDerecho)

    def eliminar(self, clave):
        """
        Pre: tamano > 0 y la clave debe estar presente en el árbol.
        Post: Nodo removido; tamano disminuido en 1; propiedad ABB preservada.
        Raises: KeyError si la clave no pertenece al árbol.
        """
        if self.tamano > 1:
            nodoAEliminar = self._obtener(clave, self.raiz)
            if nodoAEliminar:
                self.remover(nodoAEliminar)
                self.tamano = self.tamano - 1
            else:
                raise KeyError('Error, la clave no está en el árbol')
        elif self.tamano == 1 and self.raiz.clave == clave:
            self.raiz = None
            self.tamano = self.tamano - 1
        else:
            raise KeyError('Error, la clave no está en el árbol')

    def remover(self, nodoActual):
        """
        Pre: nodoActual es un objeto NodoArbol válido perteneciente al árbol.
        Post: Desconecta y reestructura los enlaces del nodo según sus hijos.
        """
        if nodoActual.esHoja():
            if nodoActual == nodoActual.padre.hijoIzquierdo:
                nodoActual.padre.hijoIzquierdo = None
            else:
                nodoActual.padre.hijoDerecho = None
        elif nodoActual.tieneAmbosHijos():
            sucesor = nodoActual.encontrarSucesor()
            sucesor.empalmar()
            nodoActual.clave = sucesor.clave
            nodoActual.cargaUtil = sucesor.cargaUtil
        else:
            if nodoActual.tieneHijoIzquierdo():
                if nodoActual.esHijoIzquierdo():
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
                elif nodoActual.esHijoDerecho():
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
                else:
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave, nodoActual.hijoIzquierdo.cargaUtil, nodoActual.hijoIzquierdo.hijoIzquierdo, nodoActual.hijoIzquierdo.hijoDerecho)
            else:
                if nodoActual.esHijoIzquierdo():
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
                elif nodoActual.esHijoDerecho():
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
                else:
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave, nodoActual.hijoDerecho.cargaUtil, nodoActual.hijoDerecho.hijoIzquierdo, nodoActual.hijoDerecho.hijoDerecho)

    def __delitem__(self, clave):
        """
        Pre: La clave existe en el árbol.
        Post: Despacha internamente a eliminar(clave).
        """
        self.eliminar(clave)

    def __contains__(self, clave):
        """
        Pre: Ninguna.
        Post: Devuelve True si la clave existe en el árbol; False de lo contrario.
        """
        return self.obtener(clave) is not None

    def __len__(self):
        """
        Pre: Ninguna.
        Post: Devuelve la longitud (tamano) actual del árbol.
        """
        return self.tamano

    def __iter__(self):
        """
        Pre: El árbol tiene al menos un nodo (raiz != None).
        Post: Retorna el iterador in-orden de la raíz.
        """
        return self.raiz.__iter__()

    def __getitem__(self, clave):
        """
        Pre: Ninguna.
        Post: Permite acceso estilo diccionario arbol[clave] llamando a obtener().
        """
        return self.obtener(clave)

    def __setitem__(self, clave, valor):
        """
        Pre: clave es comparable.
        Post: Permite asignación arbol[clave] = valor llamando a agregar().
        """
        self.agregar(clave, valor)