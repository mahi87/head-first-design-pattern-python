from abc import ABC, abstractmethod

class Duck(ABC):
    def __init__(self, quack_behavior, fly_behavior):
        self.quack_behavior = quack_behavior
        self.fly_behavior = fly_behavior
    
    @abstractmethod
    def display(self):
        raise NotImplementedError
    
    
    def perform_fly(self):
        self.fly_behavior.fly()
        
    def perform_quack(self):
        self.quack_behavior.quack()
        
    def swim(self):
        print('All ducks can swim')