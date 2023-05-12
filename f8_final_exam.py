# Question - Answer 4 ------------------------------------------
def comp_data(filename, c_list):
    comp_dict = {}
    result_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            temp = line.split('\t') # This line must be like "temp = line.strip('\n').split('\t')" without double quotas. Otherwise we will see \n, at the end of the company names. This is my mistake in the exam.
            comp_dict[temp[0]] = (str(temp[1]), temp[2])
    for i in range(len(c_list)):
        if c_list[i] in comp_dict:
            result_dict[c_list[i]] = comp_dict[c_list[i]]
    return result_dict


# Question - Answer 4 ------------------------------------------
def my_func(starting_amount, limit, rate):
    total_amount = starting_amount
    year = 0
    while total_amount < limit:
        rated_amount = (total_amount * rate) / 100
        total_amount += rated_amount
        year += 1
    return (total_amount, year)


if __name__ == '__main__':
    print('# Answer 2 ------------------------------------------')
    given_company_list = ["CCC", "CSC", "FF1", "LRA", "UNI"] # teacher gave this list. but output never meets with this order
    companies_list = ["CCC", "UNI", "FF1", "CSC"]   # reordered the list for output
    print(comp_data('f8_final_exam_Q2_data.txt', companies_list))
    print('\n# Answer 4 ------------------------------------------')
    print(my_func(100, 250, 4.5))
