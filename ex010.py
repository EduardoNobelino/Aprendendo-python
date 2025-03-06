# Crie um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-lá, sabendo que cada litro de tinta, pinta uma área de 2m²

altura = float(input('Quanto metros de altura tem a parede? '))
largura = float(input('Quantos metros de largura tem a parede? '))
area = altura * largura
tinta = area / 2
print('A quantidade de tinta necessária para pintar a parede de área {} é: {}'.format(area, tinta))