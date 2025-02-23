import arcpy

points = r'C:\GIS ArcMap\Data\ne_10m_populated_places.shp'
countries = r'C:\GIS ArcMap\Data\ne_10m_admin_0_countries.shp'
outpath = r'C:\GIS ArcMap\outputs'

arcpy.MakeFeatureLayer_management(points, 'points_layer')
arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "NAME" = 'United States' """)

arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')
arcpy.FeatureClassToFeatureClass_conversion('points_layer', outpath, 'cities_in_us')
