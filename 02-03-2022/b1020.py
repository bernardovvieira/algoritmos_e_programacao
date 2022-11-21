v = int(input())

ano = v // 365
mes = (v - (ano * 365)) // 30
dia = (v - (ano * 365)) - (mes * 30)

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')

