maiorIdade = 0
somaIdade = 0
nomeVelho = ''
mulher20 = 0
for c in range(1,4):
    print(f'-=-{c}ª PESSOA-=-')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('M/F: ')).strip()
    somaIdade += idade
    if idade > maiorIdade and sexo in 'Mm':
        maiorIdade = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1

mediaIdade = somaIdade / 3
print(f'A média é de {mediaIdade:.1f} anos.')
print(f'O mais velho tem {maiorIdade} anos e se chama {nomeVelho}.')
print(f'Tem {mulher20} mulheres com menos de 20 anos.')
