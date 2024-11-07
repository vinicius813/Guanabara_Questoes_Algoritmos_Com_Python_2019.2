from random import randint
from time import sleep
computador = randint(0, 5) # Faça o computador jogar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS, você me pegou! Venceu o jogo de adivinha.')
else:
    print(' Eu GANHEI e o jogador PERDEU o jogo, porque {} não é igual a {}'.format(computador, jogador))