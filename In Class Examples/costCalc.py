import re

f = open('costs.txt', 'r')

pattern ='(.+) - .+\$([0-9]+\.[0-9][0-9])'

costs = {}

for line in f:
    line = line.rstrip()
    match = re.findall(pattern, line)
    t = match[0]
    mealName = t[0]
    mealCost = float(t[1])
   
    mealName = mealName.upper()
    
    if mealName not in costs:
        costs[mealName] = [mealCost]
    else:
        currentList = costs[mealName]
        currentList.append(mealCost)
        costs[mealName] = currentList
    
    
highestMeal = 0
highestCost = 0

for key in costs:
    c = sum(costs[key])
    if c > highestCost:
        highestCost = c
        highestMeal = key

print(highestMeal, highestCost)

lowMeal = 0
lowCost = 10000000000000

for key in costs:
    c = sum(costs[key])
    if c < lowCost:
        lowCost = c
        lowMeal = key

print(lowMeal, lowCost)

allcost = []
for key in costs:
    l = costs[key]
    allcost = allcost + l

print(min(allcost))
print(max(allcost))
print(sum(allcost)/len(allcost))

f.close()
