'''
READ ME
Group work 4-5: Adding matrix values

Description:
    add_matrices is a function that takes the entries from two seperate matrices of equal dimensions (matrixA and matrixB)
    and displays the sum of each individual cell as a new matrix termed MatrixC

Parameters:
    MatrixA, MatrixB: list of lists containing values defined as tuples

Limitations:
    Matrix lengths have to be identical for the code to work otherwise it returns an ERROR message
    The function only accepts numbers, not characters

Structures:
    An 'if' loop containing two 'for' loops to compare the lengths of both MatrixA and MatrixB, sum up the given values
        and to append the output
    A 'for' loop to print the rows of MatrixC individually

Output:
    MatrixC: list of lists displaying the sum of the values defined in MatrixA and MatrixB

'''
mA = [[35.5, 12, 6], [-32, 5, -26], [10,8, -1]]
mB = [[-31, 29, 34], [12, 11.98, -25], [28, 21, -42]]

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
    # Check if amount of rows are identical, followed by columns
    if matr_len_compare(matrixA, matrixB):  # It checks all matrices
        matrixC = []
        for i in range(len(matrixA)):
            row = []
            for j in range(len(matrixA[i])):
                row.append(matrixA[i][j] + matrixB[i][j])
            matrixC.append(row)

        # Print matrixC in three seperate rows
        for row in matrixC:
            print(row)

    # If matrices have different lengths
    else:
        print("Error, matrices have different dimensions!")

# Call the function
add_matrices(mA, mB)