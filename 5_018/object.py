class Car:
    
    #속성
    def __init__(self, col, len):
        self.color = col
        self.length = len
        
    #기능
    def doStop(self):
        print('stop!!')
        
    def doStart(self):
        print('start!!')
    
    def printCarInfo(self):
        print(self.color)
        print(self.length)
        

car1 = Car('red', 200)
car2 = Car('blue', 300)

car1.printCarInfo()
car2.printCarInfo()

