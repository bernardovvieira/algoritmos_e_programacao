# Média Semestral

# Funções
def ler_nota(n):
    while (n < 0 or n > 10):
        print('A nota informada não é válida, tente novamente.')
        n = float(input('Informe a nota novamente: '))
    else:
        return n

def mediasemestral(nota1, nota2, nota3):
    media = ((nota1 * 3.0) + (nota2 * 4.0) + (nota3 * 3.0)) / 10
    return media

def resultado(media):
    if (media < 3):
        res = f"Aluno reprovado, média final {media:.1f}."
    elif (3 <= media < 7):
        rec = 7 - media
        res = f"Aluno em exame, média final {media:.1f}. Necessário tirar {rec:.1f} para passar."
    elif (media >= 7):
        res = f"Aluno aprovado, média final {media:.1f}."
    return res     

# Programa
n1 = ler_nota(float(input('Informe a primeira nota: ')))
n2 = ler_nota(float(input('Informe a segunda nota: ')))
n3 = ler_nota(float(input('Informe a terceira nota: ')))

print(resultado(mediasemestral(n1, n2, n3)))
