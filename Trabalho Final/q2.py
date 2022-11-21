# Bernardo Vivian Vieira (179835)

# Programa
print('----- EMPRÉSTIMO BANCÁRIO -----')

valor = int(input('Valor do imóvel: '))
salario = int(input('Salário: '))
tempo = int(input('Anos a pagar: '))

prestacao = valor / (tempo * 12)

if (prestacao > (salario * 0.3)):
    print('Infelizmente você não pode obter o empréstimo')
else:
    print('Empréstimo aprovado.')
    print(f'Valor da prestação: R$ {prestacao:.2f}')