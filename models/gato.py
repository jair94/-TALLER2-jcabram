from models.animal import Animal

class Gato(Animal):
    def __init__(self, nombre: str, peso: float, edad: int, kilos_comidos: int):
        super().__init__(nombre, peso, edad, kilos_comidos)

    def hacer_sonido(self):
        return "¡Miau Miau!"

    def __str__(self):
        return super().__str__()