def user_average():
    total = 0
    count = 0
    print('Welcome, please enter numbers to calculate an average\n\
            After each input, press enter\n\
            To stop the calculation, just press enter')
    while True:
        number = input('Please supply a number> ')
        if number == '':
            break
        total += int(number)
        count += 1
    return total/count

print("Sonuç=",user_average())