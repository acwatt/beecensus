# GIS sub-project goal
### Inputs
- name of a county  
- desired distance between latitude-longitude points

### Output
- pandas dataframe of latitudes, longitudes to search for bee boxes

## Sub-project Procedure
1. Load geographical extent (boundaries) of county using geopandas (or QGIS if needed)
   
1. Load USDA landtypes and extents.

1. Get extent of intersection between desirable landtypes and county.

1. Generate a latitude-longitude grid with given distance that covers the intersection 
   extent. Save grid as CSV of list of lat-lon points.