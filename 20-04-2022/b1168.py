num = int(input())

for v in range(num):
    led = 0
    n = input()
    
    for i in range(len(n)):
        if n[i] == '1':
            led = led + 2
        if n[i] == '2':
            led = led + 5
        if n[i] == '3':
            led = led + 5
        if n[i] == '4':
            led = led + 4
        if n[i] == '5':
            led = led + 5
        if n[i] == '6':
            led = led + 6
        if n[i] == '7':
            led = led + 3
        if n[i] == '8':
            led = led + 7
        if n[i] == '9':
            led = led + 6
        if n[i] == '0':
            led = led + 6
            
    print(f'{led} leds')
        
    

