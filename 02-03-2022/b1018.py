v  = int(input())

print(f'{v}')

qtd = v // 100
v = v % 100
print(f'{qtd} nota(s) de R$ 100,00')

qtd = v // 50
v = v % 50
print(f'{qtd} nota(s) de R$ 50,00')

qtd = v // 20
v = v % 20
print(f'{qtd} nota(s) de R$ 20,00')

qtd = v // 10
v = v % 10
print(f'{qtd} nota(s) de R$ 10,00')

qtd = v // 5
v = v % 5
print(f'{qtd} nota(s) de R$ 5,00')

qtd = v // 2
v = v % 2
print(f'{qtd} nota(s) de R$ 2,00')

qtd = v // 1
v = v % 1
print(f'{qtd} nota(s) de R$ 1,00')