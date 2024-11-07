dias = int(input('Informe para mim os dias alugados: '))
km = float(input('Informe para mim a quilometragem do veículo: '))
pagamento = (dias * 60) + (km * 0.15)
print('O total a pagar será R${:.2f}'.format(pagamento))