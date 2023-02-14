######################################
# Creator: Alfio Raymond
# Date: 7 Feb 2023
#
# Exercise 6 in Chapter 6
# Read the documentation of the string methods at
# https://docs.python.org/library/stdtypes.html#string-methods 
# You might want to experiment with some of them to make sure you 
# understand how they work. strip and replace are particularly useful.
# The documentation uses a syntax that might be confusing. 
# For example, in find(sub[, start[, end]]), the brackets indicate 
# optional arguments. So sub is required, but start is optional, 
# and if you include start, then end is optional.
#
# N/A
######################################

    
def main():
    strData = 'welcome to the show'
    
    print("Original:", strData)
    print("Capitalize:", strData.capitalize())
    print("Count o's:", strData.count('o'))
    print("Swap case:", strData.swapcase())
    print("Is upper?:", strData.isupper())
    print("Is lower?:", strData.islower())
    print("Lower case:", strData.lower())
    print("Upper case:", strData.upper())
    
    
main()