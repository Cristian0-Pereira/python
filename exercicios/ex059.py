from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
print('=-='*10)
opcao = 0
while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa''')
    opcao = int(input('>>> Qual sua opção-> '))
    if opcao == 1:
        print(f'A soma de {n1} + {n2} é {n1+n2}')
    elif opcao == 2:
        print(f'O resultado de {n1} x {n2} é {n1*n2}')
    elif opcao == 3:
        print(f'Entre {n1} e {n2} ',end='')
        if n1 == n2:
            print('Os valores são iguais.')
        else:
            lista = n1, n2
            print(f'O Maior é {max(lista)}')
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opcao == 0 or opcao > 5:
        print('Opção Inválida. Tente Novamente.')
    print('=-='*10)
    sleep(1)
print('Finalizando', end='')
for c in range(0,6):
    print('.', end=''),sleep(0.5)
print(f'\n{"=-="*10}'),sleep(0.5)
print('Fim do Programa! Volte Sempre!')
