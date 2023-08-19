while True:
    tab = int(input('Qual tabuada você quer ver?-> '))
    print('_' * 30)
    if tab < 0:
        break
    else:
        for c in range(1,11):
            print(f'{tab} x {c:2} = {tab*c:2}')
    print('_' * 30)
print('Programa TABUADA ENCERRADO! Volte Sempre!')