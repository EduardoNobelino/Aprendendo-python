# leia um ano e diga se ele é bissexto ou não

ano = int(input('Diga um Ano qualquer: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é bissexto'.format(ano))
else:
    print('o ano {} não é bissexto'.format(ano))