import numpy as np
import robotClass
import ballClass

class Vision(robotClass, ballClass):
    def getPoseRobot(self):
        # x = self.xPos
        # y = self.yPos
        # t = self.theta
        x = 150 * np.random()
        y = 130 * np.random()
        t = 2 * np.pi * np.random() - np.pi
        return [x, y, t]
    
    def getPoseBall(self):
        # x = self.xPos
        # y = self.yPos
        x = 150 * np.random()
        y = 130 * np.random()
        return [x, y]
