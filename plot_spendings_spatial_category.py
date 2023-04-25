import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import geopandas as gpd
import re
from math import ceil
import numpy as np

gpkg_dir = '/home/thiyaku/Projects/personal/datajam/gpkg'
gpkg_file = f'{gpkg_dir}/bangalore_assembly_spendings.gpkg'
png_dir = '/home/thiyaku/Projects/personal/datajam/png/spatial_v2/'

# Define a regular expression pattern to match spaces and brackets
pattern = r"[()\s]+"

gdf = gpd.read_file(gpkg_file)

plt_columns = gdf.columns[6:-1]


def get_label_position(row):
    geometry = row['geometry']
    location = geometry.representative_point()
    # We need the location as a tuple of x,y coordinates
    location_coords = location.coords[0]
    return location_coords
bdy = gdf
cat_dict = {'High': [100, 100, 100, 300, 300, 30, 8, 10, 80, 800],
            'Low': [50, 50, 50, 150, 150, 15, 4, 5, 40, 400]}
cat_order = {1: 'High', 2: 'Medium', 3: 'Low'}
def replace_legend_items(legend, mapping):
    for txt in legend.texts:
        for k,v in mapping.items():
            if txt.get_text() == str(k):
                txt.set_text(v)
n = len(plt_columns)

gdf['label_position'] = gdf.apply(get_label_position, axis=1)

for i in range(n):
    col = plt_columns[i]
    print(col)
    gdf['Cat'] = 2
    low_val = cat_dict['Low'][i]
    high_val = cat_dict['High'][i]
    gdf['Cat'][gdf[col] < low_val] = 3
    gdf['Cat'][gdf[col] > high_val] = 1
    # gdf['Cat'] = gdf['Cat'].map(cat_order)
    # break
    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(10, 10)
    gdf.plot(ax=ax, column='Cat', cmap='RdYlGn_r',
             legend=True,
             edgecolor="k",
             categorical=True,
             linewidth=1,
             legend_kwds={"fmt": "{:.0f}"})
    #bdy.plot(ax=ax,facecolor='none')
    # ax.set_axis_off()
    col = col.replace('_', ')')
    col = col.replace('(jn', '(in')
    plt.title(format(col), size=18)
    plt.xlabel('Longitude (°E)', fontsize=15, rotation=0)
    plt.ylabel('Latitude (°N)', fontsize=15, rotation=90)
    # fig, ax = plt.subplots(1, 1)
    # fig.set_size_inches(10, 10)
    # bdy.plot(ax=ax, facecolor='none')
    # plt.show()
    replace_legend_items(ax.get_legend(), cat_order)

    #for idx, row in gdf.iterrows():
    #    ax.annotate(text=row['AC_CODE'], xy=row['label_position'],
    #                size=20, color='black',
    #                path_effects=[pe.withStroke(linewidth=1, foreground="white")],
    #                horizontalalignment='center')
    # Add title and labels
    #plt.title()
    print(col)
    # Display the plot
    col_name = re.sub(pattern, "_", col)
    png_bn = 'histogram_{}.png'.format(col_name)
    png_bn = png_bn.replace('_.png', '.png')
    png_bn = png_bn.replace('.png', '_spatial.png')
    png_file = f'{png_dir}/{png_bn}'
    plt.savefig(png_file, dpi=300)
    # plt.close()
    # break
    print(png_file)
    #plt.show()
    
    
    #plt.show()
    #plt.close()
