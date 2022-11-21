v = float(input())
l = []
v = v * 2

for i in range(100):
    l.append(v)    
    print('N[{}] = {:.4f}'.format(i, v/2))
    v = v/2

