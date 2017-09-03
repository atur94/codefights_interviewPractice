def matrixElementsSum(matrix):
    sum = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if matrix[j][i] == 0:
                break
            sum = sum + matrix[j][i]
    return sum

mat   = [[0, 1, 1, 2],
         [0, 5, 0, 0],
         [2, 0, 3, 3]]
matrixElementsSum(mat)