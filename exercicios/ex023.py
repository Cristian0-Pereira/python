num = int(input('Digite um número de 0 - 9999 -> '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print(f'O número {num}')
print(f'Unidade: {uni}\nDezena:  {dez}\nCentena: {cen}\nMilhar:  {mil}')
