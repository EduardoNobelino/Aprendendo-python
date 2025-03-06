# Crie um programa que leia um angulo qualquer e mostre na tela seu seno, cosseno e tangente desse angulo
import math

angulo = float(input('Digite um angulo: '))
print('O seno, cosseno e tangente do angulo {} é: {:.2f}; {:.2f}; {:.2f}'.format(angulo, math.sin(math.radians(angulo)), math.cos(math.radians(angulo)), math.tan(math.radians(angulo))))