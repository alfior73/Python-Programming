######################################
# Creator: Alfio Raymond
# Date: 22 Jan 2023
#
# Exercise 3 in Chapter 3
# Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error message.
# If the score is between 0.0 and 1.0, print a grade using
# the following table:
# Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
# <0.6       F
#####################################

grade = input("Enter a score between 0.0 and 1.0: ")

try:
    grade = float(grade)
    
    if grade >= 0.9 and grade <= 0.9999999:
        print("A")
    elif grade >= 0.8 and grade <= 0.8999999:
        print("B")
    elif grade >= 0.7 and grade <= 0.7999999:
        print("C")
    elif grade >= 0.6 and grade <= 0.6999999:
        print("D")
    elif grade < 0.6:
        print("F")
    else:
        print("Bad Score")    
except:
    print("Bad Score ")
