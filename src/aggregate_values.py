import pandas as pd

in_file = '/home/thiyaku/Projects/personal/datajam/csv/categorised.csv'

in_df = pd.read_csv(in_file)

grouped_df = in_df.groupby(['Ward_number', 'Category']).agg({'Gross': ['sum', 'mean']})


# Flatten the column index
grouped_df.columns = grouped_df.columns.map('_'.join)

# Reset index
grouped_df = grouped_df.reset_index()

# Save the file
grouped_df.to_csv('/home/thiyaku/Projects/personal/datajam/csv/aggregated.csv')

