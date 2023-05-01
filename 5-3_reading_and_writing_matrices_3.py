def matr_len_compare(mat1, mat2): # to compare all reciprocal list elements
    result = ""
    if len(mat1) == len(mat2):
        for i in range(len(mat1)):
            if len(mat1[i]) == len(mat2[i]):
                result = True
            else:
                result = False
                break
    return result

def add_matrices(matrixA, matrixB):
    if matr_len_compare(matrixA, matrixB):
        matrixC = []
        for i in range(len(matrixA)):
            row = []
            for j in range(len(matrixA[i])):
                row.append(matrixA[i][j] + matrixB[i][j])
            matrixC.append(row)
        for row in matrixC:
            print(row)
    else:
        print("Error, matrices have different dimensions!")

def write_matrix(lst:list):
    with open('first.matrix', 'w') as wrmtx:
        wrmtx.write(lst)

def read_matrix(filename):
    matrixX = []
    with open('first.matrix', 'r') as rmtx:
        matrixX = rmtx.read()




def write_matrix(length:int):
    lst = []
    for i in range(length):
        lst += [input('Enter the matrix values')]

    with open('first.matrix', 'w') as wrmtx:
        wrmtx.write(lst)

# Call the function
#add_matrices(mA, mB)