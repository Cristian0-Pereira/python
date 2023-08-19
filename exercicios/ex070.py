total = maisMil = menor = cont = 0
maisBarato = ''
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        maisMil += 1
    if cont == 1 or preco < menor:
        menor = preco
        maisBarato = produto
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maisMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {maisBarato.title()} que custa R${menor:.2f}')
print(f'{" FIM DO PROGRAMA ":-^40}')
