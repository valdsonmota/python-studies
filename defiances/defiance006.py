#Algorithm that reads a number and displays its double, triple and square root
print('====== DEFIENCE 006 ======')
num = int(input('Enter a number: '))
dou = num * 2
tri = num * 3
sqr = num ** (1/2)
print('The double {} is {}'.format(num, dou))
print('The triple {} is {}'.format(num, tri))
print('The square root of {} is {:.2f}'.format(num, sqr))
