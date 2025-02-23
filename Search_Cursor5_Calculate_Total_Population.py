import arcpy

points = r'C:\GIS ArcMap\Data\ne_10m_populated_places.shp'

field = 'POP_MAX'

total_population = 0

with arcpy.da.SearchCursor(points, field) as cursor:
    for row in cursor:
        if row[0] is not None:   
            total_population += row[0]

print(f"Total Population across all countries: {total_population}")
