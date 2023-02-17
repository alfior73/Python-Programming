######################################
# Creator: Alfio Raymond
# Date: 16 Feb 2023
#
# Problem Set 5 Part 6
# Rerwite program #5 so that the username results are also sent to an output file
#
#####################################

def main():
    printToFile = ' '
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
            if printToFile == ' ':
                printToFile = line.rstrip() + " - " + finalOutput.lower() + "\n"
            else:
                printToFile = printToFile + line.rstrip() + " - " + finalOutput.lower() + "\n"

            fout = open('output.txt', 'w')
            fout.write(printToFile)
            fout.close()

        print("Data written to file")
    except:
        print("File cannot be opened:", fname)
        exit()


main()
