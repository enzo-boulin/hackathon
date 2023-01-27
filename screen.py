import numpy as np

class screen :
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
      self.draw_room()


   def no_conflict1(self, pos, size) : #inutile
      x,y = pos
      h,w = size
      up = 0
      for i,j in self.room_pos :
         I,J = self.room_pos[(i,j)]
         if x+h<i or y+w<j :
            return True
         if x > I or y > J :
            return True 

      up = np.array([x+h<i or y+w<j for i,j in self.room_pos ])
      up1 = up.all
      down = np.array([x > self.room_pos[(i,j)][0] or y > self.room_pos[(i,j)][0] for i,j in self.room_pos])
      down1 = down.all
      if down1 or up1 :
         return True
      return False
   
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


               


   def draw_room(self) :
      for i,j in self.room_pos :
         h,w = self.room_pos[(i,j)][0]-i, self.room_pos[(i,j)][1]-j
         mur1 = [(i+k,j) for k in range(h)]
         mur2 = [(i,j+k) for k in range(w)]
         mur3 = [(i+h-1,j+k+1) for k in range(w-1)]
         mur4 = [(i+k+1, j+w-1) for k in range(h-1)]
         mur = mur1+mur2+mur3+mur4
         for pos in mur :
            self.map[pos] = 1

         

a = screen()
print(a.map)
import matplotlib.pyplot as plt
plt.imshow(a.map)
plt.colorbar()
plt.show()
plt.close()








