""""
ReadMe

DESCRIPTION: this code computes the distance between two points supplied through parameters, and returns a floating number

PARAMETERS: degrees with minutes and direction for the latitude and longditude of two locations

LIMITATIONS: not userfriendly, could be improved though the use of a function

STRUCTURES: the pramaters are converted form degrees,minutes,direction to radians (so from 3 numbers to 1) through the deg_to_rad function the haversien equation was applied to the radians to give the distance between two points the prameters can be input in print(haver()) the form
        latitude 1: degrees,minutes,direction
        longditude 1: degrees,minutes,direction
        latitude 2: degrees,minutes,direction
        longditude 2: degrees,minutes,direction
OUTPUT: the distance between two points on Earth
"""

import math


def deg_to_rad(deg, min, direction):
    total_deg = deg + min / 60  # converting minutes to degrees and adding to total degrees
    rad = total_deg / (360 / (2 * math.pi))  # converting degrees to radians
    return rad * direction


def rad_to_deg(rad):
    dir = 1
    if rad < 0:
        dir = -1
    total_deg = abs(rad * (360 / (2 * math.pi)))
    total_sec = total_deg * 3600
    tot_min = total_sec / 60
    return [(tot_min / 60).__trunc__(), (tot_min % 60).__trunc__(), dir]


def haver(lat1_deg, lat1_min, lat1_dir, long1_deg, long1_min, long1_dir, lat2_deg, lat2_min, lat2_dir, long2_deg,
          long2_min, long2_dir):
    lat1 = deg_to_rad(lat1_deg, lat1_min, lat1_dir)
    long1 = deg_to_rad(long1_deg, long1_min, long1_dir)
    lat2 = deg_to_rad(lat2_deg, lat2_min, lat2_dir)
    long2 = deg_to_rad(long2_deg, long2_min, long2_dir)
    a_sqr = math.sin((lat2 - lat1) / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin((long2 - long1) / 2) ** 2
    b_sqr = 1 - a_sqr
    a = math.sqrt(a_sqr)
    b = math.sqrt(b_sqr)
    d = 2 * math.atan2(a, b)  # distance with r=1 units
    real_d = d * 6367  # real distance for earth, r=6367km
    return real_d


if __name__ == '__main__':
    print(haver(45, 30, 1, 73, 35, -1, 52, 22, 1, 4, 53, 1))
    print(rad_to_deg(0.9139707516276973))
    print(deg_to_rad(52, 22, 1))
