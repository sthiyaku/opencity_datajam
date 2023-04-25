import matplotlib.pyplot as plt
import geopandas as gpd
import re
from math import ceil
import numpy as np

gpkg_dir = '/home/thiyaku/Projects/personal/datajam/gpkg'
gpkg_file = f'{gpkg_dir}/bangalore_assembly_spendings.gpkg'
png_dir = '/home/thiyaku/Projects/personal/datajam/png/spatial/'

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
gdf['label_position'] = gdf.apply(get_label_position, axis=1)
for col in plt_columns[7:8]:
    min_val = 0 # min(gdf[col])
    max_val = max(gdf[col])
    if max_val < 20:
        max_val = ceil(max_val/10) * 10
        plot_bins = np.arange(min_val, max_val, 5)
    elif max_val < 100:
        max_val = ceil(max_val/10) * 10
        plot_bins = np.arange(min_val, max_val, 10)
    elif max_val < 200:
        max_val = ceil(max_val/100) * 100
        plot_bins = np.arange(min_val, max_val, 50)
    elif max_val < 400:
        max_val = ceil(max_val/100) * 100
        plot_bins = np.arange(min_val, max_val, 100)
    elif max_val < 800:
        max_val = ceil(max_val/100) * 100
        plot_bins = np.arange(min_val, max_val, 200)
    elif max_val < 1500:
        max_val = ceil(max_val/100) * 100
        plot_bins = np.arange(min_val, max_val, 300)

    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(10, 10)
    gdf.plot(ax=ax, column=col, cmap='RdYlGn_r',
             scheme='User_Defined',
             classification_kwds=dict(bins=plot_bins[1:]),
             legend=True,
             edgecolor="k",
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
    #plt.close()
    # break
    print(png_file)
    #plt.show()
    
    
    #plt.show()
    #plt.close()
