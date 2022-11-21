v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = int(input())

for i in range(len(v)):
    v[i] = c
    c = c * 2    
        
    print('N[{}] = {}'.format(i, v[i]))
