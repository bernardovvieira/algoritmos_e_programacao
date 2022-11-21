# Bernardo Vivian Vieira (179835)

# Programa
print('----- STRINGS -----')

str1 = input('1ª string: ')
str2 = input('2ª string: ')

if str2 in str1:
    print(f'{str2} encontrado na posição {str1.rfind(str2)} de {str1}')
else:
    print(f'{str2} não encontrado em {str1}')