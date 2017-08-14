def rotateImage(a):
    #
    b = [list() for x in a]
    ai = 0
    for i in range(len(a) - 1, -1, -1):
        for _ in range(0, len(a[i])):
            b[ai].append(a[i].pop(0))
            ai = ai + 1
        ai = 0
    return b

image = [[1,2,3],
 [4,5,6],
 [7,8,9]]
print(rotateImage(image))