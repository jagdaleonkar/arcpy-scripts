import arcpy

points = r'C:\GIS ArcMap\Data\ne_10m_populated_places.shp'

fields = ['NAME', 'SOV_A3']

# SQL query to filter populated places in a specific country (e.g., "India")
sql_query = '"SOV_A3" = \'USA\''

print("Populated Places in USA:")
with arcpy.da.SearchCursor(points, fields, where_clause=sql_query) as cursor:
    for row in cursor:
        print(f"Populated Place: {row[0]}, Country: {row[1]}")
