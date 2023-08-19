resp = 'S'
media = soma = qtd = maior = menor = 0
while resp in 'S':
    n = int(input('Digite um número: '))
    soma += n
    qtd += 1
    if qtd == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
if resp in 'N':
    media = soma / qtd
    print(f'Você digitou {qtd} números e a média foi {media:.2f}')
    print(f'O maior valor foi {maior} e o menor foi {menor}')
else:
    print('Opção Inválida. Tente Novamente.')
