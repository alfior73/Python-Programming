######################################
# Creator: Alfio Raymond
# Date: 7 Feb 2023
#
# Exercise 5 in Chapter 6
# Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string 
# after the colon character and then use the float function to convert 
# the extracted string into a floating point number.
# N/A
######################################

    
def main():
    strData = 'X-DSPAM-Confidence:0.8475 '
    
    startPos = strData.find(':')
    endPos = strData.find(' ',startPos)
    floatNumber = float(strData[startPos+1:endPos])
    
    print(floatNumber, type(floatNumber))
    
            
main()