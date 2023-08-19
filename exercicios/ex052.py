"""Números Primos"""
s = 0
num = int(input('Digite um valor: '))
if num > 1:
    for c in range(1, (num+1)):
        if num % c == 0:
            s += 1
    if s > 2:
        print(f'Nâo é primo, ele é divisível {s} vezes')
    else:
        print(f'É primo, ele é divisível apenas {s} vezes')
else:
    print('Não é primo')
