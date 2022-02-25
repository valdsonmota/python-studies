#Program that asks the number of km traveled by a rented car, number of days rented. Calculate the price to pay, knowing that the car costs R$60.00 per day and R$0.15 per km driven.
print('=' * 10, 'DEFIANCE 015', '=' * 10)
dia = int(input('How many days was rented? '))
kmr = float(input('How many kms driven? '))
vdi = 60 * dia
vkm = 0.15 * kmr
print('-' * 30)
print('The total payable is R${:.2f}'.format(vdi + vkm))
print('-' * 30)
