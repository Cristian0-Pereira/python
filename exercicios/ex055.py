"""Maior e menor da sequência"""
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input(f'Peso da {p}ª pessoa? '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'Maior peso é {maior} kg')
print(f'Menor peso é {menor} kg')
