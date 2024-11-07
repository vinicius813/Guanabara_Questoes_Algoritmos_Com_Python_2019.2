salario = float(input('Digite aqui o salário:R$ '))
perc_aumento = salario + (salario * 15/100)
print('O programa que mostre o salário R${:.2f} e seu novo é R${:.2f}'.format(salario, perc_aumento))