def get_vector():               # Function for getting vectors
    result = []                 # This list will contain integer data for return. I have to initialize it as a list. So it should be obvious. Because below I will use it when adding members easily
    list1 = input().split(',')  # This list contains string data. With split function, input string will be converted to a string list. We needn't to convert it to list again.
    for i in list1:
        result += [int(i)]      # Converting every string value to integer and adding them to a new list variable
    return result


def inprod(v1, v2):
    total = 0
    if len(v1) != len(v2):
        total = 'Error! Length of vectors are not same. Impossible calculation'
    else:
        for i in range(len(v1)):
            total += v1[i] * v2[i]
    return total


if __name__ == '__main__':  # I use this structure for testing and improving my code.

    print("Enter the first vector values (Use comma between the values please): ")
    vector1 = get_vector()
    print("Enter the second vector values (Use comma between the values please) : ")
    vector2 = get_vector()

    print("Outcome: ", inprod(vector1, vector2))

#    I used these examples at the beginning of coding this application
#    vec1 = [2, -7, 4, 9]
#    vec2 = [-5, 0, -4, -2]
#    print(inprod(vec1,vec2))
