# Bernardo Vivian Vieira (179835)

# Programa
print('----- CIDADES -----')

cont = 0

while True:
    n_cidade = input('Informe uma cidade: ')
    
    if (n_cidade != 'FIM'):
        if (len(n_cidade) > cont):
            maior = n_cidade
            cont = len(n_cidade)
    else:
        break

print(f'A cidade com nome mais extenso é {maior}, com {len(maior)} caracteres.')