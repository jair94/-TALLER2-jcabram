from models.animal import Animal

class Animal_Exotico(Animal):
    def __init__(self, nombre: str, peso: float, edad: int,  kilos_comidos:int, pais_origen: str, impuestos: float):
        super().__init__(nombre, peso, edad, kilos_comidos)
        self._pais_origen = pais_origen
        self._impuestos = impuestos

    def calcular_flete(self):
        return self._impuestos * self._peso

    def __str__(self):
        return f"{super().__str__()}, País de origen: {self._pais_origen}, Impuestos: {self._impuestos}"
