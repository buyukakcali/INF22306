# Import csv and pandas package
import csv
import pandas as pd


def change_column_names(file:csv, change_case:bool):
    # making data frame
    d_frame = pd.read_csv(file)
    # copying columns names to a new list
    columns = d_frame.columns
    # prepared an empty list for updated column names
    cols = []

    if change_case:
        for i in range(len(columns)):
            cols += [str(columns[i]).upper()]
    else:
        for i in range(len(columns)):
            cols += [str(columns[i]).lower()]
    d_frame.columns = cols
    return d_frame

# display - test
# you can download the test file from: "https://media.geeksforgeeks.org/wp-content/uploads/nba.csv"
# OR you can test it with one below line
#df_res = change_column_names("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv", False)

df_res = change_column_names("nba.csv", False)
print(df_res.head(5))   # Printing first 5 rows