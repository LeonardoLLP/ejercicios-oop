from enum import Enum
from inspect import ClassFoundException
from typing import List


class Dieta(Enum):
    HERBIVORO = 1
    CARNIVORO = 2
    INSECTIVORO = 3


class Animal():
    def __init__(self, id, dieta, cuidador_actual):
        self.id = id
        self.dieta = list(dieta)
        self.cuidador_actual = cuidador_actual

    def operacion1(self, *params):
        obj = []
        for item in list(params):
            obj.append(type(item))
        return obj

    def operacion2(self, *params):
        print("Doing some shit")

    def operacion3(self):
        print("Doing even more shit")


class Vacaciones():
    def __init__(self, inicio, duracion, empleado):
        self.inicio = inicio
        self.duracion = duracion
        self.empleado = empleado


class Cuidador():
    pass
    def __init__(self, nombre, apellido, animales: List[Animal]):
        self.nombre = nombre
        self.apellido = apellido
        self.animales = animales
        self.vacaciones = None
        self.animales = []

    def solicitar_vacaciones(self, inicio, duracion):
        self.vacaciones = Vacaciones(inicio, duracion, self)

    def cuidar(self, animal: Animal):
        self.animales.append(animal)

    def dejar_de_cuidar(self, animal: Animal):
        if animal in self.animales:
            self.animales.remove(animal)
        else
            print("Ese animal no está en mi lista")

    def alimentar(self, animal: Animal):
        if animal in self.animales:
            print("Alimentando a {}".format(animal.id))
        else:
            print("Yo no cuido a ese animal")


class Comida():
    # No tiene sentido lista de dietas: o es para herbivoros, o para carnivoros, o insectivoros.
    # Tiene sentido lista de dietas en animales
    def __init__(self, dieta):
        self.dieta = dieta


class Stock():
    def __init__(self):
        pass