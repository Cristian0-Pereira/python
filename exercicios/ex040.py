n1 = float(input('Primeira nota -> '))
n2 = float(input('Segunda nota -> '))
m = (n1 + n2) / 2
print(f'Sua Média foi {m:.1f}')
if m < 5:
    print('\33[31;7;1mREPROVADO!\33[m')
elif 5 <= m < 7:
    print('\33[33;7;1mRECUPERAÇÃO!\33[m')
elif m >= 7:
    print('\33[34;7;1mAPROVADO!\33[m')
