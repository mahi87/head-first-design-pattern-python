from starbuzz_coffee.beverage import Beverage

class Mocha(Beverage):
    def __init__(self, base_drink):
        self.base_drink = base_drink
        self.description = base_drink.description + ' with Mocha'
        
    def cost(self):
        return self.base_drink.cost() + 0.20
    
class Milk(Beverage):
    def __init__(self, base_drink):
        self.base_drink = base_drink
        self.description = base_drink.description + ' with Milk'
        
    def cost(self):
        return (self.base_drink.cost() + 0.50) if self.base_drink else 0.50