from starbuzz_coffee.beverage import Espresso, HouseBlend
from starbuzz_coffee.condiment import Milk, Mocha

coffee1 = Mocha(Milk(Espresso()))

print(coffee1.description)
print(coffee1.cost())

coffee2 = Mocha(HouseBlend())
print(coffee2.description)
print(coffee2.cost())

double_mocha = Mocha(Mocha(Espresso()))
print(double_mocha.description + ' - ' + str(double_mocha.cost()))