# coding=utf-8
# Name: eva vanatta
# Date: july 11th 2018


#index - starts with 0 in an index

# slice of list
    # print var[0:3]
# all but first
    # print var [1:]
# all but the last
    # print var [:-1]
# replace
    #var[0] = "tree"
# loop
    # for var in list:
    # print item
# to change
    # counter = 0
    # for item in var:
        # if item == "cat"
            # var2[counter] = "dog"
        # counter = counter + 1
# var.append(28)
    # lst = []
    # for letter in list:
     # lst.append(letter)


"""
proj04

practice with lists

"""

#Part I
#Take a list, say for example this one:


# user_input = raw_input("Enter a number: ")
# list = []
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# for item in a:
#     if item < int(user_input):
#         list.append(item)
# print list





#Part II
# Take two lists, say for example these two:
# from typing import List

# b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# d = []
# and write a program that creates and prints a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

# for item in c:
#    if item == item in b:
#        d.append(item)
# print d

# extension

# import random
# number = random.randint(0,10)
# list = []
# list2 = []
#
# for item in range(0,10):
#     number = random.randint(0,10)
#     list.append(number)
# for item in range(0,10):
#     number = random.randint(0,10)
#     list2.append(number)
# print list
#
# print list2
#
# list3 = []
#
# for item in list:
#     if item == item in list2:
#         list3.append(item)
# print "these are the numbers in common within the 2 lists: "
# print list3




#Part III
# Take a list, say for example this one:

# variables = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]
# # and write a program that replaces all “a” with “*”.
#
# counter = 0
# for item in variables:
#     if item == "a":
#         variables[counter] = "*"
#     counter = counter + 1
# print variables




# Part IV
# Ask the user for a string, and print out whether this string is a palindrome or not.

# list = []
#  user_input = raw_input("Enter a word: ")
#  user_input = user_input[0:].lower()
#
#  for letter in user_input:
#      list.append(letter)
#
#   for i in range((len(user_input))/2):
#     if list[0] == list[-1]:
#         list = list[1:-1]
#         print user_input, "is a palindrome"
#      else:
#          print user_input, "is not a palindrome"

import random
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]

number = random.randint(1, 52)
shuffledeck = []
for number in list:
    if number != shuffledeck:
        shuffledeck.append(number)
        list.remove(number)
print shuffledeck


