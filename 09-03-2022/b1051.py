renda = int(input())

if (renda <= 2000):
    print('Isento')
    
elif (2000.1 <= renda <= 3000):
    calc = (renda - 2000) * 0.08
    print(f'R$ {calc:.2f}')
    
elif (3000.1 <= renda <= 4500):
    calc = (1000 * 0.08) + ((renda - 4500) * 0.28)
    print(f'R$ {calc:.2f}')
    
else:
    calc = (1000 * 0.08) + ((renda - 4500) * 0.28)
    print(f'R$ {calc:.2f}')