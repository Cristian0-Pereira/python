produto = float(input('Qual o valor do produto? R$ '))
desconto: float = produto - (produto*5/100)
print(f'Seu produto é de R$ {produto:.2f} reais, com desconto de 5% sairá por R$ {desconto:.2f} reais')
print(f'Valor com desconto R$ {desconto:.2f} reais!')
desconto12 = desconto - (desconto*12/100)
print(f'Se você comprar outro produto, você terá um desconto de mais 12% \nE pagará apenas R$ {desconto12:.2f} reais.')
print(f'E no débito você pagará com mais um desconto de 8% \nE sairá por R$ {desconto12 - (desconto12*8/100):.2f} reais.')
print('Obrigado e Volte Sempre')