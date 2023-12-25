# coding: utf-8

'''
@author: Fabien Bonardi
'''

# snake_1.py

import random

class Snake:
    def __init__(self, kParams):
        self.x = random.randint(0, kParams['map_w']- 1)
        self.y = random.randint(0, kParams['map_h']- 1)
        
    def state_transition(self, command):
        self.j = random.randint(1, 4)
        if (self.j == 1) :
            self.x = self.x%199 +1  # update x to left
        elif (self.j == 2) :
            self.x = self.x%199-1  # update x to right
        elif (self.j == 3) :
            self.y = self.y%199+1  # update y to up
        elif (self.j == 4) :
            self.y = self.y%199 -1 
       
    def get_measurement_probability(self, measure):
        
        if measure[0][self.x,self.y, 0]==255:
            return 1.0
        else:
            return 0.0

