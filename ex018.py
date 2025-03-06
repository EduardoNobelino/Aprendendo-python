# Crie um programa que leia o nome completo de uma pessoa e mostre: Com todas as letras maiúsculas, minúsculas, quantas letras ao todo(Sem considerar espaços)

nc = input('Seu nome completo: ')
print('seu nome em maiúsculas {}, em minúsculas {} e quantas letras {}'.format(nc.upper(), nc.lower(), len(nc.replace(" ", ""))))