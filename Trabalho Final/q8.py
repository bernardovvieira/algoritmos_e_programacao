# Bernardo Vivian Vieira (179835)

# Bibliotecas
import math

# Funções
def esfera(raio):
    calc = (4 * math.pi * (raio ** 3)) / 3
    return calc

# Programa
print('----- VOLUME DA ESFERA -----')

r = float(input('Informe o raio: '))

print(f'Volume: {esfera(r):.2f}')