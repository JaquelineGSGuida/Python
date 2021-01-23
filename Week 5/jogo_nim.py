import math

# funcao de boas vindas e escolha de campeonato ou partida unica

def campeonato():
    print("Bem vindo ao jogo do NIM! Escolha:")
    print("")
    print("1 - para jogar uma partida isolada")
    e = int(input("2 - para jogar um campeonato "))
    print("")
    scorePC = 0
    scoreJogador = 0

    if e != 1 and e != 2:
        print("Oops! Opção inválida! Tente de novo.")
        print("")
        print("1 - para jogar uma partida isolada")
        e = int(input("2 - para jogar um campeonato "))
        print("")

    if e == 1:
        print("Você escolheu apenas uma partida!")
        partida()

    if e == 2:
        print("Você escolheu um campeonato!")
        print("")
        print("**** Rodada 1 ****")

        r1 = partida()
        if r1 == "Jogador":
            scoreJogador = scoreJogador + 1
        if r1 == "Computador":
            scorePC = scorePC + 1

        print("")
        print("**** Rodada 2 ****")
        r2 = partida()
        if r2 == "Jogador":
            scoreJogador = scoreJogador + 1
        if r2 == "Computador":
            scorePC = scorePC + 1

        print("")
        print("**** Rodada 3 ****")
        r3 = partida()
        if r3 == "Jogador":
            scoreJogador = scoreJogador + 1
        if r3 == "Computador":
            scorePC = scorePC + 1

        print("")
        print("**** Final do campeonato! ****")
        print("")
        print("Placar: Você", scoreJogador, "X", scorePC, "Computador")


# funcao para o usuário escolher o n de pecas e o maximo a ser retirado por jogada, entao o computador decide quem começa

def partida ():
    print ("")
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print("")
    if n % (m+1) == 0:
        print ("Você começa!")
        print("")
        while n>0:
            n1 = usuario_escolhe_jogada(m, n)
            n = n - n1
            if n > 1:
                print ("Agora restam", n, "peças no tabuleiro.")
                print("")
            if n == 1:
                print ("Agora resta apenas uma peça no tabuleiro.")
                print("")
            if n == 0:
                print ("Fim do jogo! Você ganhou!")
                return "Jogador"

            if n > 0:
                n2 = computador_escolhe_jogada(m, n)
                n= n - n2
                if n > 1:
                    print ("Agora restam", n, "peças no tabuleiro.")
                    print("")
                if n == 1:
                    print ("Agora resta apenas uma peça no tabuleiro.")
                    print("")
                if n == 0:
                    print ("Fim do jogo! O computador ganhou!")
                    return "Computador"


    else:
        print("Computador começa!")
        print("")
        while n>0:
            n1 = computador_escolhe_jogada(m, n)
            n = n - n1
            if n > 1:
                print ("Agora restam",n, "peças no tabuleiro.")
                print("")
            if n == 1:
                print ("Agora resta apenas uma peça no tabuleiro.")
                print("")
            if n == 0:
                print ("Fim do jogo! O computador ganhou!")
                return "Computador"

            if n>0:
                n2 = usuario_escolhe_jogada(m, n)
                n = n - n2
                if n > 1:
                    print ("Agora restam",n, "peças no tabuleiro.")
                    print("")
                if n == 1:
                    print ("Agora resta apenas uma peça no tabuleiro.")
                    print("")
                if n == 0:
                    print ("Fim do jogo! Você ganhou!")
                    return "Jogador"


# funcao em que o computador joga

def computador_escolhe_jogada(m,n):
    if n % (m+1) != 0:
        x = 0
        while n % (m+1) != 0 and x < m and n > 0:
            n = n - 1
            x = x + 1

    else:
        x = -1
        n = n + 1
        while n % (m+1) != 0 and x < m and n > 0:
            n = n - 1
            x = x + 1

    if x == 1:
        print ("O computador tirou uma peça.")
    else:
        print ("O computador tirou", x , "peças.")
    return x


# funcao em que o jogador joga

def usuario_escolhe_jogada(m,n):
    a = int (input("Quantas peças você vai tirar? "))

    while a > m or a > n or a <=0:
        print("")
        print("Oops! Jogada inválida! Tente de novo.")
        print("")
        a = int(input("Quantas peças você vai tirar? "))

    if a == 1:
        print("")
        print ("Você tirou uma peça.")
    else:
        print("")
        print ("Você tirou ", a , "peças.")
    return a

campeonato()
