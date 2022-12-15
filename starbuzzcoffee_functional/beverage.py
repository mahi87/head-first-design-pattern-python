from .condiments import with_milk

class Espresso():        
    def cost(self):
        return 1.99
    
class FilterCoffee():  
    
    @with_milk
    def cost(self):
        return 1.99