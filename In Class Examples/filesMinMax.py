myFile = open("numbers.dat", "r")
total = 0
smallest = -1
largest = -1
numberString = myFile.readline()
firstNumber = int(numberString.strip())
print(f"reading first line {numberString}")
largest = firstNumber
smallest = firstNumber
total = firstNumber
for line in myFile:
    print(f"reading {line}")
    num = int(line.strip())
    total = total + num
    
    largest = max(largest, num)
    smallest = min(smallest, num)
myFile.close()
print("min", smallest)
print("max", largest)
print("tatol", total)
