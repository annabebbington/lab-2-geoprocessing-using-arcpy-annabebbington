'''
Anna Bebbington
Lab 2 - Geoprocessing in ArcPy
28.10.2020
Inputs are shapefiles of the new UN zipcode, parks, facilities and bike routes. Outputs are a polygon layer for 500 m from facilities, and shapefiles of bike routes and parks clipped within the UN Zip Code.
'''  
# Clip parks layer within Zip Code layer, save to Results
arcpy.Clip_analysis("parks", "zip", "C:\Programming_for_GIS\Lab_2_Geoprocessing_Python\Results\parks_Clip.shp")
# Import env class to set environment properties
from arcpy import env
# Set current workspace to Lab folder
env.workspace = "C:\Programming_for_GIS\Lab_2_Geoprocessing_Python"
# Buffer - code from lab guide but the buffer didn't work
arcpy.Buffer_analysis("facilities.shp", "Results\facilities_buffer.shp", "500 METERS")
# Buffer the facilities point layer with 500 m buffer
arcpy.Buffer_analysis("facilities", "C:\\Programming_for_GIS\\Lab_2_Geoprocessing_Python\\Results\\facilities_buffer.shp", "500 METERS")
# Edit facilities buffer to merge all buffer polygons
arcpy.Buffer_analysis("facilities", "C:\\Programming_for_GIS\\Lab_2_Geoprocessing_Python\\Results\\facilities_buffer.shp", "500 METERS", "", "", "ALL")
# Set parameters for clip
in_features = "bike_routes"
clip_features = "zip"
out_features = "bike_Clip.shp"
xy_tolerance = ""
# Clip bike_routes layer to zip layer using above defined parameters
arcpy.Clip_analysis(in_features, clip_features, out_features, xy_tolerance)

