# Archivo de test para realizar pruebas unitarias del modulo1

#Test de prueba no es el que nos dio el profesor, lo hice yo para probar

import unittest
from proyecto_2.modules.modulo1 import ColaCircular

class TestColaCircular(unittest.TestCase):

    def test_encolar_y_desencolar(self):
        cola = ColaCircular(3)
        self.assertTrue(cola.esta_vacia())
        
        cola.encolar("P1")
        cola.encolar("P2")
        
        self.assertEqual(len(cola), 2)
        self.assertEqual(cola.frente(), "P1")
        self.assertEqual(cola.desencolar(), "P1")
        self.assertEqual(cola.desencolar(), "P2")
        self.assertTrue(cola.esta_vacia())

    def test_cola_llena(self):
        cola = ColaCircular(2)
        cola.encolar("A")
        cola.encolar("B")
        self.assertTrue(cola.esta_llena())
        with self.assertRaises(OverflowError):
            cola.encolar("C")

if __name__ == '__main__':
    unittest.main()