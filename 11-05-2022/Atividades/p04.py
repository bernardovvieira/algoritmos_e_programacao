# Conta Múltiplos

# Funções
def contamultiplos(n1, n2, n3):
    cont = 0
    for i in range(n1, n2 + 1, n3):
        cont += 1
    return cont
    
# Programa
print('----- CONTA MÚLTIPLOS -----')
v1 = int(input('Informe o início do intervalo: '))
v2 = int(input('Informe o fim do intervalo: '))
v3 = int(input('Informe o múltiplo: '))

print(f'Há {contamultiplos(v1, v2, v3)} múltiplo(s) de {v3} no intervalo digitado.')