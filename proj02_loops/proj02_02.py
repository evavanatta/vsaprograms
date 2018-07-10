# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""
pn=0
cn=1


ran= int(raw_input("How many Fibonacci numbers do you want?"))

for fib in range(1,ran):
    print(cn)
    pn = cn-int(pn)
    cn = cn+pn


