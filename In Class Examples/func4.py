"""
mpenta
functions day 2

"""
def addThem(a, b):
    num = a + b
    a = a + 1
    return num


def gradeToLetter(numberGrade):
    #valid grade
    if numberGrade < .6:
        letterGrade = "F"
    elif numberGrade < .7:
        letterGrade = "D"
    elif numberGrade < .8:
        letterGrade = "C"
    elif numberGrade < .9:
        letterGrade = "B"
    else:
        letterGrade = "A"
        
    return letterGrade


def main():
    print("Enter a number from 0.0 to 1.0")
    grade = float(input())
    
    if grade > 1.0 or grade < 0.0:
        print("not a valid grade = try another time")
    else:
        letter = gradeToLetter(grade)
        print(letter)
        
    """
    x = 4
    y = 2
    num = addThem(x, y)
    print(x)
    """
    return

main()