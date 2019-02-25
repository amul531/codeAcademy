#list of pizza type (w/toppings)
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

#list of pizza slice prices
prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)
print("We sell {X} different kinds of pizzas!".format(X=num_pizzas))

#combining pizza and price
pizzas = list(zip(prices, toppings))

pizzas.sort()
cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
three_cheapest = pizzas[:3]
print(three_cheapest)
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
