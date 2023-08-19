"""Qtos são Maior e qtos são Menor"""
from datetime import date
maior = 0
menor = 0
for pess in range(1,8):
    ano = int(input(f'Em que ano a {pess}ª pessoa nasceu? '))
    idade = date.today().year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'São {maior} pessoas maiores de idade')
print(f'São {menor} pessoas menores de idade')
