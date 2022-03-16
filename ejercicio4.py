from enum import Enum


class Dieta(Enum):
    HERBIVORO = 1
    CARNIVORO = 2
    INSECTIVORO = 3


class Animal:
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


class Empleado():
    pass
    

class Vacaciones():
    def __init__(self, inicio, duracion, empleado: Empleado):
        self.inicio = inicio
        self.duracion = duracion
        self.empleado = empleado