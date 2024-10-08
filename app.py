import streamlit as st
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import random

gdf = gpd.read_file('./map/Indian_States.shp')
df = pd.read_csv('./index_2021.csv')

def find_data(row):
    state = row['st_nm']
    for _, j_row in df.iterrows():
        if state in j_row['area_name']:
            return j_row['data']
        
    return 0

gdf['data'] = gdf.apply(find_data, axis=1)

mpl.rcParams['axes.titlesize'] = 32
mpl.rcParams['axes.titleweight'] = 3

st.write("India - All States Map")
fig, ax = plt.subplots(1, figsize=(100, 15))
plt.title("India - All States Map",
          fontdict = {
              'fontsize': mpl.rcParams['axes.titlesize'],
              'fontweight' : mpl.rcParams['axes.titleweight'],
              'verticalalignment': 'baseline',
              'horizontalalignment': 'center'
            }
        )
ax.axis('off')
gdf.plot(column='data', cmap='PuBu', linewidth=0.5, ax=ax, edgecolor='0.2',legend=True)
st.pyplot(fig)

mandal_gdf = gpd.read_file('./map/AllMandals.shp')
mandal_gdf['data'] = mandal_gdf.apply(lambda _: random.randint(1,100), axis=1)

st.write("Andhra Pradesh - Mandal Wise Map")
# st.write(mandal_gdf.head())
fig2, ax = plt.subplots(1, figsize=(100, 15))
plt.title("Andhra Pradesh - Mandal Wise Map",
          fontdict = {
              'fontsize': mpl.rcParams['axes.titlesize'],
              'fontweight' : mpl.rcParams['axes.titleweight'],
              'verticalalignment': 'baseline',
              'horizontalalignment': 'center'
            }
        )
ax.axis('off')
mandal_gdf.plot(column='data', cmap='PuBu', linewidth=0.5, ax=ax, edgecolor='0.2',legend=True)
st.pyplot(fig2)

dist_gdf = gpd.read_file('./map/AllDistricts.shp')
dist_gdf['data'] = dist_gdf.apply(lambda _: random.randint(1,100), axis=1)

st.write("Andhra Pradesh - District Wise Map")
fig2, ax = plt.subplots(1, figsize=(100, 15))
plt.title("Andhra Pradesh - District Wise Map",
          fontdict = {
              'fontsize': mpl.rcParams['axes.titlesize'],
              'fontweight' : mpl.rcParams['axes.titleweight'],
              'verticalalignment': 'baseline',
              'horizontalalignment': 'center'
            }
        )
ax.axis('off')
dist_gdf.plot(column='data', cmap='PuBu', linewidth=0.5, ax=ax, edgecolor='0.2',legend=True)
st.pyplot(fig2)