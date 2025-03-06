# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import trunc

nr = float (input("Digite um número real: "))
numero_inteiro = trunc(nr)
print("O valor digitado foi {} e a sua porção inteira é {}".format(nr, numero_inteiro))