from ayedfiuner.estructuras.monticulo import MonticuloBinario

class ColaPrioridad:
    def __init__(self):

        """Inicializa una nueva instancia de la clase ColaPrioridad.

        Pre: 
            - Ninguna.

        Post: 
            - Se ha creado una nueva instancia de ColaPrioridad con un montículo binario vacío."""

        self.monticulo = MonticuloBinario()
        self.contador=0

    def insertar(self, elemento):

        """Inserta un elemento en la cola de prioridad.

        Pre:
            - elemento es el valor que se desea insertar en la cola de prioridad.  
        
        Post:
            - El elemento se ha insertado en la cola de prioridad
            - Se utiliza de forma recursiva la funcion insertar del monticulo para mantener la propiedad 
            de la cola de prioridad."""
        
        self.monticulo.insertar(elemento)

    def atender(self):

        """Atiende (elimina y devuelve) el elemento con la mayor prioridad de la cola de prioridad.
        
        Pre:
            - La cola de prioridad no está vacía.
            
        Post:
            - Se ha eliminado el elemento con la mayor prioridad de la cola de prioridad
            - Se ha devuelto el elemento con la mayor prioridad
            - Se utiliza de forma recursiva la funcion eliminarMin del monticulo para mantener la propiedad de la 
            cola de prioridad."""

        return self.monticulo.eliminarMin()

    def ver_proximo(self):

        """Devuelve el elemento con la mayor prioridad de la cola de prioridad sin eliminarlo.
        
        Pre:
            - La cola de prioridad no está vacía.
            
        Post:
            - Se ha devuelto el elemento con la mayor prioridad de la cola de prioridad sin eliminarlo
            - Se utiliza de forma recursiva la funcion buscarMin del monticulo para mantener la propiedad de la 
            cola de prioridad."""
        
        return self.monticulo.buscarMin()

    def esta_vacia(self):

        """Verifica si la cola de prioridad está vacía.

        Pre:
            - Ninguna.

        Post: 
            - Se ha verificado si la cola de prioridad está vacía.
            - Se ha devuelto True si la cola de prioridad está vacía, de lo contrario se ha devuelto False.
            - Se utiliza de forma recursiva la funcion estaVacio del monticulo para mantener la propiedad de la 
            cola de prioridad."""
        
        return self.monticulo.estaVacio()
   
    def tamano(self):

        """Devuelve el número de elementos en la cola de prioridad.

        Pre:
            - Ninguna.

        Post:
            - Se ha devuelto el número de elementos en la cola de prioridad.
            - Se utiliza de forma recursiva la funcion tamano del monticulo para mantener la propiedad de la 
            cola de prioridad."""
        
        return self.monticulo.tamano()

    def __str__(self):

        """Devuelve una representación en cadena de la cola de prioridad.

        Pre:
            - Ninguna.

        Post:
            - Se ha devuelto una representación en cadena de la cola de prioridad que incluye los elementos 
            presentes en la cola de prioridad."""

        return str(self.monticulo)