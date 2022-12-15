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
    
class FilterCoffee(Beverage):
    def __init__(self):
        self.description = 'Filter coffee'
    
    def cost(self):
        from starbuzz_coffee.condiment import Milk
        return 0.60 + Milk(base_drink=None).cost()