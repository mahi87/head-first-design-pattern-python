class FlyBehavior():
    def fly():
        pass
    
class FlyWithWings(FlyBehavior):
    def fly():
        return 'YAY! I can fly'
    
class FlyNoWay(FlyBehavior):
    def fly():
        return "Oops! I can't fly"