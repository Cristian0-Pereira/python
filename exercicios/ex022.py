nome = str(input('Qual seu nome Completo: '))
print(nome.upper())
print(nome.lower())
dividido = nome.split()
unido = ''.join(dividido)
print(f'Seu nome completo tem {len(unido)} letras')
print(f'Seu primeiro nome é {dividido[0]} e tem {len(dividido[0])} letras')
