from models.ianimal import IAnimal
from abc import ABC, abstractmethod


class Animal(IAnimal, ABC):
    def __init__(self, nombre:str, peso:float, edad:int, kilos_comidos:int) -> None:
        self._nombre = nombre
        self._peso = peso
        self._edad = edad
        self._kilos_comidos = kilos_comidos

    def obtener_nombre(self) -> str:
        return self._nombre    
    
    @abstractmethod
    def hacer_sonido(self) -> str:
        pass

    def comer(self, kilos:int):
        self._kilos_comidos += kilos

    def obtener_kilos_comidos(self):
        return self._kilos_comidos

    def __str__(self):
        return f"Nombre: {self._nombre}, Peso: {self._peso}kg, Edad: {self._edad} años"
