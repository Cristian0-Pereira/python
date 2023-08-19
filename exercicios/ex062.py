pTermo = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(pTermo, end=' → ')
        pTermo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
