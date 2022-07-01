def calcula_media(*args, margem):
    soma = sum(args)
    media = soma / len(args)
    return media + margem

calcula_media(10, 8, 9, margem=0.3)

def print_info(**kwargs):
    print(kwargs, type(kwargs))

print_info(nome='Valdson', sobrenome='Mota')
