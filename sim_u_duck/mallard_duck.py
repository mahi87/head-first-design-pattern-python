from .duck import Duck
from .quackmixins import Quack, Squeak
from .flymixins import FlyWithWings, FlyNoWay

class MallardDuck(Duck, Quack, FlyWithWings):   
    def display(self):
        print("I'm mallard duck")

class RubberDuck(Duck, Squeak, FlyNoWay):
    def display(self):
        print('I am rubber duck')