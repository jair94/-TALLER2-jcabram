from models.animal_Exotico import Animal_Exotico

class Boa_Constrictor(Animal_Exotico):
    def __init__(self, nombre: str, peso: float, edad: int,  kilos_comidos:int, pais_origen: str, impuestos: float):
        super().__init__(nombre, peso, edad, kilos_comidos, pais_origen, impuestos)
        self.ratones_comidos = 0

    def hacer_sonido(self):
        return "¡Tsssiiiii!"

    def comer_ratones(self):
        if self.ratones_comidos >= 20:
            raise ValueError("Demasiados Ratones!")
        self.ratones_comidos += 1

    def __str__(self):
        return f"{super().__str__()}, Ratones comidos: {self.ratones_comidos}"
