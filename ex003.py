# faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele:

n = input('Digite algo: ')
print('O tipo primitvo é', type(n))

print('somente letras?', n.isalpha())
print('é um decimal', n.isdecimal())
print('é um numero?', n.isnumeric())
print('só tem espaços?', n.isspace())
print('é um alfanumerico?', n.isalnum())
print('é um digito?', n.isdigit())
print('está me maiusculas?', n.isupper())
print('está me minusculas?', n.islower())