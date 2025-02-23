import arcpy

arcpy.env.overwriteOutput = True

points = r'C:\GIS ArcMap\Data\ne_10m_populated_places.shp'
countries = r'C:\GIS ArcMap\Data\ne_10m_admin_0_countries.shp'
outpath = r'C:\GIS ArcMap\outputs'

with arcpy.da.SearchCursor(points, ['NAME', 'POP_MAX'], "POP_MAX > 1000000") as cities_cursor:
    for x in cities_cursor:
        print(f"Large City: {x[0]}, Population: {x[1]}")
