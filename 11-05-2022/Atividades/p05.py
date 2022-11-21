# Triângulos

# Funções
def testatriangulo(a, b, c):
    if ((a <= 0) or (b <= 0) or (c <= 0)):
        res = 'Não é possível formar um triângulo com valores nulos ou negativos.'
    else:
        if ((a >= b + c) or (b > c + a) or (c > a + b)):
            res = 'Não é possível formar um triângulo com os valores informados.'
        else:
            if ((a == b) and (b == c)):
                res = 'Triângulo equilátero (todos os valores são iguais).'
            elif ((a == b) or (b == c) or (c == a)):
                res = 'Triângulo isóceles (dois valores iguais).'
            else:
                res = 'Triângulo escaleno (nenhum valor igual).'
    return res

# Programa
print('----- TRIÂNGULOS -----')
v1 = int(input('Informe o valor de A: '))
v2 = int(input('Informe o valor de B: '))
v3 = int(input('Informe o valor de C: '))

print(testatriangulo(v1, v2, v3))