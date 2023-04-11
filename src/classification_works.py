import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None  # default='warn'

in_file = '/home/thiyaku/Projects/personal/datajam/csv/merged_ward_data.csv'

df = pd.read_csv(in_file)
df['Category'] = ''

col = 'Name_of_Work'
df[col] = df[col].str.lower()
df.Name_of_Work = df.Name_of_Work.replace(r'\s+', ' ', regex=True)

road_keywords = ['pot hole', 'pothole', 'road', 'asphalt', 'fly over',
                 'flyover']
for keyword in road_keywords:
    mask = np.column_stack([df[col].str.contains(keyword)])
    df['Category'].loc[mask] = 'Road'

drainage_keywords = ['drain', 'drian', 'ugd', 'rcc dra', 'culvert']
for keyword in drainage_keywords:
    mask = np.column_stack([df[col].str.contains(keyword)])
    df['Category'].loc[mask] = 'Drainage'

electricity_keywords = ['electric', 'light', 'illumination']
for keyword in electricity_keywords:
    mask = np.column_stack([df[col].str.contains(keyword)])
    df['Category'].loc[mask] = 'Electric work'
    
women_keywords = ['stri shakthi']
for keyword in women_keywords:
    mask = np.column_stack([df[col].str.contains(keyword)])
    df['Category'].loc[mask] = 'Women empowerment'

dw_keywords = ['drinking water', 'drinking', 'supply of water', 'water supply']
for keyword in dw_keywords:
    mask = np.column_stack([df[col].str.contains(keyword)])
    df['Category'].loc[mask] = 'Drinking water'

gw_keywords = ["in filtration well", "infiltration well", "borewell"]
for keyword in gw_keywords:
    mask = np.column_stack([df[col].str.contains(keyword)])
    df['Category'].loc[mask] = 'Ground water'


mask = np.column_stack([df[col].str.contains("toilet")])
df['Category'].loc[mask] = 'Toilets'

c_b_keywords = ['crematorium', 'burial ground']
for keyword in c_b_keywords:
    mask = np.column_stack([df[col].str.contains(keyword)])
    df['Category'].loc[mask] = 'Crematorium/burial ground'

health_keywords = ['hospital', 'moh building']
for keyword in health_keywords:
    mask = np.column_stack([df[col].str.contains(keyword)])
    df['Category'].loc[mask] = 'Healthcare'

school_keywords = ['school', 'anganawadi', 'anganavadi']
for keyword in school_keywords:
    mask = np.column_stack([df[col].str.contains(keyword)])
    df['Category'].loc[mask] = 'School'

mask = np.column_stack([df[col].str.contains("polling station")])
df['Category'].loc[mask] = 'Poll station'

skill_devp_keywords = ['training', 'skill dev', 'reading ro']
for keyword in skill_devp_keywords:
    mask = np.column_stack([df[col].str.contains(keyword)])
    df['Category'].loc[mask] = 'Skill development'

mask = np.column_stack([df[col].str.contains("park")])
df['Category'].loc[mask] = 'Parks'
samudhaya_keywords = ['samudhaya', 'samudaya']
for keyword in samudhaya_keywords:
    mask = np.column_stack([df[col].str.contains(keyword)])
    df['Category'].loc[mask] = 'Samudhaya bhavana'

library_keywords = ['library', 'libraury']
for keyword in library_keywords:
    mask = np.column_stack([df[col].str.contains(keyword)])
    df['Category'].loc[mask] = 'Library'

gym_yoga_keywords = ['gym', 'yoga']
for keyword in gym_yoga_keywords:
    mask = np.column_stack([df[col].str.contains(keyword)])
    df['Category'].loc[mask] = 'Gym/Yoga'

sports_keywords = ['stadium', 'badminton', 'play eq']
for keyword in sports_keywords:
    mask = np.column_stack([df[col].str.contains(keyword)])
    df['Category'].loc[mask] = 'Sports'

indira_canteen_keywords = ['indira canteen']
for keyword in indira_canteen_keywords:
    mask = np.column_stack([df[col].str.contains(keyword)])
    df['Category'].loc[mask] = 'Indira canteen'

HoW_keywords = ['temple', 'ganesha']
for keyword in HoW_keywords:
    mask = np.column_stack([df[col].str.contains(keyword)])
    df['Category'].loc[mask] = 'House of worship'

name_board_keywords = ['name_board', 'name_bord']
for keyword in name_board_keywords:
    mask = np.column_stack([df[col].str.contains(keyword)])
    df['Category'].loc[mask] = 'Name board'

empty_cols = df['Category'] == ''
foo = df.loc[empty_cols].reset_index()
print(foo['Name_of_Work'][1])
print(np.nansum(empty_cols))
