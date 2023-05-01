

def matrix_to_file(lst):    # reading and writing matrices (1): writing to a text file

    for i in range(len(lst)):
        str1 = lst[i]
        for j in range(len(str1)):
            with open('f4_3_matrixfile.txt', 'a') as file:
                file.write(str(str1[j])+' ')
        with open('f4_3_matrixfile.txt', 'a') as file:
            file.write('\n')

def file_to_matrix(filename):   # reading and writing matrices (2): reading from a text file
    matrix_data = []
    with open(filename, 'r') as doc:
        for line in doc:
            str1 = line.split()
            for j in range(len(str1)):
                str1[j] = int(str1[j])
            matrix_data.append(str1)
        print(matrix_data)

if __name__ == '__main__':
    sample_list = [[35, 12, 6], [-32, 5, -26], [10, 8, -1]]

    matrix_to_file(sample_list)
    file_to_matrix('f4_3_matrixfile.txt')