total = []
contador = 0

while True:
    valor = int(input())
    
    if valor < 0:
        break
    
    contador += 1
    list.append(total, valor)
    
print(f'{sum(total) / contador:.2f}')
    
    
    