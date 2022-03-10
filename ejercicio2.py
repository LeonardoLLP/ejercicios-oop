from typing import List

# 1) Agregación. En caso de que el aeropuerto se destruya, los aviones siguen teniendo sentido solos.
# Cardinalidad 1 ... n hacia Aeropuerto, 0 ... n hacia Avión

class Avion():
    def __init__(self, tag, mass, length):
        self.tag = tag
        self.mass = mass
        self.length = length

class Aeropuerto():
    def __init__(self, area, airplanes: List[Avion]):
        self.area = area
        self.airplanes = airplanes

    def fly_to(self, tag: int, aeropuerto):
        list_of_tags = [airplane.tag for airplane in self.airplanes]
        index = list_of_tags.index(tag)
        flying = self.airplanes.pop(index)
        aeropuerto.airplanes.append(flying)


# 2) Composición. Los países no tienen sentido sin el continente.
# Cardinalidad 1 ... n hacia País, 1 hacia Continente (dejamos de lado casos especiales como Rusia).


class Pais():
    def __init__(self, area, location: tuple):
        self.area = area
        self.location = location

class Aeropuerto():
    pass

