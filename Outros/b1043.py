a, b, c = map(float, input().split())

if (abs(b - c) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a-b) < c < (a + b)):
    v1 = a + b + c
    print(f'Perimetro = {v1:.1f}')
else:
    v1 = (a + b) * c / 2
    print(f'Area = {v1:.1f}')

 
