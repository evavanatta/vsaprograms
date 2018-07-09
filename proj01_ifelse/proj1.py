# Name: Eva VanAtta
# Date: July 9th, 2018

# project 1: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
# Then, it prints out a sentence that says the number of years until they graduate.

# variable names
user_name = raw_input("Enter your name: ")
user_grade = raw_input("Enter your grade: ")
user_name = user_name[0].upper() + user_name[1:].lower()
# code
years = 12 - int(user_grade)
if years == 1:
    print user_name + ", you will graduate from high school in", int(years), "year!"
if years > 1:
    print user_name + ", you will graduate from high school in", int(years), "years!"
if years == 0:
    print user_name + ", you will graduate from high school this year!"
if years < 0:
    print user_name + ", you have already graduated from high school!"


# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday

# variable names
birth_month = raw_input("Enter your birth month:(#): ")
birth_day = raw_input("Enter your birth day(#): ")
current_month = 7
current_day = 9

# conditions
if int(birth_month) >= current_month:
    months_left = int(birth_month) - current_month
else:
    months_left = 12 - (current_month - int(birth_month))
if int(birth_day) >= current_day:
    print user_name + ", your birthday is in ", int(months_left), "months, and ", int(birth_day) - current_day, "days!"
else:
    print user_name + ", your birthday is in ", int(months_left) - 1, "months, and ", 30 - current_day - int(birth_day), "days!"

# extension!!!!

# variable names
age = raw_input("Enter your age: ")

# conditions
if int(age) < 13:
    print user_name, ", you are allowed to see G & PG rated movies!"
if int(age) >= 13 and int(age) < 17:
    print user_name, ", you are allowed to see G, PG, and PG-13 rated movies!"
if int(age) >= 17:
    print user_name, ", you are allowed to see G, PG, PG-13, and R rated movies!"

money = raw_input("Enter how much money you have: ")
if money == 0:
    print "you can not buy any movie theatre snacks :'("
