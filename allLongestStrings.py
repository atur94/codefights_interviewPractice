def allLongestStrings(inputArray):
    length = 0
    maxArray = []

    for word in inputArray:
        wordLength = len(word)
        if wordLength > length:
            length = wordLength
            del maxArray[:]
            maxArray.append(word)
        elif wordLength == length:
            maxArray.append(word)
    return maxArray


lisA = ["aba", "aa", "ad", "vcd", "aba"]

print(allLongestStrings(lisA))