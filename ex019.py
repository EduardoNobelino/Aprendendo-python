# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

cidade = input('Nome da cidade: ').strip()
print(cidade[:5].upper() == 'Santo')