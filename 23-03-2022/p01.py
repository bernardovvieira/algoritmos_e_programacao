print('TABELA DE CONVERSÃO')
print('Decimal/Binário/Hexa')
print('')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
print('')

for i in range(inicio, fim):
    print(f'Decimal = {i} | Binário = {i:b} | Hexa = {i:x}')
