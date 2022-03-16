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
        else:
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
    def __init__(self, *args):
        """Pass in tuples of (Comida, int)

        int represents nummber of items
        """
        self.food = {}
        for item in args:
            if item[0] in self.food.keys():
                self.food[item[0]] = self.food[item[0]] + item[1]
            else:
                self.food[item[0]] = item[1]

    def sacar_comida(self, comida: Comida, quantity: int):
        if comida in self.food.keys():
            if quantity <= self.food[comida]:
                self.food[comida] = self.food[comida] - quantity
            else:
                print("No tenemos tanta comida")
        else:
            print("No tenemos esta comida")

    def añadir_comida(self, comida: Comida, quantity: int):
        if comida in self.food.keys():
                self.food[comida] = self.food[comida] + quantity
        else:
            self.food[comida] = quantity


class Zoo():
    # Tiene sentido que aunque sea composición los "items" de zoo sean objetos independientes
    def __init__(self, cuidadores: List[Cuidador], animales: List[Animal], stock: Stock):
        self.cuidadores = animales
        self.animales = cuidadores
        self.stock = stock

    def __del__(self):
        for item in self.cuidadores:
            del item
        for item in self.animales:
            del item
        del self.stock

    def cuidar(self, cuidador: Cuidador, animal: Animal):
        if cuidador in self.cuidadores and animal in self.animales:
            cuidador.cuidar(animal)

    def coger_vacaciones(self, cuidador: Cuidador, inicio, duracion):
        cuidador.vacaciones = Vacaciones(inicio, duracion, cuidador)
