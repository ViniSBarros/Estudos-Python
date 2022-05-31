import random
import forca


def jogar():
    imprime_mensagem_abertura()

    numero_secreto = random.randint(1, 101)
    pontos = 100

    total_de_tentativas = escolha_a_dificuldade()

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = informe_o_chute()

        if chute < 1 or chute > 100:
            print("Número inválido")
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos".format(pontos))
            forca.imprime_mensagem_vencedor()
            break
        else:
            if maior:
                print("Você errou!!!, O seu chute foi maior do que o número secreto")
            elif menor:
                print("Você errou!!!, O seu chute foi menor do que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

        if rodada == total_de_tentativas:
            print("O número secreto era:", numero_secreto)
            forca.imprime_mensagem_perdedor()


def imprime_mensagem_abertura():
    print("********************************")
    print("Bem vindo ao jogo de advinhação!")
    print("********************************")


def escolha_a_dificuldade():
    print("Escolha o nível de dificuldade: ")
    print("1 - Fácil \n2 - Médio\n3 - Difícil")

    nivel = int(input())

    if nivel == 1:
        total_de_tentativas = 10
    elif nivel == 2:
        total_de_tentativas = 7
    else:
        total_de_tentativas = 5
    return total_de_tentativas


def informe_o_chute():
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou", chute_str)
    chute = int(chute_str)
    return chute


if __name__ == "__main__":
    jogar()
