mercadoria = float(input('Uma bicicleta custa determinado valor: R$ '))
desconto = mercadoria - (mercadoria * 10 /100)
parcelamento = (mercadoria / 5) + (mercadoria * 8 /100)
print('O valor do produto R${:.2f} à vista(desconto) é R${:.2f} e a prazo é R${:.2f}'.format(mercadoria, desconto, parcelamento))