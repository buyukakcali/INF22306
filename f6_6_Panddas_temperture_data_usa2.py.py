import numpy as np
import pandas as pd

import f6_3_temperture_data_usa1 as tdu1


def cnv_fah2cel(fahr):
    return tdu1.convert_fah2cel(fahr)
    # Original function is:
    #
    # def convert_fah2cel(fahrenheit):
    #     return (fahrenheit-32)*5/9

def change_degrees(file):
    # copying the data to a data frame from csv file
    d_frame = pd.read_csv(file)
    # copied only the wanted columns
    df_orj = d_frame[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC', 'ANN']]
    # create a copy of the original dataframe
    df = df_orj.copy()
    # create a numpy array from the copied dataframe: it just gets the numbers from the dataframe
    df_npa = pd.DataFrame(df).to_numpy()
    for i in range(len(df_npa)):
        #df_npa[i] = cnv_fah2cel(df_npa[i])
        df_npa[i] = np.round(cnv_fah2cel(df_npa[i]),2)
    return df

if __name__ == '__main__':
    result = change_degrees('nrmavg.csv')
    print(result)