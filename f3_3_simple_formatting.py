
def string_to_right(argument, length):
    str1 = ''
    result_str = ''

    type1 = type(argument)

    if type1 == str:
        str1 = argument
    elif type1 == int or type1 == float:
        str1 = str(argument)
    elif type1 == list:
        for i in argument:
            str1 += str(i)
    else:
        str1 = 'Error: Unsupported type of your input!'
    if len(str1) < int(length): # Add space/s before the original string
        result_str += (length - len(str1)) * ' ' + str1
 #   elif len(str1) > int(length): # Truncate and add '#' as the last member
 #      for _ in range(length-1):
 #           result_str += str1[_]
 #      result_str += '#'

 #   elif len(str1) > int(length):   # Truncate and add '#' as the first member
  #      result_str='#'
   #     for _ in range(length-1):
    #        result_str += str1[_+1]

    elif len(str1) > int(length):   # Truncate and add '#' as the first member
        result_str = '#'
        str2 = list(len(str1) * '#')
        for _ in range(length-1):
            str2[len(str1)-length+1+_] = str1[len(str1)-length+1+_]
        str2 = str2[len(str1)-length+1:]
        for i in str2:
            result_str += i
    else:
        result_str = str1

    return result_str

if __name__ == '__main__':

#    print("No truncate test for integer:",string_to_right(123, 5))
#    print("No truncate test for string:", string_to_right('worrying', 9))
#    print("No truncate test for list:", string_to_right([1, 2, 3], 5))

    print(string_to_right(22221222, 5))