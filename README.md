# LAB 2: GEOPROCESSING USING ArcPy
 
This script uses a zipcode polygon, and uses it to clip a bike route line layer and a parks polygon layer. A buffer is done on a facilities point layer to create a 500 m buffer around facilities, and these buffered facility polygons are then merged together. These new shapefiles can be added to Zip Code polygon to visualise where bike lanes need to be removed in order to comply with UN safety protocols. 
![](https://github.com/IDCE-MSGIS/lab-2-geoprocessing-using-arcpy-annabebbington/blob/master/Lab2.jpg)

The inputs for this script are the bike routes, facilities, zip code and parks shapefiles. The outputs are the bike routes shapefile clipped to the zip code, the parks shapefile clipped to the zip code, and the buffered and merged facilities layer. These outputs are added to the zip code polygon layer to create the map above 

### Issues 

The main issue I ran into with this code was setting the current work environment to the lab folder. When I ran code that referenced data without using full path names that the run time errors. This code was suggested in the Lab 2 guide
''' 
arcpy.Buffer_analysis("facilities.shp", "Results\facilities_buffer.shp", "500 METERS")
'''
which then gave this error 
'''
Runtime error  Traceback (most recent call last):   File "<string>", line 1, in <module>   File "c:\program files (x86)\arcgis\desktop10.8\arcpy\arcpy\analysis.py", line 768, in Buffer raise e ExecuteError: ERROR 000732: Input Features: Dataset facilities.shp does not exist or is not supported
''' 
which stopped the buffer from completing successfully. In order to work around this, I added the facilities layer to the map table of contents, and then removed the '.shp' after calling that input parameter. I also replaced the partial pathname with the complete pathname, as I had done with the first clip. I also had to replace the '\' with '\\' for this code to run successfully. Below is the code used:
  '''
 arcpy.Buffer_analysis("facilities", "C:\\Programming_for_GIS\\Lab_2_Geoprocessing_Python\\Results\\facilities_buffer.shp", "500 METERS")
  '''
 Finally, when setting the parameters for the clip of the bike routes, I had to remove the '.shp' from the in_features and clip_features for the code to run suffessfully.
