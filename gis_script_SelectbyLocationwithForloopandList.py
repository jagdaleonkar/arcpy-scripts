import arcpy

arcpy.env.overwriteOutput = True

points = r'C:\GIS ArcMap\Data\ne_10m_populated_places.shp'
countries = r'C:\GIS ArcMap\Data\ne_10m_admin_0_countries.shp'
outpath = r'C:\GIS ArcMap\outputs'

countries_of_interest = ['United States', 'Italy', 'Kenya', 'Jordan', 'Lebanon', 'Scotland', 'France']

arcpy.MakeFeatureLayer_management(points, 'points_layer')

for X in countries_of_interest:
	print(X)
	arcpy.MakeFeatureLayer_management(countries,'countries_layer',""" "NAME" = '{}' """.format(X))
    arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')
    arcpy.FeatureClassToFeatureClass_conversion('points_layer', outpath, 'cities_in_{}'.format(X)) 