vel_carro = float(input('Diga a que velocidade você está dirigindo: '))
if vel_carro > 80:
    print('MULTADO! Dirija-se a blitz mais próxima e pague o valor cobrado.')
    multa = (vel_carro - 80) * 7
    print('Você deverá pagar um valor de {:.2f}'.format(multa))
print('OBRIGADO! Dirija sempre com segurança, durma em um colchão ONIX!')
