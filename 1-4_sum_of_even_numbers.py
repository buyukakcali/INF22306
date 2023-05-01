def sum_evens_1(n): #way 1
    t=0
    list = range(2,n+1)
    for _ in list:
        if _ % 2 == 0:
            t += _
    return t

def sum_evens_2(n): # way 2
    t = 0
    list= range(2,n+1,2)
    for _ in list:
        t = t + _
    return t

def sum_evens_3(n): # way 3
    t=0
    while n>0:
        if n%2==0:
            t=t+n
            n=n-1
        n -= 1
    return t


if __name__ == "__main__":
    number = int(input("Give a number: "))
    print(sum_evens_3(number))