import arcpy

points = r'C:\GIS ArcMap\Data\ne_10m_populated_places.shp'
countries = r'C:\GIS ArcMap\Data\ne_10m_admin_0_countries.shp'
outpath = r'C:\GIS ArcMap\outputs'

field = ['NAME','POP_MAX']

sql_query = '"POP_MAX" > 1000000'

with arcpy.da.SearchCursor(points, field, where_clause=sql_query) as cursor:
    for row in cursor:
        print(f"Place: {row[0]}, Population: {row[1]}")