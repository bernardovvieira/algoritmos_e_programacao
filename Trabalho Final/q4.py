# Bernardo Vivian Vieira (179835)

# Programa
print('----- TABUADA -----')

num = int(input('Tabuada de: '))
ini = int(input('De: '))
fim = int(input('Até: '))

for i in range(ini, fim+1):
    print(f'{num} x {i} = {num * i}')