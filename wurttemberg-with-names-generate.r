library(sf)
library(ggplot2)
library(readxl)

my_shapefile <- st_read("raw-shapefile/dissolved.shp")

ggplot() +
  geom_sf(data = my_shapefile)

# Read the names excel file.
names <- read_excel("raw-data/names.xlsx")

# Merge names with the shapefile using the "ID" column.
my_shapefile <- merge(my_shapefile, names, by = "ID")

# Drop the to_merge column.
my_shapefile <- my_shapefile[, -which(names(my_shapefile) == "to_merge")]

# Save the shapefile and call it "wurttemberg-with-names.shp".
st_write(my_shapefile, "wurttemberg-with-names.shp")
