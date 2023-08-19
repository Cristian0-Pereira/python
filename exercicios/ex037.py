num = int(input('Digite um numero inteiro: '))
n1 = int(input('''Escolha umas das bases de conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL
Sua opção é -> '''))
if n1 == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif n1 == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif n1 == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('OPÇÃO INVÁLIDA!')
