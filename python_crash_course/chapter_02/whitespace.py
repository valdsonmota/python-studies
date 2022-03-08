#Remove whitespace
language = ' python '
print('\n\t1° -', language, '-') #normal
print('\n\t2° -', language.rstrip(), '-') #remove right whitespace
print('\n\t3° -', language.lstrip(), '-') #remove left whitespace
print('\n\t4° -', language.strip(), '-') #remove both whitespace
print('\n\t5° -', language, '-') #the Strings (rstrip, lstrip and strip) only revolves from the display, to permanently remove it you must store the value with the removed character back in the variable.
language = language.strip()
print('\n\t6° -', language, '-') #now whitespace has been permanently removed in the variable.
