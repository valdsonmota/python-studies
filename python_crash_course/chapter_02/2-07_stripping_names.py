#Exercise 2-7 - Stripping Names
name = ' valdson mota '
print('\n\t1° -', name, '-')
print('\n\t2° -', name.rstrip(), '-')
print('\n\t3° -', name.lstrip(), '-')
print('\n\t4° -', name.strip(), '-')
print('-' * 50)
language = ' python '
print('\n\t1° -', language, '- normal')
print('\n\t2° -', language.rstrip(), '- Remove right whitespace')
print('\n\t3° -', language.lstrip(), '- Remove left whitespace')
print('\n\t4° -', language.strip(), '- Remove both whitespace')
print('\n\t5° -', language, '- The Strings (rstrip, lstrip and strip) only revolves from the display, to permanently remove it you must store the value with the removed character back in the variable')
language = language.strip()
print('\n\t6° -', language, '- Now whitespace has been permanently removed in the variable')
