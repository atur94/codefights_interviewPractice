def isLucky(n):
    ##Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum
    # of the first half of the digits is equal to the sum of the second half.
    eq1 = 0
    eq2 = 0
    string = list(str(n))
    for i in range(int(len(string)/2)):
        eq1 += int(string[i])
    for i in range(int(len(string)/2),len(string)):
        eq2 += int(string[i])
    return eq1 == eq2
testVar = 261534
#Output should be False


print(isLucky(testVar))
