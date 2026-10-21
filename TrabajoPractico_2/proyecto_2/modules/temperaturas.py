from datetime import datetime
from ayedfiuner.estructuras.AVL import AVL

class Temperaturas_DB:

    def __init__(self):
        self.avl=AVL()

    def convertir_fecha(self, fecha):
        return datetime.strptime(fecha, "%d/%m/%Y")

    def guardar_temperatura(self, temperatura, fecha):
        fecha_dt=self.convertir_fecha(fecha)
        self.avl.agregar(fecha_dt, temperatura)

    def devolver_temperatura(self, fecha):
        fecha_dt=self.convertir_fecha(fecha)
        return self.avl.obtener(fecha_dt)
    
    def borrar_temperatura(self, fecha):
        fecha_dt=self.convertir_fecha(fecha)
        self.avl.eliminar(fecha_dt)

    def cantidad_muestras(self):
        return len(self.avl)
    
    def devolver_temperaturas(self, fecha1, fecha2):
        fecha1_dt=self.convertir_fecha(fecha1)
        fecha2_dt=self.convertir_fecha(fecha2)
        
        lista=[]

        self._inorden_rango(self.avl.raiz, fecha1_dt, fecha2_dt, lista)

        return lista
    
    def _inorden_rango(self, nodo, fecha1, fecha2, lista):
        if nodo is None:
            return
        
        if nodo.clave>fecha1:
            self._inorden_rango(nodo.hijoIzquierdo, fecha1, fecha2, lista)
        
        if fecha1<=nodo.clave<=fecha2:
            fecha_str=nodo.clave.strftime("%d/%m/%Y")
            lista.append(f"{fecha_str}: {nodo.cargaUtil}°C")

        if nodo.clave<fecha2:
            self._inorden_rango(nodo.hijoDerecho, fecha1, fecha2, lista)

    def max_temp_rango(self, fecha1, fecha2):
        fecha1_dt=self.convertir_fecha(fecha1)
        fecha2_dt=self.convertir_fecha(fecha2)

        maximo=[float('-inf')]
        self._max_rango(self.avl.raiz, fecha1_dt, fecha2_dt, maximo)

        return maximo[0] if maximo[0] != float('-inf') else None
    
    def _max_rango(self, nodo, fecha1, fecha2, maximo):
        if nodo is None:
            return
        
        if nodo.clave>fecha1:
            self._max_rango(nodo.hijoIzquierdo, fecha1, fecha2, maximo)

        if fecha1<=nodo.clave<=fecha2:
            if nodo.cargaUtil>maximo[0]:
                maximo[0]=nodo.cargaUtil

        if nodo.clave<fecha2:
            self._max_rango(nodo.hijoDerecho, fecha1, fecha2, maximo)

    def min_temp_rango(self, fecha1, fecha2):
        fecha1_dt=self.convertir_fecha(fecha1)
        fecha2_dt=self.convertir_fecha(fecha2)

        minimo=[float('inf')]
        self._min_rango(self.avl.raiz, fecha1_dt, fecha2_dt, minimo)

        return minimo[0] if minimo[0] != float('inf') else None
    
    def _min_rango(self, nodo, fecha1, fecha2, minimo):
        if nodo is None:
            return
        
        if nodo.clave>fecha1:
            self._min_rango(nodo.hijoIzquierdo, fecha1, fecha2, minimo)

        if fecha1<=nodo.clave<=fecha2:
            if nodo.cargaUtil<minimo[0]:
                minimo[0]=nodo.cargaUtil

        if nodo.clave<fecha2:
            self._min_rango(nodo.hijoDerecho, fecha1, fecha2, minimo)

    def temp_extremos_rango(self, fecha1, fecha2):
        fecha1_dt=self.convertir_fecha(fecha1)
        fecha2_dt=self.convertir_fecha(fecha2)

        minimo=[float('inf')]
        maximo=[float('-inf')]

        self._extremos_rango(self.avl.raiz, fecha1_dt, fecha2_dt, minimo, maximo)

        return (minimo[0] if minimo[0] != float('inf') else None, maximo[0] if maximo[0] != float('-inf') else None)
    
    def _extremos_rango(self, nodo, fecha1, fecha2, minimo, maximo):
        if nodo is None:
            return
        
        if nodo.clave>fecha1:
            self._extremos_rango(nodo.hijoIzquierdo, fecha1, fecha2, minimo, maximo)

        if fecha1<=nodo.clave<=fecha2:
            if nodo.cargaUtil<minimo[0]:
                minimo[0]=nodo.cargaUtil
            if nodo.cargaUtil>maximo[0]:
                maximo[0]=nodo.cargaUtil

        if nodo.clave<fecha2:
            self._extremos_rango(nodo.hijoDerecho, fecha1, fecha2, minimo, maximo)

    
    

        

            


 



