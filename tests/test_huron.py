import unittest
from models.huron import Huron  # Asegúrate de que la ruta al archivo sea correcta

class Tests_huron(unittest.TestCase):

    def setUp(self):
        self.huron = Huron(nombre="Fuzzy", peso=1.5, edad=3, kilos_comidos=2, pais_origen="Colombia", impuestos=30.0)

    def test_init(self):
        self.assertEqual(self.huron._nombre, "Fuzzy")
        self.assertEqual(self.huron._peso, 1.5)
        self.assertEqual(self.huron._edad, 3)
        self.assertEqual(self.huron._kilos_comidos, 2)
        self.assertEqual(self.huron._pais_origen, "Colombia")
        self.assertEqual(self.huron._impuestos, 30.0)

    def test_hacer_sonido(self):
        self.assertEqual(self.huron.hacer_sonido(), "¡Eeeek Eeeeeeek!")

if __name__ == '__main__':
    unittest.main()
