######################################
# Creator: Alfio Raymond
# Date: 16 Feb 2023
#
# Problem Set 5 Part 5
# Rewrite the previous program (#4) so that the file has a
# number of names (one per line) and the program will print
# usernames untill all names are read from the file
#
#####################################

def main():
    fname = input('Enter the file name:')

    try:
        fhand = open(fname)

        for line in fhand:

            findFirstName = (line)

            firstSlice = findFirstName[0]

            lengthOfUserInput = (len(findFirstName) // 2) - 1

            secondSlice = findFirstName[lengthOfUserInput]

            length = len(findFirstName)
            thirdSlice = findFirstName[length-2]

            finalOutput = firstSlice+secondSlice+thirdSlice
            print(line.rstrip() + " - " + finalOutput.lower())

    except:
        print("File cannot be opened:", fname)
        exit()


main()
