import random as rd


class Objet:
    def __init__(self, position):
        self.position = position


class Potion(Objet):

    attributs = ["PV", "force", "defense", "esquive", "vitesse"]

    def __init__(self, position):
        super().__init__(position)
        self.attribut = self.attributs[rd.randint(0, 4)]
