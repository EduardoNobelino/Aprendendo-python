# chute e acerte o número aleatório

import random
valor_aleatorio = random.randint(1,10)
acertou = False


while acertou == False:
    chute = int(input("chute:"))
    if chute > valor_aleatorio:
        print("Chute é maior que valor gerado")
    if chute < valor_aleatorio:
        print("Chute é menor que valor gerado")
    if chute == valor_aleatorio:
        print("Acertou o chute!")
        acertou = True
    else:
        print("Você chutou um valor inválido!")