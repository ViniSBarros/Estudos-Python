import forca
import adivinhacao

print("********************************")
print("******Escolha o seu jogo!!******")
print("********************************")

print("1 - Forca\n2 - Adivinhação")
jogo = int(input())

if jogo == 1:
    forca.jogar()
elif jogo == 2:
    adivinhacao.jogar()
