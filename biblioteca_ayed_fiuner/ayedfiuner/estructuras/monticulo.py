 
class MonticuloBinario:

    def __init__(self):

        """Inicializa una nueva instancia de la clase MonticuloBinario.

        Pre: 
            - Ninguna.

        Post: 
            - Se ha creado una nueva instancia de MonticuloBinario con una lista vacía
            - tamaño actual igual a cero."""
        
        self.listaMonticulo = [0]
        self.tamanoActual = 0  
    
    def construirMonticulo(self,unaLista):

        """Construye un montículo binario a partir de una lista dada.

        Pre: 
            - unaLista es una lista de elementos.

        Post: 
            - Se ha construido un montículo binario a partir de los elementos de unaLista
            - El tamaño actual del montículo se ha actualizado para reflejar el número de elementos
              en el montículo."""
        
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [0] + unaLista[:]
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1
    
    def __str__(self):

        """Devuelve una representación en cadena del montículo binario.

        Pre: 
            - Ninguna.

        Post: 
            - Se ha generado una representación en cadena del montículo
            - La representación incluye los elementos del montículo separados por espacios."""
        
        lista = ''
        for i in range(1, len(self.listaMonticulo)):
            lista += str(self.listaMonticulo[i]) + ' '
        return lista
    
    def infiltArriba(self, i):

        """Realiza el proceso de infiltar un elemento hacia arriba en el montículo binario.
        
        Pre: 
            - i es un índice válido dentro del montículo.

        Post: 
            - El elemento en el índice i se ha infiltado hacia arriba en el montículo
            - Se han realizado los intercambios necesarios para mantener la propiedad del montículo."""

        while i // 2 > 0:
            if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            i = i // 2
    

    def insertar(self,valor):

        """Inserta un nuevo valor en el montículo binario.
        
        Pre: 
            - valor es el valor a insertar en el montículo.

        Post: 
            - El valor se ha insertado en el montículo
            - El tamaño actual del montículo se ha incrementado en uno
            - Se agrega un elemento al final del montículo con el nuevo valor
            - Se ha utilizado la función de infiltar hacia arriba para mantener la propiedad del montículo."""
        
        self.listaMonticulo.append(valor)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)
        
 
    def infiltAbajo(self,i):

        """Realiza el proceso de infiltar un elemento hacia abajo en el montículo binario.
        
        Pre: 
            - i es un índice válido dentro del montículo.

        Post: 
            - El elemento en el índice i se ha infiltado hacia abajo en el montículo.
            - Se ha utilizado la función de hijoMin para determinar el hijo con el valor mínimo.
            - Se han realizado los intercambios necesarios para mantener la propiedad del montículo."""
        
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm
        
    def eliminarMin(self):

        """Elimina y devuelve el valor mínimo del montículo binario.
        
        Pre: 
            - El montículo no está vacío.
            
        Post: 
            - El valor mínimo del montículo se ha eliminado y devuelto.
            - El tamaño actual del montículo se ha decrementado en uno.
            - Se ha utilizado la función de infiltar hacia abajo para mantener la propiedad del montículo."""

        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado

    def buscarMin(self):

        """Devuelve el valor mínimo del montículo binario sin eliminarlo.
        
        Pre:
            - El montículo no está vacío.
            
        Post: 
            - El valor mínimo del montículo se ha devuelto sin eliminarlo.
            - El tamaño actual del montículo no se ha modificado."""

        return self.listaMonticulo[1]

    def estaVacio(self):

        """Verifica si el montículo binario está vacío.

        Pre: 
            - Ninguna.

        Post:
            - Se ha verificado si el montículo está vacío.
            - Se ha devuelto True si el montículo está vacío, de lo contrario se ha devuelto False."""
        
        return self.tamanoActual == 0

    def tamano(self):

        """Devuelve el tamaño actual del montículo binario.
        
        Pre:
            - Ninguna.

        Post:
            - Se ha devuelto el tamaño actual del montículo binario."""
        
        return self.tamanoActual
    
    def hijoMin(self, i):

        """Determina el índice del hijo con el valor mínimo para un elemento dado en el montículo binario.
        
        Pre:
            - i es un índice válido dentro del montículo.
        
        Post: 
            - Se ha determinado el índice del hijo con el valor mínimo para el elemento en el índice i.
            - Se ha devuelto el índice del hijo con el valor mínimo."""

        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i * 2] < self.listaMonticulo[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
            
