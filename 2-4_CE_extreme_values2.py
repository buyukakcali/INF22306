def extreme_values(nums):
    min_num = nums[0]
    max_num = nums[0]
    min_poz = 0
    max_poz = 0

    for i in range(len(nums)):
        if nums[i] < min_num:
            min_num = nums[i]
            min_poz = i
        elif nums[i] > max_num:
            max_num = nums[i]
            max_poz = i

    return min_num, min_poz, max_num, max_poz


if __name__ == '__main__':
 #   numbers = [-5,2,3,1]
  #  mn, mx = extreme_values(numbers)
   # print("Minimum:", mn, "Maximum:", mx)
    # the results of the function with argument [1, 3, 2, 0] should be 0 and 3.
    test1 = [1, 3, 2, 0]
    expected1 = (0, 3, 3, 1)
    result1 = extreme_values(test1)  # -> 0 and 3
    # print('running', test1, 'resulted in', result1, 'vs expected', expected1)
    print('running', test1, 'result:', expected1 == result1)