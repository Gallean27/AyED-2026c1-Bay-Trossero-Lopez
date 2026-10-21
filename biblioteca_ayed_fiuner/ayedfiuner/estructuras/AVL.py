from .ABB import NodoArbol
from .ABB import ArbolBinarioBusqueda as ABB

class AVL(ABB):
    """
    Representa un Árbol Binario de Búsqueda Auto-balanceado (AVL).
    
    Invariante de clase:
        - Para cada nodo perteneciente al árbol, el valor absoluto de su factor 
          de equilibrio debe ser menor o igual a 1 (|factorEquilibrio| <= 1).
    """
    
    def __init__(self):
        """
        Pre:
            - Ninguna.
        Post:
            - El objeto AVL es inicializado correctamente invocando el constructor 
              de la clase base ABB, quedando con su raíz nula y tamaño en cero.
        """
        ABB.__init__(self)
    
    def _agregar(self, clave, valor, nodoActual):
        """
        Pre:
            - 'nodoActual' debe ser una instancia válida y no nula de la clase NodoArbol.
            - 'clave' debe ser del mismo tipo o comparable con las claves del subárbol.
            - El subárbol que tiene como raíz a 'nodoActual' cumple con el criterio AVL.
        Post:
            - Se inserta un nuevo NodoArbol en la posición ordenada correspondiente.
            - Se recalculan y balancean las alturas del camino modificado mediante 
              rotaciones si se detecta una alteración al invariante de la clase AVL.
        """
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave, valor, nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave, valor, padre=nodoActual)
                self.actualizarEquilibrio(nodoActual.hijoIzquierdo)
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave, valor, nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(clave, valor, padre=nodoActual)
                self.actualizarEquilibrio(nodoActual.hijoDerecho)
    
    def actualizarEquilibrio(self, nodo):
        """
        Pre:
            - 'nodo' es una referencia válida a un NodoArbol que ha sufrido la 
              inserción de un descendiente directo o indirecto.
        Post:
            - Los factores de equilibrio de los ancestros directos se modifican 
              en +/- 1 según corresponda el camino de inserción.
            - Si el factor de algún ancestro sale del rango [-1, 1], se invoca 
              un reequilibrio local y se detiene la propagación hacia la raíz.
        """
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre is not None:
            if nodo.esHijoIzquierdo():
                nodo.padre.factorEquilibrio += 1
            elif nodo.esHijoDerecho():
                nodo.padre.factorEquilibrio -= 1    
            if nodo.padre.factorEquilibrio != 0:
                    self.actualizarEquilibrio(nodo.padre)
        
    def reequilibrar(self, nodo):
        """
        Pre:
            - 'nodo' tiene un factor de equilibrio crítico igual a 2 o -2, alterando 
              la propiedad geométrica balanceada del árbol AVL.
        Post:
            - Se aplican las rotaciones simples o dobles correspondientes (izquierda/derecha) 
              dependiendo del signo del balance del nodo y de sus hijos directos.
            - El subárbol afectado recupera un estado donde todos sus nodos respetan el AVL.
        """
        if nodo.factorEquilibrio < 0:
            if nodo.hijoDerecho.factorEquilibrio > 0:
                self.rotarDerecha(nodo.hijoDerecho)
                self.rotarIzquierda(nodo)
            else:
                self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 0:
            if nodo.hijoIzquierdo.factorEquilibrio < 0:
                self.rotarIzquierda(nodo.hijoIzquierdo)
                self.rotarDerecha(nodo)
            else:
                self.rotarDerecha(nodo)

    def rotarIzquierda(self, pivote):
        """
        Pre:
            - 'pivote' es un NodoArbol válido que cuenta obligatoriamente con un hijo derecho.
        Post:
            - El hijo derecho del pivote pasa a ocupar su lugar jerárquico en el árbol.
            - El pivote se convierte en el hijo izquierdo de su antiguo hijo derecho.
            - Las referencias de los padres y los factores de equilibrio de ambos nodos 
              son actualizados preservando el ordenamiento.
        """
        nuevaRaiz = pivote.hijoDerecho
        pivote.hijoDerecho = nuevaRaiz.hijoIzquierdo
        if nuevaRaiz.hijoIzquierdo is not None:
            nuevaRaiz.hijoIzquierdo.padre = pivote
        nuevaRaiz.padre = pivote.padre
        if pivote.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if pivote.esHijoIzquierdo():
                pivote.padre.hijoIzquierdo = nuevaRaiz
            else:
                pivote.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoIzquierdo = pivote
        pivote.padre = nuevaRaiz
        pivote.factorEquilibrio = (pivote.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0))
        nuevaRaiz.factorEquilibrio = (nuevaRaiz.factorEquilibrio + 1 + max(pivote.factorEquilibrio, 0))
    
    def rotarDerecha(self, pivote):
        """
        Pre:
            - 'pivote' es un NodoArbol válido que cuenta obligatoriamente con un hijo izquierdo.
        Post:
            - El hijo izquierdo del pivote pasa a ocupar su lugar jerárquico en el árbol.
            - El pivote se convierte en el hijo derecho de su antiguo hijo izquierdo.
            - Las referencias de los padres y los factores de equilibrio de ambos nodos 
              son actualizados preservando el ordenamiento.
        """
        nuevaRaiz = pivote.hijoIzquierdo
        pivote.hijoIzquierdo = nuevaRaiz.hijoDerecho
        if nuevaRaiz.hijoDerecho is not None:
            nuevaRaiz.hijoDerecho.padre = pivote
        nuevaRaiz.padre = pivote.padre
        if pivote.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if pivote.esHijoDerecho():
                pivote.padre.hijoDerecho = nuevaRaiz
            else:
                pivote.padre.hijoIzquierdo = nuevaRaiz
        nuevaRaiz.hijoDerecho = pivote
        pivote.padre = nuevaRaiz
        pivote.factorEquilibrio = (pivote.factorEquilibrio - 1 - max(nuevaRaiz.factorEquilibrio, 0))
        nuevaRaiz.factorEquilibrio = (nuevaRaiz.factorEquilibrio - 1 + min(pivote.factorEquilibrio, 0))