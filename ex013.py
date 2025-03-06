# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Km pecorridos com o carro alugado: '))
dias = int(input('Dias com o carro alugado: '))
total = (60 * dias) + (0.15 * km)

print('O valor total do aluguel é: {}'.format(total))