#Exercise 4-13 - Buffet
foods = ('roast beef', 'omelet', 'fried fish', 'noodle', 'chicken rice')
print('-' * 5, 'MENU', '-' * 5)
for food in foods:
    print(food.title())

#foods[2] = 'fried chicken'

'''
Cannot modify a value in the tuple.

Traceback (most recent call last):
  File "c:\python_crash_course\chapter_04\042_buffet.py", line 7, in <module>
    foods[2] = 'fried chicken'
TypeError: 'tuple' object does not support item assignment
'''

#To modify a tuple, it is necessary to completely redefine it.
foods = ('roast beef', 'omelet', 'fried chicken', 'fried rice', 'chicken rice')
print('\n' + '-' * 5, 'NEW MENU', '-' * 5)
for food in foods:
    print(food.title())
