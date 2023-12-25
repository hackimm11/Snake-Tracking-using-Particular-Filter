import numpy as np
#Creating the snake class
class Snake:
    def __init__(self, border, state):
        self.border = border # border of image wich is 200
        self.state = state # particle contain thepostition in th first item and 0 for x and 1 for y for the second item
#the possible moves of the snake from one step t to the next one are left right top up
    def trans(self):
        n_particles = len(self.state)
        for i in range(n_particles):
            j = np.random.randint(1, 5)
            if (j == 1 and self.state[i - 1, 0] < (self.border - 1)):
                self.state[i - 1, 0] = self.state[i - 1, 0] + 1  # update x going left
            elif (j == 2 and self.state[i - 1, 0] > 0):
                self.state[i - 1, 0] = self.state[i - 1, 0] - 1  # update x going right
            elif (j == 3 and self.state[i - 1, 1] < (self.border - 1)):
                self.state[i - 1, 1] = self.state[i - 1, 1] + 1  # update y going up
            elif (j == 4 and self.state[i - 1, 1] > 0):
                self.state[i - 1, 1] = self.state[i - 1, 1] - 1  # update y going down
# function that do the measurement for each state based on if the pixel is on the snake
    def measure(self):
        m = np.zeros([len(self.state),1])
        for i in range(len(self.state)):
            if self.state[i - 1, 0] and self.state[i - 1, 1] == 0:   #check if the pixel is black
                m[i-1] = 1  #return a value of 1 if it is black (on the snake) and 0 otherwise
        return m.T

#We cannot estimate the position of the snake head with this method because it doesnt take in consideration the orientation of the snake's head        