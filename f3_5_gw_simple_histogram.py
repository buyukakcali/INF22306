'''
READ ME:
Group work 3-5
06-04-2023

DESCRIPTION:
    The function simple_histogram(v) takes a list as an input and returns a sorted dictionary with contents showing the fequancy of occurance of the elements of the list.

PARAMETERS:
    - v : is a given list of integers

LIMITATIONS:
    - The list cannot contain strings
    - If the data type given to the function is a data type other than integer or float, it will throw an error.

STRUCTURES:
    - First, the list is sorted with the sorted function
    - The function starts with creating an empty dictionary in which the output will be stored
    - The for loop loops through each number add '1' each time the value appears

OUTPUT:
    - it return the sorted dictionary in which the values and its frequencies are displayed
'''

def simple_histogram(v):
    book = {}

    for i in v:
        for j in v:
            if i == j:
                book[i] = j

    for k in book:
        counter = 0
        for l in range(len(v)):
            if book[k] == v[l]:
                counter += 1
        book[k] = counter

    return book


def convert_strTolist(str1):
    lst1 = sorted(str1.split(','))

    for i in range(len(lst1)):
        if lst1[i].isdigit():
            lst1[i] = int(lst1[i])

    return lst1

if __name__ == '__main__':

    data = [9, 18, 13, 9, 6, 6, 16, 6, 17, 10, 15, 16, 13, 11, 13, 8, 20, 6, 18, 11]
    print(simple_histogram(data))

    # test_other_data_list = input("Enter some integers or floats to get the smple histogram.\n(While entering use comma please, like 2,4.6,-5 etc.):")
    # print(simple_histogram(convert_strTolist(test_other_data_list)))