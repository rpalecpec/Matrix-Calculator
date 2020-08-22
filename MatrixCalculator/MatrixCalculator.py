def add(matrix1, matrix2):

    #nested for loop to add
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            sum[i][j]= matrix1[i][j] + matrix2[i][j]

    return sum

def sub(matrix1, matrix2):

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            difference[i][j]= matrix1[i][j] - matrix2[i][j]

    return difference

def transpose(matrix):
    for i in range(len(matrix)):
        newMatrix = matrix