media = float(input('Média semestral: '))

if (media >= 7):
    print('Aprovado.')
elif (3 <= media < 7):
    print('Exame.')
    exame = 10 - media
    print(f'Você precisa tirar {exame:.1f} para passar.')
else:
    print('Reprovado.')

