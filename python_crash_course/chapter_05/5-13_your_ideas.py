#Exercise 5-13 Your Ideas - Valdson's Barbecue
materials = ['barbecue grill', 'coal', 'lighter', 'tables', 'chairs']
foods = ['meats', 'pork sausage', 'garlic bread', 'onion']
drinks = ['soda', 'sparkling water', 'wine', 'beer']
guests = ['claudia', 'vinicius', 'miguel']
checklist = ['coal', 'lighter', 'meats', 'beer', 'miguel']
print('-' * 10, 'MATERIAL', '-' * 10)
for material in materials:
    if (material in checklist):
        print(material.title(), '- Buy')
    else:
        print(material.title(), '- I already have')
print('-' * 10, 'FOODS', '-' * 10)
for food in foods:
    if food in checklist:
        print(food.title(), '- Buy')
    else:
        print(food.title(), '- I already bought')
print('-' * 10, 'DRINKS', '-' * 10)
for drink in drinks:
    if drink == 'sparkling water':
        print(drink.title(), "- Only buy if it's cheap")    
    elif drink in checklist:
        print(drink.title(), '- Buy')
    else:
        print(drink.title(), '- I already bought')
print('-' * 10, 'GUESTS', '-' * 10)
for guest in guests:
    if guest == 'claudia':
        print(guest.title(), '- Confirmed')
    elif guest == 'vinicius':
        print(guest.title(), '- Waiting confirmation' )
    elif guest in checklist:
        print(guest.title(), '- Send invitation')
