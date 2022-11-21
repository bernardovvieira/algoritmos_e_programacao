num1, num2, num3 = map(int, input().split())
values = [num1, num2, num3]

values.sort()

for value in values:
    print(value)

print()
print(num1)
print(num2)
print(num3)