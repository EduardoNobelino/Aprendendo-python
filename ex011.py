# Faça um algoritmo que leia um preço de um produto e mostre seu novo preço, com 5% de desconto

produto = float(input('Valor do produto: '))
print('O novo preço do produto com desconto é: {}'.format(produto - (produto * 5/100)))