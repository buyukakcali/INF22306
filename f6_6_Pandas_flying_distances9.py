import pandas as pd
import f4_2_gw_flying_distance5 as fd5

def rad_to_deg(rad):
    dir = 1
    if rad<0:
        dir = -1
    tot_min = abs(rad) * 60
    return  [(tot_min/60).__trunc__(), (tot_min%60).__trunc__(), dir]

def pd_to_dict(file:str):
    dict1 = {}
    df = pd.read_json(file)
    list1 = df.values.tolist()

    for i in range(len(list1)):
        dict1[list1[i][0]] = (list1[i][0], rad_to_deg(list1[i][1]), rad_to_deg(list1[i][2]))
    return dict1

if __name__ == '__main__':
    dictionary = pd_to_dict('ch.json')
    fd5.save_to_file('f6_6_Pandas_flying_distances9_data.txt', dictionary)