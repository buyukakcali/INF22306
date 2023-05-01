'''Read Me:
DESCRIPTION: This script writes city data to a text file from a dictionary.
PARAMETERS: Two parameters are used to create the .txt file: file name ('data_cities.txt')
and data ('dict1')            where 'dict1' is the dictionary produced in assignment
 flying_distances 4
LIMITATIONS: Unable to add new city data to the dictionary and file
            If you want to make any changes to the data, it would have to be done separately
STRUCTURES: def data_cities(): this function creates a dictionary
            dict1{}: this is used while creating a .txt file as the data parameter
OUTPUTS: the output of this is a text file in Python project folder containing the same information as the dictionary (to properly read the text file, open it outside of Pycharm)

'''

def data_cities():
    d = {}
    Amsterdam = ('Amsterdam', [52 , 22, 1], [4, 53, 'E'])
    Montreal = ('Montreal', [45, 52, 'N'], [73, 35, 'W'])
    Auckland = ('Auckland', [36, 52, 'S'], [174, 45, 'E'])
    d['Amsterdam'] = Amsterdam
    d['Montreal'] = Montreal
    d['Auckland'] = Auckland
    return d


# Writing to text file
def save_to_file(file:str, dict1:dict):
    city_dict1 = dict1
    with open(file, 'w') as file:
        for city, data in city_dict1.items():
            name = data[0]

            if type(data[1][2]) != str:
                if data[1][2] == 1:
                    data[1][2] = 'N'
                elif data[1][2] == -1:
                    data[1][2] = 'S'

            if type(data[2][2]) != str:
                if data[2][2] == 1:
                    data[2][2] = 'E'
                elif data[2][2] == -1:
                    data[2][2] = 'W'

            latitude = f"{str(data[1][0])}{chr(176)}, {str(data[1][1])}\' {data[1][2]}"
            longitude = f"{str(data[2][0])}{chr(176)} {str(data[2][1])}\' {data[2][2]}"
            line = f"Name: {name} Latitude: {latitude} Longitude: {longitude}\n"
            file.write(line)


if __name__ == '__main__':
    save_to_file('f4_2_data_cities.txt',data_cities())
