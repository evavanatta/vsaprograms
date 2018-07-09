# Name: Eva VanAtta
# Date: July 9th, 2018

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.

#variable name
user_name = raw_input("Enter your name: ")
user_grade = raw_input("Enter your grade: ")
user_name = user_name[0].upper() + user_name[1:].lower()
print user_name + ", you will graduate from high school in", 12 - int(user_grade) , "years!"


# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday

name = raw_input("Enter your name: ")
birth_month = raw_input("Enter your birth month:(#): ")
birth_day = raw_input("Enter your birth day(#): ")
current_month = 7
current_day = 9

if int(birth_month) >= current_month:
    months_left = int(birth_month) - current_month
else:
    months_left = 12 - (current_month - int(birth_month))
if int(birth_day) >= current_day:
    print user_name + ", your birthday is in ", int(months_left), "months, and ", int(birth_day) - current_day , "days!"
else:
    print user_name + ", your birthday is in ", int(months_left) - 1, "months, and ", 30 - current_day - int(birth_day) , "days!"



# If you complete extensions, describe your extensions here!