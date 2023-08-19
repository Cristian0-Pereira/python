"""Detector de Palíndromo"""
frase = str(input('Digite uma frase: ')).split()
frase1 = ''.join(frase).upper()
palindromo = f'{frase1[::-1]}'
if frase1 == palindromo:
    print('Essa frase é PALÍNDROMO')
else:
    print('Não é PALÍNDROMO')
