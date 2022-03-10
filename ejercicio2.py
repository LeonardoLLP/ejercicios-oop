from typing import List
from random import randint

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
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return self.name

class Continente():
    def __init__(self, countries: List[tuple]):
        self.countries = [Pais(country[0], country[1]) for country in countries]


# 3) Agregación. Si se disuelve la molécula, los átomos siguen existiendo.
# Cardinalidad 0 ... 1 hacia Molecula, 2 ... n hacia Atomo

class Atomo():
    def __init__(self, z, mass):
        self.z = z
        self.mass = mass


class Molecula():
    """Objeto inmutable que consta de dos o más átomos.
    """
    def __init__(self, *atomos):
        self._atomos = list(atomos)
        if len(self._atomos) < 2:
            raise ValueError("Molecules can't have less than two atoms")

    def get_atoms(self):
        return self._atomos



# 4) Agregación. Si se destruye la colmena, las abejar se pueden mudar a otra.
# Cardinalidad 1 hacia Colmena, 0 ... n hacia Abeja

class Abeja():
    def __init__(self, tag):
        self.tag = tag

class Colmena():
    def __init__(self, abejas: List[Abeja]):
        self.abejas = abejas

    def count_bees(self):
        return len(self.abejas)

# 5) Agregación. Si desaparece una muñeca, las siguientes siguen funcionando.
# Cardinalidad 0 ... 1 de muñeca a muñeca, ya que cada muñeca solamente encapsula a una o ninguna otra muñeca.

class RussianDoll():
    def __init__(self, smaller_doll):
        self.smaller_doll = smaller_doll

