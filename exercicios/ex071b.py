print(f'{" Banco do Piu ":-^30}')
valor = int(input('Qual valor você quer sacar? R$'))
total = valor
nota = 50
totNota = 0
while True:
    if total >= nota:
        total -= nota
        totNota += 1
    else:
        if totNota > 0:
            print(f'Total de {totNota} notas de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 1
        totNota = 0
        break
print('Volte Sempre!')
