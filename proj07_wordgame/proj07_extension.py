# Name:
# Date:

# proj07 Extension

from proj07 import *
import time
from perm import *
word_list = load_words()

#
#
# Problem #6A: Computer chooses a word
#
#



def comp_choose_word(hand, word_list, difficulty):
    counter = 0
    cword = ""
    get_perms(hand, n)
    for word in word_list:
        counter = 0
        hand2 = hand.copy()
        for l in word:
            if difficulty == 1:
                if len(word) >= 5:
                    break
            elif difficulty == 2:
                if len(word) >= 6:
                    break
            if l in hand2 and hand2[l] != 0:
                hand2[l] = hand2[l] - 1
                counter = counter + 1
            else:
                break
        if counter == len(word):
            if len(word) > len(cword):
                cword = word
    if cword != "":
        return cword
    else:
        return "."
#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list, difficulty):

    tcscore = 0
    while True:
        print "Current Hand:",
        display_hand(hand)
        comword = comp_choose_word(hand, word_list, difficulty)
        print comword
        if comword == ".":
            print
            print "Total Score: " + str(tcscore) + " points."
            return tcscore
        else:
            if is_valid_word(comword, hand, word_list) == True:
                tcscore = get_word_score(comword, n) + tcscore
                update_hand(hand, comword)
                print str(comword), "earned", str(get_word_score(comword, n)), "points! Total", str(tcscore) + "."
                print
            else:
                print "Invalid Word"
                print

    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices 
        (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...    
    
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):

    while True:
        q = raw_input("New, Retry, or Exit? (n, r, e) ")
        if q == "n":
            hand = deal_hand(HAND_SIZE)
            phand = hand.copy()
            qu = raw_input("Computer or You?")
            if qu == "u":
                play_hand(phand, word_list)
            if qu == "c":
                difficulty = int(raw_input("Enter the difficulty you want(1=easy, 2=medium, 3=hard): "))
                comp_play_hand(phand, word_list, difficulty)
            else:
                print "Please input a valid command."
                print
        elif q == "r":
            phand = hand.copy()
            qu = raw_input("Computer or You?")
            if qu == "u":
                play_hand(phand, word_list)
            if qu == "c":
                difficulty = int(raw_input("Enter the difficulty you want(1=easy, 2=medium, 3=hard): "))
                comp_play_hand(phand, word_list, difficulty)
            else:
                print "Please input a valid command."
                print
        elif q == "e":
            break
        else:
            print "Please input a valid command."
            print



    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand 
        (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
        
#
# Build data structures used for entire session and play game
# #
# if __name__ == '__main__':
#     word_list = load_words()
#     play_game(word_list)

    
play_game(word_list)
