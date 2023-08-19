from datetime import date
ano = int(input('Em que ano você nasceu? '))
anoAtual = date.today().year
idade = anoAtual - ano
print(f'Você tem {idade} anos.')
if idade <= 9:
    print('Categoria MIRIM')
elif 9 < idade <= 14:
    # ou idade <= 14:
    print('Categoria INFANTIL')
elif 14 < idade <= 19:
    # ou idade <= 19:
    print('Categoria JUNIOR')
elif 19 < idade <= 25:
    # ou idade <= 25:
    print('Categoria SENIOR')
elif idade > 25:
    # ou else:
    print('Categoria MASTER')
