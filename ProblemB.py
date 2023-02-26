def identifyPattern(bString):
    pattern = [0]
    if (bString.startswith("1")):
        bStringNew = bString[1:]
        nextIndex = bStringNew.find("1")
    pattern.append(nextIndex + 2)
    return pattern

def verifyPattern(bString, pattern):
    startIndex = pattern[0]
    endIndex = pattern[1]
    startPattern = bString[startIndex: endIndex]
    endPattern = bString[-(endIndex):]
    if(len(startPattern) == len(endPattern)):
        return True
    return False

pattern = []
binaryString = input("Enter binary string S: ")
allNum = set(binaryString) <= {'0','1'}

if (allNum):
    pattern = identifyPattern(binaryString)
    if(verifyPattern(binaryString, pattern)):
        pattern = binaryString[0:pattern[1]]
        occurences = binaryString.count(pattern)
        print(occurences)
    else:
        print(0)

# example = 10011001100110011001
# example = 100111001110011100111001110011