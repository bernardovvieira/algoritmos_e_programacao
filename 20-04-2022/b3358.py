n = int(input())

for i in range(n):
    sn = input()
    d = False
    
    p = len(sn) - 2
    
    v = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']    
    
    for l in range(p):
        if (sn[l] not in v):
            if (sn[l+1] not in v):
                if (sn[l+2] not in v):
                    d = True

    if d:
        print(f'{sn} nao eh facil')
    else:
        print(f'{sn} eh facil')
    
    
    