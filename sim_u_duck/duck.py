from abc import ABC, abstractmethod

class Duck(ABC):
    @abstractmethod
    def display(self):
        raise NotImplementedError
        
    def swim(self):
        print('All ducks can swim')