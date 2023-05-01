import random

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


def random_list():
    result = []
    while len(result) < 4:
        x = 10 * random.random()
        x = int(x)

        if len(result) == 0:
            result.append(x)
        elif x not in result:
            result.append(x)
    return result


if __name__ == '__main__':
    test = random_list()
    ma = max(test)
    mi = min(test)
    for _ in range(len(test)):
        if test[_] == ma:
            key_ma = _
        if test[_] == mi:
            key_mi = _

    expected1 = (mi, key_mi, ma, key_ma)
    result1 = extreme_values(test)
    print('Test Result= ', result1 == expected1)
