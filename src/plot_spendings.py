import pandas as pd
import matplotlib.pyplot as plt
import re

in_file = '/home/thiyaku/Projects/personal/datajam/csv/constituency-spend-categories.csv'
png_dir = '/home/thiyaku/Projects/personal/datajam/png'
in_df = pd.read_csv(in_file)
in_df = in_df.loc[in_df['AC Num'] != 'Uncategorized']
# Define a regular expression pattern to match spaces and brackets
pattern = r"[()\s]+"

# Loop through each column in the DataFrame
for col in in_df.columns[2:]:

    # Create a histogram for the current column
    in_df.hist(column=col, bins=12)
    col = col.replace('_', ')')
    col = col.replace('(jn', '(in')
    # Add title and labels
    plt.title('Histogram of {}'.format(col))
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    # Display the plot
    col_name = re.sub(pattern, "_", col)
    png_bn = 'histogram_{}.png'.format(col_name)
    png_bn = png_bn.replace('_.png', '.png')
    png_file = f'{png_dir}/{png_bn}'
    plt.savefig(png_file)
    #plt.close()
    #break
    print(png_file)
    #plt.show()
