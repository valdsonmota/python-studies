#Exercise 7-4 Pizza Toppings
print(
    '\nEnter the toppings for your pizza.' +
    '\nTo complete the order, say finish.\n'
)
toppings = ''
pizza = []
while toppings != 'finish':
    toppings = input('Toppings: ')
    if toppings != 'finish':
        pizza.append(toppings)
    else:
        print(
            '\nFinished order with toppings:'
        )
        for topping in pizza:
            print('\t' + topping.title())
