# 1) NO: Saturno ES un planeta, por tanto, es una instancia de este:

class Planet():
    def __init__(self, mass: int, diameter: int, has_rings: bool = False):
        self.mass = mass
        self.diameter = diameter
        self.has_rings = has_rings

saturn = Planet(5.683*(10**26), 58232*2, has_rings = True)


# 2) SI: un directorio telefónico puede tener propiedades adicionales a la lista,
# y puede convenir hacer una subclase para generalizar estas propiedades

class Lista():
    def __init__(self, *args):
        self._registros = list(args)

    def get_length(self):
        return len(self._registros)

    def search_item(self, index):
        try:
            return self._registros[index]
        except:
            print("Index not valid")


class DirectorioTelefonico(Lista):
    def __init__(self, *args: tuple):
        """Expects (name, number) tuple"""
        self._registros = list(args)

    def search_by_name(self, name):
        name_list = [registro[0] for registro in self._registros]
        if name in name_list:
            index = name_list.index(name)
            return str(self._registros[index][1])
        else:
            return("Name not found")


# 3) SI: un perro puede representarse como una subclase de animal de compañia: un perro específico sería una instancia de esta clase

class AnimalCompania():
    def __init__(self, year_born, mass):
        self.year_born = year_born
        self.mass = mass

class Perro(AnimalCompania):
    def __init__(self, year_born, mass, raza):
        super().__init__(year_born, mass)  #TODO: Revisar porqué no funciona
        self.raza = raza

p = Perro(2, 3, "Chow chow")
print(p.year_born)


# 4) NO: Una bicicleta está compuesta por dos ruedas pero no tienen relación. Es uan agregación (o una composición si
# consideramos que las ruedas van ligadas a la bicicleta)


class Rueda():
    def __init__(self, diameter):
        self.diameter = diameter

class Bicicleta():
    def __init__(self, compound: str, r1: Rueda, r2: Rueda):
        self.compound = compound
        self.wheels = [r1, r2]

