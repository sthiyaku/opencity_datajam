import pandas as pd
import glob as glob
import os

in_files = glob.glob('/home/thiyaku/Projects/personal/datajam/data/Ward_Work_Orders_V2/*csv')
out_file = '/home/thiyaku/Projects/personal/datajam/csv/merged_ward_data.csv'
col_names_v2 = ['Job_Number', 'Name_of_Work', 'Contractor',
                'BR_Number', 'Gross', 'Nett', 'Deduction', 'Ward_number']

df = pd.concat(map(pd.read_csv, in_files), ignore_index=True)
df.columns = col_names_v2
df.to_csv(out_file, index=False)
