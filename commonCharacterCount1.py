def commonCharacterCount(s1, s2):
    y = list(s2)

    letters = 0
    for letter in s1:
        for c in range(len(y)):
            if letter == y[c]:
                letters = letters + 1
                del y[c]
                break
    return letters


s1 = "aabcc"
s2 = "adcaa"

print(commonCharacterCount(s1,s2))