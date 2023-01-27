#!/usr/bin/env python

# imports:
import pygame as pg
import random as rd 
import numpy as np


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
    (m,n,o,p) = chambre.coin()
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

class Screen :
   def __init__(self, height = 20, width = 20) :
      self.height = height
      self.width = width
      self.map = np.zeros((self.height, self.width), dtype='uint8')
      room_number = np.random.randint(2,4, dtype='uint8')
      #position du coin en haut à gauche en clé et bas droite attribu
      self.room_pos = {}
      c=0
      while len(self.room_pos)<room_number and c < 100000:
         c+=1
         #position du coin en haut à gauche de la room
         x,y = np.random.randint(0, self.height, dtype='uint8'),np.random.randint(0, self.width, dtype='uint8')
         h,w = np.random.randint(self.height//5, self.height//2, dtype='uint8'),np.random.randint(self.width//5, self.width//2, dtype='uint8')
         if x+h <= self.height and y+w <= self.width :
            if len(self.room_pos) == 0 :
               self.room_pos[(x,y)] = x+h,y+w

            if not self.conflict((x,y), (h,w)) :
               self.room_pos[(x,y)] = x+h,y+w
      self.room_number = len(self.room_pos)
      self.add_room()

   
   def conflict(self, pos, size) :
      x,y = pos
      h,w = size
      for i,j in self.room_pos :
         I,J = self.room_pos[(i,j)]
         if (x+h>i-3 and x+h<I+3) and (y+w>j-3 and y+w<J+3) :
            return True
         if (x>i-3 and x<I+3) and (y>j-3 and y<J+3) :
            return True
         if (x>i-3 and x<I+3) and (y+w>j-3 and y+w<J+3) :
            return True
         if (x+h>i-3 and x+h<I+3) and (y>j-3 and y<J+3) :
            return True
      return False


               


   def add_room(self) :
      for i,j in self.room_pos :
         h,w = self.room_pos[(i,j)][0]-i, self.room_pos[(i,j)][1]-j
         mur1 = [(i+k,j) for k in range(h)]
         mur2 = [(i,j+k) for k in range(w)]
         mur3 = [(i+h-1,j+k+1) for k in range(w-1)]
         mur4 = [(i+k+1, j+w-1) for k in range(h-1)]
         mur = mur1+mur2+mur3+mur4
         for pos in mur :
            self.map[pos] = 1



def main():
    pg.init()
    clock = pg.time.Clock()
    screen = Screen()
    n,p = screen.map.shape
    screen_pg = pg.display.set_mode((n*10, p*10))
    rect = pg.Rect(scases*i, scases*j, scases, scases)
    pg.draw.rect(self._screen, self._color1, rect)
    pg.display.set_caption("Rogue")

    done = False
    while not done:
        pass
    pass


if __name__ == "__main__":
    main()

    
        






