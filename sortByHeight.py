def sortByHeight(a):
    trees = []
    rel = []
    for tree in a:
        if tree != -1:
            trees.append(tree)
    trees = sorted(trees)
    for tree in a:
        if tree != -1:
            rel.append(trees.pop(0))
            continue
        rel.append(-1)
    return rel

trees = [-1, 150, 190, 170, -1, -1, 160, 180]
print(sortByHeight(trees))