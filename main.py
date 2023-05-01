import pandas as pd

# create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# print the original column names
print(df.columns)

# change the column names
df = df.rename(columns={'A': 'X', 'B': 'Y', 'C': 'Z'})

# print the updated column names
print(f'Columns with new name:\n {df.columns}')
