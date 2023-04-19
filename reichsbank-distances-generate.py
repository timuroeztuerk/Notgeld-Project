import pandas as pd
import geopandas as gpd

# Import the wurttemberg-with-names.shp file.
obs_shp = gpd.read_file('wurttemberg-with-names.shp')

# Import the reichsbank-locations.csv file.
locations = pd.read_csv('reichsbank-locations.csv')

# Create a new column in the obs_shp GeoDataFrame called 'reichsbank'.
obs_shp['reichsbank'] = 0

# Fill this column with the values from the 'reichsbank' column in the locations DataFrame, only if the ID and name match.
for i in range(len(locations)):
    obs_shp.loc[(obs_shp['ID'] == locations['ID'][i]) & (obs_shp['name'] == locations['name'][i]), 'reichsbank'] = locations['reichsbank'][i]

# Calculate the centroids of the observations.
obs_shp['centroid'] = obs_shp['geometry'].centroid

# A new dataframe where reichsbank is not 0.
reichsbank = obs_shp[obs_shp['reichsbank'] != 0]

# Calculate the distance of each observation to each reichsbank location, and keep the minimum in the distance column.
obs_shp['distance'] = 0

for j in range(len(reichsbank)):
    # Get the centroid of the current reichsbank location.
    rb_centroid = reichsbank.iloc[j]['centroid']
    # Calculate the distance from each observation to the current reichsbank location. Create a column called distance that changes for each iteration.
    obs_shp['distance_{}'.format(j)] = obs_shp['centroid'].distance(rb_centroid)

# Get the minimum distance for each observation and update the 'distance' column in the obs_shp DataFrame. Use .loc.
for i in range(len(obs_shp)):
    obs_shp.loc[i, 'distance'] = obs_shp.loc[i, obs_shp.filter(like='distance_').columns].min()

# Drop the distance columns that were created for each iteration.
obs_shp = obs_shp.drop(obs_shp.filter(like='distance_'), axis=1)

# Keep only ID, name, reichsbank, and distance.
obs_shp = obs_shp[['ID', 'reichsbank', 'distance']]

# Keep only unique ID's.
obs_shp = obs_shp.drop_duplicates(subset='ID')

# Create a new column in the obs_shp GeoDataFrame called 'reichsbank'.
obs_shp['reichsbank'] = 0

# Fill this column with the values from the 'reichsbank' column in the locations DataFrame, only if the ID and name match.
for i in range(len(locations)):
    obs_shp.loc[(obs_shp['ID'] == locations['ID'][i]), 'reichsbank'] = locations['reichsbank'][i]

# Save it as a csv.
obs_shp.to_csv('reichsbank-distances.csv', index=False)