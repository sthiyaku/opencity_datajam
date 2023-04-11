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
    'road_keywords': ['pot hole', 'pothole', 'patholes', 'road', 'asphalt',
                      'fly over', 'flyover', 'cement concrete', 'cc patch',
                      'bridge'],
    'footpath_keywords': ['footpath', 'foot path'],
    'drainage_keywords': ['drain', 'drian', ' ugd ', 'rcc dra', 'culvert',
                          'sw line', 'silt', ' swd '],
    'electricity_keywords': ['electric', 'light', 'illumination'],
    'women_keywords': ['stri shakthi'],
    'drinking water_keywords': ['drinking water', 'drinking', 'r o', 'ro plant',
                                'supply of water', 'supplying of water',
                                'water supply'],
    'ground water_keywords': ['in filtration well', 'infiltration well',
                              'borewell', 'borwell', 'water har'],
    'toilet_keywords': ['toilet'],
    'c_b_keywords': ['crematorium', 'burial ground'],
    'health care_keywords': ['hospital', 'moh ', 'phc ', 'sanitary', 'doctor',
                             'primary hea', 'covid'],
    'school or college_keywords': ['school', 'anganawadi', 'anganavadi',
                                   'anganwadi', 'pu college', 'college'],
    'poll_station_keywords': ['polling station'],
    'skill_development_keywords': ['training', 'skill dev', 'reading ro',
                                   'laptop'],
    'park_keywords': ['park'],
    'samudhaya_keywords': ['samudhaya', 'samudaya'],
    'library_keywords': ['library', 'libraury'],
    'gym_yoga_keywords': ['gym', 'yoga'],
    'sports_keywords': ['stadium', 'badminton', 'play eq', 'play gr', 'playgr'
                        'basket ball', 'kabbadi', 'volley ball', 'sports'],
    'indira canteen_keywords': ['indira canteen', 'indrira canteen',
                                'canteen'],
    'House of Worship_keywords': ['temple', 'ganesha', 'prayer'],
    'name_board_keywords': ['name board', 'name bord'],
    'emergency_keywords': ['emergency work'],
    'EWS_keywords': ['ews house'],
    'waste management_keywords': ['sweep smart'],
    'maintenance_keywords': ['annual maint', 'maintenance']
}

df.Name_of_Work = df.Name_of_Work.replace(r'\s+', ' ', regex=True)

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
print(empty_category_rows)
