largura = float(input('Escreva a largura de uma parede: '))
altura = float(input('Escreva a altura de uma parede: '))
area = largura * altura
print('Uma parede sem estar pintada com dimensões {}x{} possui área {}m2'.format(largura, altura, area))
tinta = area / 2
print('Para pintar essa parede, será necessário {}l de tinta.'.format(tinta))