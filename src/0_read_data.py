import pandas as pd
import glob as glob
import os
import datetime

in_files = glob.glob('/home/thiyaku/Projects/personal/datajam/data/Ward_Work_Orders/*csv')
out_dir = '/home/thiyaku/Projects/personal/datajam/data/Ward_Work_Orders_V2'
if not os.path.exists(out_dir):
    os.makedirs(out_dir)
    
col_names = []
col_names_v2 = ['Job Number', 'Name of Work', 'Contractor',
                'BR Number', 'Gross', 'Nett', 'Deduction']
START_DATE = datetime.datetime(2018, 1, 1)
for in_file in in_files:
    in_df = pd.read_csv(in_file)
    
    if in_df.columns[3] == 'Unnamed: 3':
        in_df = pd.read_csv(in_file, header=1)
    if in_df.columns[1] == 'Sl No':
        # in_df = pd.read_csv(in_file, header=1)
        in_df = in_df.iloc[:, 2:]

    if in_df.columns[1] == 'wo num':
        in_df = in_df.iloc[:, 1:]
        in_df.columns = col_names_v2

    if 'Start Date' in in_df.columns:
        mask = pd.to_datetime(in_df['Start Date'], errors='coerce') >= START_DATE
        in_df = in_df.loc[mask]
        # break

    in_df = in_df[col_names_v2]
    in_bn = os.path.basename(in_file)
    in_df['Ward_number'] = in_bn.replace('.csv', '')
    out_file = os.path.join(out_dir, in_bn)
    
    if not os.path.exists(out_file):
        in_df.to_csv(out_file, index=False)
    print(out_file)
