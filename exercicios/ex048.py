"""Soma ímpares múltiplos de 3"""
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1 # contar mais 1(contador)
        soma += c # somar todos (acumulador)
print(f'A soma de todos os {cont} valores é {soma}')
