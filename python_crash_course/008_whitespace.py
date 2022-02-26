#Remove whitespace
language = ' python '
print('1° -', language, '-') #normal
print('2° -', language.rstrip(), '-') #remove right whitespace
print('3° -', language.lstrip(), '-') #remove left whitespace
print('4° -', language.strip(), '-') #remove both whitespace
print('5° -', language, '-') #the Strings (rstrip, lstrip and strip) only revolves from the display, to permanently remove it you must store the value with the removed character back in the variable.
language = language.strip()
print('6° -', language, '-') #now whitespace has been permanently removed in the variable.
