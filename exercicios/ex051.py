"""Progressão Aritmética definidos pelo usuário (Primeiro Termo e a Razão)"""
print('=' * 30)
print(f'{"10 TERMOS DE UMA PA": ^30}')
print('=' * 30)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
pa = termo + (10 - 1) * razao
for c in range(termo, pa + razao, razao):
    print(c, end='►')
print('FIM')
