# É primo?

# Funções
def isprime(n):
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

# Programa
numero = int(input('Número: '))

while numero > 1:
    print(f'{isprime(numero)}')
    numero = int(input('Número: '))
    
    