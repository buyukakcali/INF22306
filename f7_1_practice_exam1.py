'''
Practice Exam:

# Question 2 ---------------------------------------------------------
# Answer 1:
def display_forecast(temp, rain_mm=None, wind_strength=None):
    forecast = 'Tomorrow\'s temperature will be %4.2f °C' % temp
    if rain_mm != None:
        forecast += ', with %4.2d millimeters of rain' % rain_mm
    if wind_strength != None:
        forecast += ' and a %s wind' % wind_strength
    return forecast

asd = display_forecast(11.2, 3.2, 'medium')
print(asd)

# Question 2 ---------------------------------------------------------
# Answer 2:

def get_median(list2):
    #list2 = list1
    list2.sort()
    if len(list2)%2 == 1:
        result = list2[(len(list2)/2).__trunc__()]
    else:
        result = (list2[(len(list2) / 2).__trunc__()-1] + list2[(len(list2)/2).__trunc__()])/2
    print(list2)
    return result

print(get_median([1, 2, 9]))
#print(get_median([1, 2, 9, 234]))

# Question 3 ---------------------------------------------------------
# Answer 3:

class MonitoringTreeNumbers():
    def __init__(self, num_trees, year):
        self.tree_book = {}
        self.all_trees = num_trees #300
        self.current_year = year #2014
        #self.tree_book[year] = num_trees # missing code

    def next_year(self):
        self.current_year = self.current_year + 1

    def plant_trees(self, num_trees):
        if self.current_year in self.tree_book:
            self.tree_book[self.current_year] += num_trees
        else:
            self.tree_book[self.current_year] = num_trees
        self.all_trees = self.all_trees + num_trees

    def harvest_trees(self, num_trees):
        if num_trees > self.all_trees:
            raise ValueError('Not enough trees to harvest')
        harvested = 0
        while harvested < num_trees:
            key = list(self.tree_book.keys())[0]
            if self.tree_book[key] <= num_trees - harvested:
                harvested += self.tree_book[key]
                del self.tree_book[key]
            else:
                self.tree_book[key] -= num_trees - harvested
                harvested += num_trees - harvested
        all_trees = self.all_trees - num_trees #left side is missing code #self.all_trees = self.all_trees - num_trees

grower_a = MonitoringTreeNumbers(300, 2014)
print(grower_a.tree_book)
print(grower_a.all_trees)
grower_a.next_year()
grower_a.plant_trees(250)
print(grower_a.tree_book)
print(grower_a.all_trees)
grower_a.next_year()
grower_a.plant_trees(300)
grower_a.harvest_trees(450)
print(grower_a.tree_book)
print(grower_a.all_trees)
'''


# Question 4 ---------------------------------------------------------
# Answer 4a
def build_filenames(year, rec):
    filenames = []

    for i in range(rec):
        rec_num = (4 - len(str(i))) * '0'
        filenames += [f'receipt_{year}_{rec_num + str(i + 1)}.txt']
    return filenames


# print(build_filenames(2020, 3))

# Answer 4b
def read_receipt(filename):
    with open(filename) as file:
        lines = file.readlines()
        products = []
        for line in lines:
            products += [line.split('\t')]
    result_dict = {}

    for i in range(len(products)):
        if products[i][1] in result_dict:
            print()
            result_dict[products[i][1]] = result_dict[products[i][1]] + int(products[i][2])
        else:
            result_dict[products[i][1]] = int(products[i][2])
    return result_dict


# print(read_receipt('receipt_2020_0002.txt')) # you can check other receipt files (~0001.txt and .ÜÜ  ~0003.txt) too.


# Answer 4c
def merge_receipts(year, number_of_rec):
    merged_dict = {}
    filenames = build_filenames(year, number_of_rec)
    for i in filenames:
        # print(filenames) # data check point ;)
        # print(i) # data check point ;)
        temp_dict = read_receipt(i)
        for j in temp_dict:
            # print(j) # data check point ;)
            # print(temp_dict[j]) # data check point ;)
            if j in merged_dict:
                merged_dict[j] += temp_dict[j]
                # print(merged_dict[j]) # data check point ;)
            else:
                merged_dict[j] = temp_dict[j]
                # print(merged_dict[j]) # data check point ;)
    return merged_dict


print(merge_receipts(2020, 3))
# called 2020 and 3. Because we have three receipt file in the project folder and its year is 2020
