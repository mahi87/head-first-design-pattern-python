from .duck import Duck
from .quack_behavior import Quack, Squeak
from .fly_behavior import FlyWithWings, FlyNoWay

class MallardDuck(Duck, Quack, FlyWithWings):   
    def display(self):
        print("I'm mallard duck")

class RubberDuck(Duck, Squeak, FlyNoWay):
    def display(self):
        print('I am rubber duck')