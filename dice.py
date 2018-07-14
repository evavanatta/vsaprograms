import random
player1 = 0
player2 = 0
odd = [1, 3, 5]
even = [2, 4, 6]
counter = 0
roll = raw_input("say how many times you would like to roll dice: ")
while 0 != 1:
    if counter <= roll:
        for item in range(int(roll)):
            dice = random.randint(1, 6)
            if dice in odd:
                player1 = player1 + 1
                counter = counter + 1
            elif dice in even:
                player2 = player2 + 1
                counter = counter + 1
    elif counter > roll:
        print "player 1 = ", player1
        print "player 2 = ", player2
        break

