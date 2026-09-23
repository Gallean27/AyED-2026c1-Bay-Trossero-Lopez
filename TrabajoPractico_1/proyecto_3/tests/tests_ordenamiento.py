import unittest
from modules.ordenamientos import ordenamiento_burbuja, ordenamiento_radix, quicksort

class TestOrdenamientos(unittest.TestCase):

    def setUp(self):
        self.lista_desordenada = [64, 34, 25, 12, 22, 11, 90]
        self.lista_ordenada_esperada = [11, 12, 22, 25, 34, 64, 90]
        self.lista_vacia = []
        self.lista_un_elemento = [42]
        self.lista_duplicados = [5, 1, 5, 2, 1, 9]
        self.lista_duplicados_esperada = [1, 1, 2, 5, 5, 9]

    def test_burbuja(self):
        self.assertEqual(ordenamiento_burbuja(list(self.lista_desordenada)), self.lista_ordenada_esperada)
        self.assertEqual(ordenamiento_burbuja(list(self.lista_vacia)), [])
        self.assertEqual(ordenamiento_burbuja(list(self.lista_duplicados)), self.lista_duplicados_esperada)

    def test_radix(self):
        self.assertEqual(ordenamiento_radix(self.lista_desordenada), self.lista_ordenada_esperada)
        self.assertEqual(ordenamiento_radix(self.lista_vacia), [])
        self.assertEqual(ordenamiento_radix(self.lista_duplicados), self.lista_duplicados_esperada)

    def test_quicksort(self):
        self.assertEqual(quicksort(self.lista_desordenada), self.lista_ordenada_esperada)
        self.assertEqual(quicksort(self.lista_vacia), [])
        self.assertEqual(quicksort(self.lista_duplicados), self.lista_duplicados_esperada)

if __name__ == '__main__':
    unittest.main()