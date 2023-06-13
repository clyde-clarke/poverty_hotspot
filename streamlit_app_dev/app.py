import plotly.express as px
import pandas as pd
import streamlit as st
import geopandas as gpd

data = pd.read_csv('/Users/mediciroad/Library/CloudStorage/GoogleDrive-cclarke@mediciroad.org/My Drive/Poverty Hotspot Project Plan/poverty_hotspot_data/data/indicator_data/indicator_subset.csv')
df_transport_geojson = gpd.read_file("/Users/mediciroad/Library/CloudStorage/GoogleDrive-cclarke@mediciroad.org/My Drive/Poverty Hotspot Project Plan/poverty_hotspot_data/data/ShapeFiles/GEOJSON/df_transport_geojson.geojson")
# Let the user select columns
selected_columns = st.multiselect('Select the columns to sum', data.columns)

# Calculate the sum of the selected columns
data['sum'] = data[selected_columns].sum(axis=1)

# Find the max value for the color scale
max_value = data['sum'].max()

fig = px.choropleth(data, geojson=df_transport_geojson, locations='GEOID',
                    color='sum',
                    color_continuous_scale="Viridis",
                    range_color=(0, max_value),
                    featureidkey="properties.GEOID",
                    projection="mercator",
                    title='Sum of selected indicators',
                    color_continuous_midpoint=data['sum'].mean())

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(coloraxis_colorbar_title='Sum', margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
