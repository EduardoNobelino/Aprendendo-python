# Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimeto da hipotenusa
import math

cateto_oposto = float(input("Número do cateto oposto: "))
cateto_adjacente = float(input("Número do cateto adjacente: "))
hipotenusa = math.hypot (cateto_oposto, cateto_adjacente)
print("O valor de hipotenusa é: {:.2f}".format(hipotenusa))