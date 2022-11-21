# Bernardo Vivian Vieira (179835)

# Programa
print('----- NEGATIVOS -----')

lista = []

for i in range(10):
    num = float(input('Insira um valor: '))
    lista.append(num)
    
n_lista = lista[::-1]
cont = 0

for i in range(10):
    if (n_lista[i] < 0):
        cont += 1
        print(f'{n_lista[i]:.1f}')

if (cont == 0):
    print('Nenhum valor negativo')
        
    
