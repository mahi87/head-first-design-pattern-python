from pizza_factory import PizzaStore, SimplePizzaFactory

store = PizzaStore(SimplePizzaFactory())
type_of_pizza = input("enter type of pizza")
store.order_pizza(type_of_pizza)