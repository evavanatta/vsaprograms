# Create a program that will play the 'cows and bulls' game with the user. The game works
# like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every
# digit that the user guessed correctly in the correct place, they have a 'cow'. For
# every digit the user guessed correctly in the wrong place is a 'bull.' Every time the
# user makes a guess, tell them how many 'cows' and 'bulls' they have. Once the user
# guesses the correct number, the game is over. Keep track of the number of guesses the
# user makes throughout the game and tell the user at the end.
#
# Say the number generated by the computer is 1038. An example interaction could look like
# this:
#
#   Welcome to the Cows and Bulls Game!
#   Enter a number:
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull

# Until the user guesses the number.

counter = 0
guesses = 0
cows = 0
counter1 = 1
counter2 = 2
counter3 = 3
counter4 = 4
bulls = 0

import random
number = str(random.randint(1000,9999)) #random 4 digit number
list = []
for letter in number:
    list.append(letter)
print number
user_input = raw_input("Guess a 4-digit number or type exit to leave: ")
user_list = []
for letter in user_input:
    user_list.append(letter)
while user_input:
    counter = 0
    user_input = raw_input("Guess a 4-digit number or type exit to leave: ")
    if list[counter] == user_list[counter]:
        cows = cows + 1
        counter = counter + 1
    if letter in user_list == letter in list:
        bulls = bulls + 1
        print "you have", int(cows), "cows and", int(bulls), "bulls."
    if user_list == list:
        cows = 4
        print "you have won!"


