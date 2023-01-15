import math

# Welcome function and choice of championship or unique game

def championship():
    print("Welcome to NIM Game! Choose:")
    print("")
    print("1 - to play an unique game")
    e = int(input("2 - to play a championship "))
    print("")
    scorePC = 0
    scorePlayer = 0

    if e != 1 and e != 2:
        print("Oops! Invalid option! Try again.")
        print("")
        print("1 - to play an unique game")
        e = int(input("2 - to play a championship "))
        print("")

    if e == 1:
        print("You chose an unique game!")
        game()

    if e == 2:
        print("You chose a championship!")
        print("")
        print("**** Game 1 ****")

        r1 = game()
        if r1 == "Player":
            scorePlayer = scorePlayer + 1
        if r1 == "Computer":
            scorePC = scorePC + 1

        print("")
        print("**** Game 2 ****")
        r2 = game()
        if r2 == "Player":
            scorePlayer = scorePlayer + 1
        if r2 == "Computer":
            scorePC = scorePC + 1

        print("")
        print("**** Game 3 ****")
        r3 = game()
        if r3 == "Player":
            scorePlayer = scorePlayer + 1
        if r3 == "Computer":
            scorePC = scorePC + 1

        print("")
        print("**** End of Championship! ****")
        print("")
        print("Points: You", scorePlayer, "X", scorePC, "Computer")


# Strategic function for the player to choose the number of pieces and the maximum amount to be taken out.
# Then, the computer decides who starts the game.

def game ():
    print ("")
    n = int(input("How many pieces in total? "))
    m = int(input("Threshold of pieces to be taken out by turn? "))
    print("")
    if n % (m+1) == 0:
        print ("You begin!")
        print("")
        while n>0:
            n1 = user_chooses_turn(m, n)
            n = n - n1
            if n > 1:
                print ("Now, there are ", n, " pieces on the board.")
                print("")
            if n == 1:
                print ("Now, there is only one piece on the board.")
                print("")
            if n == 0:
                print ("Game Over! You win!")
                return "Player"

            if n > 0:
                n2 = computer_chooses_turn(m, n)
                n= n - n2
                if n > 1:
                    print ("Now, there are ", n, " pieces on the board.")
                    print("")
                if n == 1:
                    print ("Now, there is only one piece on the board.")
                    print("")
                if n == 0:
                    print ("Game Over! The computer wins!")
                    return "Computer"


    else:
        print("The computer begins!")
        print("")
        while n>0:
            n1 = computer_chooses_turn(m, n)
            n = n - n1
            if n > 1:
                print ("Now, there are ", n, " pieces on the board.")
                print("")
            if n == 1:
                print ("Now, there is only one piece on the board.")
                print("")
            if n == 0:
                print ("Game Over! The computer wins!")
                return "Computer"

            if n>0:
                n2 = user_chooses_turn(m, n)
                n = n - n2
                if n > 1:
                    print ("Now, there are ", n, " pieces on the board.")
                    print("")
                if n == 1:
                    print ("Now, there is only one piece on the board.")
                    print("")
                if n == 0:
                    print ("Game Over! You win!")
                    return "Player"


# Computer's turn function

def computer_chooses_turn(m,n):
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
        print ("The computer took one piece out.")
    else:
        print ("The computer took ", x , "pieces out.")
    return x

# Player's turn function

def user_chooses_turn(m,n):
    a = int (input("How many pieces are you going to take out? "))

    while a > m or a > n or a <=0:
        print("")
        print("Oops! Invalid play attempt! Try again.")
        print("")
        a = int(input("How many pieces are you going to take out? "))

    if a == 1:
        print("")
        print ("You took out one piece.")
    else:
        print("")
        print ("You took out ", a , "pieces.")
    return a

championship()
