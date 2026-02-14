import random

opcoes = ["pedra","papel","tesoura"]
maquina = random.choice(opcoes)

print("Olá Jogador, Vamos brincar com o Jogo: Pedra, Papel e Tesoura")

jogador = input("Digite sua escolha para tentar me vencer: ")

jogador = jogador.lower().strip()

if (jogador == maquina):
    print(f"Vocês empatou comigo, minha escolha foi: {maquina.capitalize()}")

elif ((jogador == "pedra" and maquina == "tesoura") or (jogador == "tesoura" and maquina =="papel") or (jogador == "papel" and maquina =="pedra")):
    print(f"Você venceu, minha escolha foi: {maquina.capitalize()}")

else:
    print(f"Eu venci, minha escolha foi: {maquina.capitalize()}")