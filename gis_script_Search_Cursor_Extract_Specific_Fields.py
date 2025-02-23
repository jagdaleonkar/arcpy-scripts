import arcpy

arcpy.env.overwriteOutput = True

points = r'C:\GIS ArcMap\Data\ne_10m_populated_places.shp'
countries = r'C:\GIS ArcMap\Data\ne_10m_admin_0_countries.shp'
outpath = r'C:\GIS ArcMap\outputs'

sql_clause = ["ORDER BY POP_MAX DESC", None]
with arcpy.da.SearchCursor(points, ['NAME', 'POP_MAX'], sql_clause=sql_clause) as cities_cursor:
    for x in cities_cursor:
        print(f"City: {x[0]}, Population: {x[1]}")

