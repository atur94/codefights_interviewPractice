def almostIncreasingSequence(seq):
    tests_left = True
    count = 0
    for i in range(0, len(seq)-1):
        print(i)
        if seq[i] >= seq[i+1]:
            count = count + 1
            print(seq[i], seq[i+1], i)
            if tests_left:
                if seq[i + 1] <= seq[i - 1] and i>0:
                    print("1 in: ", seq[i+1], seq[i-1])
                    if i < (len(seq) - 2):
                        if seq[i+2] <= seq[i]:
                            print("2 in: ", seq[i + 2], seq[i])
                            return False

                tests_left = False
            else:
                return False
    return count <= 1

sequence = [1, 2, 2, 3]
print(almostIncreasingSequence(sequence))

