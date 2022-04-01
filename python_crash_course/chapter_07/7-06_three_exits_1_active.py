#Exercise 7-6 Three Exits - 1 Active
print(
    '\nEnter the toppings for your pizza.' +
    '\nTo complete the order, say finish.\n'
)
pizza = []
active = True
while active:
    toppings = input('Toppings: ')
    if toppings == 'finish':
        active = False        
    else:
        pizza.append(toppings)
print(
    '\nFinished order with toppings:'
)
for topping in pizza:
    print(
        '\t' + topping.title()
    )
