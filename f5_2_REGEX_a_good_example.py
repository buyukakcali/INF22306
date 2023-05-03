import re


def read_order2(filename):
    products = {}
    with open(filename) as f:
        for line in f:
            p = re.compile('([0-9]*)\t([A-Za-z0-9 ]*)\t([0-9]*)\t(.*)\t(.*)')
            m = p.match(line)
            print(m)    # check code
            print(m[5]) # check code example
            name = m[2]
            quantity = int(m[3])
            if name in products:
                products[name] += quantity
            else:
                products[name] = quantity
    return products


result = read_order2('receipt_2020_0001.txt')
# print(result)
