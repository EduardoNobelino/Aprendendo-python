# escreva um programa que leia um valor em metro e converta para centímetros e milímetros

metros = int(input('Valor em metros: '))
centímetros = metros * 100
milimetros = metros * 1000

print('O valor de metros convertido em centímetros é: {} e em milimétros é: {}'.format(centímetros, milimetros))