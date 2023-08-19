km = float(input('Qual a distância a percorrer? KM -> '))
if km <= 200:
    preco = km * 0.5
else:
    preco = km * 0.45
print(f'Você pagará R$ {preco:.2f} reias por {km:.0f} quilômetros!')
print('Obrigado e Boa Viagem!')
