def create_test_data():
    '''c1_name = 'Amsterdam'
    c1_lat = (52, 22, 'N')
    c1_lon = (4, 32, 'E')

    c1_data = c1_lat, c1_lon

    c1 = c1_name, c1_data
    '''

    Amsterdam = ('Amsterdam', (52, 22, 'N'), (4, 32, 'E'))
    Montreal = ('Montreal', (45, 30, 'N'), (73, 35, 'W'))
    Auckland = ('Auckland', (36, 52, 'S'), (174, 45, 'E'))

    cities = {}
    cities['Amsterdam'] = Amsterdam
    cities['Montreal'] = Montreal
    cities['Auckland'] = Auckland

    return cities


print(create_test_data())
