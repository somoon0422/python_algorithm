#추상클래스! (상위 클래스에서 하위 클래스에 메서드 구현을 강요한다.)

from abc import ABCMeta
from abc import abstractmethod

class AirPlane(metaclass=ABCMeta):
    
    @abstractmethod
    def flight(self):
        pass
    
    def forward(self):
        print('전진!')
        
    def backward(self):
        print('후진!')
        
class AirLiner(AirPlane):
    
    def __init__(self, c):
        self.color = c
        
    def flight(self):
        print('시속 400km/h 비행!!')
        
class flightPlane(AirPlane):
    
    def __init__(self,c):
        self.color = c
    
    def flight(self):
        print('시속 700km/h 비행!!')
    
        
al = AirLiner('red')
al.flight()
al.forward()
al.backward()

fl = flightPlane('purple')
fl.flight()
fl.forward()
fl.backward()
