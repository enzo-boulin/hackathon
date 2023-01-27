import random as rd


class Objet:
    def __init__(self, position, type):
        self.position = position
        if type == 5:
            self.description = "Vous avez trouvé une potion appuyé sur p pour la boire."
        if type == 4:
            moula = rd.randint(10, 101)
            self.description = f"Vous avez trouvé {moula} gold !"


class Potion(Objet):

    attributs = ["PV", "force", "defense", "esquive", "vitesse"]

    def __init__(self, position):
        super().__init__(position)
        self.attribut = self.attributs[rd.randint(0, 4)]
        self.description = "Vous avez trouvé une potion appuyé sur p pour la boire"
