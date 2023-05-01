def sum_odds(n):
    t = 0
    for i in n:
        i = int(i)
        if i % 2 != 0:
            t += i
    return t


if __name__ == "__main__":
    numbers = list(input("Give some numbers (use comma for each number): ").split(','))
    print(sum_odds(numbers))
#    print(sum_odds3([3, 5, 8, 1, -1, 39, 20]))
