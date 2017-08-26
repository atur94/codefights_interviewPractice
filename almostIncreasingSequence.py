def almostIncreasingSequence(seq):
    tests_left = True
    count = 0
    if len(set(seq)) <= len(seq) - 2:
        return False
    for i in range(1, len(seq)-1):

        if seq[i] >= seq[i+1] or (i == 1 and seq[i-1] >= seq[i]):
            count = count + 1
            if tests_left:
                if seq[i + 1] <= seq[i - 1]:
                    if i < (len(seq) - 2):
                        if seq[i+2] <= seq[i]:
                            return False
                tests_left = False
            else:
                return False
    return count <= 1

sequence = [10, 1, 2, 3, 4, 5, 6, 1]
print(almostIncreasingSequence(sequence))