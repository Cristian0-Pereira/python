dias = int(input('Quantos dias de aluguel? '))
km = float(input('Quantos km foram rodados? KM '))
dtotal = dias * 60
kmtotal = km * 0.15
print(f'Ficou R$ {dtotal:.2f} reais pelos {dias} dias de carro alugado')
print(f'E R$ {kmtotal:.2f} reais pelos quilometros rodados')
print(f'O Total de tudo ficou em R$ {dtotal + kmtotal:.2f} reais')
print('Obrigado!')
