v1 = int(input())
v2 = list(map(int, input().split()))
queda = 0 

for i in range(1, v1):
    if (v2[i] < v2[i-1]):
        queda = i + 1
        break

print(f'{queda}')