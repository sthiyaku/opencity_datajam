import pandas as pd
import numpy as np

# Read input CSV file
in_file = '/home/thiyaku/Projects/personal/datajam/csv/merged_ward_data.csv'
df = pd.read_csv(in_file)

# Disable chained assignment warning
pd.options.mode.chained_assignment = None


# Function to assign categories to rows based on keywords
def assign_category(df, col, keywords, category):
    for keyword in keywords:
        mask = df[col].str.contains(keyword, case=False)
        df['Category'].loc[mask] = category
    return df


# Define keyword-category mappings
keyword_categories = {
    'road_keywords': ['pot hole', 'pothole', 'road', 'asphalt', 'fly over',
                      'flyover'],
    'footpath_keywords': ['footpath', 'foot path'],
    'drainage_keywords': ['drain', 'drian', 'ugd', 'rcc dra', 'culvert'],
    'electricity_keywords': ['electric', 'light', 'illumination'],
    'women_keywords': ['stri shakthi'],
    'dw_keywords': ['drinking water', 'drinking', 'supply of water',
                    'water supply', 'r o'],
    'gw_keywords': ['in filtration well', 'infiltration well', 'borewell',
                    'borwell', 'water har'],
    'toilet_keywords': ['toilet'],
    'c_b_keywords': ['crematorium', 'burial ground'],
    'health_keywords': ['hospital', 'moh building'],
    'school_keywords': ['school', 'anganawadi', 'anganavadi', 'anganwadi'],
    'poll_station_keywords': ['polling station'],
    'skill_devp_keywords': ['training', 'skill dev', 'reading ro'],
    'park_keywords': ['park'],
    'samudhaya_keywords': ['samudhaya', 'samudaya'],
    'library_keywords': ['library', 'libraury'],
    'gym_yoga_keywords': ['gym', 'yoga'],
    'sports_keywords': ['stadium', 'badminton', 'play eq', 'play gr'],
    'indira_canteen_keywords': ['indira canteen'],
    'HoW_keywords': ['temple', 'ganesha', 'prayer'],
    'name_board_keywords': ['name board', 'name bord'],
    'emergency_keywords': ['emergency work']
}
df['Category'] = ''
# Assign categories to rows based on keywords
for key, value in keyword_categories.items():
    df = assign_category(df, 'Name_of_Work', value, key.split('_')[0].title())

# Get rows with empty 'Category' column
empty_category_rows = df[df['Category'] == '']

# Sort empty category rows by 'Name_of_Work' column
empty_category_rows = empty_category_rows.sort_values('Name_of_Work')

# Assign 'Category' as 'Unknown' for remaining rows with empty 'Category' column
df['Category'].fillna('Unknown', inplace=True)

# Reset index of empty category rows
empty_category_rows.reset_index(drop=True, inplace=True)

# Display final DataFrame
print(df)
