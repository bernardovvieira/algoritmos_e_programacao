# Bernardo Vivian Vieira (179835)

# Programa
print('----- MÉDIA -----')

numeros = []
soma = 0

while True:
    valor = float(input('Informe um valor: '))
    if (valor != 0):
        numeros.append(valor)
    else:
        break
    
for i in range(len(numeros)):
    soma += numeros[i] 

calc = soma / len(numeros)
print(f'Média: {calc:.2f}')

print('Maiores que a média:')
for i in range(len(numeros)):
    if (numeros[i] > calc):
        print(numeros[i])

