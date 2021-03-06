# proj11: Recursion Programming Lab

# Name: eva vanatta
# Date: july 24th

# Tests are created for you in proj11_test.py. Uncomment tests as you need them.
# Otherwise, you could call a function that you haven't defined yet, and you would get an error.

# sumList(lst);
# Task: compute the sum of a list of integers
# Pre: lst is an list of 'size' integers, size is non negative
# Post: the sum of lst[0]...lst[size-1] is returned
# Challenge: This function could be done by dividing the list in half and performing recursive calls on each half (as opposed to just shrinking the size by one each time).
def sumList(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sumList(lst[1:])


# member(target, set);
# Task: determine if target is in the set
# Pre: set is an list of 'size' integers, size is non negative
# Post: true is returned if target is in the set, else false; the set is unchanged
def member(target, set):
    if len(set) == 0:
        return False
    elif set[0] == target:
        return True
    else:
        set = set[1:]
        return member(target, set)

# addStar(str);
# Given a string, compute recursively a new string where all the adjacent characters are now separated by a "*".
# Pre: str is a string (may be empty).
# Post: a correctly starred string is returned.
# Examples:
# addStar("hello") --> "h*e*l*l*o"
# addStar("abc") --> "a*b*c"
# addStar("ab") --> "a*b"


def addStar(string):
    if len(string) == 0:
        return string
    if len(string) == 1:
        return string
    if len(string) == 2:
        return string[0] + "*" + string[1]
    else:
        return string[0] + "*" + addStar(string[1:])

# harmonicSum(n);
# Task: compute the sum of the first n harmonic terms
# Pre: n is a positive integer
# Post: the sum of the first n harmonic terms is returned.
# The harmonic series is 1 + (1/2) + (1/3) + (1/4) + ...
def harmonicSum(n):
    if n == 0:
        return 0
    if n == 1.0:
        return 1.0
    else:
        return 1.0/float(n) + harmonicSum(n-1)


# isPalindrome(str);
# Task: determine if a string is a palindrome
# Pre: str is a string object
# Post: returns true if str is a palindrome, otherwise returns false
# The test is case insensitive (user .upper() & .lower()).
# You do not need to worry about trimming blanks from the ends of the string.
# Note: the empty string is a palindrome
def isPalindrome(str):
    str = str.replace(" " , "")
    str = str.lower()
    if len(str) <= 1:
        return True
    elif str.lower()[0] != str[-1]:
        return False
    else:
        return isPalindrome(str[1:-1])


# replace(target, replacement, numbers, size);
# Task: replace all occurrences of 'target' in the list 'numbers'with 'replacement'
# Pre: 'numbers' is a list of 'size' integers, size is non negative
# Post: all occurrences of 'target' in 'numbers' have been replaced  with 'replacement';
# the number of replacements performed is returned to the caller.
def replace(target, replacement, numbers, size):
    if numbers[0] == target:
        numbers.remove(target)
        numbers.append(replacement)
    else:
        numbers = numbers[1:]
        return replace(target, replacement, numbers, size)


# g_c_d(x, y);
# Task: compute the Greatest Common Divisor (GCD) of two non negative integers using
# Euclid's formula:
# Euclid's method for computing the greatest common divisor (GCD) of two non negative
# integers a and b is as follows. Divide a and b to obtain the integer quotient q
# and remainder r, so that a = bq+r (if b = 0, then GCD(a, b) = a).
# Then GCD(a, b) = GCD(b, r). Replace a with b and b with r and repeat the procedure.
# Because the remainders are decreasing, eventually a remainder of 0 will result.
# The last nonzero remainder is the greatest common divisor of a and b.
# Pre: the parameters x & y are non negative
# Post: the GCD of x & y is returned
def g_c_d(x, y):



# void reverseLst(lst, first, last);
# Task: reverse the contents of lst[first]...lst[last]
# Pre: 'lst' is a list of at least 'last'+1 integers, first & last are non negative
# Post: the elements lst[first]...lst[last]have been reversed.
def reverseLst(lst, first, last):



# convert2Binary(num);
# Task: produce the binary representation of a decimal number
# A decimal number is converted to binary by repeated division by 2.
# For each division, keep track of the quotient and remainder.
# The remainder becomes the low-order bit (rightmost bit) of the binary representation.
# The higher-order bits are determined by repeating the processes with the quotient.
# The process stops when num is either zero or one.
# Pre: num is a non  negative integer
# Post: the binary representation of num is produced and returned as a string.
def convert2Binary(num):


# void printPattern (num);
# Task: Print a pseudo hourglass pattern on the screen
# Pre: num is a positive integer
# Post: the desired pattern is displayed on print
# You may use iteration to print a single line of *'s,
# but must use recursion to complete the pattern.
# Example: a call to printPattern(4) should produce the pattern below
# (excluding the beginning and ending comment):
# ****
# ***
# **
# *
# **
# ***
# ****
def printPattern(num):



# void lstInitialize(lst, value, lb, ub);
# Task: initialize all elements of the lst between indices lb and ub to the given value, including the elements at lb & ub
# Note: lb = lower bound, ub = upper bound
# Pre: lb and ub are valid indices into the list a [the actual size of the lst is unknown]
# Post: the list elements in the segment a[lb..ub] have been set to value
# Challenge: This function must be done by dividing the list segment in half and performing recursive calls on each half (as opposed to just shrinking the array bound by one each time)

# """
# Extensions:
# Here are some more to try on your own! These do not come with tests...
# How would you write tests for these functions?
# """

# binomialCoeff (n, r);
# Task: Compute the Binomial Coefficient using Pascal's Triangle.
# The Binomial Coefficient B(n, r) is the coefficient of the term x^r in the binormial expansion of (1 + x)^n.
# For example, B(4, 2) = 6 because (1+x)^4 = 1 + 4x + 6x^2 + 4x^3 + x^4.
# The Binomial Coefficient can be computed using the Pascal Triangle formula:
# B(n, r) = 1                          if r = 0 or r = n
# B(n, r) = B(n-1, r-1) + B(n-1, r)    otherwise
# Pre: r & n are non-negative, and r<=n



# count2(n);
# Task: Given a non-negative int n, compute recursively (no loops) the count of the occurrences of 2 as a digit, except that a 2 with another 2  immediately to its left counts double, so 2212 yields 4. Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) 10 removes the rightmost digit (126 / 10 is 12).
# Pre: n is non-negative
# Post: count of the occurrences of 2 is returned (with doubling as appropriate)
# Examples:
# count2(2) --> 1
# count2(212) --> 2
# count2(2212) --> 4



# countSubs(str, sub);
# Task: Given a string and a non-empty substring sub, compute recursively the number of times that sub appears in the string, without the sub  strings overlapping.
# Pre: sub is a non-empty string
# Post: the count of non-overlapping occurrences of sub in str is returned
# Examples:
# countSubs("catcowcat", "cat") --> 2
# countSubs("catcowcat", "cow") --> 1
# countSubs("catcowcat", "dog") --> 0



# moveXs(str);
# Task: Given a string, compute recursively a new string where all the lowercase 'x' chars have been moved to the end of the string.
# Pre: str is a string (possibly empty)
# Post: return a new string where all lowercase 'x' chars have been moved to the end
# Examples:
# moveXs("xxre") --> "rexx"
# moveXs("xxhixx") --> "hixxxx"
# moveXs("xhixhix") --> "hihixxx"


