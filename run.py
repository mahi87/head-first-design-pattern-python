from sim_u_duck import MallardDuck, RubberDuck
from sim_u_duck.quackmixins import Mute

if __name__ == '__main__':
    m = MallardDuck()
    m.display()
    m.perform_fly()
    m.perform_quack()
    m.swim()
    
    r = RubberDuck()
    r.display()
    r.perform_fly()
    r.perform_quack()
    r.swim()
    
    ans = input('do you want to mute rubber duck?')
    if ans:
        r.quack_behaviour = Mute()