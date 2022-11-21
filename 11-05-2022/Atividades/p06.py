# Valores Repetidos

# Funções
def testarepetidos(vet):
    if (len(vet) != len(set(vet))):
        res = 'Há valores repetidos na lista!'
    else:
        res = 'Não há valores repetidos na lista.'
    return res

# Programa
print('----- VALORES REPETIDOS -----')
print('Digite 0 para encerrar a lista e verificar se há valores repetidos.')

valores = []
while True:
    v = input('Insira um valor: ')
    if (v != '0'):
        valores.append(v)
    else:
        break
    
print(f'{testarepetidos(valores)}')
    
