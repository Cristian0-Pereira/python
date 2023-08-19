from datetime import date
sexo = int(input('Qual seu sexo?    [1] Masculino     [2] Femininho\nOpção -> '))
if sexo == 1:
    ano = int(input('Em que ano você nasceu? '))
    anoAtual = date.today().year
    idade = anoAtual - ano
    print(f'Você tem {idade} anos em {anoAtual}')
    if idade == 18:
        print(f'Você deve se alistar IMEDIATAMENTE!')
    elif idade > 18:
        print(f'Seu alistamento foi em {ano + 18}!')
    elif idade < 18:
        print(f'''Faltam {18 - idade} anos para se alistar
Que será no ano de {ano + 18}!''')
elif sexo == 2:
    print('Você não precisa se alistar!')
else:
    print('Opção inválida!')
