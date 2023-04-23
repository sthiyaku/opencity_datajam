import pandas as pd
import numpy as np

csv_dir = '/home/thiyaku/Projects/personal/datajam/csv'
spending_file = f'{csv_dir}/wards_category_wise_spendings.csv'
w_c_file = f'{csv_dir}/wards_constituencies_mapping.csv'

spending_df = pd.read_csv(spending_file)
w_c_df = pd.read_csv(w_c_file)

# Update 'Constituency' column with corresponding constituency names
for ward_num in spending_df['Ward No']:
    
    if np.isnan(ward_num):
        ward_s_index = np.isnan(spending_df['Ward No'])
        spending_df.loc[ward_s_index, 'Constituency'] = 'Unknown'
    else:
        ward_s_index = spending_df['Ward No'] == ward_num
        ward_c_index = w_c_df['Ward Num'] == ward_num
        c_name = (w_c_df.loc[ward_c_index, 'Parliamentary Constituency Name']
                  .reset_index()['Parliamentary Constituency Name'][0])
        spending_df.loc[ward_s_index, 'Constituency'] = c_name

# Aggregate data by 'Constituency'
grouped_df = (spending_df.groupby(['Constituency']).sum(numeric_only=True)
              .reset_index())

# Drop 'Ward No' column
grouped_df.drop('Ward No', axis=1, inplace=True)

# Save the aggregated data to a CSV file
grouped_df.to_csv(f'{csv_dir}/spendings_aggregate_constituency.csv')
