import random
nome_1 = str(input('Digite para mim o primeiro aluno: '))
nome_2 = str(input('Digite para mim o segundo nome: '))
nome_3 = str(input('Digite para mim o terceiro nome: '))
nome_4 = str(input('Digite para mim o quarto nome: '))
lista = [nome_1, nome_2, nome_3, nome_4]
sorteio = random.choice(lista)
print('O nome do(da) escolhida para apagar o quadro será {}'.format(sorteio))