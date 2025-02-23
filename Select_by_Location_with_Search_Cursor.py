import arcpy

arcpy.env.overwriteOutput = True

points = r'C:\GIS ArcMap\Data\ne_10m_populated_places.shp'
countries = r'C:\GIS ArcMap\Data\ne_10m_admin_0_countries.shp'
outpath = r'C:\GIS ArcMap\outputs'

arcpy.MakeFeatureLayer_management(points, 'points_layer')

with arcpy.da.SearchCursor(countries, ['FID', 'SOVEREIGNT']) as country_cursor:
    for x in country_cursor:

        print(x[1])
        arcpy.MakeFeatureLayer_management(countries,'countries_layer',""" "FID" = {} """.format(x[0]))
        arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')
        formatted_output_name = x[1].replace('(', '_').replace(')', '_')
        arcpy.FeatureClassToFeatureClass_conversion('points_layer', outpath, 'cities_in_(0)_(1)'.format(formatted_output_name, x[0]))
        print('Successfully Converted {}\n'.format(formatted_output_name))
print('Finished')
    




