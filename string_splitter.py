def string_split(s):
    str_parts= {}
    j=0
    begin=0
    for i in range(len(s)):
        if s[i] == " " or i==(len(s)-1):
            if i==(len(s)-1):
                str_parts[j]= s[begin:i + 1]
            else:
                str_parts[j]= s[begin:i]
                begin = i+1
                j += 1
    return str_parts
    #return str_parts[0],str_parts[1],str_parts[2]

if __name__ == '__main__':
    string = input("Enter string: ")
    ss = string_split(string)
    print(type(ss[3]))



