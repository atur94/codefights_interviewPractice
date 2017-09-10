def sortByHeight(a):
    indexes = []
    sortedOut = []
    returned = []
    for i in range(0, len(a)):
        if a[i] == -1:
            indexes.append(i)
        else:
            sortedOut.append(a[i])
    sortedOut = sorted(sortedOut)
    for i in range(0, len(sortedOut)):
        j = 0
        if indexes[j] == i:
            returned.append(-1)
            j += 1
        returned.append(sortedOut[i])
    return sorted(a)
toSort = [-1, 150, 190, 170, -1, -1, 160, 180]
print(sortByHeight(toSort))