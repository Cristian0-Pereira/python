pTermo = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
cont = 1
while cont <= 10:
    print(pTermo,end=' → ')
    pTermo += razao
    cont += 1
print('Fim')
