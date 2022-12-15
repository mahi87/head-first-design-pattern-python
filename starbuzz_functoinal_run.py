from starbuzzcoffee_functional.beverage import Espresso, FilterCoffee
from starbuzzcoffee_functional.condiments import with_milk, with_mocha


coffee1 = Espresso()
cost_fn = with_milk(coffee1.cost)
print("Cost: {}".format(cost_fn()))

print(FilterCoffee().cost())