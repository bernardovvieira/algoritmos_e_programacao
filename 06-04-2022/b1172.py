v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(v)):
    v[i] = int(input())
    
    if v[i] <= 0:
        v[i] = 1
        
    print('X[{}] = {}'.format(i, v[i]))