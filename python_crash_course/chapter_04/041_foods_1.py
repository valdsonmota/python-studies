#Code using for to display list items.
foods = ['pizza', 'falafel', 'carrot cake', 'cannoli']
friend_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream']
print("Eric Matthes' favorite foods:")
for food in foods:
    print('\t', food.title())
print("\nEric Matthes' friend's favorite foods:")
for friend in friend_foods:
    print('\t', friend.title())
