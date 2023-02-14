#In class
#Conditions 1
# MPenta

factor = 9/5
offset = 32

print("Enter F or C? F to convert C to F")
scale = input()

if scale == "F" or scale == "C":
    #lets do the conversion
    print("let's go!")
    
    if scale == "F":
        #to F
        print("C to F")
        print("temp in C please")
        tempC = float(input())
        tempF = tempC * factor + offset
        print(str(tempC) + " C is " + str(tempF) + " F")
        
    else:
        #to C
        print("F to C")
        print("temp in F please")
        tempF = float(input())
        tempC = (tempF - offset)/factor
        print(str(tempF) + " F is " + str(tempC) + " C")
    
else:
    print("sorry please follow instructions you dweeb")
