######################################
# Creator: Alfio Raymond
# Date: 22 Jan 2023
#
# Exercise 3 in Chapter 3
# Rewrite the grade program from the previous chapter using a function 
# called computegrade that takes a score as its parameter and returns a grade as a string.
#
# Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
# <0.6       F
#####################################
def computeGrade(grade):
    if grade < 0.6:
        grade = "F"
    elif grade < 0.7:
        grade = "D"
    elif grade < 0.8:
        grade = "C"
    elif grade < 0.9:
        grade = "B"
    else:
        grade = "A"
        
    return grade


def start():
    print("Enter a score between 0.0 and 1.0: ")
    try:
        grade = float(input())
    
        if grade > 0.0 and grade < 1.0:
            funcGrade = computeGrade(grade)
            print(funcGrade)
        else:
            print("Bad Score Out of Range")
    except:
        print("Bad Score")
        
start()
