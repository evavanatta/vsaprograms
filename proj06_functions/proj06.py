# Name:
# Date:

# proj05: functions and lists

# Part I

#
# def divisors(num):
#     counter = 0
#     numbers = []
#     for item in range (1, num+1):
#         if num%item == 0:
#             numbers.append(item)
#             counter = counter + 1
#         else:
#             counter = counter + 1
#     return numbers
#
#
# def prime(num):
#     divise = divisors(num)
#     length = int(len(divise))
#     if length <= 2:
#        return True
#     if length > 2:
#         return False
#

"""""
Part II:
REVIEW: Conditionals, for loops, lists, and functions

INSTRUCTIONS:

1.  Make the string "sentence_string" into a list called "sentence_list" sentence_list
should be a list of each letter in the string: ['H', 'e', 'l', 'l', 'o', ',', ' ', 'm',
'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'M', 'o', 'n', 't', 'y', ' ', 'P',
'y', 't', 'h', 'o', 'n', '.']


Hint: Use a for loop and with an append function: list.append(letter)

"""

sentence_string = "Hello, my name is Monty Python."

counter = 0
sentence_list = []
for item in sentence_string:
    sentence_list.append(item)
    counter = counter + 1
print sentence_list



# # 2. Print every item of sentence_list on a separate line using a for loop, like this:
# # H
# # e
# # l
# # l
# # o
# # ,
# #
# # m
# # y
# #  .... keeps going on from here.
#
counter = 0
for item in sentence_list:
    print sentence_list[counter]
    counter = counter + 1


# 3: Write a for loop that goes through each letter in the list vowels. If the current
# letter is 'b', print out the index of the current letter (should print out the
# number 1).
#
vowels = ['a', 'b', 'i', 'o', 'u', 'y']
for item in vowels:
    if item == "b":
        index = vowels.index("b")
        print index


# 4: use the index found to change the list vowels so that the b is replaced with an e.

for item in vowels:
    if vowels[index] == "b":
        vowels[index] = "e"
print vowels

# 5: Loop through each letter in the sentence_string. For each letter, check to see if the
#  number is in the vowels list. If the letter is in the vowels list, add one to a
# counter. Print out the counter at the end of the loop. This counter should show how
# many vowels are in sentence_string.

counter2 = 0
for item in sentence_string:
    if item == item in vowels:
        counter2 = counter2 + 1
print counter2


# 6: Make a new function called "vowelFinder" that will return a list of  the vowels
# found in a list (no duplicates).The function's parameters should be "list" and "vowels."


# Example:
# vowelList = vowelFinder(sentence_list, vowels)
# print vowelList

# ['a', 'e', 'i', 'o', 'y']

def vowelFinder(sentence_list, vowels):
    vowel_list = []
    for item in vowels:
        if item == item in sentence_list:
            vowel_list.append(item)
    return vowel_list
print vowelFinder(sentence_list, vowels)
