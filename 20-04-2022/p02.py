n = int(input())

tabela = (6,2,5,5,4,5,6,3,7,6)

for i in range(n):
    total = 0
    valor = input()
    for v in valor:
        total += tabela[int(v)]
    print("%d leds" %int(total))