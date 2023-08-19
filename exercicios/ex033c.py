n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
# MENOR NÚMERO
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# MAIOR NÚMERO
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'\33[4;34mMenor\33[m número é \33[33m{menor}\33[m')
print(f'\33[4;34mMaior\33[m número é \33[31m{maior}\33[m')
