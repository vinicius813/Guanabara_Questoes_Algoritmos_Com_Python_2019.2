import random
nome_1 = str(input('Primeiro aluno: '))
nome_2 = str(input('SEgundo aluno: '))
nome_3 = str(input('Terceiro nome: '))
nome_4 = str(input('Quarto nome: '))
lista = [nome_1, nome_2, nome_3, nome_4]
random.shuffle(lista)
print('A ordem de apresentação será ')
print(lista)