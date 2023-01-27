import pygame as pg
import random as rd


class Personnage:
    def __init__(self, PV, force, defense, esquive, vitesse, position):
        self.PV = PV
        self.force = force
        self.defense = defense
        self.esquive = esquive
        self.vitesse = vitesse
        self.position = position

    def mouvement(self, direction):
        self.position += direction


class Heros(Personnage):
    def __init__(
        self,
        PV,
        force,
        defense,
        esquive,
        vitesse,
        position,
        argent,
        armes,
        potions,
        faim,
        soif,
    ):
        super().__init__(self, PV, force, defense, esquive, vitesse, position)
        self.argent = argent
        self.armes = armes
        self.potions = potions
        self.faim = faim
        self.soif = soif

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


class Monstre(Personnage):
    def __init__(self, PV, force, defense, esquive, vitesse, position):
        super().__init__(PV, force, defense, esquive, vitesse, position)


def esquive(personnage):
    alea = rd.random
    if alea < personnage.esquive:
        return True
    return False


def attaque(attaquant, defenseur):
    if not (esquive(defenseur)):
        defenseur.PV -= max(attaquant.force - defenseur.defense, 0)


def combat(heros, monstre):
    if heros.vitesse >= monstre.vitesse:
        if not (esquive(monstre)):
            attaque(heros, monstre)
            if monstre.PV <= 0:
                return "Monstre battu"
            attaque(monstre, heros)
            if heros.PV <= 0:
                return "Game over"
    else:
        if not (esquive(heros)):
            attaque(monstre, heros)
            if heros.PV <= 0:
                return "Game over"
            attaque(heros, monstre)
            if heros.PV <= 0:
                return "Monstre battu"
