n = 0

while n < 100:
    val = int(input())
    
    if val == 0:
        break
    elif val < 0:
        continue
    
    n += val
    
print(n)