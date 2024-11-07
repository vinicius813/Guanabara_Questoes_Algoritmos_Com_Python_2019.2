metro = float(input('Digite um valor em metros: '))
conv_km = metro / 1000
conv_hm = metro / 100
conv_dam = metro / 10
conv_dec = metro * 10
conv_cm = metro * 100
conv_mm = metro * 1000
print('Analisando {} metros, vale {} quilômetros e {} hectômetros. \nCom isso, verificamos que vale {} decâmetros'.format(metro, conv_km, conv_hm, conv_dam))
print('As medidas, tomando como base os {} metros, \n vale-se de {} decímetros em {:.3f} centímetros e continuam em {} milímetros'.format(metro, conv_dec, conv_cm, conv_mm))