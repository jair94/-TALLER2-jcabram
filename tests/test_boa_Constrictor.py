import unittest
from models.boa_Constrictor import Boa_Constrictor
 
class Tests_boa_constrictor(unittest.TestCase):
 
    def setUp(self):
        self.boa = Boa_Constrictor("Kaa", 15.0, 5, 10, "Brasil", 100.0)
 
    def test_init(self):
       ## self.boa = Boa_Constrictor("Kaa", 15.0, 5, 10, "Brasil", 100.0)
        self.assertEqual(self.boa._nombre, "Kaa")
        self.assertEqual(self.boa._peso, 15.0)
        self.assertEqual(self.boa._edad, 5)
        self.assertEqual(self.boa._kilos_comidos, 10)
        self.assertEqual(self.boa._pais_origen, "Brasil")
        self.assertEqual(self.boa._impuestos, 100.0)
        self.assertEqual(self.boa.ratones_comidos, 0)
 
    def test_hacer_sonido(self):
      ##  self.boa = Boa_Constrictor(nombre="Kaa", peso=15.0, edad=5, kilos_comidos=10, pais_origen="Brasil", impuestos=100.0)
        self.assertEqual(self.boa.hacer_sonido(), "¡Tsssiiiii!")
 
    def test_comer_ratones(self):
       ## self.boa = Boa_Constrictor(nombre="Kaa", peso=15.0, edad=5, kilos_comidos=10, pais_origen="Brasil", impuestos=100.0)
        self.assertEqual(self.boa.ratones_comidos, 0)
        for _ in range(10):
            self.boa.comer_ratones()
        self.assertEqual(self.boa.ratones_comidos, 10)
        with self.assertRaises(ValueError) as context:
            self.boa.comer_ratones()
        self.assertEqual(str(context.exception), "Demasiados Ratones!")

    def test_str(self):
       ## self.boa = Boa_Constrictor(nombre="Kaa", peso=15.0, edad=5, kilos_comidos=10, pais_origen="Brasil", impuestos=100.0)self.assertEqual(str(self.boa), f"Nombre: {self.boa._nombre}, Peso: {self.boa._peso}kg, Edad: {self.boa._edad} años, País de origen: {self.boa._pais_origen}, Impuestos: {self.boa._impuestos}, Ratones comidos: {self.boa.ratones_comidos}")                    
        self.boa.comer_ratones()
        self.assertEqual(str(self.boa), f"Nombre: {self.boa._nombre}, Peso: {self.boa._peso}kg, Edad: {self.boa._edad} años, País de origen: {self.boa._pais_origen}, Impuestos: {self.boa._impuestos}, Ratones comidos: 1")
 
if __name__ == '__main__':
    unittest.main()