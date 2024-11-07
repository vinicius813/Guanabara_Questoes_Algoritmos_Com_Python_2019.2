preco = float(input('Digite aqui o preço de um violão no Paraíba:R$ '))
promocao = preco * 0.05
produto_final = preco - promocao
print('O violão, que custava R${}, com o desconto de 5%, assim custará R${}'.format(preco, produto_final))