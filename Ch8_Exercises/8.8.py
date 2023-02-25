nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)//len(nums))

total = 0
count = 0
while (True):
    inp = input("Enter a number: ")
    if inp == 'done':
        break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print("Average:", average)

numlist = list()
while (True):
    inp = input("Enter a number: ")
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print("Average:", average)
