class Robot:
    def __init__(self):
        self.L = 7.5
        self.R = 3.5
        self.xPos = 0
        self.yPos = 0
        self.theta = 0
    
    def setXPos(self, x):
        self.xPos = x
    
    def setYPos(self, y):
        self.yPos = y
    
    def setTheta(self, t):
        self.theta = t
    
    def setL(self, distancia):
        self.L = distancia
    
    def setR(self, raio):
        self.R = raio
    
    def getXPos(self, x):
        return self.xPos
    
    def getYPos(self, y):
        return self.yPos
    
    def getTheta(self, t):
        return self.theta
    
    def getL(self, distancia):
        return self.L
    
    def getR(self, raio):
        return self.R
    
    def setPose(self, x, y, t):
        self.xPos = x
        self.yPos = y
        self.theta = t
