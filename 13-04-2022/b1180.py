n = int(input())
v = list(map(int, input().split()))

print(f'Menor valor: {min(v)}')
print(f'Posicao: {v.index(min(v))}')