salario = float(input())

if (salario <= 400):
    n_salario = salario + (salario * 0.15)
    reajuste = n_salario - salario
    print(f'Novo salario: {n_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 15 %')
    
elif (400.01 <= salario <= 800):
    n_salario = salario + (salario * 0.12)
    reajuste = n_salario - salario
    print(f'Novo salario: {n_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 12 %')
    
elif (800.01 <= salario <= 1200):
    n_salario = salario + (salario * 0.10)
    reajuste = n_salario - salario
    print(f'Novo salario: {n_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 10 %')
    
elif (1200.01 <= salario <= 2000):
    n_salario = salario + (salario * 0.07)
    reajuste = n_salario - salario
    print(f'Novo salario: {n_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 7 %')
    
elif (salario >= 2000.01):
    n_salario = salario + (salario * 0.04)
    reajuste = n_salario - salario
    print(f'Novo salario: {n_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 4 %')