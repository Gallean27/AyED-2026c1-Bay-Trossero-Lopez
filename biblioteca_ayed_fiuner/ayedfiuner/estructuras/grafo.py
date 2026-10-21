class Vertice:

    def __init__(self,clave):

        """Inicializa el vertice con su clave y un diccionario de sus vecinos y sus ponderaciones
        
        Pre:
            - clave es un valor unico que identifica al vertice
        
        Post:
            - se crea un vertice con la clave dada, un diccionario vacio de vecinos, y 
            sin distancia ni predecesor asignados
            - se asigna la clave al vertice y se inicializan sus atributos de vecinos, distancia 
            y predecesor en None
        """

        self.id=clave
        self.conectadoA={}
        self.distancia=None
        self.predecesor=None

    def asignarDistancia(self,distancia):

        """Asigna una distancia al vertice
        
        Pre:
            - distancia es un valor numerico que representa la distancia del vertice a un punto de 
            referencia
        
        Post:
            - se asigna la distancia al vertice
        """
        self.distancia=distancia
    
    def obtenerDistancia(self):

        """Devuelve la distancia asignada al vertice
        
        Pre:
            - el vertice tiene una distancia asignada
        
        Post:
            - se devuelve la distancia asignada al vertice
        """
        return self.distancia
    
    def asignarPredecesor(self,predecesor):

        """Asigna un predecesor al vertice
        
        Pre:
            - predecesor es otro vertice que se considera el predecesor del vertice actual
        
        Post:
            - se asigna el predecesor al vertice
        """
        self.predecesor=predecesor
    
    def obtenerPredecesor(self):

        """Devuelve el predecesor asignado al vertice
        
        Pre:
            - el vertice tiene un predecesor asignado
        
        Post:
            - se devuelve el predecesor asignado al vertice
        """
        return self.predecesor

    def agregarVecino(self,vecino,ponderacion=0):

        """Agrega un vecino al vertice con su ponderacion
        
        Pre:
            - vecino es un vertice al que se conecta el vertice actual
            - ponderacion es un valor numerico que representa el peso de la conexion entre los vertices
        
        Post:
            - se agrega el vecino al diccionario de vecinos del vertice actual con su ponderacion
        """
        self.conectadoA[vecino]=ponderacion

    def __str__(self):

        """Devuelve una representacion en cadena del vertice y sus conexiones
        
        Pre:
            - el vertice tiene una clave y un diccionario de vecinos
        
        Post:
            - se devuelve una cadena que muestra la clave del vertice y las claves de sus vecinos
        """

        return str(self.id) + ' conectado a: ' + str([x.id for x in self.conectadoA])
    

    def __lt__(self, other):
        
        """Compara la distancia del vertice actual con la distancia de otro vertice
        
        Pre:
            - other es otro vertice con una distancia asignada
        
        Post:
            - se devuelve True si la distancia del vertice actual es menor que la distancia del otro vertice, 
            de lo contrario se devuelve False
        """

        return self.distancia < other.distancia
    
    def obtenerConexiones(self):

        """Devuelve una lista de los vecinos del vertice
        
        Pre:
            - el vertice tiene un diccionario de vecinos
        
        Post:
            - se devuelve una lista con las claves de los vecinos
        """
        return self.conectadoA.keys()

    def obtenerId(self):
        """Devuelve la clave del vertice 
        
        Pre: 
            - el vertice tiene una clave
        
        Pot:
            - se devuelve la clave del vertice
        """
        return self.id
    
    def obtenerPonderacion(self,vecino):

        """Devuelve la ponderacion de la conexion entre el vertice y un vecino dado
        
        Pre:
            - vecino es un vertice al que se conecta el vertice actual
        
        Post:
            - se devuelve la ponderacion de la conexion entre el vertice y el vecino dado
        """
        return self.conectadoA[vecino]
    
class Grafo:
    
    def __init__(self):

        """Inicializa el grafo con un diccionario de vertices y un contador de vertices
        
        Pre: 
            - el grafo no tiene vertices ni conexiones
        
        Post:
            - se crea un grafo con un diccionario vacio de vertices y un contador de vertices en 0
        """
        self.listaVertices={}
        self.numVertices=0
    
    def agregarVertice(self,clave):

        """Agrega un vertice al grafo con la clave dada
        
        Pre:
            - clave es un valor unico que identifica al vertice
            
        Post:
            - se agrega un vertice al grafo con la clave dada y se incrementa el contador de vertices
        """

        self.numVertices=self.numVertices+1
        nuevoVertice=Vertice(clave)
        self.listaVertices[clave]=nuevoVertice
        return nuevoVertice
    
    def obtenerVertice(self,n):

        """Devuelve el vertice con la clave dada
        
        Pre:
            - n es una clave que identifica a un vertice en el grafo
        
        Post:
            - se devuelve el vertice con la clave dada si existe, de lo contrario se devuelve None
        """
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None
        
    def __contains__(self,n):

        """Verifica si un vertice con la clave dada existe en el grafo
        
        Pre:
            - n es una clave que identifica a un vertice en el grafo
        
        Post:
            - se devuelve True si un vertice con la clave dada existe en el grafo, de lo contrario se 
            devuelve False
        """
        return n in self.listaVertices
    
    def agregararista(self, de, a, costo=0):

        """Agrega una arista entre dos vertices del grafo con un costo dado
        
        Pre:
            - de es la clave del vertice de origen de la arista
            - a es la clave del vertice de destino de la arista
            - costo es el peso de la arista
        
        Post:
            - se agrega una arista entre los vertices de origen y destino con el costo dado
            - si alguno de los vertices no existe en el grafo, se agrega al grafo antes de crear la arista
        """
        if de not in self.listaVertices:
            self.agregarVertice(de)
        if a not in self.listaVertices:
            self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)
        self.listaVertices[a].agregarVecino(self.listaVertices[de], costo)

    def obtenerVertices(self):

        """Devuelve una lista de las claves de los vertices del grafo
        
        Pre:
            - el grafo tiene un diccionario de vertices
        
        Post:
            - se devuelve una lista con las claves de los vertices
        """
        return self.listaVertices.keys()
    
    def __iter__(self):

        """Permite iterar sobre los vertices del grafo
        
        Pre:
            - el grafo tiene un diccionario de vertices
        
        Post:
            - se devuelve un iterador que permite recorrer los vertices del grafo
        """
        return iter(self.listaVertices.values())
    
    