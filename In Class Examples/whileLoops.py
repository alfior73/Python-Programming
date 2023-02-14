#user controlled loop
print("enter y to continue or anything else to stop")
choice = input() #1 

while choice == "y": #2

    print("lets do it again!") #the loop stuff

    print("enter y to continue or anything else to stop")
    choice = input()#3


#counting loop
count = 0  #1 initialize a control variable
limit = 10

while count <= limit: # 2 test the control variable

    print(count)  #the loop stuff
    
    count = count + 1  #3 update the control variable


#value validation
print("enter a number 1, 2, 3") #1
choice = int(input())


while choice < 1 or choice > 3:#2

    if choice <0:
        print("wow negative number you are really dumb")
    
    print("That is invalid. enter a number 1, 2, 3")#3
    choice = int(input())

print(choice)

#running total and min max
total = 0
count = 0

big = 0
little = 0

print("enter a number , enter negative quit")  #1
current_number = int(input())
big = current_number
little = current_number

while current_number >= 0:  #2

    if current_number > big:
        big = current_number

    if current_number < little:
        little = current_number
    

    count = count + 1
    total = total + current_number
    
    print("enter a number , enter negative quit")  #3
    current_number = int(input())


print("max", big)
print("min", little)

try:
    
    print(total / count)
except:
    print("bad division")
