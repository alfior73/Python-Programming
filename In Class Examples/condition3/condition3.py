#In class
#Conditions 3
#MPenta

print("enter your age")
age = int(input())
statement = "hello"

if age <= 16:
    statement = "you cant do much"
elif age > 16 and age < 18:
    statement = "you can drive"
elif age > 17 and age < 21:
    statement = "drive, vote, gamble, and join the armed services"
elif age >= 21 and age <65:
    statement = "you can drive, vote, go to war, drink, smoke weed and cigarettes"
elif age >=65 and age < 107:
    statement = "enjoy retirement"
else:
    statement = "you can do anything you want as long as death is cool with it"

print(statement)