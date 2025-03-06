# crie um programa que recebe um número e mostre sua tabuada 
numero = int(input('Número: '))

for n in range(1,11):
    resultado = numero * n
    print('A tabuada do número {} é: {}'.format(numero, resultado))