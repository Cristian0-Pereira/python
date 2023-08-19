altura = float(input('Qual sua altura? (M) '))
peso = float(input('Qual seu peso? (KG) '))
imc = peso / (altura ** 2)
print(f'Seu IMC é = {imc:.1f}')
if imc <= 0:
    print('-=-Você é um fantasma-=-')
elif 0 < imc < 18.5:
    print('-=-ABAIXO DO PESO-=-')
elif 18.5 <= imc < 25:
    print('-=-PESO IDEAL-=-')
elif 25 <= imc < 30:
    print('-=-SOBREPESO-=-')
elif 30 <= imc < 40:
    print('-=-OBESIDADE-=-')
elif imc >= 40:
    print('-=-OBESIDADE MÓRBIDA-=-')
