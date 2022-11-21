v = float(input())
l = []
v = v * 2

for i in range(100):
    l.append(v)    
    print(f'N[{i}] = {v/2:.4f}')
    v = v/2
