# Bhaskara

# Importações
import math

# Funções
def bhaskara(a, b, c):
    delta = (b ** 2) - (4 * (a) * (c))
    
    if (delta < 0):
        return False, False
    else:    
        r1 = (-(b) + math.sqrt(delta)) / (2 * a)
        r2 = (-(b) - math.sqrt(delta)) / (2 * a)
        return r1, r2

# Programa
a = int(input('Informe o valor do termo A: '))
b = int(input('Informe o valor do termo B: '))
c = int(input('Informe o valor do termo C: '))
        
print(bhaskara(a, b, c))
