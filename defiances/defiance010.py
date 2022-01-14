'''
Program that reads how much money in R$ a person has in their wallet and shows how many US$ and EUR$ they can buy.
US$ 1 = R$5,58
EUR$ 1 = R$6,42
'''
print('=' * 10, 'DEFIANCE 010', '=' * 10)
brl = float(input('How much money do you have? R$'))
print('With R${:.2f} you can buy US${:.2f} or EUR${:.2f}'.format(brl, (brl/5.68), (brl/6.42)))
