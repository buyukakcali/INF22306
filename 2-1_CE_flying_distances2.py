"""
Author: Teacher #123
Date: 27/03/2023
Script for calculating the distance flown between two cities
    Coordinates should be given in latitude & longitude (sign (+1 or -1), degrees, minutes)
    Functions: Haversine, convert, km
"""
import math
from string_splitter import string_split


def haversine(lat1, lon1, lat2, lon2):
    z = math.sin( (lat2 - lat1) / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin( (lon2 - lon1) / 2)**2
    a = math.sqrt(z)
    y = 1 - z
    b = math.sqrt(y)
    d = 2 * math.atan2(a, b)
    return d


def convert(sign, degrees, minutes):
    total_deg = degrees + minutes / 60  # converting minutes to degrees and adding to total degrees
    rad = total_deg / (360 / (2 * math.pi))  # converting degrees to radians
    rad = sign * rad  # considering the right direction
    return rad


def km(lst):
    dgr1, mn1, dr1, dgr2, mn2, dr2, dgr3, mn3, dr3, dgr4, mn4, dr4 = lst
    # Convert 4 inputs (sign, degrees, minutes) into radians
    lt1 = convert(dr1, dgr1, mn1)
    ln1 = convert(dr2, dgr2, mn2)
    lt2 = convert(dr3, dgr3, mn3)
    ln2 = convert(dr4, dgr4, mn4)
    # Calculate arc with the 4 radians
    d_rad = haversine(lt1, ln1, lt2, ln2)
    # Scale to real world
    d_km = d_rad * 6367
    return d_km

def get_data():
    result = []
    for i in range(4):
        if i % 2 == 0:
            lat_or_lon = 'Latitude'
        else:
            lat_or_lon = 'Longitude'
        if i < 2:
            which_city = 1
        else:
            which_city = 2

        data = input(f"For {which_city}. Location {lat_or_lon}: ").lower().split()

        if len(data) == 2:
            temp = data
            data[0] = temp[0]
            data[2] = temp[1]
            data[1] = '0'

        if data[2] == 'n' or data[2] == 'e':
            data[2] = 1
        elif data[2] == 's' or data[2] == 'w':
            data[2] = -1
        else:
            if data[2].__contains__('1' or '-1'):
                data[2] = int(data[2])
            else:
                print('Incorrect DIRECTION! Start entering the values at the beginning:')
                break

    # Latitude and Longitude converting and rearranging
    # Degreee
        if data[0].__contains__('!'):
            data[0] = data[0].strip('!')
        if not int(data[0]) in range(-90, 91) and lat_or_lon == 'Latitude':
            print('Incorrect DEGREE! Start entering the values at the beginning:')
            break
        elif not int(data[0]) in range(-180, 181) and lat_or_lon == 'Longitude':
            print('Incorrect DEGREE! Start entering the values at the beginning:')
            break
        else:
            data[0] = int(data[0])

        # Minute
        if data[1].__contains__("'") and 59 >= int(data[1].strip("'")) >= 0:   # '!' used instead of '°' - degree
            data[1] = int(data[1].strip("'"))
        elif 59 >= int(data[1]) >= 0:
            data[1] = int(data[1])
        else:
            print('Incorrect MINUTE! Start entering the values at the begining:')
            break
        print(data)
        result += data
    return result


if __name__ == "__main__":       # Will only run if this script is run (not if it's imported)
    print(km(get_data()))
    # Amsterdam: lat(1, 52, 22) and lon(1, 4, 32)
    # Montreal: lat(1, 45, 30) and lon(-1, 73, 35)
    #d = km(1, 52, 22, 1, 4, 32, 1, 45, 30, -1, 73, 35)
    #print('Distance is', round(d), 'km')

   # la1,lo1,la2,lo2 = get_lat_lon()
    #mesafe = km(la1[0], la1[1], la1[2], lo1[0], lo1[1], lo1[2], la2[0], la2[1], la2[2], lo2[0],
 #               lo2[1], lo2[2])
    #print(mesafe)

# print(type(la1[0]),type(la1[1]),type(la1[2]),type(lo1[0]),type(lo1[1]),type(lo1[2]),type(la2[0]),type(la2[1]),type(la2[2]),type(lo2[0]),type(lo2[1]),type(lo2[2]))
















