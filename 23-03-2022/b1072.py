n = int(input())

n_in = 0
n_out = 0

for i in range(n):
    x = int(input())
    
    if (10 <= x <= 20):
        n_in += 1
    
    else:
        n_out += 1
        
print(f'{n_in} in')
print(f'{n_out} out')