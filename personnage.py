import random as rd
import pygame as pg


class Personnage:
    def __init__(self, PV, force, defense, esquive, vitesse, position, direction):
        self.PV = PV
        self.force = force
        self.defense = defense
        self.esquive = esquive
        self.vitesse = vitesse
        self.position = position
        self.direction = direction

    def mouvement(self, map):
        case = self.position + self.direction
        if map[case[0]][case[1]] != 1:
            self.position += self.direction


class Heros(Personnage):
    def __init__(
        self,
        PV,
        force,
        defense,
        esquive,
        vitesse,
        position,
        direction,
        argent,
        potions,
    ):
        super().__init__(PV, force, defense, esquive, vitesse, position, direction)
        self.argent = argent
        self.potions = potions

    def boire(self, potion):
        attribut = potion.attribut
        if attribut == "PV":
            valeur = self.PV
            self.PV += rd.randint(-int(valeur / 2), int(valeur / 2))
        if attribut == "force":
            valeur = self.force
            self.force += rd.randint(-int(valeur / 2), int(valeur / 2))
        if attribut == "defense":
            valeur = self.defense
            self.defense += rd.randint(-int(valeur / 2), int(valeur / 2))
        if attribut == "esquive":
            valeur = self.esquive
            self.PV += rd.randint(-int(valeur / 2), int(valeur / 2))
        if attribut == "vitesse":
            valeur = self.vitesse
            self.vitesse += rd.randint(-int(valeur / 2), int(valeur / 2))


def esquive(personnage):
    alea = rd.random()
    if alea < personnage.esquive:
        return True
    return False


def attaque(attaquant, defenseur):
    if not (esquive(defenseur)):
        defenseur.PV -= max(attaquant.force - defenseur.defense, 0)
    return max(attaquant.force - defenseur.defense, 0)


def combat(heros, monstre):
    pg.init()
    print("Le combat commence")
    if heros.vitesse >= monstre.vitesse:
        if not (esquive(monstre)):
            degat = attaque(heros, monstre)
            print(f"Vous avez infligé {degat} degat(s)")
            if monstre.PV <= 0:
                heros.PV += 5
                heros.force += 1
                print("Monstre battu")
                return None
        if not (esquive(heros)):
            degat = attaque(monstre, heros)
            print(f"Le monstre a infligé {degat} degat(s)")
            if heros.PV <= 0:
                print("Game over")
                return None
    else:
        if not (esquive(heros)):
            degat = attaque(monstre, heros)
            print(f"Vous avez infligé {degat} degat(s)")
            if heros.PV <= 0:
                print("Game over")
                return None
        if not (esquive(monstre)):
            degat = attaque(heros, monstre)
            print(f"Vous avez infligé {degat} degat(s)")
            if monstre.PV <= 0:
                heros.PV += 5
                heros.force += 1
                print("Monstre battu")
                return None
