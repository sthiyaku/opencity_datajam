import pandas as pd
import numpy as np
in_file = '/home/thiyaku/Projects/personal/datajam/csv/merged_ward_data.csv'

df = pd.read_csv(in_file)
df['Category'] = ''

col = 'Name_of_Work'
df[col] = df[col].str.lower()

mask = np.column_stack([df[col].str.contains("road")])
df['Category'].loc[mask] = 'Road'

mask = np.column_stack([df[col].str.contains("drain")])
df['Category'].loc[mask] = 'Drainage'
mask = np.column_stack([df[col].str.contains("rcc dra")])
df['Category'].loc[mask] = 'Drainage'

mask = np.column_stack([df[col].str.contains("light")])
df['Category'].loc[mask] = 'Lights'

mask = np.column_stack([df[col].str.contains("drinking water")])
df['Category'].loc[mask] = 'Drinking water'
mask = np.column_stack([df[col].str.contains("borewell")])
df['Category'].loc[mask] = 'Drinking water'
mask = np.column_stack([df[col].str.contains("tiolet")])
df['Category'].loc[mask] = 'Tiolets'

empty_cols = df['Category'] == ''
foo = df.loc[empty_cols].reset_index()
print(foo['Name_of_Work'][1])
print(np.nansum(empty_cols))
