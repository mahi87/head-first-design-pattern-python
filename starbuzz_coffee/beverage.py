from abc import ABC, abstractmethod

class Beverage(ABC):
    def __init__(self):
        self.description = 'Unknown Beverage'
        
    @abstractmethod
    def cost(self):
        raise NotImplementedError
    
class Espresso(Beverage):
    def __init__(self):
        self.description = 'Espresso'
        
    def cost(self):
        return 1.99
    
class HouseBlend(Beverage):
    def __init__(self):
        self.description = 'HouseBlend'
        
    def cost(self):
        return 0.89   