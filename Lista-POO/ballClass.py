class Ball:
    def __init__(self):
        self.xPos = 0
        self.yPos = 0
    
    def setXPos(self, x):
        self.xPos = x
    
    def setYPos(self, y):
        self.yPos = y
    
    def getXPos(self, x):
        return self.xPos
    
    def getYPos(self, y):
        return self.yPos
    
    def setPose(self, x, y):
        self.xPos = x
        self.yPos = y
