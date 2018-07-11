# Name:
# Date:


# proj05: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

word = choose_word(wordlist)

list = []
for letter in word:
    list.append(letter)

length = int(len(list))

blank = []
guesses = 8
counter1 = 0
counter2 = 0

alpha = string.lowercase
print word

print "Welcome to Hangman! My word is", length, "letters long!"
while guesses > 0:
    print "Letters available:", alpha
    print "You have", guesses, "guesses left."
    while counter1 < length:
        blank.append("_")
        counter1 = counter1 + 1
    print blank
    user_input = raw_input("Guess a letter:")
    alpha = alpha.replace(user_input, "")
    counter2 = 0
    for item in word:

        if item == user_input:
            blank[counter2] = user_input

            print "You got it right!"
        counter2 = counter2 + 1





