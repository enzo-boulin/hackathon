#!/usr/bin/env python

# imports:
import pygame as pg
import random as rd 


class Game : 
    def __init__(self, height = 20, width = 20, pix = 10, colors = ['#000000', '#ffffff', '#ff0000', '#00ff00', '#0000ff', '#a0b0c0']) :
        self.h = height
        self.w = width
        self.pix = pix
        self.screen = pg.display.set_mode((self.h*self.pix, self.w*self.pix))
        self.colors = colors

    def draw(self, map) :
        n,p = map.shape
        for i in range(n) :
            for j in range(p) :
                rect = pg.Rect(self.pix*i, self.pix*j, self.pix, self.pix)
                pg.draw.rect(self.screen, self.colors[map[i,j]], rect)


    def get_arrow(self, heros):

        for event in pg.event.get():
        #fermer la fenêtre
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                # si la touche est "Q" on veut quitter le programme
                if event.key == pg.K_q:
                    self.running = False
                #faire le lien entre flèche du clavier et direction du serpent
                elif event.key == pg.K_DOWN:
                    heros.direction = [0,1]
                elif event.key == pg.K_UP:
                    heros.direction = [0,-1]
                elif event.key == pg.K_RIGHT:
                    heros.direction = [1,0]
                elif event.key == pg.K_LEFT:
                    heros.direction = [-1,0]
                elif event.key == pg.K_p:
                    heros.boire(heros.potion) 


#classe       
def generer_ennemi(chambre, matrice):
    (m,n,o,p) = get_position_coin(chambre)
    i = rd.randint(m,n)
    j = rd.randint(o,p)
    matrice[i,j] = 9

def ennemis_alentours(heros, ennemi):
    pos_ennemi = ennemi.position
    pos_heros = heros.position
    if abs(pos_ennemi[0]-pos_heros[0]) ==  1 : 
        return True
    elif abs(pos_ennemi[1]-pos_heros[1]) ==  1 : 
        return True
    else : 
        return False

def ennemi_suit_joueur(heros,ennemi):
    pos_joueur = heros.position
    pos_ennemi = ennemi.position 
    while not ennemis_alentours : #et joueur encore dans la pièce
        if pos_joueur[0] > pos_ennemi[0] :
            ennemi.mouvement(np.array([1,0]))
        elif pos_joueur[0] < pos_ennemi[0] :
            ennemi.mouvement(np.array([-1,0]))
        elif pos_joueur[1] < pos_ennemi[1] :
            ennemi.mouvement(np.array([0,-1]))
        else : 
            ennemi.mouvement(np.array([0,1]))     


def main():
    clock = pg.time.Clock()
    pg.init()

    pg.display.set_caption("Rogue")

    done = False
    while not done:
        pass
    pass


if __name__ == "__main__":
    main()


mapt = np.array(
    [
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 3, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 3, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 3, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 2, 3, 3, 3, 0, 1, 0, 0, 2, 3, 3, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 3, 3, 2, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
)
def launch() :
    pg.init()
    clock = pg.time.Clock()
    g = Game(pix=20)
    g.draw(mapt)
    pg.display.set_caption("'work like a captain, play like a pirate' cf Vic")
    pg.display.update()
    clock.tick(0.01)
    pg.quit()

launch()  
