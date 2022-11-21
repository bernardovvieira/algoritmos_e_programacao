# Bernardo Vivian Vieira (179835)

# Programa
print('----- PARES/ÍMPARES -----')

lista_p = []
lista_i = []

for i in range(8):
    v = int(input('Informe um número inteiro: '))
       
    if (v % 2 == 0):
        lista_p.append(v)
    else:
        lista_i.append(v)

print(f'{len(lista_p)} pares:')
for i in range(len(lista_p)):
    print(lista_p[i])
    
print()

print(f'{len(lista_i)} ímpares:')
for i in range(len(lista_i)):
    print(lista_i[i])