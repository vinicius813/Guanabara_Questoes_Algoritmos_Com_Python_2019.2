real = float(input('Digite um valor em reais que você tem na carteira:R$ '))
dolar = real / 3.27
# Cotacao
print('O valor de R${:.2f} convertido é U${:.2f}'.format(real, dolar))