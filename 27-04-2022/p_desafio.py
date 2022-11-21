def fibonacci(v):   
    if v != 0:
        v = v
    else:
        v = 0
    
    a1 = 1
    a2  = 0
    
    for i in range(v):
        a2 += a1
        a1 = a2 - a1
    
    return a2 

v = fibonacci(int(input("Posição do número na Sequência de Fibonacci: ")))

print(f'Resultado = {v}')