'''
Str2        Str1
--------    ------------
count("is", "Mississippi") == 2
count("an", "banana") == 2
count("ana", "banana") == 2
count("nana", "banana") == 1
count("nanan", "banana") == 0
count("aaa", "aaaaaa") == 4
'''

def count_substr(str1,str2):
    t = 0
    for i in range(len(str1)):
    #   print(str1[i:len(str2)])
    #  print(str2)
        if str1[i:len(str2)+i] == str2:
            t += 1
    return t
'''
count("an", "banana") == "bana"
count("cyc", "bicycle") == "bile"
count("iss", "Mississippi") == "Missippi"
count("eggs", "bicycle") == "bicycle"
'''
def remove_sub(str1, str2):
    for i in range(len(str1)):
        if str1[i:len(str2)+i] == str2:
            str1 = str1[0:i]+str1[i+len(str2):]
    return str1


def remove_all_sub(str1, str2):
    for i in range(len(str1)):
        asd = str1[i:len(str2) + i]
        if str1[i:len(str2) + i] == str2:
            str1 = str1[0:i] + str1[i + len(str2):]
            str1 = remove_sub(str1, str2)
    return str1

if __name__ == '__main__':
#    v = count_substr("Mississippi","is")
#    v = remove_sub("bcycle","eggs")
    v = remove_all_sub("Mississippi","iss")
    print(v)