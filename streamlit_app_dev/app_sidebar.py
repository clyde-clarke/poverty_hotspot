import plotly.express as px
import streamlit as st
import pandas as pd
import geopandas as gpd

data = pd.read_csv('/Users/mediciroad/Library/CloudStorage/GoogleDrive-cclarke@mediciroad.org/My Drive/Poverty Hotspot Project Plan/poverty_hotspot_data/data/indicator_data/indicator_subset.csv')
df_transport_geojson = gpd.read_file("/Users/mediciroad/Library/CloudStorage/GoogleDrive-cclarke@mediciroad.org/My Drive/Poverty Hotspot Project Plan/poverty_hotspot_data/data/ShapeFiles/GEOJSON/df_transport_geojson.geojson")
# Let the user select columns
selected_columns = st.sidebar.multiselect('Select Indicators', data.columns)

# Calculate the sum of the selected columns
data['Number of Indicators'] = data[selected_columns].sum(axis=1)

# Find the max value for the color scale
max_value = data['Number of Indicators'].max()

fig = px.choropleth(data, geojson=df_transport_geojson, locations='GEOID',
                    color='Number of Indicators',
                    color_continuous_scale="Viridis",
                    range_color=(0, max_value),
                    featureidkey="properties.GEOID",
                    projection="mercator",
                    title='Sum of selected indicators',
                    color_continuous_midpoint=data['Number of Indicators'].mean())

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(coloraxis_colorbar_title='Number of Indicators', margin={"r": 0, "t": 0, "l": 0, "b": 0})

# Display the figure in the Streamlit app
st.plotly_chart(fig)
