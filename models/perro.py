from models.animal import Animal

class Perro(Animal):
    def __init__(self, nombre: str, peso: float, edad: int, kilos_comidos: int):
        super().__init__(nombre, peso, edad, kilos_comidos)

    def hacer_sonido(self):
        return "¡Guau Guau!"

    def __str__(self):
        return super().__str__()