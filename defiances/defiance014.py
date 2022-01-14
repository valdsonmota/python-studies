#Program that takes a temperature typed in °C and converts it to °F
print('=' * 10, 'DEFIANCE 014', '=' * 10)
c = float(input('Enter the temperature in °C: '))
f = (c * 9/5) + 32
print('The temperature of {}°C stands for {}°F.'.format(c, f))
