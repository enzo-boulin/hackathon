import numpy as np

class screen :
   def __init__(self, height = 20, width = 20) :
      self.height = 20
      self.width = 20
      A = np.zeros((self.height, self.width), dtype='uint8')
      room_number = np.random.randint(1,6, dtype='uint8')
      room_pos = []
      while len(room_pos)<room_number :
         #position du coin en haut à gauche de la room
         x,y = np.random.randint(0, self.height, dtype='uint8'),np.random.randint(0, self.width, dtype='uint8')
         h,w = np.random.randint(self.height//5, self.height//2, dtype='uint8'),np.random.randint(self.width//5, self.width//2, dtype='uint8')
         if x+h < self.height





