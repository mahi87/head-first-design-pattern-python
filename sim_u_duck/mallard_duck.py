from .duck import Duck
from .quack_behavior import Quack
from .fly_behavior import FlyWithWings

class MallardDuck(Duck):
    def __init__(self):
        super().__init__(Quack(), FlyWithWings())
    

    def display(self):
        print("I'm mallard duck")
