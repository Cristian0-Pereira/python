r = 1
sexo = 1
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe seu Sexo [M/F]: ')).strip().upper()
    if sexo not in 'MF':
        print('Dados inválidos. ',end='')
    if sexo == 'M':
        r = 'Masculino'
    if sexo == 'F':
        r = 'Feminino'
print(f'Sexo {r} registrado com sucesso.')
