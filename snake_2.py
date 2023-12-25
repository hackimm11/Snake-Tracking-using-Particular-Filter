# coding: utf-8

'''
@author: Fabien Bonardi
'''

# snake_1.py

import random
import numpy as np

class Snake:
    def __init__(self, kParams):
        
        self.x = random.randint(0, kParams['map_w']- 1)
        self.y = random.randint(0, kParams['map_h']- 1)
        self.theta = random.randint(0,3)

        self.c1=np.array[[0,0,0],[0,3,0],[0,1,0]]
        self.c2=np.array[[0,0,0],[0,3,0],[1,1,0]]
        self.c3=np.array[[0,0,0],[0,3,0],[0,1,1]]

        self.c11=np.rot90(self.c1,1)
        self.c12=np.rot90(self.c1,2)
        self.c13=np.rot90(self.c1,3)

        self.c21=np.rot90(self.c2,1)
        self.c22=np.rot90(self.c2,2)
        self.c23=np.rot90(self.c2,3)
        
        self.c31=np.rot90(self.c3,1)
        self.c32=np.rot90(self.c3,2)
        self.c33=np.rot90(self.c3,3)

        
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
            
            #define the neighbourhood of x,y
            self.m=np.empty(3,3)
            self.m[1,1]=3
            self.m[0,0]=measure[0][self.x-1,self.y+1, 0]/255  
            self.m[0,1]=measure[0][self.x,self.y+1, 0]/255               
            self.m[0,2]=measure[0][self.x+1,self.y+1, 0]/255
            self.m[1,0]=measure[0][self.x-1,self.y, 0]/255
            self.m[1,2]=measure[0][self.x+1,self.y, 0]/255
            self.m[2,0]=measure[0][self.x-1,self.y-1, 0]/255
            self.m[2,1]=measure[0][self.x,self.y-1, 0]/255
            self.m[2,2]=measure[0][self.x+1,self.y-1, 0]/255
            

        
            # Calculate snake's orientation

            # first configuration
            if self.m-self.c1==np.zeros((3,3)):
                self.theta_s=0
                self.w=2
                if self.theta==self.theta_s:
                    return self.w+1
                else:
                    return self.w
            elif self.m-self.c11==np.zeros((3,3)):
                self.theta_s=1
                if self.theta==self.theta_s:
                    return self.w+1
                else:
                    return self.w
            elif self.m-self.c12==np.zeros((3,3)):
                self.theta_s=2
                if self.theta==self.theta_s:
                    return self.w+1
                else:
                    return self.w
            elif self.m-self.c13==np.zeros((3,3)):
                self.theta_s=3
                if self.theta==self.theta_s:
                    return self.w+1
                else:
                    return self.w
            
            # second configuration
            elif self.m-self.c2==np.zeros((3,3)):
                self.theta_s=0
                if self.theta==self.theta_s:
                    return self.w+1
                else:
                    return self.w
            elif self.m-self.c21==np.zeros((3,3)):
                self.theta_s=1
                if self.theta==self.theta_s:
                    return self.w+1
                else:
                    return self.w
            elif self.m-self.c22==np.zeros((3,3)):
                self.theta_s=2
                if self.theta==self.theta_s:
                    return self.w+1
                else:
                    return self.w
            elif self.m-self.c23==np.zeros((3,3)):
                self.theta_s=3
                if self.theta==self.theta_s:
                    return self.w+1
                else:
                    return self.w
            
            # third configuration
            elif self.m-self.c3==np.zeros((3,3)):
                self.theta_s=0
                if self.theta==self.theta_s:
                    return self.w+1
                else:
                    return self.w
            elif self.m-self.c31==np.zeros((3,3)):
                self.theta_s=1
                if self.theta==self.theta_s:
                    return self.w+1
                else:
                    return self.w
            elif self.m-self.c32==np.zeros((3,3)):
                self.theta_s=2
                if self.theta==self.theta_s:
                    return self.w+1
                else:
                    return self.w
            elif self.m-self.c33==np.zeros((3,3)):
                self.theta_s=3
                if self.theta==self.theta_s:
                    return self.w+1
                else:
                    return self.w
           
            

            
        else:
            return 0.0
