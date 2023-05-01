"""
Read Me:
Group 7 - Filtering Data

Description:
    "filter_data" function is a function that takes a file as an input, and checks each line with a pattern before writing the matching lines to a new file

Parameters:
    Input File (source_file)    : the file that is being read
    Output File (output_file)   : the file that is being written to
    Regular Expression (re_str) : the pattern that each line is being checked against
    Boolean Flag (flag)         : if True, then the line matching the pattern is copied, if False the line not matching the pattern is copied

Limitations:
    - regular expressions are not nice
    - any typo in file name leads to disaster

Structures:
    - with  : opens the file we want to read from (source file)
    - for   : checks each line
    - if    : checks if flag is condition is met
    - else  : checks if flag condition not met
    - with  : opens the output file


Output:
    - a file with the lines from the input file that match the given pattern
    - a reminder to check the output file
"""
import re  # Regular Expression framework imported


def data_filter(source_file, output_file, re_str, flag:bool):  # first two parameter: file, third one is string and we don't need last one for this example
    result = []

    with open(source_file, 'r') as ex1input:  # open the source file
        all_lines = ex1input.readlines()  # read the source file line by line and put them in a list variable

    p = re.compile(re_str)  # compile into "RegEx Object"

    for i in range(len(all_lines)):
        info = p.findall(all_lines[i].strip('\n'))
        if flag is True and info != []:
            result += [all_lines[i]]
            #result += info+['\n']
        elif flag is True and info == []:
            continue
        elif flag is False and info == []:
            result += [all_lines[i]]
        elif flag is False and info != []:
            result += [all_lines[i].replace(info[0], '')]


    with open(output_file, 'w') as ex1output: # finally, write the result list to the file (be careful, 'writelines()' is used)
        ex1output.writelines(result)
        #for i in result:
        #    ex1output.write(i)

    return 'Check the output file'  # this is for information. actually it isn't necessary. We can return "True" or "1"

if __name__ == '__main__':
    re_string1 = r'.*(?<!\w):.*' #r"( +):.*" #r'.*(?<!\w):.*'    # For first test example ---- [[ r'(?<!\w):' chatGPT example ]]
    re_string2 = r"#.*"  # For second test example
    re_string3 = r'(.*Latitude.*.*Longitude.*|.*Longitude.*.*Latitude.*)'  # For third test example
    re_string4 = r'(<h[1-6]>.*</h[1-6]>)' #.*</h[1-6]>.+)' #r'(<h[123456]>).+'  # For fourth test example

    # !!!IMPORTANT: You need to change last boolean parameter "flag" for testing code.
    # ---------------------------------------------------------------------------------

    # test 1 :
    print(data_filter('5-2_gw_source_file1.txt', '5-2_gw_output_file1.txt', re_string1, False))

    # test 2 :
    print(data_filter('5-2_gw_source_file2.py', '5-2_gw_output_file2.py', re_string2, False))

    # test 3 :
    print(data_filter('5-2_gw_source_file3.txt', '5-2_gw_output_file3.txt', re_string3, False))

    # test 4 :
    print(data_filter('5-2_gw_source_file4.html', '5-2_gw_output_file4.html', re_string4, False))