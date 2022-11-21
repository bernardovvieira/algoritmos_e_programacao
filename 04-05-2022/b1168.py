def leds_por_digito(d):
    leds = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)
    i = int(d)
    return leds[i]

def led_por_numero(num):
    soma = 0
    for d in num:
        soma += leds_por_digito(d)
    return soma

# Programa (main)
n = int(input())

for i in range(n):
    numero = input()
    leds = led_por_numero(numero)
    print(f'{leds} leds')