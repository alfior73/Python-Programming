######################################
# Creator: Alfio Raymond
# Date: 26 Jan 2023
#
# Exercise 3 in Chapter 4
# Move the function call back to the bottom and move the
# definition of print_lyrics after the definition of repeat_lyrics. # What happens when you run this program?
#
#
# N/A
######################################
    
def repeat_lyrics():
    print_lyrics()
    print_lyrics()


def print_lyrics():
    print("Why don't you go home and crawl into your hole")
    print("Why don't you go home and spend some time alone")
    
repeat_lyrics()

########################
#
# program prints lyrics because where you define the function doesn't matter
# as long as the call of the function is after it's defined
#
############################
