import re

f = open("mbox-short.txt", "r")

pattern = "^X-DSPAM-Confidence: ([0-9]+\.[0-9]+)"

nums=[]
for line in f:
    line = line.rstrip()
    match = re.findall(pattern, line)
    if len(match) > 0:
        numberasstring = match[0]
        num = float(numberasstring)
        nums.append(num)
   
print(nums)
print(max(nums))
print(min(nums))
l = len(nums)
s = sum(nums)
avg = s/l
print(avg)
percent = int(avg * 100)
print(percent, "%")

import re

f = open("mbox-short.txt", "r")

print("enter an expression")
pattern = input()

count = 0
matchlines = []
for line in f:
    line = line.rstrip()
    match = re.findall(pattern, line)
    if len(match) > 0:
       count = count + 1
       matchlines.append(line)

print("pattern match ", count)
print(matchlines)
