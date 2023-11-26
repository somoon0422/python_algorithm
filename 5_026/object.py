class Robot:
    
    def __init__(self, c,h,w):
       self.color = c
       self.height = h
       self.weight = w
       
    def fire(self):
        print('미사일발사')
        
    def printRobotInfo(self):
        print(f'self.color: {self.color}')
        print(f'self.color: {self.height}')
        print(f'self.color: {self.weight}')
         
         
class NewRobot(Robot):
    def __init__(self, c,h,w):
        super().__init__(c,h,w)
        
    def fire(self):
        print('레이저발사!')
        
        
myRobot = NewRobot('red', 200,300)
myRobot.printRobotInfo()
myRobot.fire()
