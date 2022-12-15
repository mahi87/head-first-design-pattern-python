from .pizza import CheesePizza, PepperoniPizza, ClamPizza

class SimplePizzaFactory():
    def create_pizza(self, type):
        if type=='cheese':
            return CheesePizza()
        elif type=='pepperoni':
            return PepperoniPizza()
        elif type=='clam':
            return ClamPizza()
        else:
            raise NotImplementedError('Pizza type not supported')
