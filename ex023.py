# Crie um programa que leia um numero inteiro e mostra na tela se ele é par ou impar

numero = int(input('Digite um numero: '))
if numero % 2 == 1:
    print('Seu número é Impar.')
if numero % 2 == 0:
    print('Seu número é Par.')