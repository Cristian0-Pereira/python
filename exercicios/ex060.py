n = int(input('Digite um número para \nCalcular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ',end='')
while c > 0:
    print(c, end='')
    print(f' x ' if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print(f)
