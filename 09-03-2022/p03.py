# Calculadora de IMC

print('-' * 15, 'ÍNDICE DE MASSA CORPORAL (IMC)', '-' * 15); print('')

peso = float(input('Informe seu peso (Kg): '))
altura = float(input('Informe sua altura (m): '))
print('')

imc = peso / (altura ** 2)

if (imc < 18.5):
    print(f'Seu IMC é de: {imc:.2f}. Classificação: ABAIXO DO PESO.')
elif (18.5 <= imc < 25):
    print(f'Seu IMC é de: {imc:.2f}. Classificação: PESO NORMAL.')
elif (25 <= imc < 30):
    print(f'Seu IMC é de: {imc:.2f}. Classificação: EXCESSO DE PESO.')
elif (30 <= imc < 35):
    print(f'Seu IMC é de: {imc:.2f}. Classificação: OBESIDADE I.')
elif (35 <= imc < 40):
    print(f'Seu IMC é de: {imc:.2f}. Classificação: OBESIDADE II.')
else:
    print(f'Seu IMC é de: {imc:.2f}. Classificação: OBESIDADE III.')

print(''); print('-' * 62)