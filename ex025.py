# Escreva um programa que pergunta o salário de uma pessoa e calcula o seu aumento. Para salários superiores a 1500 calcule um aumento de 10%, para inferiores o aumento é de 15%

salario = int(input('Qual o seu salário? '))
if salario > 1500:
   aumento = salario * 0.10
   print('Você recebeu um aumento salarial de {} para {}'.format(salario, salario + aumento))
if salario <= 1500:
    aumento2 = salario * 0.15
    print('Você recebeu um aumento salarial de {} para {}'.format(salario, salario + aumento2))