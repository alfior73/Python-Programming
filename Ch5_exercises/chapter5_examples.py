## Section 5.6.1

# computes how many digits are in the list/array
# count = 0
# for itervar in [3, 41, 12, 9, 74, 15]:
#    count = count + 1
# print('Count: ', count)


# computes total of values
# total = 0
# for itervar in [3, 41, 12, 9, 74, 15]:
#    total = total + itervar
# print('Total: ', total)


## Section 5.6.2

# Find the largest value in the list/sequence
# largest = None
# print('Before:', largest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#    if largest is None or itervar > largest : 
#        largest = itervar
#    print('Loop:', itervar, largest)
# print('Largest:', largest)

# Find the smallest value in the list/sequence
# smallest = None
# print('Before:', smallest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#    if smallest is None or itervar < smallest: smallest = itervar
#    print('Loop:', itervar, smallest)
# print('Smallest:', smallest)

# Use of the min() function
def min(values): 
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value 
    return smallest

