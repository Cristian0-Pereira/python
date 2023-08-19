dias = int(input('Quantos dias de aluguel?-> '))
km = float(input('Quantos km rodados?-> '))
total = (dias * 60) + (km * 0.15)
print(f'Valor Total a pagar é R$ {total:.2f} reais')
