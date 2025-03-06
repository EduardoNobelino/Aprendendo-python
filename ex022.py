# projeto medidor de velocidade:

velocidade_maxima = 80
velocidade_usuario = int(input('Qual a sua velocidade: '))

if velocidade_usuario <= velocidade_maxima:
    print("Não houve multa")
elif velocidade_usuario <= velocidade_maxima + 10:
    print("Levou multa leve")
elif velocidade_usuario <= velocidade_maxima + 20:
    print("Levou multa grave")
elif velocidade_usuario > velocidade_maxima + 20:
    print("Levou multa gravíssima")