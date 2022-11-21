# Bernardo Vivian Vieira (179835)

# Funções
def descricao(op):
    if (op == '+'):
        desc = 'soma'
    elif (op == '-'):
        desc = 'subtração'
    elif (op == '*'):
        desc = 'multiplicação'
    else:
        desc = 'divisão'
    return desc
        
def calcular(v1, v2, op):
    if (op == '+'):
        calc = v1 + v2
    elif (op == '-'):
        calc = v1 - v2
    elif (op == '*'):
        calc = v1 * v2
    else:
        calc = v1 / v2
    return calc
    
# Programa
print('----- CALCULADORA SIMPLES -----')

v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))

op = input('Qual operação? ')

desc = descricao(op)
res = calcular(v1, v2, op)
   
print(f'Resultado da operação {desc} entre {v1} e {v2} é {res}.')