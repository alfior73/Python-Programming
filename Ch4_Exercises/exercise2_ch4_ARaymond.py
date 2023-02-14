######################################
# Creator: Alfio Raymond
# Date: 26 Jan 2023
#
# Exercise 2 in Chapter 4
# Move the last line of this program to the top, so the function
# call appears before the definitions. Run the program and see 
# what error message you get.
#
# N/A
######################################

repeat_lyrics()

def print_lyrics():
    print("Why don't you go home and crawl into your hole")
    print("Why don't you go home and spend some time alone")
    
    
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
repeat_lyrics()

########################
#
# Error Generated
#
# Traceback (most recent call last):
#  File "/NECC2023/CIS 153 Programming for IT/Chapter4 Exercises/4_6.py", line 1, in <module>
#   repeat_lyrics()
# NameError: name 'repeat_lyrics' is not defined
#
############################