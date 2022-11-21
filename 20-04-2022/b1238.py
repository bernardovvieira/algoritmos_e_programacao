v = int(input())

for i  in range(v):
    l = input().split()
    carac1 = l[0]
    carac2 = l[1]
    contador = 0
    palavra = ""
    
    while contador < len(carac1) and contador < len(carac2):
        palavra += carac1[contador] + carac2[contador]
        contador += 1

    if contador < len(carac1):
        palavra += carac1[contador:]

    if contador < len(carac2):
        palavra += carac2[contador:]
    
    print(f'palavra')