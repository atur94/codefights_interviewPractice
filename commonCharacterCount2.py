def commonCharacterCount(s1, s2):
    commons = 0
    for letter in set(s1):
        commons += min(s1.count(letter),s2.count(letter))
    return commons
s1 = "aabcc"
s2 = "adcaa"

print(commonCharacterCount(s1,s2))