# Bernardo Vivian Vieira (179835)

# Funções
def substix2(numeros):
    for i in range (len(numeros)):
        if (numeros[i] % 2 != 0):
            numeros[i] += numeros[i]
    return numeros

# Programa
print('----- SUBSTITUINDO -----')
print('Digite 0 para encerrar o programa')

numeros = []

while True:
    valor = int(input('Informe um valor: '))
    if (valor != 0):
        numeros.append(valor)
    else:
        break

n_numeros = substix2(numeros)
for i in range(len(n_numeros)):
    print(n_numeros[i])
    
    

