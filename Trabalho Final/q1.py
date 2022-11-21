# Bernardo Vivian Vieira (179835)

# Programa
print('----- AMPLITUDE TÉRMICA -----')

temp = []

for i in range(1, 13):
    v = float(input(f'Informe a temperatura {i}: '))
    temp.append(v)
    
amp = max(temp) - min(temp)
print(f'{amp:.1f}')