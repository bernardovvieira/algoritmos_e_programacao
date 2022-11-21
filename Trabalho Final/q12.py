# Bernardo Vivian Vieira (179835)

# Programa
print('----- CÁLCULO -----')

lista = []
n = int(input('Informe um inteiro: '))

for i in range(n):
    valor = float(input('Informe um valor: '))
    lista.append(valor)
    
v_min = min(lista)

for i in range(len(lista)):
    if(v_min != 0):
        calc = lista[i] / v_min
        print(f'{calc:.1f}')
    else:
        print(f'{lista[i]:.1f}')
    