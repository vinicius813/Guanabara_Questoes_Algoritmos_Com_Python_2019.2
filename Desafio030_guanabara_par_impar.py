numero = int(input('Escreva aqui um número: '))
resultado = numero % 2
if resultado == 0:
    print('Então, o número {} é PAR.'.format(numero))
else:
    print('Então, o número {} é ÍMPAR.'.format(numero))