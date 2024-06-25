import random #Permite gerar números aleatórios

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100) #Gera um número aleatório e armazena na variável
    tentativas = 0 #Variável que armazena o número de tentativas
    acertou = False #Veriável para verificar se o jogador acertou, por isso começa como false

    print("Bem-vindo ao jogo de adivinhação!")
    print("Estou pensando em um número entre 1 e 100.")

    while not acertou: #Enquanto o valor de acertou for false o loop continua
        while True: # Garante que o palpite do jogador seja um número válido (entre 1 e 100)
            try:
                palpite = int(input("Qual o seu palpite? ")) #Solicita um número do jogador

                if palpite < 1 or palpite > 100:
                    print("Por favor, digite um número entre 1 e 100")
                else:
                    break #Sai do loop se o número for entre 1 e 100
            except ValueError:
                print("Entrada invalida. Por favor, digite um número válido")

        tentativas += 1 #Incrementa

        if palpite == numero_secreto: 
            acertou = True
            print(f"Parabéns! Você adivinhou em {tentativas} tentativas.")
        elif palpite < numero_secreto:
            print("O número é maior.")
        elif palpite > numero_secreto:
            print("O número é menor")
    
    print("Obrigado por jogar!")

#Inicia o jogo
jogo_adivinhacao()