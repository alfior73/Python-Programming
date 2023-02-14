import re

f = open("mbox-short.txt")

pattern='^X\S*: ([0-9.]+)'

allnums = []

for line in f:
    line = line.rstrip()
    result = re.findall(pattern, line)
    if len(result) > 0:
        for match in result:
            allnums.append(float(match))


print(allnums)
print(sum(allnums))
print(max(allnums))
