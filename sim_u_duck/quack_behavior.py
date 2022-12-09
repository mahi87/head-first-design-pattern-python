class QuackBehavior():
    def quack():
        pass
    
class Quack(QuackBehavior):
    def quack():
        return 'Quack Quack'
    
class Squeak(QuackBehavior):
    def quack():
        return 'Squeak Squeak'
    
class Mute(QuackBehavior):
    def quack():
        return "Beeeeppppp"