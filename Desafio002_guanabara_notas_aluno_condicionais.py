n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi: {:.1f}'.format(m))
if m >= 6.0:
    print('Você está APROVADO, PARABÉNS!')
else:
    print('ESTUDE MAIS para passar na prova, você está REPROVADO.')