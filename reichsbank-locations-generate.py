import pandas as pd
# Create an empty dataframe with four columns, ID, name, reichsbank, and type.
df = pd.DataFrame(columns=['ID', 'name', 'reichsbank'])
# Fill the dataframe with the following data.
df.loc[0] = ['10701', 'Heilbronn', '3']
df.loc[1] = ['41307', 'Friedrichshafen', '3']
df.loc[2] = ['41001', 'Ravensburg', '3']
df.loc[3] = ['40101', 'Biberach', '3']
df.loc[4] = ['21601', 'Tuttlingen', '3']
df.loc[5] = ['21201', 'Rottweil', '3']
df.loc[6] = ['21227', 'Schwenningen', '3']
df.loc[7] = ['30801', 'Heidenheim', '3']
df.loc[8] = ['40401', 'Geislingen', '3'] # Not sure, many Geislingens.
df.loc[9] = ['40501', 'Göppingen', '3']
df.loc[10] = ['10601', 'Eßlingen', '3']
df.loc[11] = ['30601', 'Schwäbisch Gmünd', '3']
df.loc[12] = ['30101', 'Aalen', '3']
df.loc[13] = ['41401', 'Ulm', '2']
df.loc[14] = ['21001', 'Reutlingen', '2']
df.loc[15] = ['11301', 'Stuttgart', '1']
df.loc[16] = ['41001', 'Weingarten', '4'] # Small location, could be counted in Ravensburg as well.
# Save it as a csv file.
df.to_csv('reichsbank-locations.csv', index=False)