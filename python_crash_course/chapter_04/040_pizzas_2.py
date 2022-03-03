#My pizzas and my friend's pizzas.
my_pizzas = ['portuguese', 'pepperoni', 'mozzarella']
friend_pizzas = my_pizzas[:]
print('My favorite pizzas are:')
for my in my_pizzas:
    print('\t', my.title())
print("\nMy friend's favorite pizzas are:")
for friend in friend_pizzas:
    print('\t', friend.title())
print("\nNow I'm going to add a new pizza to each list.")
my_pizzas.append('margherita')
friend_pizzas.append('napolitana')
print('\nMy favorite pizzas update are:')
for my in my_pizzas:
    print('\t', my.title())
print("\nMy friend's favorite pizzas update are:")
for friend in friend_pizzas:
    print('\t', friend.title())
