import geopandas as gpd
import pandas as pd
gpkg_dir = '/home/thiyaku/Projects/personal/datajam/gpkg'
csv_dir = '/home/thiyaku/Projects/personal/datajam/csv'
gpkg_file = f'{gpkg_dir}/bangalore_assembly.gpkg'
csv_file = f'{csv_dir}/constituency-spend-categories.csv'

df = pd.read_csv(csv_file)
df = df.loc[df['AC Num'] != 'Uncategorized']
df = df.iloc[:, [0, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]]
df = df.rename(columns={'AC Num': 'AC_CODE',
                        'AC Name': 'AC_NAME'})
gdf = gpd.read_file(gpkg_file)

merged_gdf = gdf.merge(df, on='AC_CODE', how='left')

out_file = f'{gpkg_dir}/bangalore_assembly_spendings.gpkg'
merged_gdf.to_file(out_file)

