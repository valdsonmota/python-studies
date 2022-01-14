#Algorithm that reads an employee's salary and displays his new salary with a 15% increase
print('=' * 10, 'DEFIANCE 013', '=' * 10)
nam = input('What is the employees name?: ')
sal = float(input('What is the employees salary? R$'))
adj = sal * 15 / 100
nsa = sal + adj
print('-' * 35)
print('The employee {} won: R${:.2f}'.format(nam, sal))
print('With a 15 percent increase in the value of R${:.2f}'.format(adj))
print('$' * 15)
print('Starts to receive R${:.2f}'.format(nsa))
print('$' * 15)
