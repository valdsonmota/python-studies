#Algorithm that reads a product price and displays its new price with a 5% discount
print('=' * 10, 'DEFIANCE 012', '=' * 10)
pri = float(input('Price of the product: R$'))
dis = pri * (5/100)
print('The price of the product is R${:.2f}'.format(pri))
print('          5% off -R${:.2f}'.format(dis))
print('=' * 20)
print('Total R${:.2f}'.format(pri-dis))
print('=' * 20)
