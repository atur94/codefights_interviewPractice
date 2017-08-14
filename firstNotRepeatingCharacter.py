def firstNotRepeatingCharacter(s):
    visited = set()
    repeats = set()
    deleted = set()
    for c in s:
        if c in visited:
            deleted.add(c)
            visited.remove(c)
            continue
        elif c in deleted:
            continue
        visited.add(c)
    for c in s:
        if c in visited:
            return c
    return "_"


tt = "abcdefghijklmnopqrstuvwxyziflskecznslkjfabe"
print(firstNotRepeatingCharacter(tt))