######################################
# Creator: Alfio Raymond
# Date: 16 Feb 2023
#
# Problem Set 5 Part 4
# Rewrite the username program (#1) so that instead of asking the user for the name it is read from a file.
#
#####################################

def main():
    fname = input('Enter the file name:')

    try:
        fhand = open(fname)
        for line in fhand:
            findFirstName = (line)
            firstSlice = findFirstName[0]

            lengthOfUserInput = len(findFirstName) // 2

            secondSlice = findFirstName[lengthOfUserInput]

            length = len(findFirstName)

            thirdSlice = findFirstName[length - 1]

            finalOutput = firstSlice+secondSlice+thirdSlice
        print(line + " - " + finalOutput.lower())

    except:
        print("File cannot be opened:", fname)
        exit()


main()
