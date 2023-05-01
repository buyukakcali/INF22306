import numpy as np


def convert_fah2cel(fahrenheit):
    return (fahrenheit-32)*5/9

if __name__ == '__main__':
    fah = 41
    print(convert_fah2cel(fah))
    asd = np.array([41, 49, 59])
    print(convert_fah2cel(asd))
    #:.2f