outputfile = open("myoutput.txt", "w")

myString = "Hello World"
count = -1
limit = -1* (len(myString))

while count >= limit:
    
    outputfile.write("letter " + myString[count]+", ")
    outputfile.write("count " + str(count)+ "\n")
    
    count = count - 1

outputfile.close()
"""
count = len(myString)

print("len", len(myString))
print("count", count)

while count >= 0:
    print("letter", myString[count])
    print("count", count)
    count = count - 1
"""
