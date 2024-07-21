from models.huron import Huron
from models.boa_Constrictor import Boa_Constrictor
from models.perro import Perro
from models.gato import Gato

class Guarderia:
    def __init__(self):
        self.huron1 = Huron("Huron de Colombia", 2.3, 3, 5, "Australia", 17)
        self.huron2 = Huron("Huron de Argentina", 1.7, 2, 2, "Suiza", 28)
        self.boa1 = Boa_Constrictor("Boa Constrictor Colombiana", 38.0, 7, 15, "Brasil", 75.0)
        self.boa2 = Boa_Constrictor("Boa Constrictor de Brasil", 15.0, 3, 10, "Colombia", 60.0)
        self.perro1 = Perro("Perro Labrador", 25.0, 5, 10)
        self.gato1 = Gato("Gato Persa", 4.5, 3, 7)

    def alimentar_boa(self, boa: Boa_Constrictor):
        if boa is None:
            return "¡Esta Boa no existe!"

        try:
            boa.comer_ratones()
            return "¡Éxito!"
        except ValueError:
            return "¡La boa está llena!"