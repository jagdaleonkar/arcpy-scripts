import arcpy

arcpy.env.overwriteOutput = True

points = r'C:\GIS ArcMap\Data\ne_10m_populated_places.shp'
countries = r'C:\GIS ArcMap\Data\ne_10m_admin_0_countries.shp'
outpath = r'C:\GIS ArcMap\outputs'

with arcpy.da.SearchCursor(points, ['NAME', 'POP_MAX', 'TIMEZONE']) as cities_cursor:
    for x in cities_cursor:
        print(x[0])
        print(x[1])
        print(x[2] + '\n')
        print(x)


