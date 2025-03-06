# Crie um programa que converta uma temperatura digitada em c° e converta para °F

c = float(input("Temperatura em C°: ")) 
f = c * 1.8 + 32
print('O valor de Celsius convertido para Fahrenheit é: {}°F'.format(f))